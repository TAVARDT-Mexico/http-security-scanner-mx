<p align="center">
  <a href="https://ag.tavardt.com/mx/">
    <img src="https://ag.tavardt.com/img/tavardt-banner.png" alt="TAVARDT" width="1024" />
  </a>
</p>

# Escáner de Cabeceras de Seguridad HTTP

[![Alcance de la Verificación Perimetral](https://img.shields.io/badge/TAVARDT-Diagn%C3%B3stico%20T%C3%A9cnico-5b3cf5.svg)](https://tools.tavardt.com/mx/analisis-cabeceras-seguridad/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Auditoría automatizada de medidas técnicas de seguridad perimetral y cabeceras HTTP bajo las recomendaciones del INAI y la LFPDPPP en México.

Desarrollado y mantenido por la práctica de ciberdefensa de **TAVARDT** para organizaciones mexicanas.

***

## 1. Alcance de la Verificación Perimetral

Esta herramienta de terminal audita las directivas de seguridad en navegadores y transporte cifrado de datos:

* **Strict-Transport-Security (HSTS):** Obliga al uso de conexiones cifradas mediante HTTPS y evita ataques de degradación de protocolo y SSL-stripping.
* **Content-Security-Policy (CSP):** Previene ataques de inyección de scripts (XSS) y restringe los orígenes autorizados para la carga de recursos.
* **X-Frame-Options:** Protege contra ataques de clickjacking regulando los permisos de integración en elementos frame e iframe.
* **X-Content-Type-Options:** Bloquea vulnerabilidades de interpretación errónea de tipos MIME en navegadores cliente.
* **Referrer-Policy:** Protege parámetros sensibles contenidos en rutas de URL contra filtraciones hacia orígenes externos.
* **Permissions-Policy:** Aplica control de mínimo privilegio sobre interfaces de hardware y sensores del navegador (cámara, micrófono, geolocalización).

***

## 2. Matriz de Línea Base Defensiva y Mitigación de Riesgos

<table>
  <thead>
    <tr>
      <th>Cabecera de Seguridad</th>
      <th>Vector de Riesgo Mitigado</th>
      <th>Comportamiento por Defecto (Ausente)</th>
      <th>Línea Base Recomendada</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Strict-Transport-Security</strong></td>
      <td>Ataques de SSL-stripping y degradación HTTP</td>
      <td>Conexión inicial establecida mediante HTTP en claro</td>
      <td><code>max-age=31536000; includeSubDomains; preload</code></td>
    </tr>
    <tr>
      <td><strong>Content-Security-Policy</strong></td>
      <td>Cross-Site Scripting (XSS) e inyección de datos</td>
      <td>Ejecución indiscriminada de scripts de cualquier origen</td>
      <td>Declaración explícita de orígenes seguros de scripts</td>
    </tr>
    <tr>
      <td><strong>X-Frame-Options</strong></td>
      <td>Clickjacking e incrustación maliciosa en iframes</td>
      <td>Página incrustable en cualquier portal externo</td>
      <td><code>DENY</code> o <code>SAMEORIGIN</code></td>
    </tr>
    <tr>
      <td><strong>X-Content-Type-Options</strong></td>
      <td>MIME-sniffing y confusión de tipos de archivo</td>
      <td>El navegador interpreta archivos no ejecutables como código</td>
      <td><code>nosniff</code></td>
    </tr>
    <tr>
      <td><strong>Referrer-Policy</strong></td>
      <td>Filtración de parámetros y tokens en URLs</td>
      <td>Ruta completa de URL transmitida a otros dominios</td>
      <td><code>strict-origin-when-cross-origin</code></td>
    </tr>
    <tr>
      <td><strong>Permissions-Policy</strong></td>
      <td>Acceso no autorizado a sensores de hardware</td>
      <td>Funciones de hardware expuestas sin control perimetral</td>
      <td>Restricción explícita de cámara, micrófono y ubicación</td>
    </tr>
  </tbody>
</table>

***

## 3. Guía de Inicio Rápido y Automatización

Ejecute esta herramienta directamente mediante Python sin necesidad de librerías de terceros:

```bash
python scanner.py ejemplo.com.mx
```

El motor de auditoría evalúa las respuestas perimetrales de forma determinista:

* **Librería Estándar Nativa:** Funciona exclusivamente con las bibliotecas estándar de Python (`urllib.request`), requiriendo cero dependencias externas.
* **Puntuación Determinista:** Evalúa las seis cabeceras fundamentales de forma insensible a mayúsculas y emite una calificación entera de cero a seis.
* **Compatibilidad con CI/CD:** Se integra con facilidad en etapas de despliegue continuo y validaciones de seguridad perimetral.

***

## 4. Preguntas Frecuentes (FAQ Técnico)

### 1. ¿De qué manera la ausencia de HSTS expone a los usuarios a ataques de SSL-stripping?
Sin Strict-Transport-Security, los navegadores inician conexiones mediante HTTP en texto claro antes de recibir la redirección HTTPS. Intermediarios maliciosos en la red pueden interceptar esta solicitud inicial, suprimir el cifrado y capturar credenciales en tránsito.

### 2. ¿Cuál es la función defensiva principal de Content-Security-Policy (CSP)?
Content-Security-Policy actúa como un mecanismo de defensa en profundidad contra Cross-Site Scripting (XSS) e inyección de datos. Declara orígenes confiables para la carga de scripts, estilos e imágenes, impidiendo la ejecución de código no autorizado en el cliente.

### 3. ¿Cómo protege X-Frame-Options a las aplicaciones frente a ataques de clickjacking?
X-Frame-Options indica al navegador si una página puede ser embebida dentro de elementos frame, iframe u object. Configurar esta directiva como DENY o SAMEORIGIN evita que plataformas externas superpongan capas invisibles para capturar clics de los usuarios.

### 4. ¿Por qué resulta indispensable Permissions-Policy para la privacidad del usuario?
Permissions-Policy restringe el acceso del navegador a interfaces de hardware sensibles, tales como cámara, micrófono y geolocalización. La configuración de esta cabecera impide que scripts externos accedan a sensores del dispositivo sin autorización deliberada.

### 5. ¿Puede este escáner de cabeceras integrarse en flujos de trabajo de CI/CD automatizados?
Sí, `scanner.py` opera nativamente utilizando bibliotecas estándar de Python sin dependencias externas. Proporciona una puntuación determinista y diagnósticos directos, permitiendo su integración sencilla en etapas de control de calidad y despliegue continuo.

***

## 5. Herramientas Técnicas Online (México)

Audite su infraestructura pública mediante la suite de diagnóstico de TAVARDT:

* [Validador de Consent Mode v2 y LFPDPPP](https://tools.tavardt.com/mx/validador-consent-mode-v2-lfpdppp/)
* [Verificador DMARC contra Suplantación](https://tools.tavardt.com/mx/verificador-dmarc-correo/)
* [Escáner de Archivos Sensibles Expuestos](https://tools.tavardt.com/mx/escaneo-archivos-expuestos/)
* [Portal de Diagnóstico Técnico México](https://tools.tavardt.com/mx/)

***

## 6. Consultoría y Protección Perimetral en México

Para remediación de vulnerabilidades perimetrales, pruebas de penetración ofensiva y consultoría en ciberseguridad en Ciudad de México, Monterrey o Guadalajara, contacte con **TAVARDT**.

***

## Enlaces Útiles

* **Portal Corporativo:** https://ag.tavardt.com/mx/
* **Suite de Diagnóstico:** https://tools.tavardt.com/mx/
* **Contacto Técnico:** https://ag.tavardt.com/mx/contacto/

***

### Licencia
Distribuido bajo la Licencia MIT.

***

© 2026 TAVARDT. Todos los derechos reservados.
