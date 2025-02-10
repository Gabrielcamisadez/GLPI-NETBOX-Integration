import requests
import json
import urllib3

urllib3.disable_warnings()


netbox_url = 'https://srvnetboxdsv-trf1.trf1.gov.br/api/dcim/devices/'
netbox_token = '4cd4bda8a82de5bcabf63f909ecdd801919e200a'



netbox_headers = {
    'Authorization': f'Token {netbox_token}',
    'Content-Type': "application/json"
}

def post_device():
    data = [{
        "role": 7,
        "name": "FourthLinux",
        "device_type": 5,
        "device_role": 0,
        "site": 1,
        "tenant": 2,
        "custom_fields": {
            "Patrimonio": 1003

        }
    }]

    r1 = requests.post(netbox_url, headers=netbox_headers, json=data, verify=False)
    print(r1.status_code)
    print(r1.text)

def get_device():
    r1 = requests.get(netbox_url, headers=netbox_headers, verify=False)
    print(r1.status_code)
    print(r1.text)
    



update_dt = [{
    "id": 23,
    "name": "Ubuntu LAB2",
    "tenant": 4,
    "position": 2.0,
    "device_type": 22,
    "role": 10,
    "interface_count": 55,
    }]

def update_device(data):
    r1 = requests.patch(netbox_url, headers=netbox_headers, json=data, verify=False)    
    print(r1.status_code)
    print(r1.text)
    
    


if __name__ == "__main__":
    # post_device()
    # get_device()
    update_device(update_dt)