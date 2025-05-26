import json
from django.http import JsonResponse
from django.shortcuts import render
from .qa_core import get_qa_chain

# Initialize your QA chain once when the server starts
qa_chain = get_qa_chain()

def chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Expect JSON body
            question = data.get("question", "").strip()
            print("Received question:", question)  # Debug

            if not question:
                return JsonResponse({"error": "No question provided."})

            # Use the qa_chain to get answer from your vectorstore
            result = qa_chain.run(question)
            print("Generated answer:", result)  # Debug

            if result:
                return JsonResponse({"answer": result})
            else:
                return JsonResponse({"error": "Sorry, I couldn't find an answer."})
        
        except Exception as e:
            print("Error processing question:", e)
            return JsonResponse({"error": "Error processing the request."})

    # For GET request, just render the chatbot page
    return render(request, "chatbot.html")
