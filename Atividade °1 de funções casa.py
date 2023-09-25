def lin():
    print("-"*56)
# Nesse exemplo a função está contando os valores do parametro e a quantidade de objeto no laço da função
def contador(* num):
    tam= len (num)
    print(f'Recebe os valores de {num} e são ao todo {tam} numero')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 6,5)
lin()

def dobra(lst):      
    pos = 0
    while pos < len(lst):
        lst [pos] *= 2
        pos += 1
valores=[7,5,6,7,4,6,7]
dobra(valores)
print(valores)

lin()

def soma (* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
lin()

# Exercicio do calculo de area com funções

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno{larg}x{comp} é de {a}m²')


print(' Controlde de terreno')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m):'))
area(l, c)


("""
def separatexto():
    print("="*30)
    separatexto()

    pass

lista = [0, 1, 2]

lista[0] = input("Digite seu nome:")
lista[1] = input("Programação realmente é necessario?:")
lista[2] = input("Programação é uma maldição, sim ou não?")

try:
    arquivo = open('felipe.txt', '+x', encoding='utf-8')
except Exception:
    print("Não foi possível criar o arquivo.")


try:
    salvar = open('felipe.txt', '+a')
    for n, i in enumerate(lista):
        print(f'O {n+1}° valor é: {i}.')
        salvar.write(i+'\n')
except Exception:
    print('Não foi possível salvar.')
finally:
    salvar.close()


try:
    ler = open('felipe.txt')
    for n, i in enumerate(ler):
        print(f'{n}°: {i}')
except Exception:
    print('Error')
finally:
    ler.close()

print(lista)

""")
