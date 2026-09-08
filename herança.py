class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

class Desenvolvedor(Funcionario):
        def linguagem(self):
            print("Caio programa em python")

class AnalistaDeSeguranca(Funcionario):
        def analisar(self):
            print("Caio está analisando vulnerabilidades")

dev = Desenvolvedor("Caio", 14, 1500)
analista = AnalistaDeSeguranca("JoãoBINHO", 16, 2400)

print(dev.nome)
