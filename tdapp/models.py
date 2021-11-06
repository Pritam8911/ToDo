from django.db import models

# Create your models here.
class Records(models.Model):
    
    taskName=models.CharField(max_length=40)
    deadline=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskName
