from django.urls import path
from .views import *

gas_company_CRUD = GasCompanyView.as_view({
    'get': 'list',
    'post': 'create'
})

gas_company_detail_CRUD = GasCompanyView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

gas_company_admin_CRUD = GasCompanyAdminView.as_view({
    'get': 'list',
    'post': 'create'
})

gas_company_admin_detail_CRUD = GasCompanyAdminView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

gas_company_employee_GET_POST = GasCompanyEmployeeView.as_view({
    'get': 'list',
    'post': 'create'})

gas_company_employee_detail_CRUD = GasCompanyEmployeeView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('get_post/', gas_company_CRUD),
    path('get_update_delete/<pk>/', gas_company_detail_CRUD),
    path('admin/get_post/', gas_company_admin_CRUD),
    path('admin/get_update_delete/<pk>/', gas_company_admin_detail_CRUD),
    path('employee/get_post/', gas_company_employee_GET_POST),
    path('employee/get_update_delete/<pk>/', gas_company_employee_detail_CRUD)
]


