from django.db import models


class ContactMsg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    msg = models.TextField()

    def __str__(self):
        return self.subject
