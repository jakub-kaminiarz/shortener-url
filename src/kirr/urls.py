from django.contrib import admin
from django.urls import path, re_path

from shortener.views import kirr_redirect_view, HomeView



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view()),
    re_path(r'^(?P<shortcode>[\w-]+)/$', kirr_redirect_view, name='url_shortcode'),
    
]
