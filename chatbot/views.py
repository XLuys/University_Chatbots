from django.shortcuts import render
from django.http import JsonResponse
import random

def index(request):
    return render(request, 'chatbot/index.html')

def reply(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        user_message = data.get('message')

        # Simple bot logic
        bot_reply = f"You said: {user_message}"
        return JsonResponse({'reply': bot_reply})
