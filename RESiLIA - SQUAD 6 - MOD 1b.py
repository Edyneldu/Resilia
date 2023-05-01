#INICIO DO CODIGO DA CONCESSIONÁRIA PORSCHE

print('\n --- Um Porsche é tão individual quanto o seu proprietário.---\n\n SEJA BEM VINDO A PORSCHE, A MARCA MAIS DESEJADA DO AUTOMOBILISMO.\n' )
nome= input('Como deseja ser chamado? ')
email= input('\nDigite seu e-mail: ')
tel= input('\nDigite seu telefone: ')
def menu():
    
    print ('\n1- Carros')
    print ('2- Mecânica')
    print ('3- Atendimento')
    print ('4-sair')
    
    opcao= input('\nDigite um número para o opção que desejar: ')
    

    if opcao == '1':
        menu_de_carros()
    elif opcao == '2':
        mecanica()
    elif opcao == '3':
        atendimento()
    else:
        return

def menu_de_carros():
    print ('\n1- Porche 911')
    print ('2- Panamera')
    print ('3- Macan')
    print ('4- 718\n')
    escolhe_carro= input('Digite um número para o opção do carro que deseja: ')
    
    if escolhe_carro == '1':
        opcionais_do_carro()
    elif escolhe_carro == '2':
        opcionais_do_carro()    
    elif escolhe_carro == '3':
        opcionais_do_carro() 
    elif escolhe_carro == '4':
        opcionais_do_carro()    
    else:
        return 



# Início da parte estética co carro
def opcionais_do_carro():  
     
    menu_de_cores()

    

def menu_de_cores():
    print('\nAgora vamos escolher a cor externa de seu carro')
    
    print ('\n1- Vermelho')
    print ('2- Azul')
    print ('3- Amarelo')
    print ('4-sair\n')
    
    escolhe_cor= input('Digite um número para o opção que desejar: ')
    
    if escolhe_cor == '1':
        print('\nOK A cor externa do seu carro será vermelha\n')
        menu_de_rodas()
    elif escolhe_cor == '2':
        print('\nOK A cor externa do seu carro será azul\n')
        menu_de_rodas()
    elif escolhe_cor == '3':
        print('\nOK A cor externa do seu carro será amarelo\n')
        menu_de_rodas()
    else:
        return

def menu_de_rodas():
    
    print('Agora vamos escolher a cor das rodas de seu carro\n')
    
    print ('1- Vermelho')
    print ('2- Azul')
    print ('3- Amarelo')
    print ('4-sair\n')
    
    escolhe_rodas= input('Digite um número para o opção que desejar: ')
   
    if escolhe_rodas == '1':
        print('OK A cor das rodas de seu carro será vermelha\n')
        menu_do_interior()
    elif escolhe_rodas == '2':
        print('OK A cor das rodas de seu carro será azul\n')
        menu_do_interior()
    elif escolhe_rodas == '3':
        print(' OK A cor das rodas de seu carro será amarelo\n')
        menu_do_interior()
    else:
        return
    
    

def menu_do_interior():
    print('Agora vamos escolher a cor do interior de seu carro')
    print('\n')
    print ('1- Vermelho')
    print ('2- Azul')
    print ('3- Amarelo')
    print ('4-sair\n')
    
    escolhe_interior= input('Digite um número para o opção que desejar: ')
    print('\n')
    if escolhe_interior == '1':
         print('Seu carro terá interior vermelho\n\n\n')
         mensagem()    
    elif escolhe_interior == '2':
        print('Seu carro terá interior azul\n\n\n')
        mensagem()
    elif escolhe_interior == '3':
        print(' Seu carro teraá interior amarelo\n\n\n')
        mensagem()
    else:
        return
    
    
def mensagem():
    print (nome,'\nAgradecemos o seu contato.\nAnotamos todas as suas preferências e entraremos em contato em breve.\n\n\n\n')


# Menu de Mecânica

def mecanica():
    print ('1-Motor')
    print ('2-Freio e suspensão')
    print ('3-troca de óleo')
    print ('4- retorna')
    print ('5-sair')

    opcao3= input(' digite um número para o opção que desejar')

    if opcao3 == '1':
        menumotor()
    elif opcao3 == '2':
        freio_suspensao()
    elif opcao3 == '3':
        print ('opção C')
    elif opcao3 == '4':
        menu()
    else:
        return

# Início da parte de motor

def menumotor():
    print('mensagem inicial para o cliente')
    print ('1-embreagem')
    print ('2-câmbio')
    print ('3-cabeçote')
    print ('4-sair')
    
    opcao= input('digite um número para o opção que desejar: ')


    if opcao == '1':
        print(' alguma coisa sobre embreagem')
    elif opcao == '2':
        print('alguma coisa sobre câmbio')
    elif opcao == '3':
        print('alguma coisa sobre cabeçote')
    else:
        return

# freio e suspensão

def freio_suspensao():
    print('mensagem inicial para o cliente')
    print ('1- Pastilhas de Freio')
    print ('2- óleo da suspensão')
    print ('3- Discos')
    print ('4-sair')
    
    opcao= input('digite um número para o opção que desejar: ')


    if opcao == '1':
        print(' alguma coisa sobre Pastilhas de freio')
    elif opcao == '2':
        print('alguma coisa sobre óleo da suspensão')
    elif opcao == '3':
        print('alguma coisa sobre discos')
    else:
        return
    
    # Troca de óleo

def troca_de_oleo():
    print('mensagem inicial para o cliente')
    print ('1- Óleo de motor')
    print ('2- Óleo de câmbio')
    print ('3- Óleo de freio')
    print ('4-sair')
    
    opcao= input('digite um número para o opção que desejar: ')


    if opcao == '1':
        print(' alguma coisa sobre òleo de motor')
    elif opcao == '2':
        print('alguma coisa sobre Óleo decâmbio')
    elif opcao == '3':
        print('alguma coisa sobre Óleo de freio')
    else:
        return



# Atendimento


def atendimento():
    print ('1-Recepção')
    print ('2-Peças')
    print ('3-ShowRoom')
    print ('4- retorna')
    print ('5-sair')

    opcao4= input(' digite um número para o opção que desejar')

    if opcao4 == '1':
        print ('Alguma coisa sobre Recepção')
    elif opcao4 == '2':
        print('Alguma coisa sobre Peças')
    elif opcao4 == '3':
        print ('Alguma coisa sobre showRoom')
    elif opcao4 == '4':
        menu()
    else:
        return


def reiniciar():
    opcao = input("Deseja fazer outra pergunta? (s/n)")

    if opcao.lower() == "s":
        menu()
    else:
        print("Obrigado por utilizar nosso bot de atendimento!")
        return


menu()



#REUSO DE CODIGO ABAIXO (RECICLAGEM):
#
#Menu=()
#resposta1 = None
#cliente = None
#tel = None
#email = None
#veiculo1 = ('PORSCHE 911')
#veiculo2 = ('PANAMERA')
#veiculo3 = ('MACAN')
#veiculo4 = ('718')
#veiculo=(veiculo1,veiculo2,veiculo3,veiculo4)
#
#
#print(' \n\n\n\n\n --- Um Porsche é tão individual quanto o seu proprietário.---\n\n SEJA BEM VINDO A PORSCHE, A MARCA MAIS DESEJADA DO AUTOMOBILISMO.\n\n ' )
#
#menuPrincipal=Menu
#
#print ('1 - Show Room')
#print ('2 - Mecânica')
#print ('3 - SAC: Serviço de Atendimnto ao Cliente')
#print ('4 - Sair \n\n')
#opção=input('Digite o número correspondente a opção que deseja: ')
#print('\n você digitou: '+opção)
#
#
#if opção == ('1'):
#    resposta1=input('\n Agora vamos personalisar o seu Porsche? \n\n Digite: "sim" para (sim), "nao ou não" para (não) \n\n')
#   print('\n Você digitou: ' + str(resposta1))
#
#    if resposta1 == ('sim'):
#            
#           print('\n Primeiro vamos precisar, realizar um breve cadrasto. ;) \n')
#
#           cliente=input('\nComo você gostaria de ser chamado? ')
#
#           tel=input('\n Digite o seu telefone para contato: ')
#
 #           email=input('\n Digite o seu e-mail: ')
  #         
     #         print('\n Agradecemos as informações, no momento estamos trabalhando com 3 modelos de Porsche, escolha abaixo o modelo de sua preferência: \n\n\n')
#
 #           veiculo1=print('1 - PORSCHE 911\n')
  #          veiculo2=print('2 - PANAMERA\n')
   #         veiculo3=print('3 - MACAN\n')
    #        veiculo4=print('4 - 718\n')
#
           # veicul=input('\n Digite o número correspondente ao modelo escolhido: ')
           # print('\n O modelo escolhido foi:')
           # if input(1):
#                  
#
 #           
 #          # print(veicul)
#
                #
            #
  #          
#
#
#                 
#                
#print('\n\n\n ...to be continue...\n\n\n\n')
#
#REUSO DE CODIGO ABAIXO (RECICLAGEM):
#
# teste de função para menu inicial
#def menu():
   
  
    #print ('1- Carros')
    #print ('2- Mecânica')
   # print ('3- Atendimento')
  #  print ('4-sair')
    
 #   opcao= input('Digite um número para o opção que desejar: ')
#
 #   if opcao == '1':
 #       opcionais_do_carro()
  #  elif opcao == '2':
  #      mecanica()
  #  elif opcao == '3':
  #      atendimento()
 #   else:
 #       return
