from django.contrib import admin
from django.urls import path,include
from myAPI.views import RegistrationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from myAPI import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('myAPI.urls')),
    path('user/register/',RegistrationAPIView.as_view(),name='register'),
    path('user/login/',TokenObtainPairView.as_view(),name='login'),
    path('user/<int:pk>/advisor',views.AdviserList.as_view(),name='getadviserlist')
    
   

]
