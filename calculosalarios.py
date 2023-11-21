cargo=input("digite o código do seu cargo")
salario=float(input('digite seu salário'))
auxadmnin='100'
engenheiro='101'
gerente='102'

if cargo==auxadmnin:
    print(f"Seu cargo é Auxiliar Administrativo e seu novo salário é R$ {(salario*0.20)+(salario)}")
elif cargo==engenheiro:
    print(f"Seu cargo é engenheiro e seu novo salário é R$ {(salario*0.15)+(salario)}")
elif cargo==gerente:
    print(f"Seu cargo é Gerente e seu novo salário é R$ {(salario*0.10)+(salario)}")
else:
    print('você não teve aumento salarial')