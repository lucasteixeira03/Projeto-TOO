from model.Tarefa import Tarefa
from model.TarefaProfissional import TarefaProfissional
from model.TarefaPessoal import TarefaPessoal
from model.Disciplina import Disciplina
from model.TarefaEscolar import TarefaEscolar
from model.Agendamento import Agendamento
from model.Compromisso import Compromisso

print('--- Teste Tarefa Profissional ---')
t2 = TarefaProfissional("Reunião com cliente", "Projeto Alpha", "25-09-2025", None)
print(t2.exibir_dados())

print()

print('--- Teste Tarefa Pessoal ---')
t3 = TarefaPessoal("Ir ao médico", "Saúde", "Consulta de rotina", "20-09-2025")
print(t3.exibir_dados())

print()

print('--- Teste Agendamento ---')
a1 = Agendamento("07-10-2025 14:00", "07-10-2025 15:00", "Reunião Semanal", "Daily", "Google Meet")
print(a1.exibir_dados())

print()

print('--- Teste Compromisso ---')
comp = Compromisso(
    nome_tarefa="Reunião Informal",
    descricao="Encontro com funcionários",
    data_realizacao="10-10-2025",
    data_inicio="10-10-2025 18:00",
    data_final="10-10-2025 20:00",
    atividades="Comes e Bebes",
    local="Restaurante Central"
)
print(comp.exibir_dados())