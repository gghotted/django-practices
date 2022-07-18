from django.shortcuts import render


def room(request, room_id):
    return render(request, 'chat/room.html', {'room_id': room_id})
