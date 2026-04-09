from django.shortcuts import render

def index(request):
    return render(request,"index.html", context={
        "nom" : "balilou",
        "prenom" : "John",
    })

def budget(request,number_budget):
    if number_budget in ["1","2","3"]:
        return render(request, f"budget_{number_budget}.html")
    return render(request, "budget_not_found.html")
