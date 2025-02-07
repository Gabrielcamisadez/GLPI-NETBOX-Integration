import requests
import urllib3
from config import NETBOX_TOKEN, NETBOX_URL

urllib3.disable_warnings()


netbox_headers = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}


def get_netbox_device():
    r1 = requests.get(NETBOX_URL, headers=netbox_headers, verify=False)
    
    if r1.status_code == 200:
        print(r1.text)
    else:
        print(f"Error {r1.text} !!")
if __name__ == "__main__":
    get_netbox_device()    