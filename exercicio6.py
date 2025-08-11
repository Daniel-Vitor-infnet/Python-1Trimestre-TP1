import dadosPessoais # Explicação em "README.md"


nome_proprio: str = dadosPessoais.nome_completo.split(" ")[0]
ultimo_sobrenome: str = dadosPessoais.nome_completo.split(" ")[-1]
codigo_classe: str = "GRLEDC01C1-N2-L1"

print("Bem-vindo(a), " + nome_proprio + " " + ultimo_sobrenome + "! Sua turma é " + codigo_classe + ".")