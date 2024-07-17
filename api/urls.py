from django.urls import path
from . import views
from .views import JobTrackerView

urlpatterns = [
    path("api/example_get", views.example_get, name="example-get-function"),
    path("api/job_trackers", JobTrackerView.as_view(), name="view__job_trackers"),
    path("api/job_trackers/<uuid:pk>", JobTrackerView.as_view(), name="view__job_tracker"),
    path("api/metrics", views.get_metrics, name="prometheus-custom-get-metrics-endpoint"),
]