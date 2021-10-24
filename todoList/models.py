from django.db import models

# Create your models here.
class TodoList(models.Model):
    task = models.CharField(max_length=45)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task