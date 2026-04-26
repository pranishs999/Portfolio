from django.db import models

class Experience(models.Model):
    role = models.CharField(max_length=200)
    org = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    current = models.BooleanField(default=False)
    desc = models.TextField()

    def __str__(self):
        return f"{self.role} at {self.org}"

class Training(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.year})"
