from django.shortcuts import render

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        print('This is post function')
    else:
        print('This is not post method')
    return render(request, 'signup.html', {'some':100})
