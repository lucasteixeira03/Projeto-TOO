from datetime import datetime

class Agendamento:
    def __init__(self, data_inicio, data_final, atividades, nome_agendamento, local):
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.atividades = atividades
        self.nome_agendamento = nome_agendamento
        self.local = local

    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self, d):
        self.__data_inicio = None 
        if d is not None:
            try:
                self.__data_inicio = datetime.strptime(d, "%d-%m-%Y %H:%M")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")

    @property
    def data_final(self):
        return self.__data_final
    
    @data_final.setter
    def data_final(self, d):
        self.__data_final = None 
        if d is not None:
            try:
                self.__data_final = datetime.strptime(d, "%d-%m-%Y %H:%M")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")

        if self.data_inicio and self.data_final:
            if self.data_final < self.data_inicio:
                print("Data final não pode ser anterior a data de início.")
                self.__data_final = None

    @property
    def atividades(self):
        return self.__atividades

    @atividades.setter
    def atividades(self, atv):
        self.__atividades = atv

    @property
    def nome_agendamento(self):
        return self.__nome_agendamento

    @nome_agendamento.setter
    def nome_agendamento(self, nomeAg):
        self.__nome_agendamento = nomeAg

    @property
    def local(self):
        return self.__local

    @local.setter
    def local(self, local):
        self.__local = local

    def exibir_dados(self):
        data_inicio = f"{self.data_inicio.strftime('%d-%m-%Y %H:%M') if self.data_inicio is not None else 'Sem data definida'}"
        data_final = f"{self.data_final.strftime('%d-%m-%Y %H:%M') if self.data_final is not None else 'Sem data definida'}"
        return f"Agendamento:\n Nome: {self.nome_agendamento}\n Local: {self.local}\n Data Início: {data_inicio}\n Data Final: {data_final}\n Atividades: {self.atividades}"