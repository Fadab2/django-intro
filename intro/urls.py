from django.urls import path
from .views import HomePageView, AboutPageView,  ContactPageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
]

urlpatterns += staticfiles_urlpatterns()