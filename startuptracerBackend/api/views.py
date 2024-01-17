from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import StartupProgress
from rest_framework import status
from .serializers import StartupSerializers
# Create your views here.

def Home(request):
        return JsonResponse({'response':'Hello world.Welcome to my Django Project.'})


class StartupTracer(APIView):
        def post(self,request):
                ProgressReport=StartupSerializers(StartupProgress.objects.filter(Applicant_id__username=request.data['username']).all(),many=True)
                return JsonResponse({"response":ProgressReport.data},status=status.HTTP_200_OK)

def git_update(request):
    repo = git.Repo('./Startup-Tracer')
    origin = repo.remotes.origin
    repo.create_head('main',origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return JsonResponse({})