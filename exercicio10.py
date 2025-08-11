import dadosPessoais # Explicação em "README.md"

opiniao: str = f'Serviço excelente aluno {dadosPessoais.nome_completo}, voltarei a comprar!'

print(f"A opinião do cliente tem {len(opiniao)} caracteres.")
print(f"A opinião do cliente tem {opiniao.count(' ')} palavras.")