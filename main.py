from transliterate import translit
import requests
import json


try:
    data = requests.get('https://api.myip.com').json()

    json_data = []
    ip = data['ip']
    country = translit(data['country'], 'ru')
    print(f'Ваш IP-адрес равен {ip}')
    print(f'Страна: {country}')
    json_data.append({
        "ip": ip,
        "country": country,
    })
    data_ds = requests.get(f'https://ipapi.co/{ip}/json/').json()
    ds_data_json = []
    city = translit(data_ds['city'], 'ru')
    region = translit(data_ds['region'], 'ru')
    country_population = data_ds['country_population']
    postal = data_ds['postal']
    currency_name = data_ds['currency_name']
    print(f'Город {city}')
    print(f'Регион {region}')
    print(f'Численность населения {country_population} человек')
    print(f'Почтовый индекс {postal}')
    print(f'Валюта {sum}')
    print(f'Main')
    with open('ipcookie.json', mode='w', encoding='UTF-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)

except:
    print('Ошибка')