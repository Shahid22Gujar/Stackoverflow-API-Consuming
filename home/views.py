from django.shortcuts import render
import json
from django.views.decorators.cache import cache_page
from ratelimit.decorators import ratelimit
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger
from .stackoverflow_api import stackoverflowapi

# Create your views here.
@cache_page(60 * 5)
@ratelimit(key='ip', rate='5/m', block=True,method="GET")
def home(request):
    if request.method == "GET":
        search=request.GET.get('search')
        page = request.GET.get('page', 1)
        
      
    result=stackoverflowapi(search)
    
    temp_data=json.loads(result)
    paginator = Paginator(tuple(temp_data.get('items')), 3)

    try:
        temp_data = paginator.page(page)
    
    except PageNotAnInteger:
        temp_data = paginator.page(1)
    except EmptyPage:
        temp_data= paginator.page(paginator.num_pages)

    context={'result':temp_data,'search':search}
    
    return render(request,'home.html',context=context)