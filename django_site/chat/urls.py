from django.urls import path

from chat.views import RoomListView, room

urlpatterns = [
    path('room/<int:room_id>/', room),
    path('room/', RoomListView.as_view()),
]
