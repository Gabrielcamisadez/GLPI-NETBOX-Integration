import requests
import json
import urllib3

urllib3.disable_warnings()


netbox_url = 'http://localhost:8000/api/dcim/devices/'
netbox_token = '1ec53d4afb6b10cd085586b44b37e985760140ce'

netbox_headers = {
    'Authorization': f'Token {netbox_token}',
    'Content-Type': "application/json"
}

def post_device():
    data = [{
        "role": 1,
        "name": "ngFw WAN2",
        "device_type": 1,
        "device_role": 1,
        "site": 1,
        "tenant": 1
    }]

    r1 = requests.post(netbox_url, headers=netbox_headers, json=data, verify=False)
    print(r1.status_code)
    print(r1.text)



if __name__ == "__main__":
    post_device()
