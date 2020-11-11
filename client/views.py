from django.shortcuts import render

# Create your views here.
def list_client(request):
    return render(request,'client/client.html')
