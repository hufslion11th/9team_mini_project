import board.views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = "groups"

urlpatterns = [
    path('main/', board.views.main, name="main"),
    path('detail/<int:pk>', board.views.detail, name="detail"),
    path('register/', board.views.register),
    path('search/', board.views.search),

]

