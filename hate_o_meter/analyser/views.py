# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from .models import *
from .serializers import dataSerializer
import json
from .yo import runningFunc

# Create your views here.
def index(request):
	context={}
	return render(request, 'analyser/index.html', context)

class dataList(APIView):

	def get(self, request):
		answer=solution.objects.all()
		serial_sol=dataSerializer(answer, many=True)
		return Response(serial_sol.data)

	def post(self, request):
		request_data=request.data
		# for item in request_data['table']:
		# 	print(item['id'], item['message'])
		score, count = runningFunc(request_data)
		temp = ""
		warning = ""
		# if(count<150):
		# 	if(score<35.0):
		# 		temp+="Non Offensive Post"
		# 	else:
		# 		temp+="Offensive Post"
		# 		warning+="**WARNING Read at your own discretion.**"
		# else:
		if(score<10.0):
			temp+="Non Offensive Post"
		else:
			temp+="Offensive Post"
			warning+="**WARNING Read at your own discretion.**"
		return Response("Score: " + str(score) + "\n" + temp+"\n" + warning)
