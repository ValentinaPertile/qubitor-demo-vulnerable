# qubitor-demo-vulnerable

> ⚠️ **Este repositorio es inseguro a propósito.** No usar este código en ningún proyecto real.

Repositorio de demostración de [Qubitor](https://github.com/ValentinaPertile/qubitor) (TPI de Desarrollo de Software Cloud, UTN FRLP 2026). Contiene vulnerabilidades plantadas para probar los motores de auditoría y mostrarlos en vivo: como se sabe qué hay en cada archivo, el resultado del escaneo es predecible.

Todas las credenciales que aparezcan acá son **inventadas** y visiblemente falsas.

## Fallas plantadas

| Falla | Motor | Módulo | Archivo | Estado |
|---|---|---|---|---|
| `requests==2.19.0` (CVE-2018-18074) | SCA | D | `requirements.txt` | ✅ |
| `lodash` 4.17.4 (CVE-2018-3721, CVE-2019-10744) | SCA | D | `package.json` | ✅ |
| Firma con ECDSA (riesgo cuántico) | Cripto post-cuántica | D | `app/signing.js` | ✅ |
| RSA, ECDH y AES-128 (riesgo cuántico) | Cripto post-cuántica | D | `app/keys.py` | ✅ |
| Consulta SQL armada con f-string | SAST | C | `app/db.py` | pendiente |
| `eval()` sobre input del usuario | SAST | C | `app/utils.py` | pendiente |
| AWS key y token de GitHub falsos | Secretos | C | `config/settings.py`, `.env.example` | pendiente |
| `hashlib.md5` para contraseñas | Cripto clásica | C | `app/auth.py` | pendiente |
| RSA de 1024 bits y AES en modo ECB | Cripto clásica | C | `app/crypto_utils.py` | pendiente |

Al plantar una falla, agregarla o marcarla en esta tabla.
