# ========== Classe =============

class LinkedList:
    def __init__(self):
        raise NotImplemented

    def add_to_end(self, value):
        """ Adiciona um nono valor ao final da lista"""
        raise NotImplemented

    def add_to_beginning(self, value):
        """ Adiciona um nono valor ao início da lista"""
        raise NotImplemented

    def delete(self, value):
        """ Acha o valor e apaga o nó correspondente"""
        raise NotImplemented

    def get_size(self):
        """ Retorna a quantidade de elementos da lista"""
        raise NotImplemented

    def get_in_position(self, position):
        """ Retorna o valor na posição informada"""
        raise NotImplemented


# ========== Problemas =============

def is_palindrome(lista_encadeada):
    """ Retorna se a lista encadeada é palíndromo"""
    raise NotImplemented


def find_last_even(lista_encadeada):
    """ Retorna o último valor par da lista"""
    raise NotImplemented


def invert(lista_encadeada):
    """ Inverte a lista encadeada"""
    raise NotImplemented


def remove_duplicates(lista_encadeada):
    """ Remove duplicatas em uma lista ordenada"""
    raise NotImplemented


def merge(listaA, listaB):
    """ Retorna uma lista encadeada com as listas A e B intercaladas
    Exemplo:
        listaA = 1 -> 2 -> 4 ->8
        listaB = 3 -> 6 -> 12
        resposta = 1 -> 3 -> 2 -> 6 -> 4 -> 12 -> 8
    """