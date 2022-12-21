from django.shortcuts import render
from .tasks import textToAudio

def home(request):
    text=request.GET.get("text")
    if text:
        textToAudio.delay(text)
    context = {}
    return render(request, 'home.html', context)