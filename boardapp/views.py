from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def signupfunc(request):

    # Userモデルから取得したデータをobjectに格納している
    object = User.objects.get(username="chiho")
    print(object.email)
    if request.method == "POST":
        print('This is post function')
    else:
        print('This is not post method')
    return render(request, 'signup.html', {'some':100})

