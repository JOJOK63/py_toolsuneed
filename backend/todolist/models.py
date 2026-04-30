from django.db import models


# Create your models here.
class Collection(models.Model):
    name: str = models.CharField(max_length=60)
    slug: str = models.SlugField()


class Task(models.Model):
    description: str = models.TextField()
    collection: Collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

