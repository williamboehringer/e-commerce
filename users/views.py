from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Userprofile
from django.contrib.auth import login


# Create your views here.
def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'users/vendor_detail.html', {'user':user})

def myaccount(request):
    return render(request, 'users/myaccount.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            user = Userprofile.objects.create(user=user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
