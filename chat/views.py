from django.http import HttpResponseRedirect
from django.shortcuts import render
from  .models import Message
from  .models import Chat
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        print("Received Data  " + request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1) #chat mit der ID 1
    return render(request, 'chat/index.html', {"messages": chatMessages})


def login_view(request):
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            if redirect == None:
                return redirect('/login/')
            else:
                return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect } )        
    return render(request, 'auth/login.html',  {'redirect': redirect} )


def sign_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/chat/')  # Weiterleitung zur Anmeldeseite nach erfolgreicher Registrierung
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})