from database import Database


def continueOrExit():
  return input("Se quiser continuar escolhendo pesquisas, digite 0. Se nao, digite -1 para terminar o programa.")

def Main():
  db = Database()
  db.accesDatabase()
  #Todos os perfis da conta1
  query1 = '''Create view PerfisConta1
                AS select *
                from perfil natural join conta
                WHERE cpf = '123456789091';'''
  query1Select = "select * from PerfisConta1;"
  # Perfis que assistiram alguma série com x episodios
  query2 = "select DISTINCT nomep from perfil NATURAL JOIN assistiu where videoid in (select videoid from serie NATURAL join episodio natural join video group by videoid having count(*) = %s)"
  # possibilidade de escolha do numero de episodios
  numEpisodes = 0

  #Perfis da conta 1 que assitiram filmes de x categoria
  query3 = "select DISTINCT nomep from PerfisConta1 natural join assistiu natural join filme NATURAL join categFilme WHERE categoria = '%s';"
  # possibilidade de escolha de categoria do filme
  categMovie = 'acao'

  #Perfis que assistiram filmes com mais de x categorias
  query4 = "select nomep from perfil NATURAL join assistiu NATURAL join video NATURAL join filme natural join categFilme  group by nomep having count(DISTINCT categoria) > %s;"
  # possibilidade de escolha de quantas categorias
  numCategories = 0

  #Perfis que não assistiram nenhum documentario
  query5 = "select distinct nomep, perfilid from perfil NATURAL join assistiu where videoid not in (select videoid from video NATURAL join documentario);"

  #Locais que possuem contas do tipo de plano basico ou padrao que assistiram apenas menos que x videos
  #No trabalho, foi usado 2 videos
  query6 = "select DISTINCT local from perfil NATURAL join conta where nomep in (select nomep from perfil NATURAL JOIN assistiu group by nomep having count(*) < %s) and (conta.tipoPlano = 'Padrão' or conta.tipoPlano = 'Basico')"
  numVideos = 0

  # Planos utilizados por pessoas que assistiram documentarios
  query7 = "select DISTINCT tipoplano from perfil NATURAL join conta NATURAL JOIN assistiu natural join documentario;"

  #Perfis da conta 1 que assitiram series com mais de x temporadas
  query8 = "select DISTINCT nomep from assistiu natural join PerfisConta1 natural join serie WHERE temporadas > %s;"
  numSeasons = 0

  #Atores que participaram de videos assistidos ordenados pela quantidade de videos em que atuaram
  query9 = "select nomeart, COUNT(videoID) as videos from assistiu natural join video NATURAL join atuacao group by nomeart order by COUNT(videoID);"
  
  endLoop = False
  option = 0
  #db.callAddConta('222222232222',"RS", "Super Basic")
  #db.callChangePlan('222222232222', "Super Premium")
  while not endLoop:
    print('''
          -1- Sair do programa
          0- Criar o view da consulta 1
          1- Todos os perfis da conta1 usando view
          2- Perfis que assistiram alguma série com x episodios
          3- Perfis da conta 1 que assitiram filmes de x categoria
          4- Perfis que assistiram filmes com mais de x categorias
          5- Perfis que não assistiram nenhum documentario
          6- Locais que possuem contas do tipo de plano basico ou padrao que assistiram apenas menos que x videos
          7- Planos utilizados por pessoas que assistiram documentarios
          8- Perfis da conta 1 que assitiram series com mais de x temporadas
          9- Atores que participaram de videos assistidos ordenados pela quantidade de videos em que atuaram
          10- Executar comando digitado pelo usuario
          ''')
    option = input()
    if (option == '0'):
        db.genericModifyDatabase(query1)

    elif (option == '1'):
        db.genericBrowseDatabase(query1Select)
      
    elif (option == '2'):
        numEpisodes = input("Informe o numero de episodios desejado:")
        db.specificBrowseDatabase(query2, numEpisodes)
        
    elif (option == '3'):
        categMovie = input("Informe a categoria desejada:")
        db.specificBrowseDatabase(query3, categMovie)
        
    elif (option == '4'):
        numCategories = input("Informe o numero de categorias desejado:")
        db.specificBrowseDatabase(query4, numCategories)
    elif (option == '5'):
        db.genericBrowseDatabase(query5)

    elif (option == '6'):
        numVideos = input("Informe do numero de videos desejado:")
        db.specificBrowseDatabase(query6, numVideos)
      
    elif (option == '7'):
        db.genericBrowseDatabase(query7)
      
    elif (option == '8'):
        numSeasons = input("Informe o numero de temporadas desejado:")
        db.specificBrowseDatabase(query8, numSeasons)
      
    elif (option == '9'):
        db.genericBrowseDatabase(query9)
      
    elif (option == '-1'):
        print("Obrigado por usar o programa! :)")
        endLoop = True
    
    elif (option == '10'):
        queryModify = input("Digite o comando para atualizar, inserir ou deletar:")
        db.genericModifyDatabase(queryModify)


    else:
        print("Opcao invalida.")
        

    
    # option = continueOrExit()
        





  db.closeDatabase()

Main()
  