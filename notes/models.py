from django.db import models
from django.utils import timezone
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
    title = models.CharField(max_length=200)
    due_date = models.DateTimeField()
    label = models.CharField(max_length=2,choices=LABEL_CHOICES,default="P")

    def __str__(self):
        return self.title
