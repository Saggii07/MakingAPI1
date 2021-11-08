from django.urls import path
from .views import ListAdvisor, DetailAdvisor,BookedAdvisor,BookedAdvisorList

urlpatterns = [

    path('advisors/',ListAdvisor.as_view(),name="advisors"),
    path('advisors/<int:pk>/',DetailAdvisor.as_view(),name="detailadvisors"),

    
    path('user/list/advisor',BookedAdvisor.as_view(),name="bookinglist"),
    path('user/<int:pk>/advisor',BookedAdvisorList.as_view(),name="booking"),
    

]
