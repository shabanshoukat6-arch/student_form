from django.shortcuts import render, redirect

from student.models import Profile
from student.forms import ProfileForm


def home(request):
    candidates = Profile.objects.all()

    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProfileForm()

    return render(
        request,
        'student/home.html',
        {'form': form,'candidates':candidates}
    )

def candidate_detail(req,pk):
    candidate = Profile.objects.get(pk=pk)
    return render(req,'student/candidate.html',{'candidate':candidate})