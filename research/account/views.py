# Create your views here.
from account.models import research
from account.models import multiple_choice
from account.models import dissertative
from account.forms import loginForm
from account.forms import signupForm

from django import forms
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response as render
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponseRedirect
import datetime

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

import re

# from django.contrib.auth.models import User
# adding users in django: python manage.py shell
# user = User.objects.create_user('admin', 'admin@admin.com', '123456')
# user.is_staff = True
# user.save()

class researchForm(ModelForm):
    class Meta:
        model = research

class multForm(ModelForm):
    class Meta:
        model = multiple_choice

class dissertativeForm(ModelForm):
    class Meta:
        model = dissertative

def home(request):
    if request.user:
        user = request.user
    else:
        user = "AnonymousUser"

    return render("index.html", {
        "user": user,
    }, context_instance=RequestContext(request))

def loginPage(request, cookie):
    if request.POST:
        frm = loginForm(request.POST)
        frm_dict = request.POST
        user_email = frm_dict['username']
        username = get_object_or_404(User, email=user_email)
        user = authenticate(username=username, password=frm_dict['passwd'])

        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                return HttpResponseRedirect('/admin/')
            elif user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/%s'%user)
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        frm = loginForm()

        return render("login.html", {
            "frm": frm,
        }, context_instance=RequestContext(request))

def signup(request, cookie):
    if request.POST:
        frm = signupForm(request.POST)
        frm_dict = request.POST

        username = frm_dict['username']
        password = frm_dict['passwd']
        email = frm_dict['email']
        user = User.objects.create_user(username, email, password)
        user.save()

        return HttpResponseRedirect('/')

    else:
        frm = signupForm()

        return render("signup.html", {
            "frm": frm,
        }, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def admin(request, cookie):
    if request.POST:
        frm = loginForm(request.POST)
        if frm.is_valid():
            frm_dict = request.POST
    else:
        frm = loginForm()

    return render("admin.html", {
        "frm": frm,
        "user": request.user,
    }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def research_edit(request, cookie):
    research_id = re.sub(r"\/research\/",'', request.path)
    research_id = re.sub(r"\/edit",'', research_id)
    if request.POST:
        frm_dict = request.POST
        edit_resear = research.objects.filter(id=research_id).update(title = frm_dict['title'],
                                                                     description = frm_dict['description'],
                                                                     start_at = frm_dict['start_at'],
                                                                     finish_at = frm_dict['finish_at'],
                                                                     status = frm_dict['status'],
                                                                     publish = frm_dict['publish'])
        return HttpResponseRedirect('/research')
    else:
        edit_resear = research.objects.get(id=research_id)
        frm = researchForm(instance=edit_resear)

        return render("edit_research.html", {
            "research": research.objects.get(id=research_id),
            "frm": frm,
        }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def research_delete(request):
    research_id = re.sub(r"\/research\/",'', request.path)
    research_id = re.sub(r"\/delete",'', research_id)
    research.objects.get(id=research_id).delete()
    return HttpResponseRedirect('/research')

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def new_question(request):
    research_id = re.sub(r"\/research\/",'', request.path)
    research_id = re.sub(r"\/question\/new",'', research_id)

    if request.POST:
        frm_diss = dissertativeForm(request.POST)
        frm_mult = multForm(request.POST)
    else:
        frm_diss = dissertativeForm()
        frm_mult = multForm()

    return render("add_question.html", {
        "research": research.objects.get(id=research_id),
        "multForm": frm_mult,
        "dissForm": frm_diss,
    }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def research_answer(request):
    research_id = int(re.sub(r"\/research\/",'', request.path))
    return render("answer_research.html", {
        "research": research.objects.get(id=research_id)
    }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def research_new(request):
    lst_research = list(research.objects.all())
    if request.POST:
        frm_dict = request.POST
        new_resear = research(title = frm_dict['title'],
                              description = frm_dict['description'],
                              start_at = frm_dict['start_at'],
                              finish_at = frm_dict['finish_at'],
                              status = frm_dict['status'],
                              publish = frm_dict['publish'])
        new_resear.save()
        return HttpResponseRedirect('/research')
    else:
        frm = researchForm()

        return render("new_research.html", {
            "frm": frm,
            "user": request.user,
            "list_research": lst_research,
        }, context_instance=RequestContext(request))

@login_required(login_url='/login/')
def research_list(request):

    expiration_list = []
    now =  datetime.datetime.now().date()

    for i in research.objects.all():
        if i.finish_at < now:
            expiration_list.append(i.id)
            research_exp = research.objects.filter(id=i.id).update(status="X")

    return render("research_list.html", {
        "user": request.user,
        "expiration_list": expiration_list,
        "list_research": research.objects.all(),
    },context_instance=RequestContext(request))

@login_required(login_url='/login/')
def userhome(request, cookie):
    return render("home.html", {
        "user": request.user,
    },context_instance=RequestContext(request))

def logoff(request, cookie):
    logout(request)
    return render("logout.html")
