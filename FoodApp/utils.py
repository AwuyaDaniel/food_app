import requests


def ip_address(request):
    remote_addr = request.META.get('HTTP_X_FORWARDED_FOR')
    if remote_addr:
        address = remote_addr.split(',')[-1].strip()
    else:
        address = request.META.get('REMOTE_ADDR')

    return address


def get_location(request):
    ip = ip_address(request)
    if ip == "127.0.0.1":
        ip = "197.210.84.237"
    url = f"http://api.ipstack.com/{ip}?access_key=237a58b37a4b3369777bddaaadf600e2"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # If the response contains JSON data
        latitude = data['latitude']
        longitude = data['longitude']
        api = "xO48gKWgq9qzMG3qkgMFySomhUdlgZH7"
        main_url = f"https://api.tomtom.com/search/2/nearbySearch/.json?key={api}&lat={latitude}&lon={longitude}"
        res = requests.get(main_url)
        res = res.json()
        return res



def get_usd_rate():
    API_Key = "CH5lzlmhzAtLQ37ukWVEqfNGmYhcPhzq"
    url = "https://api.apilayer.com/fixer/latest"
    params = {
        "base": "USD",
        "symbols": "NGN"
    }

    headers = {
        "apikey": f"{API_Key}"
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        data = {'success': True, 'timestamp': 1698401283, 'base': 'USD', 'date': '2023-10-27',
                'rates': {'NGN': 802.70312}}
        return data


def get_recipe(q):
    from serpapi import GoogleSearch

    params = {
        "q": q,
        "api_key": "2502e4ad425b2090e752825bc18571effc6c1bc6e9c0a4864514b43b4828dc98"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    recipes_results = results["recipes_results"]
    return recipes_results
