h = float(input ('digite sua altura em metros:'))
sexo=str(input ('digite seu sexo, sendo F feminino e M masculino'))
feminino='f'
masculino='m'
formulah=(72.7*h)-58
formulam= (62.1*h)-44.7

if sexo == masculino:
    print(f"seu peso ideal é: {formulah} kg")
          
else:
    print(f" seu peso ideal é: {formulam}kg")