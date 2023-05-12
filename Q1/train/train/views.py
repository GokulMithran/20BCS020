from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from flask import redirect
import requests
import requests
import time
from rest_framework import status
from rest_framework.response import Response

def index(request):
          return render(request,'register.html')

def login(request):
                companyName=request.POST.get('companyName')
                ownerName=request.POST.get('ownerName')
                rollNo=request.POST.get('rollNo')
                ownerEmail=request.POST.get('ownerEmail')
                accessCode=request.POST.get('accessCode')
                print(companyName)
                attempt_num = 0  # keep track of how many times we've retried
                while attempt_num < 10:
                            url = 'http://104.211.219.98/train/register'
                            payload = {'Token':'My_Secret_Token',"companyName":companyName,"ownerName":ownerName,"rollNo":rollNo,"ownerEmail":ownerEmail,"accessCode":accessCode}
                            r = requests.post(url, data = payload)
                            if r.status_code == 200:
                                data = r.json()
                                return Response(data, status=status.HTTP_200_OK,)
                            else:
                               attempt_num += 1
                # You can probably use a logger to log the error here
                            time.sleep(5)  # Wait for 5 seconds before re-trying
                            return Response({"error": "Request failed"}, status=r.status_code)
                else:
                     return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)

                # return redirect("http://104.211.219.98/train/register")
                # return render(request,'http://104.211.219.98/train/register',{"companyName":companyName,"ownerName":ownerName,"rollNo":rollNo,"ownerEmail":ownerEmail,"accessCode":accessCode})
                # url='http://104.211.219.98/train/register'
                # response
# def users(request):
#     #pull data from third party rest api
#     response = requests.get('http://104.211.219.98/train/register')
#     #convert reponse data into json
#     users = response.json()
#     print(users)
#     # return render(request, "users.html")
      