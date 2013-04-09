# Create your views here.
from django.db import DatabaseError
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import Template,Context, RequestContext
from django.template.loader import get_template
#from django.views.generic.simple import direct_to_template
from C2C.forms import RegistrationForm
from django.shortcuts import render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from C2C.models import *

import re


def registration(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST' and request.POST["password"] == request.POST["retype_password"]:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            try:
                p = Customer(first_name=cleaned_data["First_Name"],  #Creating for entering it in to Database
                             last_name=cleaned_data["Last_Name"],
                             phno=cleaned_data["phno"],
                             email=cleaned_data["email"],
                             username=cleaned_data['username']
                             )
                p.save()
                user = User.objects.create_user(username=cleaned_data['username'], #for user Authentication
                                                email=cleaned_data['email'],
                                                password=cleaned_data['password'],
                                                )
                user.first_name = cleaned_data['First_Name']
                user.last_name = cleaned_data['Last_Name']
                user.is_active = True
                user.save()
                return render_to_response("thanks.html", {}, context_instance=RequestContext(request))
            except DatabaseError:
                print "Database Error Occured"
                return render_to_response("oops.html", {}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
    t = get_template("registration.html")
    c = RequestContext(request, {"form": form})
    return HttpResponse(t.render(c))
    #return render_to_response("registration.html", {"form":form})



def thanku(request):
    return direct_to_template(request, "thanks.html")


def oops(requst):
    return HttpResponse("Some thing wrong Happened! Sorry. Please try after some time.")


def index(request):
    return render_to_response("index.html", {}, context_instance=RequestContext(request))


def search(request):
    if request.method == 'POST':

        if 'search' in request.POST and not request.POST['search']:
            ad_id = []
            regular = re.compile('\w' + request.POST['search'] + '\w')
            try:
                for i in Advertisement.objects.all(): #Using Query set to iterate through the model
                    if regular.match(i.name):
                        ad_id.append(i.id)
                    elif regular.match(i.type):
                        ad_id.append(i.id)
                    elif regular.match(i.description):
                        ad_id.append(i.id)
                #list = Advertisement.objects.get()
                message = "you have searched for %s " % request.POST['search']
            except Advertisement.DoesNotExist:
                message = "Sorry! What you are searching is not found.."
        else:
            message = "you have submitted an empty form"
        return HttpResponse(message)


def login(request):
    """

    :param request:
    :return:
    """
    """m = Customer.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['user_id'] = m.id"""
    username = request.POST['name']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return render_to_response('welcome.html', {},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('sorry.html', {},
                                  context_instance=RequestContext(request))




def logout(request):
    """try:
        del request.session['user_id']
    except KeyError:
        pass
    return render_to_response('index.html', {},
                              context_instance=RequestContext(request))
"""
    auth.logout(request)
    return render_to_response('index.html', {},
                              context_instance=RequestContext(request))




def add(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        diction = {}
        if request.method == 'POST':
            form = AdvertiseForm(request.POST)
            if form.is_valid():
                try:
                    advertise = form.save(commit=False)
                    username = Customer.objects.get(username=request.user)
                    advertise.ad_by = username
                    advertise.save()
                    diction['add'] = True
                except DatabaseError:
                    print "Database Error Occured"
                    diction['add'] = False
                finally:
                    return render_to_response("index.html", diction,
                                              context_instance=RequestContext(request))
        else:
            form = AdvertiseForm()
            return render_to_response("advertisement_form.html", {'form': form},
                                      context_instance=RequestContext(request))




#def add_register(reqeust):