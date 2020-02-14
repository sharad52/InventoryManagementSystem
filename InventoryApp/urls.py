from django.urls import path
from .views import HomeView,add_assets,edit_assets,delete_assets

app_name='baseapp'

urlpatterns = [

    
    path('home/',HomeView.as_view(),name='index'),
    path('home/add/',add_assets,name='add_assets'),
    path('home/edit/<int:good_id>',edit_assets,name='edit_assets'),
    path('home/delete/<int:good_id>',delete_assets,name='delete_assets')



]
