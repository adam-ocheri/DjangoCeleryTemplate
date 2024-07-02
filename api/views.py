from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import JobTracker
from .serializers import JobTrackerSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def my_get(request):
    my_value = request.GET.get("my_value") # read `?my_value=`
    
    return Response({"message": f"hello! | {my_value}"}, status=status.HTTP_200_OK)
    
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