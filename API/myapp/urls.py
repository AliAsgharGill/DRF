from django.contrib import admin
from django.urls import path
from .views import Get_API, Post_API, Put_API, Patch_API, Delete_API, Get_Student
urlpatterns = [
    path("admin/", admin.site.urls),
    path('GET/', Get_API),
    path("GET_STUDENT/<int:id>/",Get_Student),
    path('POST/', Post_API),
    path("PUT/<int:id>/",Put_API),
    path("PATCH/<int:id>/",Patch_API),
    path("DELETE/<int:id>/",Delete_API),
    
]
