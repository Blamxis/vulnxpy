**VulnXPy** est un outil de test de vulnérabilités web en Python. Il permet de détecter les failles courantes de type **XSS**, **SQLi**, et de tester automatiquement les **formulaires web** via navigateur grâce à Selenium.

---

## 🚀 Fonctionnalités

- 🔎 Scan XSS (GET)
- 🐍 Scan SQL Injection (GET)
- 🌐 Scan XSS via navigateur (headless ou visuel)
- 🧾 Test automatique des **formulaires de contact**
- 🧪 Injection automatique de **payloads personnalisés**
- 💻 Support des requêtes GET / POST
- 🐛 Sauvegarde du HTML pour analyse en cas d’erreur

---

## 🧰 Installation

1. **Cloner le repo :**

```bash
git clone https://github.com/Blamxis/vulnxpy.git
cd vulnxpy
```
2. **Créer un environnement virtuel**

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```
3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```
4. **Installer ChromeDriver (obligatoire pour les scans via formulaire/navigateur)**

- Va ici : https://googlechromelabs.github.io/chrome-for-testing/

- Télécharge la version de ChromeDriver qui correspond à ta version de Chrome

- Place chromedriver :

    - soit dans vulnxpy/bin/

    - soit dans un dossier accessible via le PATH

    - soit modifie le chemin dans le code Python si besoin

## ⚙️ Utilisation

1. **📌 Scan XSS GET**
```bash
python src/main.py --url "https://example.com/page?param=TEST" --type xss --payloads payloads/xss.txt

```

2. **🧪 Scan SQL Injection**
```bash
python src/main.py --url "https://example.com/page?user=TEST" --type sqli --payloads payloads/sqli.txt

```

3. **🌐 Scan XSS via navigateur (GET)**
```bash
python src/main.py --url "https://example.com/page?input=TEST" --type xss-browser --payloads payloads/xss.txt

```

4. **🧾 Scan XSS sur formulaire (POST via navigateur)**
```bash
python src/main.py --url "https://exemple.com/" --type xss-form --payloads payloads/xss.txt

```

## ✏️ Ajouter des payloads

- Fichier : **payloads/xss.txt**

```bash
<script>alert(1)</script>
"><img src=x onerror=alert(1)>
"><svg/onload=alert(1)>
...
```
Ajoute ou modifie librement !

## 🛠️ Requis

- Python 3.7+

- Google Chrome (installé sur ta machine)

- ChromeDriver (compatible avec ta version de Chrome)

## 🧪 Recommandations

- Ne teste que sur des sites que tu possèdes ou avec autorisation.

- Utilise un proxy (ex: Burp Suite) pour observer les requêtes si besoin.

- Regarde debug_last_page.html si un test échoue (page sauvegardée automatiquement).

## 🔐 Avertissement

⚠️ Cet outil est à usage pédagogique ou professionnel avec autorisation uniquement.
Ne jamais utiliser VulnXPy sur des sites sans consentement.

## 👨‍💻 Auteur

Développé par Maxime Gavinet — Développeur Web Junior motivé 🚀