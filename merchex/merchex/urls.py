from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
path('admin/', admin.site.urls),
path('bands/', views.band_list),
path('about-us/', views.about),
]