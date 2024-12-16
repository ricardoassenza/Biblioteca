from itens.avaliacao import Avaliacao
from itens.item_biblioteca import ItemBiblioteca
class Biblioteca():
    bibliotecas = []
    def __init__(self, nome):
        self.nome = nome
        self.ativo = False
        self.avaliacoes = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome

    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'NOME DA BIBLIOTECA'.ljust(25)} // {'MEDIA DE AVALIAÇÕES'.ljust(25)} // {'STATUS'} ")
        for biblioteca in Biblioteca.bibliotecas:
            print(f'{biblioteca.nome.ljust(25)} // {str(biblioteca.media_avaliacoes).ljust(25)} // {biblioteca.ativo}')

    def alterna_estado(self):
        self.ativo = not self.ativo

    @property
    def ativacao(self):
        return 'ativada' if self.ativo else 'desativada'
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self.avaliacoes:
            return '-'
        soma = sum(avaliacao.nota for avaliacao in self.avaliacoes)   
        media = round(soma / len(self.avaliacoes))
        return media

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def exibir_itens(self):
        print(f'itens da biblioteca {self.nome}\n')
        for i, item in enumerate(self._itens, start=1):
            if hasattr(item, 'isbn'):
                msg_livro = f'{i}. (Livro-->) Titulo= {item._titulo} // autor= {item._autor} // preço= {item._preco} // ISBN= {item.isbn}'
                print(msg_livro)
            else:
                msg_revista = msg_livro = f'{i}. (Revista-->) Titulo= {item._titulo} // autor= {item._autor} // preço= {item._preco} // ISBN= {item.edicao}'
                print(msg_revista)     

