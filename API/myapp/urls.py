from django.contrib import admin
from django.urls import path
from .views import Get_API, Post_API, Put_API, Patch_API, Delete_API
urlpatterns = [
    path("admin/", admin.site.urls),
    path('GET/', Get_API),
    path('POST/', Post_API),
    path("PUT/<int:id>/",Put_API),
    path("PATCH/<int:id>/",Patch_API),
    path("DELETE/<int:id>/",Delete_API),
    
]
