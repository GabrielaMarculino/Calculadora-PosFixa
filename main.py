# Gabriela Marculino
# Complexidade do algoritmo: O(n) 

# GLOSSÁRIO
# Tokenizar: dividir a expressão matemática em partes menores para  facilitar a análise e avaliação da expressão matemática 
# em etapas posteriores do processo de cálculo.

# ESTRUTURAS DE DADOS UTILIZADAS:
# Lista, Pilha e Notação Polonesa Reversa (por mais que ela não seja considerada uma estrutura de dados).

# Converte a expressão matemática em uma lista de tokens (números, operadores, parênteses).
# Percorre cada caractere da expressão exatamente uma vez.
# Adiciona caracteres a um número atual ou diretamente à lista de tokens.

# Complexidade: A função percorre a expressão uma vez, adicionando tokens a uma lista.
# Portanto, a complexidade é O(n), onde n é o número de caracteres na expressão.
def tokenizar(expressao):
    
    # Função que converte a expressão em uma lista de tokens (números, operadores, parênteses)
    tokens = []  # Lista para armazenar os tokens
    numero_atual = ""  # String para acumular dígitos de números
    
    for caractere in expressao:
        
        if caractere.isdigit() or caractere == '.':  # Se o caractere é um dígito ou ponto decimal
            numero_atual += caractere  # Adiciona o caractere ao número atual
        else:
            
            if numero_atual:  # Se há um número acumulado
                tokens.append(numero_atual)  # Adiciona o número à lista de tokens
                numero_atual = ""  # Reseta o número atual
            if caractere in "+-*/()":  # Se o caractere é um operador ou parêntese
                tokens.append(caractere)  # Adiciona o operador ou parêntese à lista de tokens
                
    if numero_atual:  # Adiciona o último número acumulado, se houver
        tokens.append(numero_atual)
    return tokens  # Retorna a lista de tokens


# Converte a lista de tokens em uma árvore de expressão e avalia a expressão.
# A função analisar_expressao(indice) percorre a lista de tokens, processando cada um de forma linear.
# Utiliza duas pilhas, uma para valores e outra para operadores.
# Manipula os tokens de forma direta, sem iteração aninhada que dependeria do tamanho da lista.

# Complexidade: Cada token é processado uma vez, e operações de empilhar/desempilhar são O(1).
# Portanto, a complexidade é O(n), onde n é o número de tokens.
def analisar(tokens):
    
    # Função que converte os tokens em uma árvore de expressão e avalia a expressão
    def analisar_expressao(indice):
        
        valores, operadores = [], []  # Listas para valores e operadores
        
        while indice < len(tokens):  # Itera sobre os tokens
            token = tokens[indice]
            
            if token.isdigit() or '.' in token:  # Se o token é um número
                valores.append(float(token))  # Adiciona o número à lista de valores
                
            elif token in "+-*/":  # Se o token é um operador
                # Enquanto houver operadores na pilha e a precedência for correta, adiciona operadores à lista de valores
                while (operadores and operadores[-1] in "*/" and token in "+-") or (operadores and operadores[-1] in "+-*/" and token in "+-"):
                    valores.append(operadores.pop())
                operadores.append(token)  # Adiciona o operador à pilha
            elif token == '(':  # Se o token é um parêntese de abertura
                val, indice = analisar_expressao(indice + 1)  # Chama recursivamente para a subexpressão
                valores.append(val)  # Adiciona o valor da subexpressão à lista de valores
            elif token == ')':  # Se o token é um parêntese de fechamento
                break  # Termina o loop
            indice += 1  # Avança para o próximo token
            
        while operadores:  # Adiciona os operadores restantes à lista de valores
            valores.append(operadores.pop())
        return avaliar_notacao_polonesa(valores), indice  # Retorna o resultado da avaliação e o índice atual
    
# Avalia uma expressão em notação polonesa reversa usando uma pilha.
# Cada token é processado uma vez, com operações de empilhar/desempilhar.  

# Complexidade: Cada token é processado uma vez, e operações de pilha são O(1).
# Portanto, a complexidade é O(n), onde n é o número de tokens.  

    def avaliar_notacao_polonesa(tokens):
        
        # Função que avalia uma expressão em notação polonesa reversa (RPN)
        pilha = []  # Pilha para armazenar números
        
        for token in tokens:
            if isinstance(token, float):  # Se o token é um número
                pilha.append(token)  # Adiciona o número à pilha
            else:  # Se o token é um operador
                b = pilha.pop()  # Remove o topo da pilha
                a = pilha.pop()  # Remove o próximo número da pilha
                
                if token == '+':
                    pilha.append(a + b)  # Realiza a operação e adiciona o resultado à pilha
                elif token == '-':
                    pilha.append(a - b)
                elif token == '*':
                    pilha.append(a * b)
                elif token == '/':
                    pilha.append(a / b)
                    
        return pilha[0]  # Retorna o resultado final

    return analisar_expressao(0)[0]  # Inicia o parsing a partir do índice 0 e retorna o resultado

def calcular(expressao):
    # Função principal que calcula o resultado de uma expressão
    tokens = tokenizar(expressao)  # Tokeniza a expressão
    return analisar(tokens)  # Analisa e avalia os tokens

def main():
    # Função principal que permite a interação com o usuário
    while True:
        expr = input("Digite a expressão matemática (ou 'sair' para terminar): ")  # Pede ao usuário para digitar uma expressão
        if expr.lower() == 'sair':  # Se o usuário digitar "sair"
            break  # Termina o loop
        try:
            resultado = calcular(expr)  # Calcula o resultado da expressão
            print(f"Resultado: {resultado}")  # Imprime o resultado
        except Exception as e:  # Em caso de erro
            print(f"Erro: {e}")  # Imprime a mensagem de erro

if __name__ == "__main__":
    main()  # Chama a função principal se o script for executado diretamente
