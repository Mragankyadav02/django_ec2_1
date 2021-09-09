from django.shortcuts import render
import boto3
import os

# Create your views here.
def home(request):
    return render(request, 's3_upload/home.html')
def upload(request):

    target_lang = request.GET.get('language')
    filename = request.GET.get('file')
    #path = os.path.abspath(filename)
    path = 'C:/a/' + filename

    s3_client = boto3.client('s3')
    file_name = path
    bucket = 'awstranslationoutput'
    object_name = filename
    response = s3_client.upload_file(file_name, bucket, object_name)

    return render(request,'s3_upload/path.html',{'path' : path})
