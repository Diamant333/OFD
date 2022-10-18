from django.views.generic import ListView
from django.shortcuts import render
from ofdload.models import Company, Kkt
import requests
import json
import datetime

class GetOfdInfo(object):
    def kkts(company):
        token_key = company['token_key']
        headers = {
            'Token': token_key,
            'Host': 'ofv-api-v0-1-1.evotor.ru',
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8',
        }
        response = requests.get('https://ofv-api-v0-1-1.evotor.ru/v1/client/kkts', headers=headers)
        data = response.json()
        encode_data = json.dumps(data)
        decode_data = json.loads(encode_data)
        company = decode_data['kktList']
        shops = company['orgBranches']
        kkts = shops[0]['kkts']
        for kkt in kkts:
            if not kkt['kktRegNumber'] and kkt['kktCheckState'] == 'Success':
                obj, created = Kkt.objects.update_or_create(
                    name=kkt['kktName'],
                    status=kkt['kktCheckState'],
                    reg_number=kkt['kktRegNumber'],
                    address=kkt['retailAddress'],
                    date_fn=kkt['kktFnInstallDate'],
                    company_id_id=company['id']
                )
    def receipts(kkt):
        f

def get_company_list(request):
    company_filter = Company.objects.all()
    context = {'comp_list': company_filter}

    return render(request, 'ofdload/company.html', context)


def get_data_kkts(request, pk=None):
    company_get = Company.objects.values('token_key').get(id=pk)
    token_key = company_get['token_key']
    headers = {
        'Token': token_key,
        'Host': 'ofv-api-v0-1-1.evotor.ru',
        'Accept': 'application/json',
        'Accept-Charset': 'utf-8',
    }

    response = requests.get('https://ofv-api-v0-1-1.evotor.ru/v1/client/kkts', headers=headers)
    data = response.json()
    encode_data = json.dumps(data)
    decode_data = json.loads(encode_data)
    company = decode_data['kktList']
    shops = company['orgBranches']
    kkts = shops[0]['kkts']
    context = {'object_list': kkts}

    for kkt in kkts:
        print(kkt['kktFnInstallDate'])
        obj, created = Kkt.objects.update_or_create(
            name=kkt['kktName'],
            status=kkt['kktCheckState'],
            reg_number=kkt['kktRegNumber'],
            address=kkt['retailAddress'],
            date_fn=kkt['kktFnInstallDate'],
            company_id_id=pk
        )

    return render(request, 'ofdload/kkts.html', context)


def kkt_info(request):
    company = Company.objects.all()
    kkt = Kkt.objects.all().order_by('-status')
    context = {'company_list': company, 'kkt_list': kkt}

    return render(request, 'ofdload/info.html', context)


def kkt_collation(request):
    company = Company.objects.all()
    kkt = Kkt.objects.all()
    context = {'company_list': company, 'kkt_list': kkt}
    return render(request, 'ofdload/collation.html', context)


class LW(ListView):
    model = Company
    template_name = 'ofdload/company.html'
    context_object_name = 'comp_list'

def receipts_load(request):
    company = Company.objects.values('name', 'token_key', 'id')
    #kkts = Kkt.objects.values('reg_number')
    
    for comp in company:
        kkts = Kkt.objects.filter(company_id_id = comp['id']).values('reg_number')
        token_key = comp['token_key']
        df = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        dt = datetime.datetime.now().replace(microsecond=0)
        df = str(df)
        dt = str(dt)
        df = df.replace(" ", "%20")
        dt = dt.replace(" ", "%20")
        print(df)
        print(dt)
        for kkt in kkts:
            kktRegId = kkt['reg_number']
            #print(kktRegId)
            headers = {
                'Token': token_key,
                'Host': 'ofv-api-v0-1-1.evotor.ru',
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
                'dateFrom': str(df),
                'dateTo': str(dt),
                
            }
            rget = 'https://ofv-api-v0-1-1.evotor.ru/v1/client/receipts?kktRegId='+kktRegId+'&dateFrom='+df+'&dateTo='+dt
            print(rget)
            response = requests.get(rget, headers=headers)
            data = response.json()
            encode_data = json.dumps(data)
            decode_data = json.loads(encode_data)
            if decode_data['receipts']:
                print(decode_data['receipts'][0]['totalSum'])


        context = {'company_list': comp, 'kkt_list': df}

    return render(request, 'ofdload/receipts_load.html', context)
