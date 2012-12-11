from django.db import models

class vertical(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField()
	char_count = models.IntegerField()
	question1 = models.TextField()
	answer1 = models.CharField(max_length=100)
	question2 = models.TextField()
	answer2 = models.CharField(max_length=100)
	question3 = models.TextField()
	answer3 = models.CharField(max_length=100)
	question4 = models.TextField()
	answer4 = models.CharField(max_length=100)
	question5 = models.TextField()
	answer5 = models.CharField(max_length=100)
	question6 = models.TextField()
	answer6 = models.CharField(max_length=100)
	question7 = models.TextField()
	answer7 = models.CharField(max_length=100)
	question8 = models.TextField()
	answer8 = models.CharField(max_length=100)
	question9 = models.TextField()
	answer9 = models.CharField(max_length=100)
	question10 = models.TextField()
	answer10 = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class simple_words(models.Model):
	word = models.CharField(max_length=30)

	def __unicode__(self):
		return self.word

class complicated_words(models.Model):
	word = models.CharField(max_length=30)

	def __unicode__(self):
		return self.word