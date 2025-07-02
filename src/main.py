import argparse
from scanner import scan_xss, scan_sqli

def main():
    parser = argparse.ArgumentParser(description="VulnXPy - Scanner Web")
    parser.add_argument(
        "--url",
        required=True,
        help="URL cible (ex: https://example.com/page?id=)")
    
    parser.add_argument(
        "--payloads",
        required=True,
        help="Fichier contenant les payloads")
    
    parser.add_argument(
        "--type",
        required=True,
        choices=["xss", "sqli"],
        help="Type de test (xss, sqli)")

    args = parser.parse_args()

    if args.type == "xss":
        scan_xss(args.url, args.payloads)
    elif args.type == "sqli":
        scan_sqli(args.url, args.payloads)

if __name__ == "__main__":
    main()
