from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class PdCategory(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey('Category')

	def __str__(self):
		return str(self.category) + " -> " + self.name

class Perk(models.Model):
	name = models.CharField(max_length=200)
	pd_category = models.ForeignKey('PdCategory')

	def __str__(self):
		return str(self.pd_category) + " -> " + self.name

class UserPerk(models.Model):
	user = models.ForeignKey('auth.User')
	perk = models.ForeignKey('Perk')
	percent = models.IntegerField(default=0)

	def __str__(self):
		return str(self.user) + " -> " + str(self.perk) + " -> " + str(self.percent)