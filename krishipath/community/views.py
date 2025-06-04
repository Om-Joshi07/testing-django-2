from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage, BlockedUser
from django.contrib.auth.models import User
import json




def community_home(request):
    users = User.objects.exclude(username=request.user.username)

    return render(request, 'community/home.html', {'users': users})




@csrf_exempt
@login_required
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        to_username = data.get('receiver')
        content = data.get('message')

        try:
            receiver = User.objects.get(username=to_username)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404)
        
        # Check if the reciver has blocked the sender
        if BlockedUser.objects.filter(blocker=receiver, blocked=request.user).exists():
            return JsonResponse({'error': 'You have blocked this user'}, status=403)
        
        # Checks if the sender has blocked the receiver
        if BlockedUser.objects.filter(blocker= request.user, blocked= receiver).exists():
            return JsonResponse({'error': 'You have blocked this user'}, status=403)
        
        ChatMessage.objects.create(
            sender=request.user,
            receiver=receiver,
            message=content
        )
        return JsonResponse({'status': 'Message sent successfully'})
    


@login_required
def chat_history(request, username):
    try:
        other_user = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=404)
    
    messages = ChatMessage.objects.filter(
        sender__in = [request.user, other_user],
        receiver__in = [request.user, other_user]
    ).order_by('timestamp')
    

    history = [{
        'from': m.sender.username,
        'to': m.receiver.username,
        'message': m.message,
        'timestamp': m.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for m in messages]
    
    return JsonResponse({'history': history})


@login_required
@csrf_exempt
def block_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        try:
            to_block = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        BlockedUser.objects.get_or_create(blocker=request.user, blocked=to_block)
        return JsonResponse({"success": "User blocked"})
