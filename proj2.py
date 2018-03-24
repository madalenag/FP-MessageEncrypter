#Madalena Galrinho - 87546


#TIPO POSICAO

#Construtor:
def faz_pos(l,c):
    """
    Tem como argumentos l(linha) c(coluna) e devolve uma posicao. Ambos os argumentos tem de ser inteiros positivos
    """
    if not (isinstance(l,int) and isinstance(c,int) and l>=0 and c>=0):
        raise ValueError("faz_pos: argumentos errados")
    return (l,c)


#Seletor:
def linha_pos(posicao):
    """
    Recebe um argumento do tipo posicao e devolve a linha correspondente.
    """
    return posicao[0]


def coluna_pos(posicao):
    """
    Recebe um argumento do tipo posicao e devolve a coluna correspondente.
    """
    return posicao[1]


#Reconhecedores:
def e_pos(arg):
    """
    Devolve True ou False, caso o arg seja do tipo posicao ou nao, respectivamente.
    """
    return isinstance(arg,tuple) and len(arg)==2  and isinstance(arg[0],int) and isinstance(arg[1],int) and arg[0]>=0 and arg[1]>=0


#Testes:
def pos_iguais(p1,p2):
    """
    Devolve True caso os argumentos p1 e p2 sejam iguais e False caso contrario.
    """
    return p1[0]==p2[0] and p1[1]==p2[1]



#TIPO CHAVE
tuplo_letras=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

#Construtores:

def gera_aux(l,mgc):
    """
    Funcao que recebe l(tuplo de letras) e mgc(cadeia de caracteres) e devolve uma lista com os elementos de mgc e posteriormente os de l, sem repeticoes.
    """    
    lst=[]
    for el in l:
        for e in mgc:
            if e not in lst and e!=" ": #verifica se ha elementos repetidos de mgc
                lst=lst+[e]
        if el not in lst and el!=" ": #verifica quais os elementos que nao estao em l
            lst=lst+[el]
    return lst

def gera_erros(l,mgc):
    """
    Funcao que recebe l(tuplo de 25 letras) e mgc(cadeia de caracteres) e devolve True caso existam erros nos argumentos. Cada elemento dos argumentos deve ser uma letra maiuscula do conjunto: 
    L={A,B,C,D,E,F,G,H,I,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}.
    """    
    if not (len(l)==25 and isinstance(mgc,str) and isinstance(l,tuple)):
        return True
    
    for m in tuplo_letras: 
        if m not in l:
            return True
   
    for n in range(len(mgc)):
        if mgc[n] not in l and mgc[n]!=" ":
            return True
    

def gera_chave_linhas(l,mgc):
    """
    Recebe dois argumentos, l(um tuplo de 25 letras) e mgc(uma cadeia de caracteres) e devolve a chave gerada disposta por linhas.
    """
    if gera_erros(l,mgc):
        raise ValueError("gera_chave_linhas: argumentos errados")
    
    lst=gera_aux(l,mgc)
            
    final=[]
    for n in range(0,len(lst),5): #devolve uma lista de 5 listas
        final=final+[lst[n:n+5]]
    return final

    
def gera_chave_espiral(l,mgc,s,pos):
    """
    Recebe quatro argumentos, l(um tuplo de 25 letras), mgc(uma cadeia de caracteres),pos(posicao em que comeca) e devolve a chave gerada disposta em espiral, atraves do sentido indicado pelo arg s('r' no sentido dos ponteiros do relogio e 'c' caso contrario).
    """    
    if gera_erros(l,mgc):
        raise ValueError("gera_chave_espiral: argumentos errados")
    
    if e_pos(pos)==False or (s!='r' and s!='c'):
        raise ValueError("gera_chave_espiral: argumentos errados")
    
    i,x,y,tam=0,pos[0],pos[1],0
    
    #Movimentos no sentido do relogio:
    if s=='r':
        mov1=lambda x,y:(x,y+i) #direita
        mov2=lambda x,y:(x,y-i) #esquerda
        mov3=lambda x,y:(x+i,y) #cima
        mov4=lambda x,y:(x-i,y) #baixo
    
    #Movimentos no sentido contrario:
    if s=='c':
        mov1=lambda x,y:(x+i,y) #cima
        mov2=lambda x,y:(x-i,y) #baixo
        mov3=lambda x,y:(x,y-i) #esquerda
        mov4=lambda x,y:(x,y+i) #direita
    
    
    tuplo_pos=() #tuplo onde vao ser concatenadas as posicoes
    lim_inf,lim_sup=0,4 #limites iniciais da matriz 5x5
    
    
    #Ciclo da espiral:
    while tam!=23: #antes de atingir a posicao do meio
        for i in range(lim_sup+1):
            if x==y or x-lim_inf==y or x+lim_inf==y: #analise dos movimentos em funcao dos limites
                if y==lim_inf or y==0:
                    el=(mov1(x,y))
                if y==lim_sup or y==4 or y==lim_sup+1:
                    el=(mov2(x,y))
            elif x!=y:
                if x==lim_inf or x==0:
                    el=(mov3(x,y))
                if x==lim_sup or x==4 or x==lim_sup+1:
                    el=(mov4(x,y))
            if el in tuplo_pos:
                tuplo_pos=tuplo_pos
            else:
                tuplo_pos=tuplo_pos+((el),)
        
        if 12<=tam<18:
            lim_sup,lim_inf=3,1
        if 18<=tam<22:
            lim_sup=2
        if 22<=tam<=24:
            lim_sup=1
            
        tam=tam+(lim_sup)#tam aumenta com o limite de cada iteracao
        pos=tuplo_pos[tam] #posicao ate atingir o limite da iteracao respetiva
        x,y=pos[0],pos[1] 
    
    tuplo_pos=tuplo_pos+((2,2),) #concatena-se a posicao do meio
    
    
    #Implementacao da forma da espiral:
    final=[[' ',' ',' ',' ',' '], [' ',' ',' ',' ',' '], [' ',' ',' ',' ',' '], [' ',' ',' ',' ',' '], [' ',' ',' ',' ',' ']]
    lst=gera_aux(l,mgc)
    
    for posic,elem in zip(range(len(tuplo_pos)),range(len(lst))):
        final[linha_pos(tuplo_pos[posic])][coluna_pos(tuplo_pos[posic])]=lst[elem] #mete os elementos de lst nas posicoes ditas em tuplo_pos
    return final


#Seletor:
def ref_chave(c,p):
    """
    Recebe como parametros c(chave) e p(posicao) e devolve a letra correspondente a posicao inserida nessa mesma chave.
    """
    l=linha_pos(p)
    col=coluna_pos(p)
    return c[l][col]



#Modificador:
def muda_chave(c,p,l):
    """
    Recebe como argumentos c(chave), p(posicao), l(letra) e devolve a chave c com a letra l na posicao p.
    """
    c[linha_pos(p)][coluna_pos(p)]=l
    return c



#Reconhecedor:
def e_chave(arg):
    """
    Devolve True se arg for do tipo chave e False caso contrario.
    """

    for k in range(len(arg)):
        for j in range(len(arg[k])):
            if arg[k][j] not in tuplo_letras:
                return False
    return isinstance(arg,list) and len(arg)==5


#Transformadores:
def string_chave(c):
    """
    Devolve uma string que quando impressa apresenta as letras de c dispostas numa tabela 5x5.
    """
    string=""
    for n in range(len(c)):
        for m in range(len(c[n])):
            string=string+c[n][m]+" " #adiciona cada caractere
        string=string+'\n' #divide os caracteres de 5 em 5
    return string



#FUNCOES A DESENVOLVER

def digramas(mens):
    """
    Funcao que recebe uma mensagem, que corresponde a uma cadeia de carateres, como argumento e devolve a cadeia de caracteres sem espacos
    """
    junta_mens=transf=""
    for c in mens:
        if c==" ":
            junta_mens=junta_mens
        else:
            junta_mens=junta_mens+c
    
    tam=len(junta_mens)

    for car in range(0,tam,2):
        if car==tam-1 and tam%2!=0: #como o step=2 nao atinge o ultimo elemento quando tam for impar
            transf=transf+junta_mens[car]        
        elif junta_mens[car]==junta_mens[car+1]:
            transf=transf+junta_mens[car]+'X'+junta_mens[car+1]
        else:
            transf=transf+junta_mens[car:car+2]
    if len(transf)%2!=0:
        transf=transf+'X' #concatena 'X' para ficar par
    return transf



#Funcao auxiliar para figura e codifica_diagrama
def define_pos(c,chave):
    """
    Funcao que tem como argumentos c(caractere) e chave, e devolve um tuplo correspondente a linha e a coluna desse caractere.
    """
    for linha in range(len(chave)):
        for col in range(len(chave[linha])):
            if chave[linha][col]==c:
                pos=(linha,col)
    return pos
 

    
def figura(digrm,chave):
    """
    Funcao que recebe como argumentos uma cadeia de caracteres e uma chave, e devolve um tuplo de 3 elementos com a forma (fig,pos1,pos2)
    """
    pos1=define_pos(digrm[0],chave)
    pos2=define_pos(digrm[1],chave)
    
    if linha_pos(pos1)==linha_pos(pos2):
        fig="l"
    elif coluna_pos(pos1)==coluna_pos(pos2):
        fig="c"
    else:
        fig="r"
    return (fig,pos1,pos2)



#Funcao geral para codifica_l e codifica_r:
def geral(pos,x,y):
    """
    Funcao que recebe como argumentos pos(posicao),x e y(valores que se querem incrementar ou decrementar na linha ou na coluna dessa mesma posicao). Devolve um tuplo correspondente a posicao nova.
    """
    pos_cod=(linha_pos(pos)+x,coluna_pos(pos)+y)
    return pos_cod



def codifica_l(pos1,pos2,inc):
    """
    Recebe tres argumentos: pos1 e pos2 (posicoes das letras de um diagrama na mesma linha) e inc(que toma valores 1 e -1, consoante se pretende fazer uma encriptacao ou uma desencriptacao, respetivamente. Devolve um tuplo com as novas posicoes dos diagramas.
    """
    final=()
    for pos in(pos1,pos2):
        if inc==1 and coluna_pos(pos)==4: #analise o caso limite para inc=1
            final=final+((linha_pos(pos),0),)
        elif inc==-1 and coluna_pos(pos)==0: #caso limite para inc=-1
            final=final+((linha_pos(pos),4),)
        else:
            final=final+((geral(pos,0,inc)),) #caso geral
    return final



def codifica_c(pos1,pos2,inc):
    """
    Recebe tres argumentos: pos1 e pos2 (posicoes das letras de um diagrama na mesma coluna) e inc(que toma valores 1 e -1, consoante se pretende fazer uma encriptacao ou uma desencriptacao, respetivamente. Devolve um tuplo com as novas posicoes dos diagramas.
    """    
    final=()
    for pos in(pos1,pos2):
        if inc==1 and linha_pos(pos)==4:
            final=final+((0,coluna_pos(pos)),)
        elif inc==-1 and linha_pos(pos)==0:
            final=final+((4,coluna_pos(pos)),)
        else:
            final=final+((geral(pos,inc,0)),)
    return final   
    

    
def codifica_r(pos1_cod,pos2_cod):
    """
    Recebe dois argumentos: pos1 e pos2 (posicoes das letras de um diagrama que se situam em linhas e colunas diferentes) e devolve um tuplo corresponde as posicoes das letras do diagrama encriptado ou desencriptado.
    """        
    pos1=(linha_pos(pos1_cod),coluna_pos(pos2_cod)) 
    pos2=(linha_pos(pos2_cod),coluna_pos(pos1_cod)) #trocam as colunas
    return (pos1,pos2)



def codifica_digrama(digrm,chave,inc):
    """
    Recebe tres argumentos: digrm(digrama), chave e inc(que toma valores 1/-1 consoante se prentende fazer uma encriptacao/desencriptacao, respetivamente. Devolve o diagrama modificado usando a chave.
    """  
    pos1=define_pos(digrm[0],chave)
    pos2=define_pos(digrm[1],chave)
    
    if linha_pos(pos1)==linha_pos(pos2):
        cod=codifica_l(pos1,pos2,inc)
    elif coluna_pos(pos1)==coluna_pos(pos2):
        cod=codifica_c(pos1,pos2,inc)
    else:
        cod=codifica_r(pos1,pos2)
    
    elem1=chave[cod[0][0]][cod[0][1]] #correspondente a pos1
    elem2=chave[cod[1][0]][cod[1][1]] #pos2
    return elem1+elem2



def codifica(mens,chave,inc):
    """
    Recebe tres argumentos: mens(mensagem), chave e inc(que toma valores 1/-1 consoante se prentende fazer uma encriptacao/desencriptacao, respetivamente. Devolve a mensagem transformada usando a chave.
    """        
    if inc==1:
        mens=digramas(mens) #quando inc=1 e necessario transformar mens
        
    msg_final=""
    for s in range(0,len(mens),2):
        msg_final=msg_final+codifica_digrama(mens[s:s+2],chave,inc)
    return msg_final