from django.urls import path

# from .views import home, second_view,  post_detail, post_create
from .views import PostList, PostDetail, PostCreate, PostUpdate, api_posts

urlpatterns = [
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('', PostList.as_view(), name='home'),
    # path('second/', , name='second'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('api/posts/', api_posts, name='api_posts')


]
