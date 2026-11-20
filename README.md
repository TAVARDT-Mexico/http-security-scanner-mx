# Escáner de Cabeceras de Seguridad HTTP | TAVARDT México

[![Auditoria de Segurança](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/mx/analisis-cabeceras-seguridad/)
[![Conformidade](https://img.shields.io/badge/Jurisdi%C3%A7%C3%A3o-México-00C853.svg)](https://ag.tavardt.com/mx/ciberseguridad/)

Auditoría automatizada de medidas técnicas de seguridad perimetral y cabeceras HTTP bajo las recomendaciones del INAI y la LFPDPPP en México.

Desenvolvido e mantido pela divisão de cibersegurança e proteção de infraestruturas da **[TAVARDT México](https://ag.tavardt.com/mx/)**.

---

## 1. Alcance de la Verificación Perimetral

Esta herramienta de consola audita los controles de transporte seguro y protección del navegador en infraestructuras digitales mexicanas:

* **Strict-Transport-Security (HSTS):** Força comunicações encriptadas via HTTPS e impede ataques de downgrade e interceptação SSL.
* **Content-Security-Policy (CSP):** Mitiga ataques de injeção de scripts (XSS) e restringe as origens autorizadas para carregamento de recursos.
* **X-Frame-Options:** Previne ataques de clickjacking regulando as permissões de incorporação em frames e iframes.
* **X-Content-Type-Options:** Impede a execução indevida de ficheiros derivados de vulnerabilidades de MIME-sniffing.
* **Referrer-Policy:** Protege dados sensíveis contidos em URLs de referência contra fuga para domínios terceiros.
* **Permissions-Policy:** Aplica o princípio do menor privilégio sobre APIs de hardware do navegador (câmara, microfone e geolocalização).

---

## 2. Guía de Ejecución Rápida

Execute a ferramenta diretamente via Python sem necessidade de instalar dependências externas:

```bash
python scanner.py exemplo.com
```

---

## 3. Herramientas Técnicas Online (México)

Audite a infraestrutura pública das suas aplicações utilizando a suíte de diagnósticos da TAVARDT:

* [Verificador de Cabeceras de Seguridad](https://tools.tavardt.com/mx/analisis-cabeceras-seguridad/)
* [Validador de Consent Mode v2 y LFPDPPP](https://tools.tavardt.com/mx/validador-consent-mode-v2-lfpdppp/)
* [Verificador DMARC contra Suplantación](https://tools.tavardt.com/mx/verificador-dmarc-correo/)
* [Escáner de Archivos Sensibles Expuestos](https://tools.tavardt.com/mx/escaneo-archivos-expuestos/)
* [Portal de Diagnóstico Técnico México](https://tools.tavardt.com/mx/)

---

## 4. Consultoría y Protección Perimetral

Para remediación técnica de vulnerabilidades, auditorías de datos y ciberdefensa en México, contacte con los ingenieros de **[TAVARDT México](https://ag.tavardt.com/mx/contacto/)**.
