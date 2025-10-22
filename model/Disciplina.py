from .Agendamento import Agendamento
from .Tarefa import Tarefa

class Compromisso(Agendamento, Tarefa):
    """
    Um compromisso é, ao mesmo tempo, uma Tarefa e um Agendamento.
    """
    def __init__(self, nome_tarefa, descricao=None, data_realizacao=None,
                 data_inicio=None, data_final=None, atividades=None, nome_agendamento=None, local=None):

        Tarefa.__init__(self, nome_tarefa, descricao, data_realizacao)
        Agendamento.__init__(self, data_inicio, data_final, atividades,
                             nome_agendamento if nome_agendamento else nome_tarefa, local)

    def __str__(self):
        return f"[Compromisso] {Tarefa.__str__(self)} | {Agendamento.__str__(self)}"

    def exibir_dados(self):
        return f"{Tarefa.exibir_dados(self)}\n{Agendamento.exibir_dados(self)}"

    