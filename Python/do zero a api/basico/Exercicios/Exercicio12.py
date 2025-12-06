class Filme:
    
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.numero_exibicoes = 0
        
        
    def __str__(self):
        return f'Filme: {self.titulo}'
    
    def __len__(self):
        return self.duracao
        
filme = Filme('John Wick', 113)
print(filme)
print(len(filme))

print(vars(filme))
    