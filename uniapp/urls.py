from django.urls import path

from uniapp import views

urlpatterns = [
   path('chat_with_unihelp/' , views.chat_with_unihelp , name="chat_with_unihelp")
    
]
