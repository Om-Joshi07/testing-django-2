import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from .qa_core import get_qa_chain

qa_chain = get_qa_chain()

@login_required
def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = data.get("question", "").strip()

            if not question:
                return JsonResponse({"error": "No question provided."})

            # Save user question
            ChatMessage.objects.create(
                user=request.user,
                role="user",
                content=question
            )

            # Get answer
            answer = qa_chain.run(question)

            # Save bot response
            ChatMessage.objects.create(
                user=request.user,
                role="bot",
                content=answer
            )

            return JsonResponse({"answer": answer})

        except Exception as e:
            print("Error processing question:", e)
            return JsonResponse({"error": "Error processing the request."})

    # For GET request, render chat UI with chat history
    chat_history = ChatMessage.objects.filter(user=request.user).order_by('timestamp')[:50]
    return render(request, "chatbot.html", {
        "chat_history": [
            {
                "role": msg.role, 
                "content": msg.content,
                "timestamp": msg.timestamp  # Make sure to pass timestamp
            } 
            for msg in chat_history
        ]
    })