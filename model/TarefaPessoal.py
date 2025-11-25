from .Tarefa import Tarefa
from .StatusTarefa import StatusTarefa
from .TipoTarefaPessoal import TipoTarefaPessoal
from datetime import datetime

class TarefaPessoal(Tarefa):
    def __init__(self, titulo, tipo: TipoTarefaPessoal, descricao=None, data_realizacao=None, status=StatusTarefa.A_FAZER):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao, status=status)
        self.tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if isinstance(valor, TipoTarefaPessoal):
            self._tipo = valor
        else:
            raise TypeError("Tipo deve ser um valor do Enum TipoTarefaPessoal.")

    def definir_termino(self):
        self.data_realizacao = datetime.now()

    def exibir_dados(self):
        base = super().exibir_dados()
        txt = f"Tipo de tarefa pessoal: {self.tipo.value}"
        return f"{base}\n{txt}"