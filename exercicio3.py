#O problema no geral é tranquilo, porém o enunciado deixo bem confuso

km_por_dia: int = 23 # Pensei em usar float, porém não vejo necessidade.
gasto_diario: int = 300 + 2 # Sou de 2002 e o enunciado pede 2 digitos, porém n vejo sentido em colocar 02 como é uma soma 02 é igual a 2.



print(f'Total percorrido em uma semana de {km_por_dia * 7}km')
print(f'Diferença entre 100 reais e o gasto diário é de {gasto_diario - 100} reais')
print(f'Quantos dias o valor de R$500 cobre {500 // gasto_diario} dias')
print(f'Porcentagem do gasto diário em relação a 100 é de {gasto_diario % 100}')
print(f'Média diária de custo por km rodado é de {gasto_diario / km_por_dia} reais por km')

