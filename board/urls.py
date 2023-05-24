import board.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('main/', board.views.main),
    path('detail/', board.views.detail),
    path('register/', board.views.register),
    path('search/', board.views.search),

]

