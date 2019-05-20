from django.shortcuts import render
from gtts import gTTS
from django.conf import settings

# Create your views here.
def convert(req):
    if req.method == 'POST':
        text = req.POST["text"].split("\r\n")
        result = []
        for t in text:
            tts = gTTS(t)
            t = t.replace('?','')
            t = t.replace('.','')
            t = t.replace('"','')
            t = t.replace("'",'')
            print("/"+settings.MEDIA_ROOT + "/" + t+'.mp3')
            tts.save("/"+settings.MEDIA_ROOT + "/" + t+'.mp3')
            result.append([t,settings.MEDIA_URL + "/" + t+'.mp3'])
        context = {"result":result}
        template = 'download.html'
        return render(req, template, context)
    context = {}
    template = 'convert.html'
    return render(req, template, context)