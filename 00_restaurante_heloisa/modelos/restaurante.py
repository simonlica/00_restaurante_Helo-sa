#criando uma classe em py

class Restaurante:
    nome=''
#questao 4 
    categoria=''
    ativo=false

restaurante_praca=Restaurante()
#questao 5
restaurante_praca.nome='Bistro'
#questao 1
restaurante_praca.categoria='Italiana'

restaurante_pizza=Restaurante()
#qustao 6
restaurante_pizza.nome="PizzaPlace"
restaurante_pizza.categoria="Fast Food"

restaurantes=[restaurante_praca,restaurante_pizza]

#print(restaurante_praca.ativo)

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))
#questao 2
print(restaurante_praca.nome)

#questao 3
if (restaurante_praca.ativo):
        print("Restaurante praça ativo")
else:
        print("Restaurante praça inativo")

#questao 7

if (restaurante_pizza.categoria):
        print("A categoria e Fast Food")

else:
        print("A categoria não e Fast Food")

#questao 8 
if (restaurante_pizza.ativo):
        print("Restaurante praça inativo")
else:
        print("Restaurante praça ativo")


