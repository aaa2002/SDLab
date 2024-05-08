from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Role, Project
from django.views.decorators.csrf import csrf_exempt  

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
        # Get user email from request data
        user_email = request.POST.get('user_email')

        print(user_email)

        try:
            # Get the user object with the provided email
            user = User.objects.get(email=user_email)
            
            # Create the project
            project_name = request.POST.get('name')
            project_description = request.POST.get('description')
            project = Project.objects.create(name=project_name, description=project_description, user=user)
            
            return JsonResponse({'success': True, 'message': 'Project created successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User with provided email does not exist.'})

    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed.'})