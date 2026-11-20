#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Exige conexiones encriptadas mediante protocolo HTTPS (HSTS).'), ('Content-Security-Policy', 'Bloquea inyecciones maliciosas y vectores de ataque XSS.'), ('X-Frame-Options', 'Evita ataques de suplantacion visual y clickjacking.'), ('X-Content-Type-Options', 'Previene riesgos derivados de la deteccion automatica de MIME.'), ('Referrer-Policy', 'Salvaguarda informacion sensible en las URLs de origen.'), ('Permissions-Policy', 'Aplica minimos privilegios sobre sensores y APIs del dispositivo.')]

def scan_target(target_url):
    print(f"\n[TAVARDT México] Iniciando verificacion perimetral de cabeceras tecnicas para: {target_url}\n")
    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "TAVARDT-Security-Scanner/3.0 (es-MX)"}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            headers = dict(response.headers.items())
            
            score = 0
            total = len(SECURITY_HEADERS)
            
            for header_name, desc in SECURITY_HEADERS:
                found = any(h.lower() == header_name.lower() for h in headers.keys())
                if found:
                    print(f"  [CONFORME] {header_name}")
                    score += 1
                else:
                    print(f"  [AUSENTE] {header_name}: {desc}")
                    
            print(f"\n[TAVARDT México] Puntuacion Final: {score}/{total}")
            print(f"\nVerificacao completa online: https://tools.tavardt.com/mx/analisis-cabeceras-seguridad/")
            print(f"Suporte corporativo e ciberdefesa: https://ag.tavardt.com/mx/ciberseguridad/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT México] Erro ao inspecionar o alvo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
