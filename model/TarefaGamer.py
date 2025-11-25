from .Tarefa import Tarefa
from .StatusTarefa import StatusTarefa
from .DificuldadeJogo import DificuldadeJogo
from datetime import datetime

class TarefaGamer(Tarefa):
    def __init__(self, titulo, tipo=None, descricao=None, data_realizacao=None, jogo=None, dificuldade=DificuldadeJogo.MEDIO, status=StatusTarefa.A_FAZER):
        super().__init__(titulo, descricao=descricao, data_realizacao=data_realizacao, status=status)
        self.tipo = tipo
        self.jogo = jogo
        self.dificuldade = dificuldade

    @property
    def jogo(self):
        return self._jogo
    
    @jogo.setter
    def jogo(self, nome_jogo):
        self._jogo = nome_jogo.strip().title() if nome_jogo else None

    @property
    def dificuldade(self):
        return self._dificuldade
    
    @dificuldade.setter
    def dificuldade(self, valor):
        if isinstance(valor, DificuldadeJogo):
            self._dificuldade = valor
        else:
            raise TypeError("Dificuldade deve ser um valor do Enum DificuldadeJogo.")

    def definir_termino(self):
        self.data_realizacao = datetime.now()
        
    def exibir_dados(self):
        base = super().exibir_dados()
        txt = f"Tipo: {self.tipo}\nJogo: {self.jogo}\nDificuldade: {self.dificuldade.value}"
        return f"{base}\n{txt}"