from django.urls import path,re_path
from . import api_views
urlpatterns = [
    path('home/',api_views.HomeViews.as_view()),
    path('about/',api_views.AboutViews.as_view()),
    path('', api_views.BlogList.as_view()),
    path('site/',api_views.MySiteDatas.as_view()),
    path('book/',api_views.BookList.as_view()),
    re_path('detail/(?P<slug>[\w-]+)/', api_views.BlogDetail.as_view()),
    re_path('tag/(?P<slug>[\w-]+)/', api_views.BlogTagList.as_view()),
]
