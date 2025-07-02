import argparse
from scanner import scan_xss, scan_sqli, scan_xss_post
from scanner_browser import scan_xss_browser
from scanner_form_browser import scan_xss_form 

def main():
    parser = argparse.ArgumentParser(description="VulnXPy - Scanner Web")

    parser.add_argument(
        "--url",
        required=True,
        help="URL cible (ex: https://example.com/page)"
    )
    parser.add_argument(
        "--payloads",
        required=True,
        help="Fichier avec les payloads"
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=["xss", "sqli", "xss-browser", "xss-post", "xss-form"],
        help="Type de test (xss, sqli, xss-browser, xss-post, xss-form)"
    )
    parser.add_argument(
        "--data",
        help="Corps de la requête POST (ex: name=John&message=PAYLOAD)"
    )

    args = parser.parse_args()

    if args.type == "xss":
        scan_xss(args.url, args.payloads)
    elif args.type == "sqli":
        scan_sqli(args.url, args.payloads)
    elif args.type == "xss-browser":
        scan_xss_browser(args.url, args.payloads)
    elif args.type == "xss-post":
        if not args.data:
            print("[!] Le paramètre --data est requis pour xss-post.")
        else:
            scan_xss_post(args.url, args.payloads, args.data)
    elif args.type == "xss-form":
        scan_xss_form(args.url, args.payloads)

if __name__ == "__main__":
    main()
