from django.contrib import admin
from django.urls import path
from .views import ProductView,ProductDetailView,field_lookup,CategoryDetailView

urlpatterns = [
    
    path('Products/',ProductView.as_view()),
    path('Products/<int:pk>',ProductDetailView.as_view(),name="productdetail"),
    path('productlookup/',field_lookup),
    path('category/<slug:slug>',CategoryDetailView.as_view(),name="category")

]