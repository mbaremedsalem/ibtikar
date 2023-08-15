from django.urls import path
from . import views
app_name='home'
app_name='formation_detail'
app_name='course_detail'

urlpatterns = [
path('home/',views.formation_list,name='home'),
path('<int:id>/',views.formation_detaile,name='formation_detaile'),
path('detaile/<int:id>/',views.course_detail,name='course_detail'),
path('contact/',views.contact,name='contact'),
path('about/',views.about,name='about'),
path('course/',views.course,name='course'),
path('allFormation/',views.allFormation,name='allFormation'),
]