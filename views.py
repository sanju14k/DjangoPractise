from django.shortcuts import render
from django.http import HttpResponse
import csv

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def createcsv(request):
    http = HttpResponse(content_type= "text/csv")
    http['Content-Disposition'] = 'attachment; filename = "employee.csv"'
    wr = csv.writer(http)
    wr.writerow([101,"Ravi",25000.00])
    return http