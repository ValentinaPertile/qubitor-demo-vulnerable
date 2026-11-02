"""Fallas plantadas (Módulo D): criptografía vulnerable a computación cuántica."""

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, rsa
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generar_clave_rsa():
    # RSA de 2048 bits: seguro hoy, pero lo rompe Shor.
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def acordar_clave(privada, publica_del_otro):
    # ECDH: lo rompe Shor.
    return privada.exchange(ec.ECDH(), publica_del_otro)


def generar_clave_de_sesion():
    # AES-128: Grover reduce su seguridad efectiva a la mitad.
    return AESGCM.generate_key(bit_length=128)


def huella(datos: bytes) -> bytes:
    # SHA-256: seguro, solo aparece en el inventario criptográfico (CBOM).
    digest = hashes.Hash(hashes.SHA256())
    digest.update(datos)
    return digest.finalize()
