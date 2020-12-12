from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def signupfunc(request):

    # Userモデルから取得したデータをobject_listに格納している
    object_list = User.objects.all()
    print(object_list)
    if request.method == "POST":
        print('This is post function')
    else:
        print('This is not post method')
    return render(request, 'signup.html', {'some':100})

