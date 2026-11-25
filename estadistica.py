"""Utilidades mínimas de estadística (con un bug a propósito)."""


def media(datos):
    """Media aritmética de una secuencia de números.

    Con una secuencia vacía debe lanzar ValueError.
    """
    # Guarda explícita: el contrato (docstring + test) exige ValueError en secuencia vacía.
    # Sin esta guarda, len([]) == 0 provocaría ZeroDivisionError (no ValueError) tras el fix del divisor.
    if not datos:
        raise ValueError("media() requires at least one data point")
    # Divisor correcto: media aritmética = suma / n (no n-1). El bug original usaba n-1
    # que es el divisor para varianza muestral, no para media.
    return sum(datos) / len(datos)
