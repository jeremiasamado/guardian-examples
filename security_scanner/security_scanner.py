# security_scanner.py
import requests, argparse, sys

# Lista de headers de segurança importantes
SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options"
]

def scan_website(url: str) -> dict:
    # Adiciona "https://" 
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    
    try:
        response = requests.get(url, timeout=15)
        results = {
            "url": response.url,
            "status_code": response.status_code,
            "uses_https": response.url.startswith("https://"),
            "security_headers": {header: (header in response.headers) for header in SECURITY_HEADERS}
        }
        return results
    except Exception as e:
        print(f"Erro ao aceder ao site: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # Ferramenta de linha de comandos para  inserires o teu site
    parser = argparse.ArgumentParser(description="Verifica segurança básica de um site.")
    parser.add_argument("site", help="Exemplo: example.com")
    args = parser.parse_args()

    scan_results = scan_website(args.site)
    
    # Mostra os resultados de forma legível
    print(f"Site analisado: {scan_results['url']}")
    print(f"Status Code: {scan_results['status_code']}")
    print(f"Usa HTTPS: {'SIM' if scan_results['uses_https'] else 'NÃO'}")
    print("\nHeaders de Segurança:")
    for header, is_present in scan_results["security_headers"].items():
        print(f" - {header}: {'✅ Presente' if is_present else '❌ Ausente'}")

if __name__ == "__main__":
    main()
