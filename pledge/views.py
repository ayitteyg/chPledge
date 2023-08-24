from django.shortcuts import render, HttpResponse, redirect
#from django.http import HttpResponse, Http404,response
#from http import HTTPStatus
#from rest_framework import status,generics
#from rest_framework.response import Response
#from rest_framework.decorators import parser_classes
#from rest_framework.parsers import MultiPartParser
from .resources import RegisterResource,ReceiptsResource,PledgesResource,ExportFile
from django.db.models import Sum, F, Count
from django.db.models.functions import TruncMonth
import json
import pandas as pd
from .forms import loginform, Registerform,Pledgeform,receiptform
from .models import Register,Receipts,Pledges
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
#import datetime
from tablib import Dataset

# Create your views here.
def index(request):
    #return HttpResponse("Hello, You're view is rendering.")
    pass



def loginpage(request):

    user  = None
    form = loginform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            #action here
            #form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #authenticate and log user in at backend
            user = authenticate(username=username, password=password)
            #print(request.user)
            if user is not None:
                user_login(request, user)
                #print(request.user)
                return redirect ('homepage')

            else:
                messages.info(request, 'Username or Password is incorrect')
                return render (request, 'loginpage.html', {'form':form})
    else:
        form = loginform()
        user_logout(request)
        #print(request.user)
    return render (request, 'loginpage.html', {'form':form})





def registerpage(request):
    form = Registerform(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            #action here
            form.save()
            #print(form.cleaned_data)
            return redirect ('pledgesummary')
        else:
            messages.info(request, 'incorrect input / error')
            return render (request, 'registermemberpage.html', context)

    context = {'form':form}
    return render (request, 'registermemberpage.html', context)





def addpledge(request):
    form = Pledgeform(request.POST)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            #action here
            form.save()
            #print(form.cleaned_data)
            return redirect ('membersearch')
        else:
            messages.info(request, 'incorrect input / error')
            return render (request, 'addpledgepage.html', context)

    context = {'form':form}
    return render (request, 'addpledgepage.html', context)





def homepage(request):
    pyr = [ i['pdate'] for i in Pledges.objects.values('pdate').distinct()] #pledge dates
    ryr = [i['rdate'] for i in Receipts.objects.values('rdate').distinct()] #receipts dates
    
    yr = pyr+ryr #join the dates

    #print(yr)
  
    yrlst = list(set([i.strftime("%Y") for i in yr]))#get year list from date 
    yrlst.sort()

    #break down for datefilter
    #for years in yrlst:
        #q = Pledges.objects.filter(pdate__year=years) #filter by year
        #print(q)
        #t = q.values('pdate__year').annotate(total=Sum('pamount')) #get totals for each name
        #print(queryset)"""
    plg = [Pledges.objects.filter(pdate__year=years).values('pdate__year').annotate(total=Sum('pamount'), count=Count('name')) for years in yrlst]
    #print(plg)

    rct = [Receipts.objects.filter(rdate__year=years).values('rdate__year').annotate(total=Sum('ramount'), count=Count('rname')) for years in yrlst]
    #print(rct)

    context = {'yr':yrlst, 'plg':plg, 'rct':rct}
    return render (request, 'homepage.html', context)
    #return HttpResponse("hi") #for debug





def pledgesummary(request):
    plg = Register.objects.distinct().all()
    #print(plg)
    context = {'plg':plg}
    return render (request, 'pledgesumpage.html', context)




def monthlysum(request, yr):
    #print(yr)--debug
    mnths = [Receipts.objects.filter(rdate__year=yr).values('rdate__year') #filter by year
         .annotate(month=TruncMonth('rdate')).values('month') #group into month
         .annotate(total=Sum('ramount'), count=Count('ramount')).values('month', 'total', 'count') ] #sum values

    #print(mnths) #--debug
    context = {'yr':yr, 'mnths':mnths}
    return render (request, 'monthlysum.html', context)




def membersearch(request):
    mem = Register.objects.all()
    context = {'mem':mem}
    return render (request, 'membersearch.html', context)



def addreceipt(request, nm, id):
    #print(nm)
    form = receiptform(request.POST)
    context = {'form':form, 'name':nm}
    if request.method == 'POST':
        if form.is_valid():
            #action here
            #form.save()
            rdate = form.cleaned_data['date']
            ramount = form.cleaned_data['amount']
            rct = {'user':request.user, 'date':rdate, 'name':nm, 'amnt':ramount}

            #save to receipts data
            receipt,created = Receipts.objects.get_or_create(
                                            user=rct['user'],
                                            rdate=rct['date'],
                                            rname_id=id,
                                            ramount=rct['amnt'],
                                            )
            #receipt.save()
            return redirect ('pledgesummary')
        else:
            messages.info(request, 'incorrect input / error')
            return render (request, 'addreceiptpage.html', context)

    context = {'form':form, 'name':nm}
    return render (request, 'addreceiptpage.html', context)





def viewrecords(request):
    rcds = Receipts.objects.all()
    context = {'rcds':rcds}
    return render (request, 'viewrecordspage.html', context)


def viewpledge(request):
    plgs = Pledges.objects.all()
    context = {'plgs':plgs}
    return render (request, 'pledgeRecords.html', context)


def updateReceipt(request):
    data = json.loads(request.body)
    rctid = int(data['rctId'])
    #print(data)
    Receipts.objects.filter(id=rctid).delete()
    return render (request, 'viewrecordspage.html')



def ImportingFiles(request):
    if request.method == 'POST':
        file_resource = PledgesResource()
        dataset = Dataset()
        file = request.FILES['document']
        df = pd.read_excel(file)
        df['contact'] =  df['contact'].apply(lambda x:'0'+str(x))

        dataset = dataset.load(df)
        result = file_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            file_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, "fileExport.html")










#FILES  EXPORTS AND DOWNLOADING

def ExportingFiles(request):
    yr = Receipts.objects.values('rdate')
    lst = list(set([i['rdate'].strftime("%Y") for i in yr]))
    lst.sort()
    #print(list)
    context = {'yr':lst}
    return render (request, 'fileExport.html', context)


def memContact(request):
     response = ExportFile.exportEXCEL(rsc=RegisterResource(), fln='membersContactData')
     return response


def rctFiles(request):
     response = ExportFile.exportEXCEL(rsc=ReceiptsResource(), fln="receciptsdata")
     return response


def Memberspledge(request,yr):
    #print(yr)
    date_list = Pledges.objects.all().dates('pdate', 'year') #extract year from date field
    for years in date_list:
        queryset = Pledges.objects.filter(pdate__year = yr).values('name__name','pamount')
        #print(queryset)
        df = pd.DataFrame.from_dict(queryset)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={yr}pledgesMade.csv'
        df.to_csv(response, index=False)
    return response


def Memberspayments(request,yr):
    #print(yr)
    date_list = Receipts.objects.all().dates('rdate', 'year') #extract year from date field
    for years in date_list:
        q = Receipts.objects.filter(rdate__year = yr) #filter by year
        #print(q)
        queryset = q.values('rname_id__name').annotate(total=Sum('ramount')) #get totals for each name
        #print(queryset)
        df = pd.DataFrame.from_dict(queryset)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={yr}pledgePayments.csv'
        df.to_csv(response, index=False)
        return response
    #return HttpResponse("hi")



def Membersbalances(request,yr):
    return redirect('homepage')
    #print(yr)
    date_list = Receipts.objects.all().dates('rdate', 'year') #extract year from date field
    for years in date_list:
        q = Receipts.objects.filter(rdate__year = yr) #filter by year
        #print(q)
        queryset = q.values('rname_id__name').annotate(Bal=Sum('ramount') - F('rname_id__pamount'))
        #print(queryset)
        df = pd.DataFrame.from_dict(queryset)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={yr}pledgeBalances.csv'
        df.to_csv(response, index=False)
        return response
    #return HttpResponse("hi")




