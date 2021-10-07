from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import json

# Create your views here.
def home(request):

    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        tweet = data['tweet']
        tweetDate = datetime.now()

        if username and tweet:
            response = f"New Tweet added by {username}"
            return JsonResponse({"msg":response, "user":username, "tweet":tweet, "tweetDate":tweetDate}, status=201)

        else:
            response = "username or tweet is empty"
            return JsonResponse({"err":response}, status=400)

    return render(request, 'poorTwitterClient/home.html')