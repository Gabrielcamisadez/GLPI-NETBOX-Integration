import requests
import urllib3
from config import NETBOX_TOKEN, NETBOX_URL, GLPI_TOKEN, GLPI_URL, GLPI_SESSION_TOKEN, GLPI_INIT_URL

urllib3.disable_warnings()


netbox_headers = {
    "Authorization": f"Token {NETBOX_TOKEN}",
    "Content-Type": "application/json"
}

glpi_headers = {
    "Authorization": "Basic Z2xwaTpnbHBp",
    "Content-Type": "application/json",
    "App-Token": GLPI_TOKEN,
    "Session-Token": GLPI_SESSION_TOKEN
}


# --- NETBOX FUNCTIONS ---
# ==========================================

def get_netbox_device():
    r1 = requests.get(NETBOX_URL, headers=netbox_headers, verify=False)
    
    if r1.status_code == 200:
        print(r1.text)
    else:
        print(f"Error {r1.text} !!")



# --- GLPI FUNCTIONS ---
# ===========================================
def get_session_token():
    r1 = requests.get(GLPI_INIT_URL, headers=glpi_headers, verify=False)
    print(r1.text)


def get_glpi_device():
    r1 = requests.get(GLPI_URL, headers=glpi_headers, verify=False)
    print(r1.text)


if __name__ == "__main__":
    get_session_token()
    # get_glpi_device()
    # get_netbox_device()
