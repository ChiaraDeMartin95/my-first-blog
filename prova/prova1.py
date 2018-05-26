print('Ciao,Chiara')
#ciao, bello
def ciao():
    print('Ciao')
    print('come stai?')

ciao()

def hello(nome):
    if nome == 'Sonia':
        print("hello, Sonia")
    elif nome == 'Chiara':
        print("Ciao, Chiara")
    else:
        print('Ciao, anonimo')

hello('Sonia')

def ciaone(nome):
    print ('Ciao ' + nome +'!')

ragazze = ['Chiara', 'Lucia', 'Tommasa']
for nome in ragazze:
    ciaone(nome)

print('ecco lista di numeri')
for i in range(1,6):
    print(i)
