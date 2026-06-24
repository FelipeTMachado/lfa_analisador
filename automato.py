import os

class Automato:
    def __init__(self):
        # PALAVRAS RESERVADAS
        self.palavras_reservadas = ['se', 'entao', 'senao', 'enquanto', 'faca', 'funcao', 'retorne', 'exit']
        
    def analisador_lexico(self, texto):
        posicao = 0
        tokens = []
        tamanho = len(texto)

        while posicao < tamanho:
            caractere_atual = texto[posicao]

            # PULAR ESPAÇOS EM BRANCO E QUEBRAS DE LINHA
            if caractere_atual.isspace():
                posicao += 1
                continue

            # ESTADO: IDENTIFICADORES E PALAVRAS RESERVADAS
            if caractere_atual.isalpha():
                palavra = ""
                while posicao < tamanho and (texto[posicao].isalnum() or texto[posicao] == '_'):
                    palavra += texto[posicao]
                    posicao += 1
                
                if (palavra in self.palavras_reservadas) and (palavra == "exit"):
                    os._exit(0)
                elif palavra in self.palavras_reservadas:
                    tokens.append(('PALAVRA_RESERVADA', palavra))
                else:
                    tokens.append(('IDENTIFICADOR', palavra))
                
                continue

            # ESTADO: NÚMEROS (INTEIROS E REAIS)
            if caractere_atual.isdigit():
                numero = ""
                eh_real = False

                while (posicao < tamanho) and ((texto[posicao].isdigit() or texto[posicao] == '.') or (texto[posicao].isalpha())):
                    if texto[posicao].isalpha: 
                        if texto[posicao] == '.':
                            if eh_real: # SE JÁ FOR REAL E ENCONTRAR OUTRO PONTO, PARAMOS O NÚMERO AQUI
                                break
                            eh_real = True
                    
                    numero += texto[posicao]
                    posicao += 1

                
                
                if eh_real:
                    tokens.append(('NUMERO_REAL', numero))
                else:
                    if numero.isdigit():
                        tokens.append(('NUMERO_INTEIRO', numero))
                    else:
                        tokens.append(('ERRO_IDENTIFICADOR_INVALIDO', numero))
                        
                continue

            # ESTADO: LITERAIS (STRINGS) 
            if caractere_atual == '"' or caractere_atual == "'":
                aspa_inicial = caractere_atual
                conteudo_literal = ""
                posicao += 1 # PULA A ASPA INICIAL
                
                while posicao < tamanho and texto[posicao] != aspa_inicial:
                    conteudo_literal += texto[posicao]
                    posicao += 1
                
                if posicao < tamanho and texto[posicao] == aspa_inicial:
                    posicao += 1 # PULA A ASPA FINAL
                    tokens.append(('LITERAL', conteudo_literal))
                else:
                    # SE CHEGOU AO FIM DO TEXTO SEM FECHAR ASPAS
                    tokens.append(('ERRO_LITERAL_NAO_FECHADO', conteudo_literal))
                continue


            # ESTADO: OPERADORES E SÍMBOLOS ESPECIAIS 
            # OPERADORES DE UM ÚNICO CARACTERE
            if caractere_atual in "+-*/^~":
                tokens.append(('OPERADOR', caractere_atual))
                posicao += 1
                continue

            # OPERADOR DIFERENTE (!=) OU NEGAÇÃO SIMPLES (!)
            if caractere_atual == '!':
                if posicao + 1 < tamanho and texto[posicao + 1] == '=':
                    tokens.append(('OPERADOR_DIFERENTE', '!='))
                    posicao += 2
                else:
                    tokens.append(('OPERADOR_NEGACAO', '!'))
                    posicao += 1
                continue

            # OPERADORES LÓGICOS E DE COMPARAÇÃO
            if caractere_atual in "<>=":
                tokens.append(('OPERADOR_LOGICO', caractere_atual))
                posicao += 1
                continue

            # SE ENCONTRAR ALGO QUE NÃO RECONHECE AINDA, AVANÇA PARA NÃO TRAVAR O LOOP
            if not caractere_atual.isspace():
                print(f"CARACTERE AINDA NÃO TRATADO: {caractere_atual}")
            posicao += 1

        return tokens

# EXEMPLO DE TESTE INTERATIVO
if __name__ == "__main__":
    meu_automato = Automato()
    
    print("DIGITE SEU CODIGO PARA ANALISE (OU 'SAIR' PARA FINALIZAR):")
    while True:
        teste = input(">> ")
        if teste.lower() == 'sair':
            break

        resultado = meu_automato.analisador_lexico(teste)
        
        print("+" + "-"*55 + "+")
        print("|                   TOKENS ENCONTRADOS                  |")
        print("+" + "-"*55 + "+")

        for resul in resultado:
            tipo = resul[0]
            valor = str(resul[1])
            # FORMATAÇÃO PARA ALINHAMENTO NA TABELA
            print(f"| {tipo:<28} | {valor:<22} |")

        print("+" + "-"*55 + "+")
