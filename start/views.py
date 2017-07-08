from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,authenticate
from start.forms import SignUpForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Answer
from django.template import loader
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Twoje hasło zostało zmienione!')
            return redirect('/panel/change-password')
        else:
            messages.error(request, 'Popraw wprowadzone dane')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def about(request):
    return render(request, 'about.html')

@login_required
def goPremium(request):
    if request.user.profile.premium:
        return redirect('/premium')
    else:
        return redirect('/get-premium')

@login_required
def get_premium(request):
    return render(request, 'get-premium.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # messages.success(request, 'Twoje hasło zostało zmienione!')
            return redirect('/change-password')
        # else:
        #     messages.error(request, 'Popraw wprowadzone dane')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password.html', {
        'form': form
    })

@login_required
def userAccount(request):
    answers = Answer.objects.filter(user=request.user).order_by('-pub_date')
    indexTemplate = loader.get_template('user-account.html')
    context = {
        'answers': answers,
    }
    return HttpResponse(indexTemplate.render(context, request))