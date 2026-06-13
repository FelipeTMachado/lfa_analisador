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
                while posicao < tamanho and (texto[posicao].isdigit() or texto[posicao] == '.'):
                    if texto[posicao] == '.':
                        if eh_real: # SE JÁ FOR REAL E ENCONTRAR OUTRO PONTO, PARAMOS O NÚMERO AQUI
                            break
                        eh_real = True
                    numero += texto[posicao]
                    posicao += 1
                
                if eh_real:
                    tokens.append(('NUMERO_REAL', numero))
                else:
                    tokens.append(('NUMERO_INTEIRO', numero))
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
