from django.shortcuts import render
from django.views.generic import ListView

from chat.models import Room


def room(request, room_id):
    return render(request, 'chat/room.html', {'room_id': room_id})


class RoomListView(ListView):
    queryset = Room.objects.all()
