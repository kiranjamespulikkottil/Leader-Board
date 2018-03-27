from django.urls import path

from . import views

urlpatterns = [
    path('', views.ScoreListView.as_view(), name='home'),
    path('score/<pk>/', views.ScoreDetailView.as_view(), name='score_detail'),
    path('userscores/', views.scoreUserView, name='score_user'),
    path('new/', views.ScoreCreateView.as_view(), name='score_new'),
    path('score/<pk>/update/', views.ScoreUpdateView.as_view(), name='score_update'),
    path('score/<pk>/delete/',views.ScoreDeleteView.as_view(), name='score_delete'),
]
