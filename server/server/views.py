from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Role

def get_all_users(request):

    # Create three users
    user1 = User.objects.create(name='User1', email='user1@example.com', password='password1', role=Role.USER.value)
    user2 = User.objects.create(name='User2', email='user2@example.com', password='password2', role=Role.USER.value)
    admin_user = User.objects.create(name='Admin', email='admin@example.com', password='adminpassword', role=Role.ADMIN.value)

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
