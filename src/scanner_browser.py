from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from colorama import Fore, Style
from pathlib import Path

def scan_xss_browser(url, payload_file):
    print(f"{Fore.CYAN}[*] Scan XSS (navigateur) sur {url}{Style.RESET_ALL}")

    options = Options()
    options.headless = True
    chromedriver_path = Path(__file__).parent.parent / "bin" / "chromedriver.exe"
    service = Service(executable_path=str(chromedriver_path))
    driver = webdriver.Chrome(service=service, options=options)

    with open(payload_file, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    for payload in payloads:
        try:
            test_url = url + payload
            print(f"\n{Fore.YELLOW}[*] Test du payload : {payload}{Style.RESET_ALL}")

            driver.get(test_url)
            time.sleep(2)  # Attente du rendu JS

            if payload in driver.page_source:
                print(f"{Fore.RED}[VULNÉRABLE] Payload reflété dans le DOM !{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[OK] Payload non trouvé dans le DOM{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.MAGENTA}[!] Erreur navigateur : {e}{Style.RESET_ALL}")

    driver.quit()
