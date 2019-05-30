from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
	return render(request,"home.html",{})



def add(request):
	if request.method=="POST":
		a = request.POST.get('val1', False)
		b = request.POST.get('val2', False)
	request.POST.get('submit',False)
	if request.POST.get('ad',False)=='add':
		try:
			if  a and b:
				return render(request,"home.html",{'p':int(a)+int(b)})
			else:
				return render(request,"home.html",{'p':"please enter data"})
		except Exception:
			return render(request,"home.html",{'p':"INVALID DATA"})
	if request.POST.get('su',False)=='sub':
		try:
			if  a and b:
				return render(request,"home.html",{'p':int(a)-int(b)})
			else:
				return render(request,"home.html",{'p':"please enter data"})
		except Exception as e:
			return render(request,"home.html",{'p':"INVALID DATA"})	

	if request.POST.get('mu',False)=='multiply':
		try:
			if  a and b:
				return render(request,"home.html",{'p':int(a)*int(b)})
			else:
				return render(request,"home.html",{'p':"please enter data"})
		except Exception as e:
			return render(request,"home.html",{'p':"INVALID DATA"})	

	if request.POST.get('di',False)=='div':
		try:
			if  a and b:
				return render(request,"home.html",{'p':int(a)/int(b)})
			else:
				return render(request,"home.html",{'p':"please enter data"})
		except Exception as e:
			return render(request,"home.html",{'p':"INVALID DATA"})	

	if request.POST.get('mo',False)=='modulo':
		try:
			if  a and b:
				return render(request,"home.html",{'p':int(a)%int(b)})
			else:
				return render(request,"home.html",{'p':"please enter data"})
		except Exception as e:
			return render(request,"home.html",{'p':"INVALID DATA"})	

