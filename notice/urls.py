from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('list/', views.CommentNoticeListView.as_view(), name='list'),
    path('udpate/', views.CommentNoticeUpdateView.as_view(), name='update'),
]
