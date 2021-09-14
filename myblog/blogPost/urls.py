from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('postDetail/<str:pk>',views.postDetail,name='postDetail'),
    path('createPost/',views.createPost,name='createPost'),
    path('deletePost/<str:pk>',views.deletePost,name='deletePost'),
    path('updatePost/<str:pk>',views.updatePost,name='updatePost'),
    path('createCatagory/',views.createCatagory,name='createCatagory'),
    path('catagory/<str:pk>',views.catagoryPage,name='catagory'),

]