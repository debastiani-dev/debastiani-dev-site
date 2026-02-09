from django.urls import path
from apps.portfolio.views.projects import ProjectListView, ProjectDetailView

app_name = "portfolio"

urlpatterns = [
    path("", ProjectListView.as_view(), name="list"),
    path("<uuid:pk>/", ProjectDetailView.as_view(), name="detail"),
]