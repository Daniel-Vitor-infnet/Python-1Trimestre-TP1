#O problema no geral é tranquilo, porém o enunciado deixo bem confuso

import dadosPessoais # Explicação em "README.md"

km_por_dia: int = dadosPessoais.idade 
gasto_diario: int = 300 + int(dadosPessoais.data_nascimento.split('/')[2][-2:])


print(f'Total percorrido em uma semana de {km_por_dia * 7}km')
print(f'Diferença entre 100 reais e o gasto diário é de {gasto_diario - 100} reais')
print(f'Quantos dias o valor de R$500 cobre {500 // gasto_diario} dias')
print(f'Porcentagem do gasto diário em relação a 100 é de {gasto_diario % 100}')
print(f'Média diária de custo por km rodado é de {gasto_diario / km_por_dia} reais por km')

