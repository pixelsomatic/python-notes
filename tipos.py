tipo = input('Coloca mais um número por favor: ')
print('E {} é:\n Int -> {}\n String -> {}\n Alfanumérico -> {}'.format(tipo, tipo.isnumeric(), tipo.isalpha(), tipo.isalnum()))

tipos = input('Escreve alguma coisa aí: ')
print('O que tu mandou só tem espaço: ', tipos.isspace())
print('O que tu mandou é número: ', tipos.isdigit())
print('O que tu mandou é alfabético: ', tipos.isalpha())
print('O que tu mandou é alfanumérico: ', tipos.isalnum())
print('O que tu mandou está em maiúscula: ', tipos.isupper())
print('O que tu mandou está em minúscula: ', tipos.islower())
print('O que tu mandou está capitalizada: ', tipos.istitle())