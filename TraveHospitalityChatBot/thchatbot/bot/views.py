from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import send_and_receive_msg

def index(request):
    
    context = {
        "title":"Travel and Hospitality Bot"
    }
    return render(request, "index.html", context)

def chat(request, msg):
    ai_res = send_and_receive_msg(msg)
    return JsonResponse({"message": ai_res})