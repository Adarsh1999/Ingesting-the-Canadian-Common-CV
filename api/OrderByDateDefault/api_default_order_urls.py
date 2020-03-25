from django.conf.urls import url
from .api_default_order_views import DefaultOrder
urlpatterns = [
  url('', DefaultOrder.as_view(), name='getting_sort_by_view'),
]