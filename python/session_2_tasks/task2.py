import requests

def get_my_public_ip():
    return requests.get("https://api.ipify.org/?format=json").json()["ip"]

def get_my_location(ip):
    url = f"https://ipinfo.io/{ip}/geo"
    return requests.get(url).json()

print(f"My public ip is {get_my_public_ip()}")

print(f"My location is {get_my_location(get_my_public_ip())}")

