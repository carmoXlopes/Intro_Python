# 1 - importação de bibliotecas

# 2 - Classe

# 3- Métodos e funções

def print_hi(name):
   print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def area_retangulo(largura, comprimento):
    resultado  = largura * comprimento
    return resultado

def area_quadrado(lado):
    return lado ** lado
if __name__ == '__main__':
    print_hi('Aline')

def contagem_progressiva(fim):
    for numero in range(fim):  #range significa intervalo... Ele vai repetir o bloco de 0 até o fim
        print(numero)

def apoiar_candidato(nome,vezes):
    for numero in range(vezes):
        # contador = numero +1
        # print(f'{contador} - {nome}')
        if numero < 9:
            print(f'00{numero+1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome)

def brincar_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('plim!')
        else:
            print('{:0>3}'.format(numero))

#exibição de resultado

resultado = area_retangulo(3,4)
print(f'a area do retangulo é de  {resultado} m²')

resultado = area_quadrado(5)
print(f'a area do quadrado é {resultado}')

contagem_progressiva(11)

apoiar_candidato('aline', 100)

brincar_plim(3)