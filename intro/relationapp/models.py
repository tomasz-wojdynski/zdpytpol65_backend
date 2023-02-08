from django.db import models


# jeden do jeden (one-to-one)
class Country(models.Model):
    name = models.CharField(max_length=124)
    models.OneToOneField("Capital", on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=256)

