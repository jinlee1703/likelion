from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.CharField(unique=True, max_length=20)

    def __str__(self):
        return self.tag