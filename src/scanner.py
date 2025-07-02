import requests
import urllib.parse
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

def scan_sqli(url, payload_file):
    print(f"{Fore.CYAN}[*] Scan SQLi sur {url}{Style.RESET_ALL}")

    error_signatures = [
        "you have an error in your sql syntax",
        "mysql_fetch",
        "mysql_num_rows()",
        "ORA-01756",
        "sqlite error",
        "unclosed quotation mark",
        "syntax error"
    ]

    with open(payload_file, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    for payload in payloads:
        try:
            full_url = url + payload
            res = requests.get(full_url, timeout=5)

            content_lower = res.text.lower()
            found_error = any(sig in content_lower for sig in error_signatures)

            print(f"\n{Fore.YELLOW}[*] Payload testé : {payload}{Style.RESET_ALL}")
            print(f"    ➤ Statut HTTP : {res.status_code}")
            print(f"    ➤ Longueur de réponse : {len(res.text)} caractères")

            if found_error:
                print(f"{Fore.RED}[VULNÉRABLE] Erreur SQL détectée avec payload : {payload}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[OK] Pas d'erreur détectée pour ce payload{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.MAGENTA}[!] Erreur avec {payload}: {e}{Style.RESET_ALL}")

def scan_xss_post(url, payload_file, data_template):
    print(f"{Fore.CYAN}[*] Scan XSS POST sur {url}{Style.RESET_ALL}")

    with open(payload_file, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    for payload in payloads:
        try:
            # Remplacer PAYLOAD par le payload actuel dans le corps de la requête
            raw_data = data_template.replace("PAYLOAD", payload)

            # Convertir le corps POST en dictionnaire
            post_data = dict(urllib.parse.parse_qsl(raw_data))

            # Envoyer la requête POST
            res = requests.post(url, data=post_data, timeout=5)

            print(f"\n{Fore.YELLOW}[*] Payload testé : {payload}{Style.RESET_ALL}")
            print(f"    ➤ Statut HTTP : {res.status_code}")
            print(f"    ➤ Longueur réponse : {len(res.text)} caractères")

            if payload in res.text:
                print(f"{Fore.RED}[VULNÉRABLE] Payload reflété dans la réponse !{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[OK] Payload non trouvé dans la réponse{Style.RESET_ALL}")

        except Exception as e:
            print(f"{Fore.MAGENTA}[!] Erreur avec {payload}: {e}{Style.RESET_ALL}")

