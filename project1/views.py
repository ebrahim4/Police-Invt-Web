from django.shortcuts import render
from django.http import HttpResponse
from .models import case

def home(request):
     return render(request,'project1/homepage.html')
def login(request):
     return render(request,'project1/login.html')
def investigate(request):
     return render(request,'project1/investigate.html')
def addcase(request):
     if request.method == 'POST':
            if request.POST.get('case_id') and request.POST.get('crime_date') and request.POST.get('victim_name') and request.POST.get('io_name') and request.POST.get('io_id') and request.POST.get('victim_id') and request.POST.get('crime_loc') and request.POST.get('category') :
                post=case()
                post.case_id= request.POST.get('case_id')
                post.victim_name=request.POST.get('victim_name')
                post.io_name=request.POST.get('io_name')
                post.crime_date= request.POST.get('crime_date')
                post.io_id=request.POST.get('io_id')
                post.category=request.POST.get('category')
                post.victim_id=request.POST.get('victim_id')
                post.crime_loc=request.POST.get('crime_loc')
                post.save()
                
                return render(request, 'project1/addcase.html')  

     else:
                return render(request,'project1/addcase.html')
      
                
    

