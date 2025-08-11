import dadosPessoais # Explicação em "README.md"

score_credito: float = 772.4
cliente_ativo: bool  = True


print(f'Nome: {dadosPessoais.nome_completo} | Tipo: {type(dadosPessoais.nome_completo)}')
print(f'Idade: {dadosPessoais.idade} | Tipo: {type(dadosPessoais.idade)}')
print(f'Score de Crédito: {score_credito} | Tipo: {type(score_credito)}')
print(f'Cliente Ativo: {cliente_ativo} | Tipo: {type(cliente_ativo)}')