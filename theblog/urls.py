from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, AddCommentView,SearchResultsView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',AddPostView.as_view(), name='add_post' ),
    path('add_category/',AddCategoryView.as_view(), name='add_category' ),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category_list'),
    # path('like/<int:pk>', LikeView, name='like_post')
    # path('update_avatar/',UpdateAvatar.as_view(), name='update_avatar')
    path('article/<int:pk>/comment',AddCommentView.as_view(), name='add_comment' ),
    path('search/', SearchResultsView, name='search_results'),
]

