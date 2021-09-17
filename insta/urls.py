from django.urls import path

from .views import PostListView, PostCreateView, PostDetailView




app_name = 'insta'




urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('newpost/', PostCreateView.as_view(), name='new_post'),
    path('detail/', PostDetailView.as_view(), name='detail_post')
]
