import socket
import urllib.request

#set your locale ip or public ip here
TARGET_LOCAL_IP = '192.168.0.9'
TARGET_PUBLIC_IP = '198.0.0.0'
TARGET_PORT = 4546

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Local IP Error: {e}"

def get_public_ip():
    try:
        external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf-8')
        return external_ip
    except Exception as e:
        return f"Public IP Error: {e}"

def send_ip_info(target_ip, target_port, ip_info):
    print(f"[INFO] Sending IP info to {target_ip}:{target_port} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((target_ip, target_port))
            s.sendall(ip_info.encode())
            print("[INFO] IP info sent successfully.")
        except Exception as e:
            print(f"[ERROR] Could not send IP info to {target_ip}: {e}")

def main():
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    ip_info = f"Local IP: {local_ip}\nPublic IP: {public_ip}\n"

    send_ip_info(TARGET_LOCAL_IP, TARGET_PORT, ip_info)
    send_ip_info(TARGET_PUBLIC_IP, TARGET_PORT, ip_info)

if __name__ == "__main__":
    main()
