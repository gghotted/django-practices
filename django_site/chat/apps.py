from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    def ready(self):
        self.user_get_or_create('user1', 'user1')
        self.user_get_or_create('user2', 'user2')
    
    def user_get_or_create(self, username, password):
        from django.contrib.auth.models import User
        user = User.objects.filter(username=username).first()
        if user:
            return user
        return User.objects.create_user(username, password=password)
