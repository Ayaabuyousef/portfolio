from django.shortcuts import render
def myport(request):
    return render(request, 'myport.html', {})
# Create your views here.
