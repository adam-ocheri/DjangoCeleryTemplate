from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import JobTracker
from .serializers import JobTrackerSerializer
from rest_framework import status
from django.http import HttpResponse
import requests

# Create your views here.
@api_view(['GET'])
def example_get(request):
    example_value = request.GET.get("example_value") # this reads `?example_value=` query-param
    
    return Response({"message": f"hello! | {example_value}"}, status=status.HTTP_200_OK)

# Custom Prometheus scraping route - using exposed flower json data and converting it to prometheus metrics format
@api_view(['GET'])
def get_metrics(request):
    try:
        # Make request to flower metrics route and get json data
        url = "http://flower:5555/api/workers?refresh=1"
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        response = requests.get(url, headers)
        data = response.json()

        # declarations of stats to be used
        worker_up_metrics = [
            '# HELP worker_uptime Status of worker health',
            '# TYPE worker_uptime gauge',
        ]
        active_queues_metrics = [
            '# HELP active_queues Number of active queues',
            '# TYPE active_queues counter',
        ]
        total_active_workers_metrics = [
            '# HELP num_active_workers Number of active workers',
            '# TYPE num_active_workers counter',
        ]
        result_metrics = []
        num_active_workers = 0

        # iterate over each celery worker
        for idx, worker in enumerate(data):
            num_active_workers = num_active_workers + 1
            
            # set worker_uptime (per worker)
            worker_up_time = data[worker]["stats"]["uptime"]
            result_metrics += worker_up_metrics
            result_metrics.append(f'worker_uptime{{worker="{worker}"}} {worker_up_time}') 

            # set num active queues (per worker)
            active_queues : list = data[worker]["active_queues"]
            num_active_queues = len(active_queues)
            result_metrics += active_queues_metrics
            result_metrics.append(f'active_queues{{worker="{worker}"}} {num_active_queues}') 

        # set total num of active celery workers
        result_metrics += total_active_workers_metrics
        result_metrics.append(f'num_active_workers {num_active_workers}') 

        # stringify the result_metrics array, using line seperation
        result = '\n'.join(result_metrics)

        return HttpResponse(result, content_type='text/plain', status=200)

    except Exception as e:
        return Response(data={"EXCEPTION": e.__str__()}, status=400)

class JobTrackerView(APIView):
    def get(self, request, pk=None, format=None):
        try:
            if pk != None:
                item = JobTracker.objects.get(pk=pk)
                serializer = JobTrackerSerializer(item)
            else:
                items = JobTracker.objects.all()
                serializer = JobTrackerSerializer(items, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = JobTrackerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk, format=None):
        try:
            item = JobTracker.objects.get(pk=pk)
        except JobTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = JobTrackerSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            item = JobTracker.objects.get(pk=pk)
        except JobTracker.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)