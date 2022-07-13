from django.db import models


class AuthUser(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email