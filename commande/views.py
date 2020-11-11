from django.shortcuts import render

# Create your views here.
def list_commande(request):
    return render(request,'commande/commande.html')
