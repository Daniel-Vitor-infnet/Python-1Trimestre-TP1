import dadosPessoais # Explicação em "README.md"


msg_aspas_simples: str = f"Projeto '{dadosPessoais.nome_completo}' em execução."
msg_aspas_duplas: str= f'Aluno "{dadosPessoais.nome_completo}" aprovado no teste.'
relatorio_triple: str = """Projeto do TP de python 1º trimestre
Pretendo concluir todos itens do TP. 
Status Final: Concluído
"""

print(f"{msg_aspas_simples} \n{msg_aspas_duplas} \n{relatorio_triple}" )