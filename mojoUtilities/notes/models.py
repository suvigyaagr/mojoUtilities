from django.db import models

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length = 40, unique = True)
	user_password = models.CharField(max_length = 40)

	def __str__(self):
		return f'{self.user_name}'

class NotesEntry (models.Model):
	user_name = models.ForeignKey(User)
	note_title = models.CharField(max_length=40)
	note_text = models.CharField(max_length = 100)

	def __str__(self):
		return f'{self.note_title}'