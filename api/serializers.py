from rest_framework import serializers
from .models import JobTracker

class JobTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTracker
        fields = "__all__"
