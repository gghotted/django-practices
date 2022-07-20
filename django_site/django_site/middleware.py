from pickle import NONE

from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken


def get_validated_token(raw_token):
    try:
        return AccessToken(raw_token)
    except TokenError:
        return None


class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        self.user_model = get_user_model()
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        scope['user'] = await self.get_user(scope)
        return await super().__call__(scope, receive, send)

    async def get_user(self, scope):
        raw_token = self.get_raw_token(scope['query_string'])
        if raw_token is None:
            return AnonymousUser()

        validated_token = get_validated_token(raw_token)
        if validated_token is None:
            return AnonymousUser()

        scope['raw_token'] = raw_token
        return await self._get_user(validated_token)

    def get_raw_token(self, query_string):
        raw_token = (dict((x.split('=') for x in query_string.decode().split("&")))).get('token', None)
        return raw_token

    @database_sync_to_async
    def _get_user(self, validated_token):
        try:
            user_id = validated_token['user_id']
            user = self.user_model.objects.get(id=user_id)
        except (KeyError, self.user_model.DoesNotExist):
            return AnonymousUser()

        if not user.is_active:
            return AnonymousUser()
            
        return user
        