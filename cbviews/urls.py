from django.urls import path
from .views import PostList, PostUpdateView, PostCreateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view(), name='my_list_view'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='my_update_view'),
    path('create/', PostCreateView.as_view(), name='create_view'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete_view'),
    path('create/', PostCreateView.as_view(), name='create_view'),
]
