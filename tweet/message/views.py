from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import datetime
import json

from . import models
from . import serializers

def index(request):

    if request.method == 'POST':
        # from IPython import embed; embed()

        data = json.loads(request.body)

        name = data.get('name', None)
        tweet = data.get('tweet', None)
        if name and tweet:
            message = models.Message.objects.create(name=name, tweet=tweet, date=datetime.now(tz=timezone.utc))
        
        messages = models.Message.objects.all()        
        result = serializers.MessageSerializer(messages, many=True).data
        return JsonResponse(result, safe=False)

    messages = models.Message.objects.all()
    context = {}
    context['messages'] = json.dumps(serializers.MessageSerializer(messages, many=True).data)

    return render(request, 'page.html', context)