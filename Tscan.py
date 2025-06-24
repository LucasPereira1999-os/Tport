import socket, time, random
import threading
import socks
import argparse
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--Domain", "-d", help="Input your domain", required=True)
    parser.add_argument("--not_tor", "-nT", help="Disable TOR", action="store_true")
    args = parser.parse_args()

    with open("scan_file.txt", "w"):
        pass

    ports = list(range(20, 3501))
    random.shuffle(ports)
    lock = threading.Lock()
    progress = tqdm(total=len(ports))
    use_tor = not args.not_tor

    if use_tor:
        socks.setdefaultproxy(socks.SOCKS5, "127.0.0.1", 9050)

    def scan_port(port, domain_temp):
        if use_tor:
            s = socks.socksocket()
            ip_target = domain_temp
        else:
            s = socket.socket()
            try:
                ip_target = socket.gethostbyname(domain_temp)
            except socket.gaierror:
                print(f"[!] Cannot resolve {domain_temp}")
                return

        s.settimeout(0.5)

        try:
            result = s.connect_ex((ip_target, port))
            if result == 0:
                s.send(f"GET / HTTP/1.1\r\nHost: {domain_temp}\r\nUser-Agent: Mozilla/5.0\r\n\r\n".encode())
                try:
                    response = s.recv(1024)
                    response.decode(errors="ignore")
                except:
                    pass

                with lock:
                    with open("scan_file.txt", "a") as f:
                        f.write(f"Port : {port} | OPEN\n")

        except:
            pass
        finally:
            s.close()
            with lock:
                progress.update(1)
            time.sleep(random.uniform(0.1, 0.3))

    def wait_tor():
        while True:
            try:
                s = socket.create_connection(("127.0.0.1", 9050), timeout=2)
                s.close()
                print("[✓] TOR active, continue scanning...\n")
                break
            except:
                print("[!] TOR not active yet, please activate it first")
                time.sleep(10)

    if use_tor:
        wait_tor()

    threads = []
    for i in ports:
        t = threading.Thread(target=scan_port, args=(i, args.Domain))
        t.start()
        threads.append(t)
        time.sleep(0.05)

    for k in threads:
        k.join()

if __name__ == "_main_":
    main()