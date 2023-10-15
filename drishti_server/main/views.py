from django.shortcuts import HttpResponse
import requests


def home(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    res = requests.get(f"http://ip-api.com/json/{ip}")

    return HttpResponse(f"{ip}\n {res.text()}")
