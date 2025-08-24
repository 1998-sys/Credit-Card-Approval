def categorização_status(valor_status):
    """
    Função para categorizar os valroes da coluna STATUS
    C -> 6
    X -> 7
    0, 1, 2, 3, 4, 5 -> mantem o valor
    """
    if valor_status == 'C':
        return 6
    
    if valor_status == 'X':
        return 7
    
    else:
        return valor_status