
from django.shortcuts import render
from ofdload.models import Company, Kkt
import requests
import json


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


