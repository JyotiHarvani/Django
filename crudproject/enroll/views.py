from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegistrationForm
from .models import Student
from django.urls import reverse


def add_show_student(request):
	if request.method == 'POST':
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			name1 = form.cleaned_data['name']
			email1 = form.cleaned_data['email']
			password1 = form.cleaned_data['password']
			student1 = Student(name = name1, email = email1, password = password1)
			student1.save()
			return redirect(reverse('addandshow'))
	else:
		form = StudentRegistrationForm()
	students = Student.objects.all()
	return render(request, 'enroll/add_show_student.html',{'form' : form, 'student_records' : students})


def delete_student(request, id):
	if request.method == 'POST':
		get_record = Student.objects.get(pk=id)
		get_record.delete()
	return HttpResponseRedirect('/')

def update_student(request, id):
	if request.method == 'POST':
		get_record = Student.objects.get(pk=id)
		form = StudentRegistrationForm(request.POST,instance = get_record)
		if form.is_valid():
			form.save()
	else:
		get_record = Student.objects.get(pk=id)
		form = StudentRegistrationForm(instance = get_record)

	return render(request, 'enroll/update_student.html',{'form' : form})

