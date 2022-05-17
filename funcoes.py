"""
def series():
    return print("Mr Robot")

series() #chamada da função

def series():
    return "Mr Robot"

print(series()) #chamada da função

## Função com parâmetros
def series(nome, ano):
    return print(f"A série {nome} foi lançada em {ano}.")

series("Mr Robot", 2015)

def series(*args):
    # args = ("mr robot", "onisciente")
    return print(type(args)) #retorna uma tupla, que é uma coleção como um dict, list, set

series("mr robot", "onisciente")


tupla = ("mr robot", "onisciente")
for s in tupla:
    print(s)

def series(*args):
    for s in args:
        print(f"Série: {s}")

#series() # pode não receber parâmetro
series("mr robot", "onisciente", "death, love & robots", "better than us", "sexify")
"""

import json

def series(**kwargs):
    for nome, ano in kwargs.items():
        print(f"A série {nome} foi lançada em {ano}.")
    
    #print(type(kwargs))
    with open("series.json", "w", encoding="utf8") as f:
        json.dump(kwargs, f, indent=2)

series(mr_robot=2015, onisciente=2020, death_love_and_robots=2019, better_than_us=2018, sexify=2021, black_mirror=2011)