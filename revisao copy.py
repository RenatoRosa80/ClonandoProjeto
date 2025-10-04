"""
. Crie uma classe Pessoa com atributos de instância nome e idade.
2. Adicione um método de instância que mostre nome e idade.
3. Crie uma subclasse Aluno que herda de Pessoa e tenha um atributo adicional curso.
4. Na classe Aluno, sobrescreva o método de instância para também mostrar o curso.
5. Crie objetos de Pessoa e Aluno e teste os métodos.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
       
    def mostrar(self):
        print(f"Meu nome é {self.nome} e minha idade é {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def mostrar(self):
        print(f"Meu nome é {self.nome} e minha idade é {self.idade} e estou cursando {self.curso}")

p1 = Pessoa("Pablo", 34)
a1 = Aluno("Matheus", 34, "python")
p1.mostrar()
print()
a1.mostrar()


      
