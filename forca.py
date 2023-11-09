AUTORES = [119042,118716]
import os
import random
import re

def erro(numeroErros,usadas,disponiveis,traços):
    os.system("cls")
    #desenho dos enforcados
    if numeroErros==0:
        print("________\n |/  |\n |\n |\n |\n_|__")
    elif numeroErros==1:
        print("________\n |/  |\n |   O\n |\n |\n_|__")
    elif numeroErros==2:
        print("________\n |/  |\n |   O\n |   |\n |\n_|__")
    elif numeroErros==3:
        print("________\n |/  |\n |   O\n |  /|\n |\n_|__")
    elif numeroErros==4:
        print("________\n |/  |\n |   O\n |  /|\\\n |\n_|__")
    elif numeroErros==5:
        print("________\n |/  |\n |   O\n |  /|\\\n |  /\n_|__") 
    print("ERROS:", numeroErros)  
    print(traços)
    #transforma a lista em string com o espaço depois da virgula
    print("letras usadas:",", ".join(usadas))   
    print("letras disponiveis:",", ".join(disponiveis))  
    
def verificaçãoLetra(letra,secret,secretTamanho,novosTraços,usadas,palavraSemAcentos,numeroErro,disponiveis):
    os.system("cls")
    #conta qtas vezes a letra aparece na palavra
    qtdLetra = palavraSemAcentos.count(letra)
    indexLetra = -1
    #ciclo q corre a qtdd de vezes que a letra aparece na palavra
    for x in range(0,qtdLetra):
            # o x e i vao correr juntos o i comparando o que está na lista com a letra e o x sabendo o numero da posição para depois saber onde substiruir
            for x, i in enumerate(disponiveis): 
                if(i == letra):
                    disponiveis[x]="+"
            #guarda o index da letra, para na proxima repetição do ciclo começar no index+1
            indexLetra = palavraSemAcentos.find(letra,indexLetra+1,secretTamanho) 
            #através de string slicing subistitui os traços pela letra introduzida 
            novosTraços= novosTraços[:indexLetra]+secret[indexLetra:indexLetra+1]+novosTraços[indexLetra+1:]
    erro(numeroErro,usadas,disponiveis,novosTraços)
    #envia de volta a qtdd de vezes q a letra aparece na palavra, para o caso de ser 0, corre a função erro e a versão atualizada da parte adivinhada da palavra com a letra introduzida        
    return qtdLetra,novosTraços

def letrasDisponiveis(letra,disponiveis):
    for x, i in enumerate(disponiveis):
        if i == letra :
            disponiveis[x]="-"
    print("letras disponiveis:",", ".join(disponiveis))  

def removerAcentos(secret):
    #esta função usa a livraria re para substituir as letras q aparecem no primeiro parametro de re.sub pelas q aparecem no segundo parametro na palavra incial
    secret= re.sub(u"[ÁÀÃÂ]", "A",secret)
    secret= re.sub(u"[ÍÌÎ]", "I", secret)
    secret= re.sub(u"[ÉÈÊ]", "E", secret)
    secret= re.sub(u"[ÓÒ]", "O", secret)
    secret= re.sub("Ç","C", secret)
    #devolve a palavra secreta sem acentos
    return secret

def win(word):
    os.system("cls")
    word=word.lower()
    print("      _________________\n     (_________________)\n    __|               |__\n   (  _     ____      _  )\n   | ( )   /_   |    ( ) |\n   | (_)     |  |    (_) |\n   (__       |  |      __)\n      \\    __|  |__   /\n       \\  |________| /\n        \\           /\n         \\         /\n          \_______/\n            (___)\n         __(_____)__\n        |           |\n        |___________|")    
    print("     parabéns, acertaste!")
    repetir()
        

def lose(traços,word):
    os.system("cls")
    print("________\n |/  |\n |   O\n |  /|\\\n |  / \\\n_|__")
    print("ERROS: 6")    
    word = word.lower()
    print(traços)
    print("Perdeste :(")
    print("A palavra era", word)
    repetir()

def repetir():
    repetir=input("Quer voltar a jogar? (sim/nao): ")
    if "sim" in repetir:
        main()
    else:
        print("Obrigado por ter jogado")
        exit()

            
def main():
   
    from wordlist import words1, words2
    import sys                  # INCLUA estas 3 linhas para permitir
    if len(sys.argv) > 1:       # correr o programa com palavras dadas:
        words = sys.argv[1:]    #   python3 forca.py duas palavras
    else:
        words =  words1 + words2    
    secret = random.choice(words).upper()
    secretTamanho = len(secret)
    traços=secretTamanho*"_"
    numeroErro=0
    #remove os acentos da palavra sercreta
    palavraSemAcentos= removerAcentos(secret)
    usadas=[]
    disponiveis=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    erro(numeroErro,usadas,disponiveis,traços)
    #print(secret)

    #ciclo q corre enquantos forem dados menos de 6 erros ou a palavra for não estiver completamente descoberta
    while numeroErro<6 and traços!=secret:
        #input da letra que é passada a maiuscula e removidos os espaços existentes
        letra = input("letra? ").upper().strip()
        letra = removerAcentos(letra)
        #se for introduzida a palvra inteira certa, ganha o jogo
        if (letra==secret or letra==palavraSemAcentos):
            win(letra)
        #se a palavra escrita tiver o mesmo tamanho de letras da secreta mas não for igual conta como erro
        elif (len(letra)==secretTamanho and letra!=palavraSemAcentos):
            numeroErro+=1
            usadas.append(letra)
            erro(numeroErro,usadas,disponiveis,traços)
        #se o input não for uma letra ou tiver mais q uma letra volta ao inicio do ciclo        
        elif not letra.isalpha() or len(letra) != 1:
            print("erro- introduza uma letra")
        #se for introduzida uma letra, que não é repetida, é testada e adicionada aos traços se existente na palavra secreta ou adicionado um erro caso não apareça na palavra        
        elif letra not in usadas :
            #a letra é adicionada á lista de letras usadas
            usadas.append(letra)
            qtdLetra, traços=verificaçãoLetra(letra,secret,secretTamanho,traços,usadas,palavraSemAcentos,numeroErro,disponiveis)
            #se a letra não for encontrada na palavra, é adicionada um erro 
            if qtdLetra==0:
                numeroErro+=1
                letrasDisponiveis(letra,disponiveis)
                erro(numeroErro,usadas,disponiveis,traços)
                
        #se a letra já tiver sido usada volta ao inicio do ciclo        
        elif letra in usadas:
            print("erro- letra já usada")
    #se a palavra for adivinhada, ganha o jogo e corre a funçao win()     
    if(traços==secret):
        win(traços)
    #se chegar a 6 erros, perde o jogo e corre a função lose    
    elif(numeroErro==6):
        lose(traços,secret)                                 
              
def menu():
    os.system("cls")
    print("+++Bem vindo ao jogo da forca+++")
    print("1-Jogar")
    print("2-sair")
    start=input("Escolha:").strip()
    if start=="1":
        main()
    elif start=="2":
        exit()
    elif start:
        print("Valor invalido")
        menu()

menu()