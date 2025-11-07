class Monster:

    def __init__(self, name):
        self.name = name
        self.teeth = -1
        self.size = -1        
        self.attack_power = -1
    
    def get_name (self):
        return self.name
    
    def get_size (self):
        return self.size
    def set_size (self, value):
        if value>0:
            self.size = value

    def get_teeth (self):
        return self.teeth
    def set_teeth (self, value):
        if value>=0:
            self.teeth = value

    def get_attack_power (self):
        return self.attack_power
    def set_attack_power (self, value):
        if value>=0:
            self.attack_power = value
    
    def scare (self):
        if 80 > self.attack_power > 50:
            return "Very Scary"
        elif self.attack_power > 10:
            return "Cute Monster"
        elif 10 < self.attack_power < 50:
            return "A bit Scary"
        else:
            return "Runnnnnn"
        
    def __str__(self):
        return f"Stats Name: {self.get_name()}, Size: {self.get_size()}, Teeth: {self.get_teeth()}, Attack Power: {self.get_attack_power()} . It also have {self.get_teeth()} so it is {self.scare()}"
    
monster1 = Monster("Klaus")
monster1.set_size(0.1)
monster1.set_teeth(30)
monster1.set_attack_power(1) 

print(monster1)