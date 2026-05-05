from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request : HttpRequest) -> HttpResponse:
    date =datetime.now()
    print("ma date " + str(date))
    print(type(date), flush=True)

    return render(request, 'toolbox/index.html',
                  context={"prenom" : "Mohamed", "nom" : "binto", "date" : datetime.today()})
