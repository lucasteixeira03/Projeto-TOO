from .Tarefa import Tarefa
from datetime import datetime

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao)
        self.tipo = tipo  # Exemplo: "Saúde", "Estudos", "Lazer" etc.

    def definir_termino(self):
        self.data_realizacao = datetime.now()

    def exibir_dados(self):
        return super().exibir_dados()