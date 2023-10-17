import requests
import json


def meraki_get(resource):
    """Helper function to reduce repetitive HTTP GET statements. Takes in a specific REST resource and returns
     the JSON-formatted body text."""

    # Defining variables for API requests.
    api_path = "https://dashboard.meraki.com/api/v0"
    headers = {"Content": "application/json", "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

    # Send request to base API path with passed in resource and headers
    get_resp = requests.get(f"{api_path}/{resource}", headers=headers)

    # Raise an error if status code >= 400
    get_resp.raise_for_status()

    return get_resp.json()


def main():
    """Execution begins here"""
    orgs = meraki_get("organizations")
    print("Organizations discovered:")

    devnet_id = 0
    for org in orgs:
        print(f"ID: {org['id']:<6} Name: {org['name']}")
        if "devnet sandbox" == org["name"].lower():
            devnet_id = "549236"

    if devnet_id:
        networks = meraki_get(f"organizations/{devnet_id}/networks")
        print(f"\nNetworks seen for DevNet org ID {devnet_id}")

    devnet_network = ""
    for network in networks:
        print(f"Network ID: {network['id']} Name: {network['name']}")
        if "devnet" in network["name"].lower():
            devnet_network = network["id"]

    if devnet_network:
        devices = meraki_get(f"networks/{devnet_network}/devices")

    print(f"\nDevices seen on DevNet network {devnet_network}:")

    for device in devices:
        print(f"Model: {device['model']:<8} IP: {device['lanIp']}")


if __name__ == "__main__":
    main()
