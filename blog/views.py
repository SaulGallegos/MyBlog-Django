from django.shortcuts import render

##############
#### HOME ####
##############
def home(request):
     context = {
          
     }
     return render(request, 'home.html', context)