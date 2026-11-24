# Escáner de Cabeceras de Seguridad HTTP

[![Alcance de la Verificación Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/mx/analisis-cabeceras-seguridad/)
Auditoría automatizada de medidas técnicas de seguridad perimetral y cabeceras HTTP bajo las recomendaciones del INAI y la LFPDPPP en México.

Desarrollado y mantenido por el equipo de ciberdefensa y protección de datos de **TAVARDT**.

***

## 1. Alcance de la Verificación Perimetral

Esta herramienta de consola audita los controles de transporte seguro y protección del navegador en infraestructuras digitales mexicanas:

* **Strict-Transport-Security (HSTS):** Exige conexiones cifradas mediante HTTPS e impide ataques de degradación e interceptación SSL.
* **Content-Security-Policy (CSP):** Bloquea inyecciones de código malicioso (XSS) y restringe las fuentes de carga autorizadas.
* **X-Frame-Options:** Evita ataques de suplantación visual y clickjacking regulando el uso de iframes.
* **X-Content-Type-Options:** Previene la ejecución indebida de archivos por detección automática de tipos MIME.
* **Referrer-Policy:** Salvaguarda parámetros confidenciales en las URLs de origen contra fugas a terceros.
* **Permissions-Policy:** Aplica mínimos privilegios sobre el acceso a sensores y periféricos del dispositivo.

***

## 2. Guía de Ejecución Rápida

Ejecute la herramienta directamente en Python sin requerir librerías externas adicionales:

```bash
python scanner.py ejemplo.mx
```

***

## 3. Herramientas Técnicas Online (México)

Audite la seguridad perimetral de sus sistemas web con las herramientas oficiales de TAVARDT:

* Verificador de Cabeceras de Seguridad
* [Validador de Consent Mode v2 y LFPDPPP](https://tools.tavardt.com/mx/validador-consent-mode-v2-lfpdppp/)
* [Verificador DMARC contra Suplantación](https://tools.tavardt.com/mx/verificador-dmarc-correo/)
* [Escáner de Archivos Sensibles Expuestos](https://tools.tavardt.com/mx/escaneo-archivos-expuestos/)
* [Portal de Diagnóstico Técnico México](https://tools.tavardt.com/mx/)

***

## 4. Consultoría y Protección Perimetral

Para remediación técnica de vulnerabilidades, auditorías de datos y ciberdefensa en México, contacte con los ingenieros de **TAVARDT**.

***

## Enlaces Útiles

* **Portal Corporativo:** https://ag.tavardt.com/mx/
* **Suite de Diagnósticos:** https://tools.tavardt.com/mx/
* **Contacto Técnico:** https://ag.tavardt.com/mx/contacto/

***

© 2026 TAVARDT. Todos los derechos reservados.
