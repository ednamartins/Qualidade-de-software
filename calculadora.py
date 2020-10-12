#  1 trabalho de Qualidade de Sotware, Calculadora
#Recebe uma expressão de números e operadores
#precorre  toda a espreção a busca de um operador
def buscar_op(exp):
    vetor=['+','-','*','/']
    for valor in exp:
         if valor in vetor:
             return exp.find(valor)
# verifica a o nível de prioridade do operador
#calcula de acordo com o operador
def calcular(n1,n2,op):
    cal=0
    if op == '+':
        cal=n1 + n2
    elif op == '-':
        cal=n1 - n2
    elif op == '*':
        cal = n1 * n2
    elif op == '/':
        cal=n1 / n2
    else :
        print("Operador Invalido")
    return cal
#resultado=calcular(n1,n2,op)
#print("resultado",resultado)
def operacao(exp):

    posi_op1 = buscar_op(exp)
    n1 = float(exp[0:posi_op1])
    exp2 = exp[posi_op1 + 1:len(exp)]
    posi_op2 = buscar_op(exp2)
    # não tem mais operadores
    resultado=0
    if not posi_op2:
        #Condição se for vazio
        n2 = float(exp[posi_op1 + 1:len(exp)])
        resultado = calcular(n1, n2, exp[posi_op1])
        print("Resultado", resultado)
    else :
        n2 = float(exp[posi_op1 + 1:posi_op1 + 1+posi_op2])
        resultado = calcular(n1, n2, exp[posi_op1])
        epx2=str(resultado)+exp2[posi_op2:len(exp2)]
        operacao(epx2)


#main
exp= input("Digite uma expressão")
operacao(exp)



