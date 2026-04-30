from django.shortcuts import render

def index(request):
    return render(request,"budget/index.html", context={
        "nom" : "balilou",
        "prenom" : "John",
    })

def budget(request,number_budget):
    if number_budget in ["01","02","03"]:
        return render(request, f"budget/budget_{number_budget}.html")
    return render(request, "budget/budget_not_found.html")
