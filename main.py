import requests
import urllib3
from config import NETBOX_TOKEN, NETBOX_URL, GLPI_TOKEN, GLPI_URL, GLPI_SESSION_TOKEN, GLPI_INIT_URL

urllib3.disable_warnings()


# ------ GLPI DEVICE FOR VIEW ONLY ->
glpi_device = {
    "id": 20,
    "entities_id": 0,
    "name": "srvesxi01-rvd",
    "serial": "F6ZM813",
    "otherserial": "null",
    "contact": "null",
    "contact_num": "null",
    "users_id_tech": 0,
    "groups_id_tech": 0,
    "comment": "null",
    "date_mod": "2025-02-05 17:23:33",
    "autoupdatesystems_id": 0,
    "locations_id": 0,
    "networks_id": 0,
    "computermodels_id": 5,
    "computertypes_id": 2,
    "is_template": 0,
    "template_name": "null",
    "manufacturers_id": 14,
    "is_deleted": 0,
    "is_dynamic": 1,
    "users_id": 0,
    "groups_id": 0,
    "states_id": 0,
    "ticket_tco": "0.0000",
    "uuid": "4c4c4544-0036-5a10-804d-c6c04f383133",
    "date_creation": "2025-02-05 17:23:33",
    "is_recursive": 0,
    "last_inventory_update": "null",
    "last_boot": "null",
}


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


def update_netbox_device(infos):
    r1 = requests.post(NETBOX_URL, headers=netbox_headers, json=infos, verify=False)
    print(r1.status_code)
    print(r1.text)

    if r1.status_code in [200, 201]:
        print(f"Device {infos} send to netbox!")
    else:
        print(f"Error {r1.text}")



test = {
    "nome": glpi_device['name']
}


# --- GLPI FUNCTIONS ---
# ===========================================
def get_session_token():
    r1 = requests.get(GLPI_INIT_URL, headers=glpi_headers, verify=False)
    print(r1.text)


def get_glpi_device():
    r1 = requests.get(GLPI_URL, headers=glpi_headers, verify=False)
    print(r1.text)


if __name__ == "__main__":
    # get_session_token()
    # get_glpi_device()
    # get_netbox_device()
    update_netbox_device(test)
        