class Villager:
    
    def __init__(self, name, attack = 0, health = 50, defense = 0, is_alive = True):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack = attack
        self.is_alive = is_alive
        

    def check_health(self, incoming_attack_value):
        dano  = (incoming_attack_value - self.defense) if incoming_attack_value > self.defense else 0 
        self.health -= dano
        if self.health <= 0:
            self.is_alive = False
            self.health = 0
            return(False, 'Target is Dead!')
            
    def normal_attack(self, target):
        return target.check_health(self.attack)
        
    def __str__(self):
        return f'Nome: {self.name}, HP: {self.health}, Defesa:{self.defense}, Ataque: {self.attack}, Esta vivo?: {self.is_alive}'
    
    
class Mage(Villager):
    
    def __init__(self, name):
        super().__init__(name)
        self.mana = 100
        self.attack = 10
 
    def __str__(self):
        return f'Nome: {self.name}, HP: {self.health}, Mana: {self.mana}, Defesa:{self.defense}, Ataque: {self.attack}, Esta vivo?: {self.is_alive}'
        
    def fire_ball(self, target):
        
        if self.mana > 0:
            super().normal_attack(target)
            self.mana -= 20
        else:
            return (False, 'Not enough mana!')
        









        
        