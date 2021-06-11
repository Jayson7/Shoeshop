from auths import views
from django.urls import path, include

from auths import views
from auths.views import Register

urlpatterns = [
    path('', Register.as_view(), name="register"),
    

]
