from django.urls import path,re_path
from . import api_views
urlpatterns = [
    path('', api_views.BlogList.as_view()),
    re_path('detail/(?P<slug>[\w-]+)/', api_views.BlogDetail.as_view()),
    re_path('tag/(?P<slug>[\w-]+)/', api_views.BlogTagList.as_view()),
]
