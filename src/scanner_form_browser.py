from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from colorama import Fore, Style
import time
import os


def scan_xss_form(url, payload_file):
    print(f"{Fore.CYAN}[*] Scan XSS via formulaire sur {url}{Style.RESET_ALL}")

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x800')
    options.add_argument('--log-level=3')

    driver = webdriver.Chrome(options=options)

    with open(payload_file, "r") as f:
        payloads = [line.strip() for line in f if line.strip()]

    for payload in payloads:
        try:
            driver.get(url)
            wait = WebDriverWait(driver, 10)

            form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form")))

            name_input = driver.find_element(By.NAME, "name")
            email_input = driver.find_element(By.NAME, "email")
            subject_input = driver.find_element(By.NAME, "subject")
            message_input = driver.find_element(By.NAME, "message")
            submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")

            name_input.clear()
            email_input.clear()
            subject_input.clear()
            message_input.clear()

            name_input.send_keys("XSS Tester")
            email_input.send_keys("test@example.com")
            subject_input.send_keys("XSS Test")
            message_input.send_keys(payload)

            submit_btn.click()

            try:
                success = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Message envoy')]"))
                )
                print(f"{Fore.GREEN}[OK] Soumission réussie pour le payload : {payload}{Style.RESET_ALL}")
            except:
                print(f"{Fore.YELLOW}[!] Formulaire soumis mais aucun message de confirmation visible pour : {payload}{Style.RESET_ALL}")

        except TimeoutException:
            print(f"{Fore.RED}[!] Formulaire non détecté après attente (chargement JS ?) : {Style.RESET_ALL}")
            html_path = "debug_last_page.html"
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            print(f"[DEBUG] Code HTML sauvegardé dans {html_path}")
        except Exception as e:
            print(f"{Fore.MAGENTA}[!] Erreur pendant le test : {e}{Style.RESET_ALL}")

    driver.quit()
