from django.db import models


class Room(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    participant_num = models.PositiveBigIntegerField()
