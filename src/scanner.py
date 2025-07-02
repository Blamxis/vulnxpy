import requests
from colorama import Fore, Style

def scan_xss(url, payload_file):
    print(f"{Fore.CYAN}[*] Scan XSS sur {url}{Style.RESET_ALL}")

    with open(payload_file, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    for payload in payloads:
        try:
            full_url = url + payload
            res = requests.get(full_url, timeout=10)

            # Analyse basique
            vuln = payload in res.text
            headers = res.headers

            # Analyse complémentaire : statut, CSP, longueur
            content_length = len(res.text)
            csp = headers.get("Content-Security-Policy", "Non défini")
            status = res.status_code

            print(f"\n{Fore.YELLOW}[*] Payload testé : {payload}{Style.RESET_ALL}")
            print(f"    ➤ Statut HTTP : {status}")
            print(f"    ➤ Longueur de réponse : {content_length} caractères")
            print(f"    ➤ Content-Security-Policy : {csp[:80]}...")

            if vuln:
                print(f"{Fore.RED}[VULNÉRABLE] Payload reflété : {payload}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[OK] Aucun reflet détecté{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.MAGENTA}[!] Erreur : {e}{Style.RESET_ALL}")
