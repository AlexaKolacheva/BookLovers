from django.shortcuts import render
from .models import Review, Activity



def activity_feed(request):
    activity_list = Activity.objects.all()
    return render(request, 'activity/activity_feed.html', {'activity_list': activity_list})



