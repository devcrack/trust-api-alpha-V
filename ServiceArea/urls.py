from django.urls import path
from .views import *

service_area_Get_Post = ServiceAreaview.as_view({
    'get': 'list',
    'post': 'create'
})

service_area_detail_CRUD = ServiceAreaview.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('get_post/', service_area_Get_Post),
    path('get_update_delete/<pk>/', service_area_detail_CRUD),
]
