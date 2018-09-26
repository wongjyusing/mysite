from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include
from . import api_views

router = DefaultRouter()
router.register(r'blog', api_views.BlogList)
router.register(r'blogtag', api_views.BlogTagList)



urlpatterns = [

    path('', include(router.urls))

]
