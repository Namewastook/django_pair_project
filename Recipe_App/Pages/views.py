from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    return render(request, "Pages/home.html")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('Home')
    template_name = 'registration/signup.html'

@login_required(login_url='/')
def profile_create(request):
    return render(request, "Pages/profile.html")

def add_profile(request):

    if request.method == "POST":

        new_profile = Profile(first=request.POST['first'],
                            last=request.POST['last'],
                            username=request.POST['username'],
                            aboutyou=request.POST['aboutyou'])

        new_profile.save()

        return redirect("/meals/")

    return render(request, 'Pages/profile')

# def update_profile(request, id):
#     to_update = Profile.objects.get(id=id)
#     if request.method == "POST":

#         for key, value in request.POST.items():

#             if (value and key != "csrfmiddlewaretoken"):
#                 setattr(to_update, key, value)

#         to_update.save()

#         return redirect("/meals/")

#     context={
#         "id": id,
#         "update_profile":to_update
#     }

#     return render(request, 'Pages/profile', context=context)

# def delete_profile(request, id):
#     to_delete = Profile.objects.get(id=id)
#     to_delete.delete()
    
#     return redirect("Registration/signup")
