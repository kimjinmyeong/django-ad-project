from django.contrib import admin
from django.urls import include, path

from pybo.views import page_views
from common import home_page_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include("pybo.urls")),
    path("pybo/", page_views.index, name="index"),
    path("", home_page_views.HomeView.as_view(), name="home"),  # '/' 에 해당되는 path
    path("common/", include("common.urls")),
]
