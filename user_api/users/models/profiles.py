"""Profile model."""

#   Django
from django.db import models
from django.db.models.deletion import CASCADE

#   utilities
from user_api.utils.models import ApiModel

class Profile(ApiModel):
    """Profile model.
    
    A profile holds a user's public data like biography and picture.
    """
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture  = models.ImageField(
        'profile picture', 
        upload_to='users/pictures', 
        blank=True, 
        null=True
        )
    
    biography = models.TextField(max_length=500, blank=True)


    def __str__(self):
        """Return user's str representation."""
        return str(self.users)