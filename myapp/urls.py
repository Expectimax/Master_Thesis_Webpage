from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("user_data_input/", views.user_data_input, name='user_data_input'),
    path("gallery_euclidian/", views.gallery_euclidian, name='gallery_euclidian'),
    path("gallery_social/", views.gallery_social, name='gallery_social'),
    path("gallery_pheno/", views.gallery_pheno, name='gallery_pheno'),
    path("gallery_intuitive/", views.gallery_intuitive, name='gallery_intuitive'),
    path("view_image/<str:pk>", views.view_image, name='view_image'),
    path("add_image/", views.add_image, name='add_image'),
    path("final_page/", views.final_page, name='final_page'),
    path("update_model_fields/", views.update_model_fields, name='update_model_fields'),
]
