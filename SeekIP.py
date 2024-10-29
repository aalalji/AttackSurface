import socket
import subprocess
import requests
import json


def get_whois_info(ip_address):
    # Retrieves WHOIS information using the whois service
    try:
        import whois
        return whois.whois(ip_address)
    except ImportError:
        return "Whois library not installed."


def get_geolocation(ip_address):
    # Retrieves geolocation information from an IP geolocation service
    try:
        response = requests.get(f'https://ipinfo.io/{ip_address}/json')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get geolocation data"}
    except Exception as e:
        return {"error": str(e)}


def trace_route(ip_address):
    # Executes a traceroute command and returns the output
    try:
        command = ["tracert" if os.name == 'nt' else "traceroute", ip_address]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)


def reverse_dns(ip_address):
    # Performs a reverse DNS lookup
    try:
        return socket.gethostbyaddr(ip_address)
    except Exception as e:
        return str(e)


def main(ip_address):
    print(f"Tracing IP Address: {ip_address}")

    # Perform WHOIS lookup
    whois_info = get_whois_info(ip_address)
    print("WHOIS Information:")
    print(whois_info)

    # Get Geolocation Information
    geo_info = get_geolocation(ip_address)
    print("Geolocation Information:")
    print(json.dumps(geo_info, indent=4))

    # Perform Traceroute
    trace_info = trace_route(ip_address)
    print("Traceroute Information:")
    print(trace_info)

    # Perform Reverse DNS Lookup
    dns_info = reverse_dns(ip_address)
    print("Reverse DNS Information:")
    print(dns_info)


if __name__ == "__main__":
    ip_address = input("Enter IP address to trace: ")
    main(ip_address)
