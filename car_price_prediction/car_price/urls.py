
from django.urls import path
from .views import Login,home, user_input,Signup, show_results



urlpatterns = [
    path('',home,name='home'),
    path('user_input/',user_input,name ='user-input'),
    path('login/',Login),
    path('signup/',Signup),
    path('results/',show_results, name='show-results')
    
]
