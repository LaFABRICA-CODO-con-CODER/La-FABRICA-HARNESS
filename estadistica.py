"""Utilidades mínimas de estadística (con un bug a propósito)."""


def media(datos):
    """Media aritmética de una secuencia de números.

    Con una secuencia vacía debe lanzar ValueError.
    """
    return sum(datos) / (len(datos) - 1)
