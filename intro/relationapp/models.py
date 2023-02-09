from django.db import models


# jeden do jeden (one-to-one)
class Country(models.Model):
    name = models.CharField(max_length=124)
    capital = models.OneToOneField("Capital", on_delete=models.CASCADE)


class Capital(models.Model):
    name = models.CharField(max_length=256)


# jeden do wielu (one-to-many)
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Framework(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
