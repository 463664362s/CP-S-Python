# Listas RM para todos #
listanome = []
listaserie = []
listarm = []

# Listas RM e nomes para cada série#
lista2rm = []
lista3rm = []
lista4rm = []
lista5rm = []
listarms = (lista2rm,lista3rm,lista4rm,lista5rm)

#VoltaCallison
# Lista dos eventos #
evento1 = [] # Criar e contar história #
evento2 = [] # Teatro: Luz, Câmera e Ação #
evento3 = [] # A língua de sinais #
evento4 = [] # Expressão Artística #
evento5 = [] # Soletrando #
evento6 = [] # Leitura dramática #
evento7 = [] # O corpo fala #
evento8 = [] # O mundo da imaginação #
evento9 = [] # Leitura dinâmica #
evento10 = [] # Criando e recriando com emojis #
lista_oficinas = (evento3,evento10,evento1,evento4,evento9,evento6,evento7,evento8,evento5,evento2)
nome_oficinas = ("A língua de sinais","Criando e recriando com emojis","Criar e contar história","Expressão Artística","Leitura dinâmica",
                "Leitura dramática","O corpo fala","O mundo da imaginação","Soletrando","Teatro: Luz, Câmera e Ação")                     


#-------------------------------------------------------------------------------------------------------------------------------------------------#

while(1):
    # Limitar que o aluno so pode se matricular em no maximo 3 cursos linha 114 #
    listatudo=evento1+evento2+evento3+evento4+evento5+evento6+evento7+evento8+evento9+evento10    
    print("\nMenu de opções")
    print("1 – Cadastrar alunos")
    print("2 – Fazer inscrições")
    print("3 – Listar inscrições")
    print("4 – Sair")
    menu = int(input(""))

    if menu == 1 and len(listarm) == 0:
        while(1):
            rm = int(input("Digite o RM do aluno: "))
            if rm == 0:
                print("Cadastros de alunos finalizado")
                break 
            elif rm in listarm:
                print("RMs duplicados não são validos")  

            elif rm not in listarm:
                nome = str(input("Nome do aluno: "))
                print("Digite a série do aluno: ")
                print("2 - 2ª Série")
                print("3 - 3ª Série")
                print("4 - 4ª Série")
                print("5 - 5ª Série")
                serie = int(input(""))

                def cadastrar_alunos():
                    listaserie.append(serie)
                    listarm.append(rm)
                    listanome.append(nome)

                if serie == 2:
                    listarms[0].append(rm)
                    cadastrar_alunos()

                elif serie == 3:
                    listarms[1].append(rm)
                    cadastrar_alunos()

                elif serie == 4:
                    listarms[2].append(rm)  
                    cadastrar_alunos()

                elif serie == 5:
                    listarms[3].append(rm)
                    cadastrar_alunos()
     
                else:
                    print("Série invalida") 
    elif menu == 1 :
     print("Cadastro indisponivel")       

#-------------------------------------------------------------------------------------------------------------------------------------------------#

    elif menu == 2:
            # Funções para fazer as incrições nas oficinas,limitando no max 3, sem repetições e mostrando a quantidade de vagas #
            def inscricao_oficinas():
                print("Oficinas para esse aluno:")  
                if len(lista_oficinas[lista_inscricao_oficina[0]]) < 10 and rm not in lista_oficinas[lista_inscricao_oficina[0]]:
                    print("1 -",nome_oficinas[lista_inscricao_oficina[0]],10 - len(lista_oficinas[lista_inscricao_oficina[0]]),"vagas disponiveis")
                if len(lista_oficinas[lista_inscricao_oficina[1]]) < 10 and rm not in lista_oficinas[lista_inscricao_oficina[1]]:    
                    print("2 -",nome_oficinas[lista_inscricao_oficina[1]],10 - len(lista_oficinas[lista_inscricao_oficina[1]]),"vagas disponiveis")
                if len(lista_oficinas[lista_inscricao_oficina[2]]) < 10 and rm not in lista_oficinas[lista_inscricao_oficina[2]]: 
                    print("3 -",nome_oficinas[lista_inscricao_oficina[2]],10 - len(lista_oficinas[lista_inscricao_oficina[2]]),"vagas disponiveis")
                if len(lista_oficinas[lista_inscricao_oficina[3]]) < 10 and rm not in lista_oficinas[lista_inscricao_oficina[3]]:    
                    print("4 -",nome_oficinas[lista_inscricao_oficina[3]],10 - len(lista_oficinas[lista_inscricao_oficina[3]]),"vagas disponiveis")
                evento = int(input(""))
                if evento == 1 and rm not in lista_oficinas[lista_inscricao_oficina[0]]:
                    lista_oficinas[lista_inscricao_oficina[0]].append(rm)
                elif evento == 2 and rm not in lista_oficinas[lista_inscricao_oficina[1]]:
                    lista_oficinas[lista_inscricao_oficina[1]].append(rm)
                elif evento == 3 and rm not in lista_oficinas[lista_inscricao_oficina[2]]:
                    lista_oficinas[lista_inscricao_oficina[2]].append(rm)
                elif evento == 4 and rm not in lista_oficinas[lista_inscricao_oficina[3]]:
                    lista_oficinas[lista_inscricao_oficina[3]].append(rm)
                else:
                    print("Oficina invalida")       

            rm = int(input("Digite o RM do aluno: "))
            if rm not in listarm:
                print("“Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")

            elif listatudo.count(rm) == 3:
                print("Aluno ja esta matricula no numero maximo de oficinas")

            # Funções para fazer as incrições nas oficinas para cada serie #
            elif rm in lista2rm: 
                lista_inscricao_oficina = [2,0,7,1]
                inscricao_oficinas()
            elif rm in lista3rm:  
                lista_inscricao_oficina = [2,9,0,6]               
                inscricao_oficinas()
            elif rm in lista4rm:
                lista_inscricao_oficina = [9,0,3,5]                            
                inscricao_oficinas()
            elif rm in lista5rm:  
                lista_inscricao_oficina = [0,3,8,4]                             
                inscricao_oficinas()


#-------------------------------------------------------------------------------------------------------------------------------------------------#

    #Listar por aluno (ordem alfabética de nome)#
    elif menu == 3:
        if len(listatudo) >= 1:
            print("Menu Listar Inscrições")
            print("1 - Listar por aluno (ordem alfabética de nome)")
            print("2 - Listar por oficina (ordem alfabética)")
            menu_3 = int(input())

            if menu_3 == 1:
                x = 0
                for x in range(len(listarm)):
                    y = 0   
                    listanome,listarm,listaserie = zip(*sorted(zip(listanome,listarm,listaserie)))        
                    print("\nRM:", listarm[x], "-", listanome[x], "-",listaserie[x],"ª. série")
                    print("Oficinas:")
                    for n in range(10):
                        if listarm[x] in lista_oficinas[y]:
                            print(nome_oficinas[y])
                        y = y + 1    
                    x = x+1    
                        

            #Listar por oficina (ordem alfabética)#           
            elif menu_3 == 2:
                    y = 0
                    for n in range(10):
                        if  len(lista_oficinas[y]) >= 1:
                            x = 0
                            print("\n",nome_oficinas[y])
                            for n in range(len(lista_oficinas[y])):
                                #Procurar a posição do rm na lista completa#
                                o = listarm.index(lista_oficinas[y][x])
                                print("RM:", listarm[o], "-", listanome[o], "-",listaserie[o],".série")
                                x = x + 1 
                            if len(lista_oficinas[y]) == 1:  
                                print("Total:",len(lista_oficinas[y]),"aluno")   
                            else:
                                print("Total:",len(lista_oficinas[y]),"alunos")
                        y = y + 1
            else:
                print("Opção invalida")


        else:
            print("Nenhum RM inscrito em oficinas")

    elif menu == 4:
        print("Programa finalizado")
        break
    else:
        print("Opção invalida")