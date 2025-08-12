import dadosPessoais # Explicação em "README.md"


desconto_txt: str = str(dadosPessoais.idade)
desconto_num: float = float(desconto_txt) / 3.14

preco_produto: float = 599.99


valor_desconto: float = preco_produto * (desconto_num / 100)

valor_final: float = preco_produto - valor_desconto

print(f"Idade: {dadosPessoais.idade} anos")
print(f"Preço original: {preco_produto}")
print(f"Valor do desconto: R${valor_desconto}")
print(f"Valor final: R${valor_final}")