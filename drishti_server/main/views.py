from django.shortcuts import render, HttpResponse
from .models import PreOrder
import requests


def home(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    res = requests.get(f"http://ip-api.com/json/{ip}").json()
    return render(request, "main.html", {"country": res.get("country")})


def pre_order(request):
    if request.method == "POST":
        product = request.POST.get("product")
        quantity = request.POST.get("quantity")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone_number = request.POST.get("mobile_number")
        email_address = request.POST.get("email_address")
        address = request.POST.get("address")
        comment = request.POST.get("comment")

        PreOrder.objects.create(
            product=product,
            quantity=quantity,
            first_name=fname,
            last_name=lname,
            phone_number=phone_number,
            email_address=email_address,
            address=address,
            comment=comment,
        )

        return HttpResponse("OK")

    return HttpResponse("Invalid Method!")
