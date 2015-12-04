from django.shortcuts import render, redirect
from django.contrib.auth import user

from secretsantaapp.forms import SecretSantaGroupForm


# Create your views here.

def homepage(request):
	return render(request, 'homepage.html')

def create_group(request):
	ssgForm = SecretSantaGroupForm(request.POST)
	print request.POST.user

	if ssgForm.is_valid():
		#ssgForm.save()
		newGroup = {'owner':'fads'}
		newGroup.update(ssgForm.data)
		print(newGroup)

		newGroup = SecretSantaGroup()
		newGroup.group_name = newGroup['group_name']
		# newGroup.user = request.POST.user
		return render(request, 'homepage.html')

	return render(request, 'create_group.html', {'SecretSantaGroupForm':ssgForm})
