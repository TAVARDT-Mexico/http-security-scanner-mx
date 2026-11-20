#!/usr/bin/env python3
import sys
import urllib.request
import urllib.error
from urllib.parse import urlparse

SECURITY_HEADERS = [('Strict-Transport-Security', 'Exige conexiones cifradas mediante HTTPS e impide ataques de degradación e interceptación SSL.'), ('Content-Security-Policy', 'Bloquea inyecciones de código malicioso (XSS) y restringe las fuentes de carga autorizadas.'), ('X-Frame-Options', 'Evita ataques de suplantación visual y clickjacking regulando el uso de iframes.'), ('X-Content-Type-Options', 'Previene la ejecución indebida de archivos por detección automática de tipos MIME.'), ('Referrer-Policy', 'Salvaguarda parámetros confidenciales en las URLs de origen contra fugas a terceros.'), ('Permissions-Policy', 'Aplica mínimos privilegios sobre el acceso a sensores y periféricos del dispositivo.')]

def scan_target(target_url):
    print(f"\n[TAVARDT México] Iniciando verificación perimetral de cabeceras técnicas para: {target_url}\n")
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
                    
            print(f"\n[TAVARDT México] Puntuación Final: {score}/{total}")
            print(f"\nVerificación completa online: https://tools.tavardt.com/mx/analisis-cabeceras-seguridad/")
            print(f"Soporte corporativo y ciberdefensa: https://ag.tavardt.com/mx/ciberseguridad/\n")
            
    except urllib.error.URLError as e:
        print(f"[TAVARDT México] Error al inspeccionar el objetivo: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python scanner.py <URL>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    if not urlparse(url).scheme:
        url = "https://" + url
        
    scan_target(url)
