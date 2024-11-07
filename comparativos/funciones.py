def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo.

    Args:
        base: La base del rectángulo.
        altura: La altura del rectángulo.

    Returns:
        El área del rectángulo.
    """

    area = base * altura
    return area

base = 5
altura = 10
resultado = calcular_area_rectangulo(base, altura)
print("El área es:", resultado)