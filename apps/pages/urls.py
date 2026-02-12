from django.urls import path
from apps.pages.views.home import HomeView
from apps.pages.views.about import AboutView

app_name = "pages"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
]