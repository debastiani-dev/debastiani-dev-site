from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.portfolio.models import Project

class StaticViewSitemap(Sitemap):
    """Sitemap for static pages like Home and About"""
    priority = 0.5
    changefreq = "monthly"

    def items(self):
        # These match the 'name' in your urls.py
        return ["pages:home", "pages:about", "portfolio:list"]

    def location(self, item):
        return reverse(item)

class ProjectSitemap(Sitemap):
    """Sitemap for dynamic project pages"""
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        # Only include projects that are visible/featured
        return Project.objects.filter(is_featured=True)

    def lastmod(self, obj):
        # Tells Google when the page was last updated
        return obj.modified_at
    
    def location(self, obj):
        return reverse("portfolio:detail", kwargs={"pk": obj.pk})