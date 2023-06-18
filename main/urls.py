from django.urls import path

from .views import PostList, PostDetail, PostCreate, PostUpdate, APIpost, api_detail_posts, post_comment




urlpatterns = [

    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('api/posts/', APIpost.as_view(), name='api_posts'),
    path('api/posts/<int:pk>/', api_detail_posts, name='api_detail_posts'),
    path('<int:post_id>/comment/', post_comment, name='post_comment'),

]
