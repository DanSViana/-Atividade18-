'''
Crie, em Python, um CRUD de usuários completo (Cadastrar, Pesquisar/Listar, Alterar e Excluir).
O programa deverá:

- Cadastrar usuário
- Listar todos os usuários
- Alterar os dados do usuário
- Excluir usuário
- Sair do programa

O usuário deverá cadastrar:

- Nome completo
- Data de Nascimento
- CPF
- Profissão
- E-mail
- Endereço
- Telefone
'''
# tupla 
chaves = ('Nome Completo', 'Data de Nascimneto', 'CPF', 'Profissão', 'E-mail', 'Endereço', 'Telefone')

usuarios = [
    {
        chaves[0]: 'Vinicius Nelson Castro',
        chaves[1]: '25/05/1944',
        chaves[2]: '697.334.828-97',
        chaves[3]: 'Autônomo',
        chaves[4]: 'vinicius_castro@img.com.br',
        chaves[5]: 'Travessa Flamengo_Belo Jardim I_Rio Branco',
        chaves[6]: '(43) 98774-6133'
    },
    {
        chaves[0]: 'Osvaldo Cauã Gonçalves',
        chaves[1]: '06/07/1960',
        chaves[2]: '647.989.633-56',
        chaves[3]: 'Desempregado',
        chaves[4]: 'osvaldo-goncalves94@lavabit.com',
        chaves[5]: 'Rua Lino Galbetti_Rua Lino Galbetti',
        chaves[6]: '(43) 2649-4930'
    },
    {
        chaves[0]: 'Gustavo Iago Cláudio Farias',
        chaves[1]: '24/01/1947',
        chaves[2]: '832.824.993-61',
        chaves[3]: 'Empreendedor',
        chaves[4]: 'gustavo_iago_farias@focoreducao.com.br',
        chaves[5]: '(47) 98639-8319',
        chaves[6]: 'Rua Antônio Raulino_Blumenau'
    },  
    {
        chaves[0]:'Milena Betina Isabela Dias',
        chaves[1]: '21/01/1964',
        chaves[2]: '884.059.172-92',
        chaves[3]: 'Cabeleireira',
        chaves[4]: 'milena_dias@montcalm.com.br',
        chaves[5]: '(18) 98349-6853',
        chaves[6]: 'Praça Américo Fiorotto_Birigüi'
    }
]
# adicionar um novo dicionário a lista
usuario = {}

for i in range(len(chaves)):
    usuario[chaves[i]] = input(f'Informe {chaves[i]}:')

usuarios.append(usuario)
print(f'\nUsuário cadastrado com sucesso!')

# reexibindo a nova lista de usuário
print(f'\n{'='*10} LISTA DE USUÁRIOS {'='*10}\n') 

for usuario in usuarios:
    for chave in chaves:
        print(f'{chave}: {usuario[chave]}')



