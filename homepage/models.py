import random
import string

from django.db import models


def generate_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(16))
    return user_id


class User(models.Model):
    worker_login = models.TextField(null=True)
    worker_password = models.TextField(null=True)
    user_id = models.TextField(default=generate_user_id())
    this_worker = models.BooleanField(default=False)
