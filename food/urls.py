from django.urls import path
from . import views

#namespacing
app_name = 'food'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:item_id>/', views.detail, name="detail"),
    path('item/', views.item, name="item"),
]