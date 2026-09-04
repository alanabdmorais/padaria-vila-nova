def calcular_total(preco_unitario, quantidade):
    if preco_unitario < 0 or quantidade < 0:
        raise ValueError("preco_unitario e quantidade devem ser nao negativos")
    return round(preco_unitario * quantidade, 2)
