from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import rotate_token
from . import forms



@login_required
def dummy(request, template_name=None):
    return render(request, template_name)

money = 20

@login_required
def csrf_exempt_dummy(request, template_name=None):
    global money
    money = request.POST.get('money', money)
    message = 'your money is {money}'.format(money=money)
    rotate_token(request)
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if not form.is_valid():
            message = "your data get problem"
    return render(request, template_name, {'message': message})


def easier_form(request, template_name='django_form.html'):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
    else:
        form = forms.UserForm()
    return render(request,
                  template_name,
                  {'form': form}
                  )


def model_form(request, template_name='django_form.html'):
    if request.method == "POST":
        form = forms.UserForm2(request.POST)
    else:
        form = forms.UserForm2()
    return render(request,
                  template_name,
                  {'form': form}
    )


def home(request):
    return render(request, template_name="home.html")
