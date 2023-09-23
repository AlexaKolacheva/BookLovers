from django.shortcuts import render
from django.db.models import Q

from .models import Review, Activity

from apps.profiles.models import Friend
from ..accounts.models import CustomUser


def activity_feed(request):
    current_user = request.user

    # Найдите всех друзей текущего пользователя, у которых статус 'accepted'
    friends = Friend.objects.filter(Q(status='accepted', friend=current_user) | Q(status='accepted', user=current_user))

    # Получите всех друзей текущего пользователя
    friend_users = [friend.user if friend.friend == current_user else friend.friend for friend in friends]

    # Теперь вы можете получить посты (Activity) от этих друзей
    activity_list = Activity.objects.filter(review__user__in=friend_users)

    # friend_reviews содержит только обзоры, оставленные друзьями текущего пользователя

    # activity_list = Activity.objects.filter()
    return render(request, 'activity/activity_feed.html', {'activity_list': activity_list})
    #


