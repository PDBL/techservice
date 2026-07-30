def validar_texto_obrigatorio(valor, campo):

    valor = valor.strip()

    if valor == "":
        raise ValueError(f"{campo} é obrigatório.")

    return valor