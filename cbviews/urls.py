from django.urls import path
from .views import PostList, PostUpdateView

urlpatterns = [
    path('', PostList.as_view(), name='my_list_view'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='my_update_view'),
]

