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
        "role": 1,
        "name": "Fedora Lab",
        "device_type": 1,
        "device_role": 1,
        "site": 2,
        "tenant": 1,
        "custom_fields": {
            "Patrimonio": 1007

        }
    }]

    r1 = requests.post(netbox_url, headers=netbox_headers, json=data, verify=False)
    print(r1.status_code)
    print(r1.text)

def get_device():
    r1 = requests.get(netbox_url, headers=netbox_headers, verify=False)
    print(r1.status_code)
    print(r1.text)
    



def update_device():
    update_dt = [{
        "id": 31,
        "role": 3,
        "name": "Fedore LAB",
    }]
    r1 = requests.patch(netbox_url, headers=netbox_headers, json=update_dt, verify=False)    
    print(r1.status_code)
    
    


if __name__ == "__main__":
    post_device()
    # get_device()
    # update_device()