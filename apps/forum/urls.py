from django.urls import path
from django.conf.urls import include, url

from . import views
from .views import ForumIndexView
from .views import CategoryDetailView
from .views import TopicDetailView
from .views import CreateTopic
from .views import CreateReply

app_name = 'forum'

urlpatterns = [
    path('', ForumIndexView.as_view(), name='index'),
    #../category/5
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('topic/create_topic/<int:pk>', CreateTopic.as_view(), name='create_topic'),
    #../topic/5
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic'),
    path('topic/<int:pk>/reply', CreateReply.as_view(), name='reply'),
]