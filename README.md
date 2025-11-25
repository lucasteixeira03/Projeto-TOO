# 📌 Projeto-TOO – Sistema de Tarefas e Agendamentos  

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python 3.x">
  <img src="https://img.shields.io/badge/POO-Orientada%20a%20Objetos-orange.svg" alt="POO">
  <img src="https://img.shields.io/badge/Status-%20Finalizado-success.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-Acadêmico-lightgrey.svg" alt="Licença acadêmica">
</p>


### **Disciplina: Tecnologia Orientada a Objetos (TOO) – BCC | IFSUL**

Este projeto foi desenvolvido para a disciplina **Tecnologia Orientada a Objetos (TOO)** do curso de **Bacharelado em Ciência da Computação – IFSUL – Campus Passo Fundo**.  
Seu objetivo é demonstrar, na prática, a aplicação dos **princípios fundamentais de Programação Orientada a Objetos em Python**, incluindo:

- Abstração  
- Encapsulamento  
- Herança (simples e múltipla)  
- Polimorfismo  
- Classes abstratas  
- Uso de propriedades (`@property`)  
- Enumerações  
- Modularização  
- Padrões de criação (Factory Method)

O sistema implementado permite manipular diferentes tipos de **tarefas**, **agendamentos** e **compromissos**, simulando diversos cenários práticos dentro da POO.

---

# 🎯 Objetivos do Sistema

O projeto implementa um sistema de gerenciamento de tarefas, subdivididas em:

- **Tarefas pessoais**  
- **Tarefas profissionais**  
- **Tarefas escolares**  
- **Tarefas gamer**  
- **Agendamentos**  
- **Compromissos** (herança múltipla: Tarefa + Agendamento)

Os arquivos de teste demonstram o funcionamento de cada parte.

---

# 🧱 Principais Conceitos de POO Aplicados

### ✔️ 1. **Classe Abstrata**
A classe `Tarefa` é abstrata e define métodos obrigatórios:

- `exibir_dados()`
- `definir_termino()`

Isso garante que TODAS as subclasses implementem sua própria versão.

---

### ✔️ 2. **Herança**
- `TarefaEscolar`, `TarefaProfissional`, `TarefaGamer` e `TarefaPessoal` herdam de `Tarefa`.
- `Compromisso` herda **simultaneamente** de `Agendamento` e `Tarefa`.

---

### ✔️ 3. **Polimorfismo**
Cada subclasse implementa sua própria versão de:

- `exibir_dados()`
- `definir_termino()` (quando aplicável)

---

### ✔️ 4. **Encapsulamento**
Uso consistente de:

```python
@property
def atributo(self): ...

@atributo.setter
def atributo(self, valor): ...
```
---

### ✔️ 5. **Enumerações (Enum)**
Utilizado em:

- `StatusTarefa`
- `TipoTarefaPessoal` 
- `DificuldadeJogo`

Para garantir valores válidos e evitar strings soltas no código.

---

### ✔️ 6. **Factory Method**

`TarefaFactory.py` implementa um criador de tarefas baseado em:

```bash
TarefaFactory.criar_tarefa(tipo_tarefa="pessoal", ...)
```
Uma forma muito comum e importante de abstrair a criação de objetos.

--- 

## 🛠️ Como Executar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/SEU-USUARIO/Projeto-TOO.git
```

2. **Acesse a pasta do projeto:**

```bash
cd Projeto-TOO
```

3. **Dica: Certifique-se de estar com o Python configurado corretamente e execute sempre a partir da raiz do projeto.**

---

## 📚 Conteúdos Exercitados

- **Classes**

- **Objetos**

- **Herança simples e múltipla**

- **Encapsulamento e propriedades**

- **Classes abstratas**

- **Métodos abstratos**

- **Polimorfismo**

- **Módulos e organização de pastas**

- **Padrão Factory Method**

- **Manipulação de datas com datetime**

- **Validação e limpeza de dados**

---

## 🏁 Conclusão

#### Este projeto reúne e demonstra os conceitos essenciais da Programação Orientada a Objetos utilizando Python.
#### Foi desenvolvido com foco em aprendizado, boa organização de código e clareza estrutural para facilitar manutenção e expansão.

## 👨‍💻 Autor

*Desenvolvido por Lucas de Sousa Teixeira.*