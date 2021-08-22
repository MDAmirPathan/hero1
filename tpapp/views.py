from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.

class Home(View):
    def post(self, request):
        return HttpResponse('sucsess!!!!')

    def get(self, request):
        return render(request, 'home.html')
