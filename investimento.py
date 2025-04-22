def calcular_rendimento(valor_inicial, dias): 

    taxa_ao_dia = 0.1415 / 365 

    valor_bruto = valor_inicial * ((1 + taxa_ao_dia) ** dias) 

    # Desconto IOF 

    iof = calcular_iof(valor_bruto - valor_inicial, dias) 

  

    # Desconto IR 

    ir = calcular_ir(valor_bruto - valor_inicial - iof, dias) 

  

    valor_liquido = valor_bruto - iof - ir 

    return valor_liquido, valor_bruto, iof, ir 

def calcular_iof(rendimento, dias): 

    if dias > 30: 

        return 0 

    tabela_iof = { 

        1: 0.96, 2: 0.93, 3: 0.90, 4: 0.86, 5: 0.83, 6: 0.80, 

        7: 0.76, 8: 0.73, 9: 0.70, 10: 0.66, 11: 0.63, 12: 0.60, 

        13: 0.56, 14: 0.53, 15: 0.50, 16: 0.46, 17: 0.43, 18: 0.40, 

        19: 0.36, 20: 0.33, 21: 0.30, 22: 0.26, 23: 0.23, 24: 0.20, 

        25: 0.16, 26: 0.13, 27: 0.10, 28: 0.06, 29: 0.03, 30: 0.0 

    } 

    aliquota = tabela_iof.get(dias, 0) 

    return rendimento * aliquota 
  

def calcular_ir(rendimento, dias): 

    if dias <= 180: 

        aliquota = 0.225 

    elif dias <= 360: 

        aliquota = 0.20 

    elif dias <= 720: 

        aliquota = 0.175 

    else: 

        aliquota = 0.15 

    return rendimento * aliquota 

  

  

valor_investido = float(input("Digite o valor inicial: ")) 

dias_aplicados = int(input("Digite o tempo do investimento em dias: ")) 

  

valor_liquido, valor_bruto, iof, ir = calcular_rendimento(valor_investido, dias_aplicados) 

  

print(f"Valor bruto: R${valor_bruto:.2f}") 

print(f"IOF: R${iof:.2f}") 

print(f"IR: R${ir:.2f}") 

print(f"Valor líquido final: R${valor_liquido:.2f}")