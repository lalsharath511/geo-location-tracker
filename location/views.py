from locale import locale_alias
from django.shortcuts import render
import requests
import json

# Create your views here.
def index(request):
    appdata=open("appdata.text","wt+")
    if request.method == 'POST':
      var = (request.POST['ipaddress'])
      # var1=int(var)
      res = requests.get('http://ip-api.com/json/'+var)
      print(res)
      location_data_one = res.text
      appdata.write(location_data_one)
      appdata.close()
      location_data = json.loads(location_data_one)
      return render(request,'user.html', {'data': location_data})
    else:
        ip = requests.get('https://api64.ipify.org?format=json')
        ip_data = json.loads(ip.text)
        res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
        location_data_one = res.text
        location_data = json.loads(location_data_one)
        return render(request,'index.html', {'data': location_data})
def userdetails(request):
    appdata=open("appdata.text","wt+")
    if request.method=="POST":
      var = (request.POST['ipaddress'])
      res = requests.get('http://ip-api.com/json/'+var)
      location_data_one = res.text
      appdata.write(location_data_one)
      appdata.close()
      location_data = json.loads(location_data_one)
      return render(request,'user.html', {'data': location_data})
    else:
      ip = requests.get('https://api64.ipify.org?format=json')
      ip_data = json.loads(ip.text)
      res = requests.get('http://ip-api.com/json/'+ip_data["ip"])
      location_data_one = res.text
      location_data = json.loads(location_data_one)
      return render(request,'userdetails.html', {'data': location_data})
      