# from django.contrib.auth.signals import user_logged_in
# import json 
# from datetime import datetime
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
# from django.contrib.auth import authenticate,login 
# import jwt
# from rest_framework_jwt.serializers import jwt_payload_handler
# from django.contrib.auth.hashers import make_password
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response	
# from django.contrib.auth.models import User


# class LoginView(APIView):
# 	def post(self,request):
# 		print("/*/*/**/*/*/*/*/*/*/*/*/*/",request.body)
# 		#try:
# 		email = json.loads(request.body.decode("utf-8"))['username']
# 		password =  json.loads(request.body.decode("utf-8"))['password']
# 		auth = authenticate(self.request,username=email,password=password)
# 		if auth is not None:
# 			try:
# 				check_user = User.objects.filter(username=email,verify_email=True,is_active=True)
# 				#print("/*/*/*/ checked user",check_user)
# 				if check_user:
# 					for i in check_user:
# 						payload = jwt_payload_handler(i)
# 						token = jwt.encode(payload, settings.JWT_SECRET_KEY)
# 						user_details = {}
# 						# user_details['first_name'] = "%s" % (i.first_name)
# 						# user_details['last_name'] = "%s" % (i.last_name)
# 						user_details['username'] = "%s" % (i.username)
# 						user_details['token'] = token
# 						user_logged_in.send(sender=i.__class__,request=request, user=i)
# 						return Response(user_details, status=status.HTTP_200_OK)
# 				else:
# 					res = {
# 					'error': 'Invalid credentials'
# 					}
# 					return JsonResponse(res,safe=False)

# 			except Exception as e:
# 				return JsonResponse({'error':'Your account is not activated kindly check your mail'},safe=False)
# 		else:
# 			res = {
# 			'error': 'Invalid credentials'}
# 			return JsonResponse(res,safe=False)