from django.shortcuts import render
from django.http import JsonResponse
from .models import Events


def index(request):
    all_events = Events.objects.all()
    context = {
        "events": all_events,
    }
    return render(request, 'index.html', context)

def all_events(request):
    all_events = Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)