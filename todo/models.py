from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    dueDate = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}. {self.description} - {self.dueDate}"