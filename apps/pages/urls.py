from django.urls import path
from apps.pages.views.home import HomeView

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]