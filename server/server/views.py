from django.shortcuts import render
from django.http import JsonResponse
from .models import User

def get_all_users(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        user_list.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'role': user.role
        })
    return JsonResponse({'users': user_list})
