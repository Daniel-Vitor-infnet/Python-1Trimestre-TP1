import dadosPessoais # Explicação em "README.md"

nome_completo: str = f"{dadosPessoais.nome_completo.split(" ")[0]} {dadosPessoais.nome_completo.split(" ")[-1]}"

# Apesar to meu nome já estar formatado corretamente apliquei o método title() e capitalize() para demonstrar o uso.

print(f"Nome em maiúsculas: {nome_completo.upper()}")
print(f"Nome em minúsculas: {nome_completo.lower()}")
print(f"Nome com primeira letra maiúscula: {nome_completo.title()}")
print(f"Nome com primeira letra de cada palavra maiúscula: {nome_completo.capitalize()}")
print(f"Nome com inversão de maiúsculas/minúsculas : {nome_completo.swapcase()}")