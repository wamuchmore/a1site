from django.urls import path
from . import views

app_name = "catalog"
urlpatterns = [
    
    path("catalog_cards/", views.catalog_cards, name="catalog_cards"),
    path("catalog_list/", views.catalog_list, name="catalog_list"),
    path("catalog_detail/<int:pk>/", views.catalog_detail, name="catalog_detail"),
    path("catalog_edit/<int:pk>/", views.catalog_edit, name="catalog_edit"),
    path("catalog_add/", views.catalog_add, name="catalog_add"),
]