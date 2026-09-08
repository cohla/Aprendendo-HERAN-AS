# 🐍 Herança em Python — POO
Neste projeto pratiquei os conceitos básicos de Herança em Programação Orientada a Objetos (POO) utilizando Python.

# 📚 O que aprendi
Criar uma classe pai (superclasse).
Criar classes filhas (subclasses).
Utilizar herança através da sintaxe class ClasseFilha(ClassePai).
Herdar atributos da classe pai.
Herdar e reutilizar métodos da classe pai.
Adicionar métodos específicos às classes filhas.
Criar objetos a partir das subclasses.
Diferenciar atributos de métodos.
Entender como a herança ajuda a evitar repetição de código.


# 💻 Exemplo
class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


class Desenvolvedor(Funcionario):
    def linguagem(self):
        print("Caio programa em Python")


class AnalistaDeSeguranca(Funcionario):
    def analisar(self):
        print("Caio está analisando vulnerabilidades")


dev = Desenvolvedor("Caio22", 14, 1500)
analista = AnalistaDeSeguranca("JoãoBINHO", 16, 2400)

print(dev.nome)
dev.linguagem()

print(analista.nome)
analista.analisar()


# 🧠 Estrutura
Funcionario
├── nome
├── idade
├── salario
│
├── Desenvolvedor
│   └── linguagem()
│
└── AnalistaDeSeguranca
    └── analisar()


# 🎯 Objetivo
Meu objetivo com este exercício foi entender como classes podem reutilizar características de outras classes, começando a desenvolver uma base sólida em POO com Python.
Projeto criado durante meus estudos de Programação Orientada a Objetos.

📝 Explicando

⚠️ Vale lembrar: este não é meu primeiro projeto. Este projeto já é meio antigo e estou repostando ele no GitHub para registrar minha evolução nos estudos. 🚀

Estou utilizando este repositório para documentar minha evolução e meus aprendizados durante os estudos de programação.
