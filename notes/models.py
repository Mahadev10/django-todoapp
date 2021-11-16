from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Note(models.Model):
    LABEL_CHOICES = (
        ('P', 'primary'),
        ('SE', 'secondary'),
        ('S', 'success'),
        ('D', 'danger'),
        ('W', 'warning'),
        ('I', 'info'),
        ('L', 'light'),
        ('DA', 'dark'),
    )
    user =models.ForeignKey(User,on_delete=models.CASCADE,related_name="todos")
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    label = models.CharField(max_length=2, choices=LABEL_CHOICES, default="P")
    finished = models.BooleanField(default=False)
    def __str__(self):
        return self.title
