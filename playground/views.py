from tokenize import String
from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

import requests
import json

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')

# Get App ID for a game name
def appID(request, gameName):
    allApps = "https://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    
    # query URL and get a list of all apps dictionary - keys: appid, name
    response = requests.get(allApps).json()
    applist = response['applist']['apps']['app']

    # find the app ID for the game in URL parameter
    for item in applist:
        if item['name'] == gameName:
            return JsonResponse(item)




