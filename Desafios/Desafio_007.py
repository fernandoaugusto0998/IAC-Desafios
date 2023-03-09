p = float(input('Digite o valor do produto: '))
d = p * 0.05
pd = p - d
print('O valor do produto com desconto de 5% é R${:.2f}, você economizou R${:.2f}.'.format(pd, d))