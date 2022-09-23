from django.http import HttpResponse
from django.shortcuts import render
from .bincvt import decimalToBinary
import json
import requests
#from forms import Formss
def index(request):
    return render(request,'index.html')
def home(request,input):
    x = format(input)
    y = x.split(' ')
    t = int(y[0])
    l = int(y[1])
    k= decimalToBinary(t,l)
    ##for logic not using json
    #z1 = ""
    #for x1,y1 in k.items():   
        #z1 = z1 + str(x1) + str(" ") + str(y1) + str (" ;")
    return HttpResponse(json.dumps(k))  
    #json is used becuse hhtpresponse only returns string type and cannot return a dictionary
    #return HttpResponse(z1[0:len(z1)-1])
        
def calc(request):
    return render(request,'form.html')
def calcbin(request,pagename):
    return HttpResponse("hello {} {}".format(pagename, pagename) )
