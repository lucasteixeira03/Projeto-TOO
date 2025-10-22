from .Tarefa import Tarefa
from datetime import datetime

class TarefaGamer(Tarefa):
    def __init__(self, nome_tarefa, jogo: str, nivel=0, descricao=None, data_realizaca=None, data_limite=None):
        super().__init__(nome_tarefa, descricao, data_realizaca)
        self.jogo = jogo
        self.nivel = nivel
        self.__data_limite = None
        if data_limite is not None:
            self.data_limite = data_limite

    def __str__(self):
        return f"[Tarefa Gamer] {super().__str__()}"

    @property
    def jogo(self) -> str:
        return self.__jogo

    @jogo.setter
    def jogo(self, nome_jogo: str):
        self.__jogo = nome_jogo

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, valor):
        self.__nivel = valor

    @property
    def data_limite(self):
        return self.__data_limite

    @data_limite.setter
    def data_limite(self, str_data_limite):
        self.__data_limite = None
        if str_data_limite is not None:
            try:
                self.__data_limite = datetime.strptime(str_data_limite, "%d-%m-%Y")
            except ValueError as e:
                print(f"Erro ao converter \"{str_data_limite}\": {e}")

    def exibir_dados(self):
        data_limite = f"{self.__data_limite.strftime('%d-%m-%Y')}" if self.data_limite is not None else "Sem data definida"
        txt = f"{super().exibir_dados()} \n Data Limite: {data_limite}"
        if self.jogo:
            txt += f"\n Jogo: {self.jogo}"
        if self.nivel != 0:
            txt += f"\n Nível: {self.nivel}"
        return txt

    def definir_termino(self):
        self.data_realizacao = datetime.now()
        if self.data_limite is not None and self.data_realizacao > self.data_limite:
            str_desc = f"{self.descricao} [Concluída em atraso]" if self.descricao else "[Concluída em atraso]"
            self.descricao = str_desc
