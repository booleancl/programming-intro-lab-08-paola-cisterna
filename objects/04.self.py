# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 
class Student:
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills
    def say_name(self):
        print("mi nombre es",self.name,"mi cargo es",self.position,"y mis habilidades son",self.skills)



alice = Student("alice","fullstack developer",["pyhon","git","html","css","javascrip"])
alice.say_name()


chef_Paola = Student("Paola la chef","pasteria",["panqueques","tortas"])
chef_Paola.say_name()