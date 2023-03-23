#Desenvolva um método que calcula o consumo de combustível, ou seja a
#quantidade de litros consumidos em uma viagem de veículo.

distância  =  int ( input ( 'Informe a distância percorrida (Km): ' ))
kmLitro  =  float ( input ( 'Informe o consumo (Km/L): ' ))

def  calcConsumo ( distancia , kmLitro ):
    res  =  distancia / kmLitro
    return res

consumo  =  calcConsumo (distância, kmLitro)

print ( f'Foram consumidos {consumo :.2F} L de combustível' )