from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.context_processors import csrf

from secretsantaapp.forms import SecretSantaGroupForm
from secretsantaapp.models import SecretSantaGroup, assignment


# Create your views here.

#homepage has a link to create a new group
#homepage has a view to every group that the logged in user is accessed to
def homepage(request):
	if (request.user.is_anonymous()):
		return render(request, 'homepage.html')

	user = request.user
	userGroups = []
	allGroups = SecretSantaGroup.objects.all()

	for group in allGroups:
		if user in group.members.all():
			userGroups.append(group)

	return render(request, 'homepage.html', {'SecretSantaGroups':userGroups})


def SecretSantaPage(request, post_id, invite=''):
	SS = SecretSantaGroup.objects.all().filter(pk=post_id)
	inv = request.POST.get("invite", "")
	if (inv != ""):
		alreadyInvited = False

		if not SS:
			return redirect('secretsantaapp.views.homepage')

		if (request.user not in SS[0].members.all()):
			return redirect('secretsantaapp.views.homepage')

		if (request.user != SS[0].owner):
			return redirect('secretsantaapp.views.SecretSantaPage', post_id)

		#I need to check to see if the invitee is an actual user
		invitee = User.objects.filter(username=inv)
		if not invitee:
			return redirect('secretsantaapp.views.SecretSantaPage', post_id)

		#check if that user is already invited
		for invitees in SS[0].invites.all():
			if (invitee[0].username == invitees.username):
				alreadyInvited = True

		#if user is already invited, return to the santa page
		if (alreadyInvited == True):
			return redirect('secretsantaapp.views.SecretSantaPage', post_id)

		SS[0].invites.add(invitee[0])
		return render(request, 'secret_santa_page.html', {'SecretSanta':SS[0]})

	if not SS:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS[0].members.all()):
		return redirect('secretsantaapp.views.homepage')



	return render(request, 'secret_santa_page.html', {'SecretSanta':SS[0]})

def SecretSantaInvite(request, post_id, invite=''):
	SS = SecretSantaGroup.objects.all().filter(pk=post_id)
	alreadyInvited = False
	print('here')

	if not SS:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS[0].members.all()):
		return redirect('secretsantaapp.views.homepage')

	if (request.user != SS[0].owner):
		return redirect('secretsantaapp.views.SecretSantaPage', post_id)

	#I need to check to see if the invitee is an actual user
	invitee = User.objects.filter(username=invite)
	if not invitee:
		return redirect('secretsantaapp.views.SecretSantaPage', post_id)

	#check if that user is already invited
	for singleInv in SS[0].invites.all():
		if (invitee == invitees):
			alreadyInvited = True

	#if user is already invited, return to the santa page
	if (alreadyInvited == True):
		return redirect('secretsantaapp.views.SecretSantaPage', post_id)

	SS[0].invites.add(invitee[0])
	

	return render(request, 'secret_santa_page.html', {'SecretSanta':SS[0]})


def create_group(request):
	ssgForm = SecretSantaGroupForm(request.POST)

	if ssgForm.is_valid():
		newGroup = SecretSantaGroup()
		newGroup.owner = request.user
		newGroup.group_name = ssgForm.data['group_name']
		newGroup.save()
		newGroup.members.add(newGroup.owner)
		newGroup.save()

		return render(request, 'homepage.html')

	return render(request, 'create_group.html', {'SecretSantaGroupForm':ssgForm})


