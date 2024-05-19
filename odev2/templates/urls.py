from django import views 
from django.urls import path
from . import views #aynı klasordekı vıews .

urlpatterns = [
  
    path ('', views.index, name='index'),

    path('register/', views.register, name='register'),  # Register page
    path('login/', views.login, name='login'),  # Login page  
    path('logout/', views.logout, name='logout'), 

    path ('index/', views.index, name='indexUser'), 

    path('blog/', views.blog, name='blog'),
    path ('add_blog' , views.add_blog , name = 'add_blog'),
    path('blog-single-post/<int:pk>/', views.singleBlog, name='single_post'), 

    path ('industries/' , views.industries , name = 'industries'),
    path ('add_industry' , views.add_industry , name = 'add_industry'),
    path('single-industry/<int:pk>/', views.singleIndustry, name='single_industry'),
    path('loginCustom/', views.show_login_popup, name='my_custom_login_page'),

    ]

   