# Escáner de Cabeceras de Seguridad HTTP | TAVARDT México

[![Security Audit](https://img.shields.io/badge/TAVARDT-Security%20Diagnostic-5b3cf5.svg)](https://tools.tavardt.com/mx/)
[![Compliance Standard](https://img.shields.io/badge/Framework-MXN%20Region-00C853.svg)](https://ag.tavardt.com/mx/)

Verificación de medidas de seguridad técnicas en cabeceras HTTP bajo la LFPDPPP en México.

Maintained by the enterprise cybersecurity and edge protection division at [TAVARDT México](https://ag.tavardt.com/mx/).

---

## 1. Scope of Verification

This lightweight command-line tool verifies critical perimeter HTTP security headers:

* **Strict-Transport-Security (HSTS):** Enforces HTTPS encryption and prevents downgrade attacks.
* **Content-Security-Policy (CSP):** Mitigates cross-site scripting (XSS) and unauthorised content injection.
* **X-Frame-Options:** Prevents clickjacking attacks by controlling frame embedding permissions.
* **X-Content-Type-Options:** Prevents MIME-sniffing attacks.
* **Referrer-Policy:** Protects sensitive URL path data from leaking to third parties.
* **Permissions-Policy:** Enforces least-privilege access for browser hardware APIs.

---

## 2. Quick Start

Execute directly via Python without external library dependencies:

```bash
python scanner.py example.com
```

---

## 3. Online Diagnostic Suite

For comprehensive vulnerability scanning, DNS verification, and technical audits, visit our localized tools portal:

* [Online HTTP Security Headers Checker](https://tools.tavardt.com/mx/security-headers-check/)
* [Exposed Secret & Credential Scanner](https://tools.tavardt.com/mx/exposed-files-scanner/)
* [DMARC & Anti-Spoofing Verifier](https://tools.tavardt.com/mx/dmarc-checker/)
* [Full Diagnostic Portal](https://tools.tavardt.com/mx/)

For professional remediation and cybersecurity advisory, contact [TAVARDT México](https://ag.tavardt.com/mx/contact/).
