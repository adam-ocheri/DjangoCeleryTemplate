from django.urls import path
from . import views
from .views import JobTrackerView

urlpatterns = [
    # path("", views.home, name="home"),
    path("api/my_get", views.my_get, name="example-get-function"),
    path("api/job_trackers", JobTrackerView.as_view(), name="view__job_trackers"),
    path("api/job_trackers/<uuid:pk>", JobTrackerView.as_view(), name="view__job_tracker"),
]