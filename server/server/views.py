from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Role, Project
from django.views.decorators.csrf import csrf_exempt  
import json


@csrf_exempt
def get_all_users(request):

    # # Create three users
    # user1 = User.objects.create(name='User1', email='user1@example.com', password='password1', role=Role.USER.value)
    # user2 = User.objects.create(name='User2', email='user2@example.com', password='password2', role=Role.USER.value)
    # admin_user = User.objects.create(name='Admin', email='admin@example.com', password='adminpassword', role=Role.ADMIN.value)

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

@csrf_exempt
def create_project(request):
    if request.method == 'POST':
        rq = json.loads(request.body.decode('utf-8'))

        print(rq, "\n\n")


        user_email = rq['user_email']
        project_name = rq['name']
        project_description = rq['description']

        print (user_email)
        print (project_name)
        try:
            # Get the user object with the provided email
            user = User.objects.get(id=user_email)
            
            # Check if project_name is not None
            if project_name is None:
                return JsonResponse({'success': False, 'message': 'Project name is required.'}, status=400)

            # Create the project
            project = Project.objects.create(name=project_name, description=project_description, user=user)
            
            return JsonResponse({'success': True, 'message': 'Project created successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User with provided email does not exist.'})

    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed.'})
