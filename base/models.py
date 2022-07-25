from pyexpat import model
from django.db import models

# we use this to import user model already built in...
from django.contrib.auth.models import User

# we make use of models.Model to make class a Model


class Task(models.Model):
    # create many to one relationship
    # i.e, many taks can have smae user
    # models.set_Null to keep childs even after deleting User
    # in onder to avoid errors we use null and blank as true
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    # order data

    class Meta:
        ordering = ['complete']
