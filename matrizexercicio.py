pessoa1={}

pessoa1['nome']='Renato'
pessoa1['email']='renato@teste'
pessoa1['telefone']='9865-5689'

pessoa2={}

pessoa2['nome']='paula'
pessoa2['email']='paulatejando@teste'
pessoa2['telefone']='9865-745545'


pessoa3={}

pessoa3['nome']='luisa'
pessoa3['email']='luisa123@teste'
pessoa3['telefone']='9865-4545'

agenda=[]

agenda.append(pessoa1)
agenda.append(pessoa2)
agenda.append(pessoa3)

for contato in agenda:
    print(contato['nome'])
    print(contato['email'])
    print(contato['telefone'])