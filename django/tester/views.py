from django.shortcuts import render
import json

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def upload(request):
    resp = json.dumps(
        {
            "Resp": "Hello, you have sent a request with the following:",
            "ReqHead":str(request.headers),
            "ReqBody":str(request.body, encoding='utf-8'),
        }
    )
    print(resp)
    return HttpResponse(resp)