from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
	res = {
		"code": 0,
		"msg": "成功success",
		"data": []
	}
	# return HttpResponse("hello world!")
	return JsonResponse(res, json_dumps_params={"ensure_ascii": False})
