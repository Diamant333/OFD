from django.views.generic import ListView
from django.shortcuts import render
from ofdload.models import Company, Kkt
import requests
import json
import datetime

company = Company.objects.all()
    
for comp in company:
    token_key = comp['token_key']
    df = datetime.datetime.now()
    dt = datetime.datetime.now()
    headers = {
        'Token': token_key,
        'Host': 'ofv-api-v0-1-1.evotor.ru',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8',
        'dateFrom': df,
        'dateTo': dt,
    }
    print(df)
    print(dt)
    response = requests.get('https://ofv-api-v0-1-1.evotor.ru/v1/client/all-documents', headers=headers)
