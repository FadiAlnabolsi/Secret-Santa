from django.db import models
from django.contrib.auth.models import User

import random

# Create your models here.
class SecretSantaGroup(models.Model):
	group_name = models.TextField()
	owner = models.ForeignKey(User, related_name="owner")
	members = models.ManyToManyField(User, blank=True)
	invites = models.ManyToManyField(User, related_name="invites_sent", blank=True)
	assignments_generated = models.BooleanField(default=False)

	def __str__(self):
		return self.group_name

	class Meta:
		verbose_name_plural = 'Secret Santa Groups'

	def save(self):
		# self.update_assignments()
		super().save()

	def check_if_giver(self, group, member):
		#returns true if assigned already, else false
		assignments = assignment.objects.filter(group=group,giver=member)
		if not assignments:
			return False
		else:
			return True

	def check_if_receiver(self, group, member):
		#returns true if assigned already, else false
		assignments = assignment.objects.filter(group=group,receiver=member)
		if not assignments:
			return False
		else:
			return True

	def check_all_members_are_assigned(self):
		for member in self.members.all():
			assignements_giver = assignment.objects.filter(group=self, giver=member)
			assignements_receiver = assignment.objects.filter(group=self, receiver=member)

			if member not in assignements_giver:
				return False
			if member not in assignements_receiver:
				return False

		return True

	def generate_assignments(self):
		assignments = assignment.objects.filter(group=self)
		if (self.assignments_generated == False):
			self.assignments_generated = True
			self.save()

			for member in self.members.all():
				if (self.check_if_giver(self, member) == False):
					#if not a giver, give to someone
					added_user = False
					while added_user == False:
						receiver = random.choice(self.members.all())
						if (self.check_if_receiver(self, receiver) == False):
							#can't give to yourself
							if(receiver != member):
								new_assignment = assignment()
								new_assignment.group = self
								new_assignment.group_id = self.id
								new_assignment.giver = member
								new_assignment.receiver = receiver
								new_assignment.save()
								added_user = True

    #generate to create assignments
    #update to check for any removed & new users, and only assign to the new users

class assignment(models.Model):
	group = models.ForeignKey(SecretSantaGroup)
	giver = models.ForeignKey(User, related_name="giver_user", null=True, blank=True)
	receiver = models.ForeignKey(User, related_name="receiver_user", null=True, blank=True)

	def __str__(self):
		return self.group.group_name

class UserInfo(models.Model):
	user = models.OneToOneField(User, null=True)
	groups = models.ManyToManyField(SecretSantaGroup, related_name='participating_in', blank=True)
	invites = models.ManyToManyField(SecretSantaGroup, related_name='invited_to', blank=True)

	# def clean(self):
	# 	if self.giver not in self.group.members:
	# 		raise ValidationError(('giver', 'The giver is not in this group'))
	# 	super().clean()

class Item(models.Model):
    text = models.TextField(default='')
    user = models.ForeignKey(User, default=None)
