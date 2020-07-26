
from django.urls import path

from . import views



urlpatterns = [

path('index/',views.index,name="index"),
path('report/',views.report,name="report"),
path('complaint/',views.complaint,name="complaint"),
path('helpline/',views.helpline,name="helpline"),
path('check_status/',views.checkstatus,name="checkstatus"),
path('submitcomplaint/',views.submitcomplaint,name="submitcomplaint"),
path('loginhandle/',views.loginhandle,name="loginhandle"),
path('checkstatushandle/',views.checkstatushandle,name="checkstatushandle"),
path('signuphandle/',views.signuphandle,name="signuphandle"),
path('contact/',views.contact,name="contact"),
path('logouthandle/',views.logouthandle,name="logouthandle"),
path('changes/',views.changes,name="changes"),
path('updateStatus/',views.updateStatus,name="updateStatus"),

path('updateDetails/',views.updateDetails,name="updateDetails"),

path('updates/',views.updates,name="updates"),




]