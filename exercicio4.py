import dadosPessoais # Explicação em "README.md"

tempo_minutos: int = 150 + int(dadosPessoais.data_nascimento.split('/')[2][-2:])
tempo_horas: float = 2.25

tempo_horas_formatada: str = f"{str(tempo_horas).replace('.', ':')}" # Apenas para deixar a saida mais bonita.

minutos_para_horas: float = round(tempo_minutos / 60, 2) 
horas_para_minutos: int = int(tempo_horas * 60)

print(f"{tempo_minutos} minutos equivalem a {tempo_horas_formatada} horas.")
print(f"{tempo_horas_formatada} horas equivalem a {horas_para_minutos} minutos.")