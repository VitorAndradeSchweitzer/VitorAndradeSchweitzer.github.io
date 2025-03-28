class Pilha():
    def __init__(self, limit):
        self.pilha = []
        self.limit = limit
        
    def push(self, valor):
        if len(self.pilha) < self.limit:
            self.pilha.append(valor)
            return
        raise MemoryError
        
    def pop(self):
        if len(self.pilha) >= 1:
            valor = self.pilha(len(self.pilha - 1))
            self.pilha.pop()
            return valor
        return MemoryError
            
    def top(self):
        if len(self.pilha) >= 1:
            return self.pilha[len(self.pilha) - 1]
        return MemoryError
        
    def pilha_cheia(self):
        if len(self.pilha) >= self.limit:
            return True
        return False
    
    def pilha_vazia(self):
        if len(self.pilha) == 0:
            return True
        return False
    
    def num_elements(self):
        return len(self.pilha)
    
