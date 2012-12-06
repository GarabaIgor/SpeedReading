from django.db import models

class Text(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()