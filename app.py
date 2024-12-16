from itens.maquinario import Biblioteca
from itens.livro import Livro
from itens.revista import Revista
biblioteca_cn = Biblioteca('Da Vila')
biblioteca_you = Biblioteca('Mooneys')

#biblioteca_cn.alterna_estado()
#biblioteca_cn.receber_avaliacao('Alessandro', 9.0)
#biblioteca_you.receber_avaliacao('Beck', 3.0)
livro1 = Livro('Diary of a Wimpy Kid', 'Jeff Kinny', 36.99, '654-032')
revista1 = Revista('National Geographic', 'Jhon Doe', 23.99, 'Quinta')
biblioteca_cn.adicionar_item(livro1)
biblioteca_you.adicionar_item(revista1)

def main():
    #Biblioteca.listar_bibliotecas()
    biblioteca_cn.exibir_itens()
    biblioteca_you.exibir_itens()

if __name__ == '__main__':
    main()    