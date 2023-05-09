from django.urls import path
from resttest.views import F1DriverCreateView, F1DriverList, F1DriverUpdateView

urlpatterns = [
    path('create-f1driver/', F1DriverCreateView.as_view(), name='create-f1driver'),
    path('f1drivers/', F1DriverList.as_view(), name='f1driver-list'),
    path('f1drivers/<int:pk>/', F1DriverUpdateView.as_view(), name='f1driver_update'),
]
