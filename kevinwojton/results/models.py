from django.db import models
from datetime import *

from django.contrib.auth.models import User

class email_subscribers(models.Model):

	name = models.CharField(max_length=50, blank = True, null = True)
	email = models.CharField(max_length=50, blank = True, null = True)
	message = models.CharField(max_length=300, blank = True, null = True)
	#radio button for beginner starting set
