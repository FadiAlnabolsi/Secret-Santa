from django.shortcuts import render, redirect

from secretsantaapp.forms import SecretSantaGroupForm
from secretsantaapp.models import SecretSantaGroup


# Create your views here.

def homepage(request):
	return render(request, 'homepage.html')

def create_group(request):
	ssgForm = SecretSantaGroupForm(request.POST)
	print(request.user.username)

	if ssgForm.is_valid():
		print(request.user)
		newGroup = SecretSantaGroup()
		newGroup.owner = request.user
		#newGroup.members.add(request.user)
		newGroup.group_name = ssgForm.data['group_name']
		newGroup.save()
		#ssgForm.save()
		#newGroup = {'owner':'fads'}
		#newGroup.update(ssgForm.data)
		#print(newGroup)

		#newGroup = SecretSantaGroup()
		#newGroup.group_name = newGroup['group_name']
		#newGroup.user = request.POST.user
		return render(request, 'homepage.html')

	return render(request, 'create_group.html', {'SecretSantaGroupForm':ssgForm})
