from typing import List

from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def dashboard(request: HttpRequest):
    poul = 123
    numbers : List[int] = list(range(1,10))
    return render(request, "currency/dashboard.html",context={
        "testing" : poul,
        "numberss"  : numbers,
    })