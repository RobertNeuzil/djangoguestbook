from django.db import models

class Home(models.Model):
	email = models.EmailField(max_length=100)
	url = models.URLField(max_length=100)

	def __str__(self):
		return f"{self.email}"