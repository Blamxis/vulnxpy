import argparse
from scanner import scan_xss

def main():
    parser = argparse.ArgumentParser(description="VulnXPy - Scanner Web XSS")
    parser.add_argument("--url", required=True, help="URL cible (ex: https://example.com/page?q=)")
    parser.add_argument("--payloads", required=True, help="Fichier avec les payloads")
    parser.add_argument("--type", required=True, choices=["xss"], help="Type de test (ex: xss)")

    args = parser.parse_args()

    if args.type == "xss":
        scan_xss(args.url, args.payloads)

if __name__ == "__main__":
    main()
