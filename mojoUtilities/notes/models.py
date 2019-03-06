from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
	user_name = models.CharField(
		max_length = 40,
		unique = True
	)		
	user_password = models.CharField(
		max_length = 40
	)
	fullName = models.CharField(
		max_length = 40,
		blank = True
	)
	GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
	user_gender = models.CharField(
		max_length = 1,
		choices = GENDER_CHOICES,
		blank = True,
		default = 'm',
		help_text='User gender',
	)
	dob = models.DateField(
		blank = True,
		default = datetime.now
	)

	def __str__(self):
		return f'{self.user_name}'

class NotesEntry (models.Model):
	user_name = models.ForeignKey(User)
	note_title = models.CharField(max_length=40)
	note_text = models.CharField(max_length = 100)

	def __str__(self):
		return f'{self.note_title}'