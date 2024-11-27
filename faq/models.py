from django.db import models

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    keywords = models.JSONField()

    def __str__(self):
        return self.question