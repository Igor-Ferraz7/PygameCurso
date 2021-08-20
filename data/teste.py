from random import choice
from unittest.case import TestCase
lst = [str(i) for i in range(10)]
es = choice(lst)
# print(es)
a = False


class teste_a(TestCase):
    def teste_False(self):
        self.assertFalse(a)

# def teste():
#     for p in range(0, 1):
#         if p == 0:
#             return True
#     return False #caso p == 0, o False não irá sobrepor o True, pois o return irá "breakar" :>
#
# if not True:
#     print('nao vai ser mostrado, pois não é verdadeiro')
# if not False:
#     print('vai ser mostrado, pois é verdadeiro')

