from django.urls import path
from .views import BookedAdvisorDetail, ListAdvisor, DetailAdvisor,BookedAdvisor

urlpatterns = [
    # advisor adding please use :  api/v1/advisors    for add the advisor
    path('advisors/',ListAdvisor.as_view(),name="advisors"),
    path('advisors/<int:pk>/',DetailAdvisor.as_view(),name="detailadvisors"),

    # advisor booking and  booked advisors List with specific user
    path('user/list/advisor',BookedAdvisor.as_view(),name="bookinglist"),
    path('user/<int:pk>/advisor',BookedAdvisorDetail.as_view(),name="booking"),
    

]
