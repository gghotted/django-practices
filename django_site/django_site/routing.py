import chat.routing
from channels.routing import ProtocolTypeRouter, URLRouter

from django_site.middleware import TokenAuthMiddleware

application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})
