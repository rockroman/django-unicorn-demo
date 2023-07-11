from django.db import models


# Create your models here.
class Comment(models.Model):
    content = models.CharField(max_length=150)

    def __str__(self) -> str:
        return str(self.content)
