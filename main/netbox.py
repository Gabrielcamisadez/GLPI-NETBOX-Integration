import requests
import json
import urllib3

urllib3.disable_warnings()


netbox_url = 'https://srvnetboxdsv-trf1.trf1.gov.br/api/virtualization/virtual-machines/'
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

# -------------------------------------

def get_device():
    r1 = requests.get(netbox_url, headers=netbox_headers, verify=False)
    print(r1.status_code)
    print(r1.text)
    
# -------------------------------------

def update_device(data):
    r1 = requests.patch(netbox_url, headers=netbox_headers, json=data, verify=False)    
    print(r1.status_code)
    print(r1.text)
    

def update_vm(data):
    netbox_vms_url = "https://srvnetboxdsv-trf1.trf1.gov.br/api/virtualization/virtual-machines/"
    r1 = requests.patch(netbox_vms_url, headers=netbox_headers, json=data, verify=False)    
    print(r1.status_code)
    print(r1.text)


update_devic = [{
    "id": 3,
    "name": "VMEsxi12",
    "tenant": 4,
    "position": 3.0,
    "device_type": 22,
    "role": 10,
    "interface_count": 55,
    }]

data_vm = [{
    "id": 24,
    "name": "srvfw010-vca",
    "status": "active",
    "custom_fields": {
        "Transport": "ssh"
    },
    "serial": "",
    "description": "VM TEST FOR UPDATES",
    "serial": 1010
    
}]
    


if __name__ == "__main__":
    # post_device()
    # get_device()
    update_vm(data_vm)
    # update_device(update_devic)