from django.shortcuts import render

from django.http import HttpResponse

import requests
import json

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello World')


def getAppID(request):
    allApps = "https://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    
    # query URL and get a list of all apps dictionary - keys: appid, name
    response = requests.get(allApps).json()
    applist = response['applist']['apps']['app']

    # find the app ID for the game in URL parameter
    for item in applist:
        if item['name'] == gameName:
            return item['appid']





