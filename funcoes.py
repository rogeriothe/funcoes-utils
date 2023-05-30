def ajeita(frase: str):
    """
    Capitaliza a primeira letra de cada palavra em uma frase, exceto para certas palavras.
    Utilizo para nomes pr

    Args:
        frase (str): A frase a ser modificada.

    Returns:
        str: A frase modificada com a primeira letra de cada palavra em maiúsculo,
             exceto para as palavras especificadas.

    Examples:
        >>> capitalize_words_except_certain("o gato e o rato na casa")
        'O Gato e o Rato na Casa'

        >>> capitalize_words_except_certain("o sol nasce em todos os dias")
        'O Sol Nasce em Todos os Dias'
    """
    palavras = frase.split()
    excecoes = ['a', 'o', 'as', 'os', 'na', 'no', 'nas', 'nos', 'de', 'da', 'do', 'em', 'dos', 'das', 'e']
    resultado = []
    for palavra in palavras:
        if palavra.lower() in excecoes:
            resultado.append(palavra)
        else:
            resultado.append(palavra.capitalize())
    return ' '.join(resultado)
