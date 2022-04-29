# # classes
# class Car:
    
#     def __init__(self, ismi, familiya, ish):
#         self.ismi = ismi
#         self.familiya = familiya
#         self.ish = ish
          
#     def __str__(self):
#         return f"mening ismim {self.ismi} familiyam {self.familiya}. mening ishim {self.ish}."
    
    
#     #Inheritance
# class Malibu(Car):
#     def __init__(self, ismi, familiya, ish, yoshi):
#         super().__init__(ismi, familiya, ish)
#         self.yoshi = yoshi
        
#     def __str__(self):
#         text = super(Malibu, self).__str__()
#         text += f" bundan tashqari yoshim {self.yoshi}."
#         return text
    
# ism1 = Malibu('javohir', 'nematov', 'dasturchi', '15')
# print(ism1)


class My:
    def __init__(self, ism, familiya, ish):
        self.ism = ism
        self.familiya = familiya
        self.ish = ish
        
    def __str__(self):
        return f"Mening ismim {self.ism} va familiyam {self.familiya}. Mening ishim {self.ish}."
        ###
class Pc(My):
    def __init__(self, ism, familiya, ish, pc):
        super().__init__(ism, familiya, ish)
        self.pc = pc
        
    def __str__(self):
        text = super(Pc, self).__str__()
        text += f" Mening kompyuterimning nomi {self.pc}."
        return text
        ###
class coreI(Pc):
    def __init__(self, ism, familiya, ish, pc, coreI):
        super().__init__(ism, familiya, ish, pc)
        self.coreI = coreI
        
    def __str__(self):
        text2 = super(coreI, self).__str__()
        text2 += f" Kompyuterim {self.coreI} protsessorli."
        return text2
    ###
class age(coreI):
    def __init__(self, ism, familiya, ish, pc, coreI, age):
        super().__init__(ism, familiya, ish, pc, coreI)
        self.age = age
        
    def __str__(self):
        text3 = super(age, self).__str__()
        text3 += f" Men {self.age} yoshdaman"
        return text3
    
name1 = age('Javohir', "Ne'matov", 'dasturchi', 'Acer', '3', '15')
print(name1)