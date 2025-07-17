import requests
from ipwhois import IPWhois
import json

def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
        return ip
    except Exception as e:
        return f"Error retrieving IP: {e}"

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/json/")
        data = response.json()
        print("\n🌐 IP Geolocation Info:")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
    except Exception as e:
        print(f"Error retrieving geolocation info: {e}")

def get_whois_info(ip):
    try:
        print("\n🔎 WHOIS Info:")
        obj = IPWhois(ip)
        res = obj.lookup_rdap()
        # Print key WHOIS data
        print(f"Network Name: {res.get('network', {}).get('name')}")
        print(f"CIDR: {res.get('network', {}).get('cidr')}")
        print(f"ASN: {res.get('asn')}")
        print(f"ASN Description: {res.get('asn_description')}")
        print(f"Registry: {res.get('asn_registry')}")
        print(f"Country: {res.get('asn_country_code')}")
    except Exception as e:
        print(f"Error retrieving WHOIS info: {e}")

def ip_checker():
    print("🔧 IP Information Tool")
    choice = input("1. Check your IP\n2. Enter custom IP\nChoose option (1 or 2): ")

    if choice == "1":
        ip = get_public_ip()
        print(f"\nYour Public IP: {ip}")
    elif choice == "2":
        ip = input("Enter IP address: ").strip()
    else:
        print("Invalid choice.")
        return

    get_ip_info(ip)
    get_whois_info(ip)

if __name__ == "__main__":
    ip_checker()
