from django.shortcuts import render
import requests
from exchange_app.config import API_USER

def exchange(request):
    response = requests.get(url=f"https://v6.exchangerate-api.com/v6/{API_USER}/latest/USD").json()
    currencies = response.get("conversion_rates")


    
    if request.method == "GET":
        context = {
            "currencies": currencies,
        }

        return render(request, "exchange_app/index.html", context)

    if request.method == "POST":
       
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from_curr')
        to_curr = request.POST.get("to_curr")
       
        response2 = requests.get(url = f"https://v6.exchangerate-api.com/v6/{API_USER}/pair/{from_curr}/{to_curr}/{from_amount}").json() 
      
        converted_amount = response2
        result = round(converted_amount["conversion_result"], 1)
        context = {
            "from_amount": from_amount,
            "from_curr": from_curr,
            "to_curr": to_curr,
            "currencies": currencies,
            "converted_amount": converted_amount,
            "result": result
        }

        return render(request, "exchange_app/index.html", context)

    
