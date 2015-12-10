from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf

from secretsantaapp.forms import SecretSantaGroupForm
from secretsantaapp.models import SecretSantaGroup, assignment, UserInfo


# Create your views here.

#homepage has a link to create a new group
#homepage has a view to every group that the logged in user is accessed to

def about_us(request):
	return render(request, 'about_us.html')


def homepage(request):
	if (request.user.is_anonymous()):
		return render(request, 'homepage.html')

	userGroups = []
	userInfo = UserInfo.objects.get(user=request.user)

	for group in userInfo.groups.all():
		userGroups.append(group)

	return render(request, 'homepage.html', {
										'SecretSantaGroups':userGroups,
										'userInfo':userInfo,
										})


def SecretSantaPage(request, post_id, invite=''):
	try:
		SS = SecretSantaGroup.objects.get(pk=post_id)
	except Exception as e:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS.members.all()):
		return redirect('secretsantaapp.views.homepage')

	inv = request.POST.get("invite", "")
	assign = {}

	#check if an invite was sent
	if (inv != ''):
		alreadyInvited = False

		#check if the owner is sending an invite
		if (request.user != SS.owner):
			return render(request, 'secret_santa_page.html', {'SecretSanta':SS})

		#I need to check to see if the invitee is an actual user
		try:
			invitee = User.objects.get(username=inv)
		except Exception as e:
			return redirect('secretsantaapp.views.SecretSantaPage', post_id)

		#check if that user is already invited
		for invitees in SS.invites.all():
			if (invitee.username == invitees.username):
				alreadyInvited = True

		#if user is already invited, return to the santa group page
		if (alreadyInvited == True):
			return redirect('secretsantaapp.views.SecretSantaPage', post_id)

		try:
			newInfo = UserInfo()
			newInfo.user = invitee
			newInfo.save()
			newInfo.invites.add(SS)
			newInfo.save()
		except Exception as e:
			newInfo = UserInfo.objects.get(user=invitee)
			newInfo.invites.add(SS)
			newInfo.save()
			print(newInfo.user)


		SS.invites.add(invitee)

		return render(request, 'secret_santa_page.html', {'SecretSanta':SS})


	if (SS.assignments_generated == True):
		assign = assignment.objects.get(group=SS, giver=request.user)

	return render(request, 'secret_santa_page.html', {'SecretSanta':SS, 'assignment':assign})

#For Owner Of a group
def CancelInvite(request, post_id, invite):
	try:
		SS = SecretSantaGroup.objects.get(pk=post_id)
	except Exception as e:
		return redirect('secretsantaapp.views.homepage')

	if (request.user != SS.owner):
		return redirect('secretsantaapp.views.homepage')

	#remove invite from user
	removedUser = User.objects.get(username=invite)
	removedUserInfo = UserInfo.objects.get(user=removedUser)
	removedUserInfo.invites.remove(SS)

	#remove invite from group
	SS.invites.remove(removedUser)

	return redirect('secretsantaapp.views.SecretSantaPage', post_id)

#for a person invited to a group
def AcceptInvite(request, post_id, invite):
	try:
		SS = SecretSantaGroup.objects.get(pk=post_id)
	except Exception as e:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS.invites.all()):
		return redirect('secretsantaapp.views.homepage')

	AddedUser = User.objects.get(username=invite)
	AddedUserInfo = UserInfo.objects.get(user=AddedUser)
	AddedUserInfo.invites.remove(SS)
	AddedUserInfo.groups.add(SS)

	SS.invites.remove(AddedUser)
	SS.members.add(AddedUser)
	SS.assignments_generated = True

	return redirect('secretsantaapp.views.homepage')

def DeclineInvite(request, post_id, invite):
	try:
		SS = SecretSantaGroup.objects.get(pk=post_id)
	except Exception as e:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS.invites.all()):
		return redirect('secretsantaapp.views.homepage')

	AddedUser = User.objects.get(username=invite)
	AddedUserInfo = UserInfo.objects.get(user=AddedUser)
	AddedUserInfo.invites.remove(SS)

	SS.invites.remove(AddedUser)

	return redirect('secretsantaapp.views.homepage')

def LeaveGroup(request, post_id, invite):
	try:
		SS = SecretSantaGroup.objects.get(pk=post_id)
		RemoveUser = User.objects.get(username=invite)
		RemoveUserInfo = UserInfo.objects.get(user=RemoveUser)
	except Exception as e:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS.members.all()):
		return redirect('secretsantaapp.views.homepage')

	if (request.user == SS.owner):
		SS.delete()
		return redirect('secretsantaapp.views.homepage')

	SS.members.remove(RemoveUser)
	RemoveUserInfo.groups.remove(SS)

	return redirect('secretsantaapp.views.homepage')

def GenerateAssignment(request, post_id, invite):
	try:
		SS = SecretSantaGroup.objects.get(pk=post_id)
	except Exception as e:
		return redirect('secretsantaapp.views.homepage')

	if (request.user != SS.owner):
		return redirect('secretsantaapp.views.homepage')

	SS.generate_assignments()
	SS.invites.clear()

	for people in SS.invites.all():
		peopleInfo =  UserInfo(user=people)
		peopleInfo.invites.clear()
	return redirect('secretsantaapp.views.SecretSantaPage', post_id)



def create_group(request):
	ssgForm = SecretSantaGroupForm(request.POST)

	if ssgForm.is_valid():
		newGroup = SecretSantaGroup()
		newGroup.owner = request.user
		newGroup.group_name = ssgForm.data['group_name']
		newGroup.save()
		newGroup.members.add(newGroup.owner)
		newGroup.save()

		owner = UserInfo.objects.get(user=request.user)
		owner.groups.add(newGroup)

		return redirect('secretsantaapp.views.homepage')

	return render(request, 'create_group.html', {'SecretSantaGroupForm':ssgForm})




