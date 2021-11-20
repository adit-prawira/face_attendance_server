from django.db import models


# Create your models here.
class FaceIdentity(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    imageUrl = models.URLField()
    encodedFace = models.TextField(null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name