from django.db import models


class Room(models.Model):
    """ Represents chat rooms that users can join"""
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=155)
    slug = models.CharField(max_length=50)

    def __str__(self):
        """Return human readable representation of model instance"""
        return self.name