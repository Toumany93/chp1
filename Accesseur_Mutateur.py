class Computer():
    def __init__(self):
        self._cpu = "Intel"
        self._ram = 32
        self._hdd = 512
        print("Création de l'objet")
    
    def _get_cpu(self):
        # print("Passage par l'accesseur de cpu pour afficher sa valeur")
        return self._cpu

    def _set_cpu(self,newValue):
        # print("Passage par le mutateur de cpu pour modifier sa  valeur")
        self._cpu = newValue

    cpu = property(_get_cpu,_set_cpu)



    
    def _get_ram(self):
        # print("Passage par l'accesseur de ram pour afficher sa valeur")
        return self._ram

    def _set_ram(self,newValue):
        # print("Passage par le mutateur de ram pour modifier sa  valeur")
        self._ram = newValue

    ram = property(_get_ram,_set_ram)


    def _get_hdd(self):
        # print("Passage par l'accesseur de hdd pour afficher sa valeur")
        return self._hdd

    def _set_hdd(self,newValue):
        # print("Passage par le mutateur de hdd pour modifier sa  valeur")
        self._hdd = newValue

    hdd = property(_get_hdd,_set_hdd)

monPc = Computer()
monPc.cpu = "AMD"
monPc.ram = 64
monPc.hdd = "1 To"

print("L'attribut cpu:",monPc.cpu)
print(f"L'attribut ram est: {monPc.ram}")
print(f"L'attribut hdd est: {monPc.hdd}")
