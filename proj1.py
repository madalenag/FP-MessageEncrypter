#Madalena Galrinho: 87546


#VERSAO SIMPLIFICADA#

def gera_chave1(letras):
    """
    Funcao que devolve um tuplo de 5 tuplos de caracteres, com 5 elementos cada, que correspondem aos caracteres do argumento letras.
    """
    tuplo=()
    for n in range(5,len(letras)+1,5):
        tuplo=tuplo+(letras[n-5:n],) #devolve o tuplo de 5 em 5
    return tuplo



def obtem_codigo1(car,chave):
    """
    Funcao que recebe um argumento car e uma chave.
    Devolve uma cadeia de 2 caracteres, que representam o respetivo codigo do caractere, de acordo com a chave inserida.
    """
    for linha in range(len(chave)):
        if car in chave[linha]: #verifica a linha do caractere
            for coluna in range(len(chave[linha])):
                if chave[linha][coluna]==car: #verifica a coluna
                    return str(linha)+str(coluna)
 
 
     
def codifica1(cad,chave):
    """
    Funcao que tem como argumentos cad (uma cadeia de caracteres) e uma chave.
    Retorna a cadeia de caracteres respetiva a encriptacao do argumento cad.
    """
    final=""
    for elem in cad:
        codigo=obtem_codigo1(elem,chave) #determina o codigo de cada caractere na cadeia
        final=final+codigo 
    return final



def obtem_car1(cod,chave):
    """
    Funcao que recebe como argumentos cod(codigo que pretendemos desencriptar) e uma chave.
    Devolve o caractere que corresponde ao codigo cod, tendo em conta a chave.
    """
    linha_chave=int(cod)//10 #obtem a linha do codigo
    coluna_chave=int(cod)%10 #obtem a coluna
    finalcod=chave[linha_chave][coluna_chave]
    return str(finalcod)



def descodifica1(cad_codificada,chave):
    """
    Funcao que recebe uma cadeia de caracteres (cad_codificada) e uma chave.
    Devolve a cadeia de caracteres correspondente a original mensagem.
    """
    soma=""
    for i in range(0,len(cad_codificada),2):
        cadacod=cad_codificada[i]+cad_codificada[i+1] #analisa cada 2 caracteres consecutivos
        soma=soma+obtem_car1(cadacod,chave)
    return soma




#VERSAO FINAL#

def gera_chave2(letras):
    """
    Funcao que tem como argumento letras, que consiste num tuplo com qualquer numero de caracteres.
    Gera um tuplo de tuplos, consoante o numero de caracteres inserido.
    """
    s=1
    num_tuplos=1
    while s<=len(letras)-1: #verifica o menor quadrado perfeito nao inferior ao comprimento
        num_tuplos=num_tuplos+1 
        s=num_tuplos*num_tuplos
    #calcula o numero de tuplos
    
    tam=(len(letras)%num_tuplos)
    if tam>0: #ve se sobram elementos
        tam=(len(letras)//num_tuplos)+1
    else:
        tam=(len(letras)//num_tuplos)
    #calcula o tamanho de cada tuplo
    
    
    tuplo=()
    for n in range(0,len(letras),tam):
        tuplo=tuplo+(letras[n:n+tam],)
        n=n+tam
    return tuplo


def obtem_codigo2(car,chave):
    """
    Funcao que recebe como argumento uma chave e um car(que tem de pertencer a chave, caso contrario devolve 'XX').
    Devolve uma cadeia de 2 caracteres, que representam o respetivo codigo do caractere, de acordo com a chave.
    """
    for i in range(len(chave)):
        if car in chave[i]:
            return obtem_codigo1(car,chave)
    else:
        return 'XX' 



def codifica2(cad,chave):
    """
    Funcao que tem como argumentos cad (uma cadeia de caracteres) e uma chave.
    Devolve a cadeia de caracteres respetiva a encriptacao do argumento cad.
    """    
    final=""
    for el in cad:
        codigo=obtem_codigo2(el,chave)
        final=final+codigo
    return final



def obtem_car2(cod,chave):
    """
    Funcao que recebe como argumentos cod(codigo que pretendemos desencriptar) e uma chave.
    Devolve o caractere que corresponde ao codigo cod, tendo em conta a chave.
    Caso na encriptacao o caractere nao pertenca a chave, devolve '?'.
    """
    if cod=='XX':
        return'?'
    else:
        return obtem_car1(cod,chave)


def descodifica2(cad_codificada,chave):
    """
    Funcao que recebe uma cadeia de caracteres (cad_codificada) e uma chave.
    Devolve a cadeia de caracteres correspondente a original mensagem.
    """
    soma=""
    for i in range(0,len(cad_codificada),2):
        cadacod=cad_codificada[i]+cad_codificada[i+1]
        soma=soma+obtem_car2(cadacod,chave)
    return soma
