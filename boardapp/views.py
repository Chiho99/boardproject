from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def signupfunc(request):
    print(request.POST)
    # Userモデルから取得したデータをobjectに格納している
    object = User.objects.get(username="chiho")
    print(object.email)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
    return render(request, 'signup.html', {'some':100})

