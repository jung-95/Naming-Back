from django.urls import path
from .views import *

app_name = 'dictionary'

urlpatterns = [
    path('', dictionaryMakeView.as_view()),
    path('<int:pk>/', dictionaryView.as_view()),
    path('<int:pk>/post/', postListView.as_view()),
    path('<int:pk>/post/<int:post_pk>', postDeleteView.as_view()),
    path('<int:pk>/post/<int:post_pk>/like', postLikeView.as_view()),
    path('<int:pk>/people/', NicknameListView.as_view()),
    path('search/', SearchView.as_view()),
]