from django.urls import path
from .views import IdeaListView,IdeaDetailView,IdeaCreateView,IdeaUpdateView,IdeaDeleteView
from .import views

urlpatterns = [
    path('', IdeaListView.as_view(), name='idea-list'),
    path('<int:pk>/', IdeaDetailView.as_view(), name='idea-detail'),
    path('new/', IdeaCreateView.as_view(), name='idea-create'),
    path('<int:pk>/update/', IdeaUpdateView.as_view(), name='idea-update'),
    path('<int:pk>/delete/', IdeaDeleteView.as_view(), name='idea-delete'),
]