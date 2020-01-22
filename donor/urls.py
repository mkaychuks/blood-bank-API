from django.urls import path

from .views import (
    UserList, DonorList, DonorCreateDetails, UserDetail, DonorEditDetails
)


urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('user/profile/', UserDetail.as_view(), name='user-detail'),
    path('donors/', DonorList.as_view(), name='donor-list'),
    path('create-details/', DonorCreateDetails.as_view(), name='create-details'),
    path('edit-details/<pk>/', DonorEditDetails.as_view(), name='edit-details'),
]
