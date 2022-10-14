

from django.urls import path
from ofdload.views import *

urlpatterns = [
    #path('', get_data_kkts, name='get_data_kkts'),
    path('', get_company_list, name='get_company_list'),
    path('company/<int:pk>/', get_data_kkts, name='get_data_kkts'),
    path('info', kkt_info, name='kkt_info'),
    path('collation', kkt_collation, name='collation'),

    #path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]