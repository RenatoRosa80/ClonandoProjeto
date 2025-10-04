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

   
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

 
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    
    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Curso: {self.curso}")

 
pessoa1 = Pessoa("Carlos", 45)
aluno1 = Aluno("Ana", 20, "Engenharia")

print("Dados da Pessoa:")
pessoa1.mostrar_dados()

print("\nDados do Aluno:")
aluno1.mostrar_dados()
print()



      
