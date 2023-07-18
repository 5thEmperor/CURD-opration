from django.shortcuts import render, get_object_or_404,redirect
from .models import User
from .forms import UserForm
from django.db.models import Q

def hello(request):
    return render(request, 'hello.html')

def users(request):
    user_list = User.objects.all()
    return render(request, 'users.html', {'user_list': user_list})

def new_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        role = request.POST['role']
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'new_user.html', {'error': 'Email already exists.'})
        
        user = User(name=name, email=email, role=role)
        user.save()
        return render(request, 'new_user_success.html')
    
    return render(request, 'new_user.html')



def delete_user(request, user_id):
    # Retrieve the user object with the given user_id
    user = get_object_or_404(User, pk=user_id)
    
    if request.method == 'POST':
        # Delete the user object
        user.delete()
        # Redirect to the user list page or any other desired page
        return redirect('users')

    return render(request, 'confirm_delete.html', {'user': user})
def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    form = UserForm(request.POST or None, instance=user)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('users')
    
    return render(request, 'update_user.html', {'form': form,'user_id':user_id})


def user_list(request):
    user_list = User.objects.all()
    return render(request, 'users.html', {'user_list': user_list})

from django.shortcuts import render
from .models import User

def search_users(request):
    if 'search' in request.GET:
        search_query = request.GET['search']
        try:
            # Check if the search query can be converted to an integer (ID search)
            if search_query.isdigit():
                user = User.objects.get(Q(id=int(search_query)) | Q(email__icontains=search_query))
            else:
                user = User.objects.get(Q(name__icontains=search_query) | Q(email__icontains=search_query))
            return render(request, 'search_user.html', {'user': user})
        except User.DoesNotExist:
            message = 'User not found. Please try a different ID, name, or email.'
            return render(request, 'search_user.html', {'message': message})

    return render(request, 'search_user.html')
