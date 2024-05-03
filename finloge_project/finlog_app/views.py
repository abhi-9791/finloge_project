from django.shortcuts import render

def index_page(request):
    '''
        this function represents index page
    '''
    return render(request,'index.html')