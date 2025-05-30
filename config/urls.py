# config/urls.py

"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from config.settings import THE_SITE_NAME

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="home.html",
            extra_context={"the_site_name": THE_SITE_NAME},
        ),
        name="home",
    ),
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("journals/", include("self_enquiry.urls")),
    path("vitals/", include("vitals.urls")),
    path("app-tracker/", include("app_tracker.urls")),
    path("cbt/", include("cbt.urls")),
    path("pharma-tracker/", include("pharma_tracker.urls")),
    path("unimportant-notes/", include("unimportant_notes.urls")),
    path("activity-tracker/", include("activity_tracker.urls")),
    path("project-manager/", include("project_manager.urls")),
    path("goals/", include("goals.urls")),
    path("pi-tracker/", include("pi_tracker.urls")),
    path("uc-goals/", include("uc_goals.urls")),
    path("journal/", include("journal.urls")),
    path("sonic-text/", include("sonic_text.urls")),
    path("boosts/", include("boosts.urls")),
    path("plan-it/", include("plan_it.urls")),
    path("do-it/", include("do_it.urls")),
    path("pomodo/", include("pomodo.urls")),
    path("storages/", include("storage.urls")),
]
