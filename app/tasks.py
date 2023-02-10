from celery import shared_task
import pyttsx3


@shared_task
def textToAudio(txt):
    engine = pyttsx3.init()
    engine.setProperty("rate", 135)
    engine.say(txt)

    engine.runAndWait()
