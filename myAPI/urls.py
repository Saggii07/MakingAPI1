from django.urls import path
from .views import ListAdvisor, DetailAdvisor,BookedAdvisor

urlpatterns = [

    path('advisors/',ListAdvisor.as_view(),name="advisors"),
    path('advisors/<int:pk>/',DetailAdvisor.as_view(),name="detailadvisors"),
    path('user/<int:pk>/advisor',BookedAdvisor.as_view(),name="booking"),
    

]
