from django.shortcuts import render, redirect

from secretsantaapp.forms import SecretSantaGroupForm
from secretsantaapp.models import SecretSantaGroup, assignment


# Create your views here.

#homepage has a link to create a new group
#homepage has a view to every group that the logged in user is accessed to
def homepage(request):
	user = request.user
	userGroups = []
	allGroups = SecretSantaGroup.objects.all()

	for group in allGroups:
		if user in group.members.all():
			userGroups.append(group)

	return render(request, 'homepage.html', {'SecretSantaGroups':userGroups})


def SecretSantaPage(request, post_id):
	SS = SecretSantaGroup.objects.all().filter(pk=post_id)

	if not SS:
		return redirect('secretsantaapp.views.homepage')

	if (request.user not in SS[0].members.all()):
		return redirect('secretsantaapp.views.homepage')

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


