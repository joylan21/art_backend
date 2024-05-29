from django.db import models

class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(TimestampedModel):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    photo = models.ImageField(upload_to='author_photos')

    def __str__(self) -> str:
        return self.name

class Category(TimestampedModel):
    name = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name

class Art(TimestampedModel):
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='art_photos')
    address = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    measurement = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
