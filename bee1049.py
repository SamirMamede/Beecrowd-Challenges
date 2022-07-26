'''
Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a 
figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

c1 = input()
c2 = input()
c3 = input()

animais = {
    'vertebrado': {
            'ave':{
                'carnivoro': 'aguia',
                'onivoro': 'pomba'
        },
            'mamifero':{
                'onivoro': 'homem',
                'herbivoro': 'vaca'
        }
    },
    'invertebrado':{
            'inseto':{
                'hematofago': 'pulga',
                'herbivoro': 'lagarta'
        },
            'anelideo':{
                'hematofago': 'sanguessuga',
                'onivoro': 'minhoca'
        }
    }
}

print(animais[c1][c2][c3])