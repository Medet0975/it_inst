from django.db import models

# Create your models here.
class Author(models.Model):

    sur_name = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='inst_image', max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f"{self.image.url}"

class HashTag(models.Model):
    hash = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name='a_h')

    def __str__(self) -> str:
        return self.hash


