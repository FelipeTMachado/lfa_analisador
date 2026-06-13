# Reconhecedor de Linguagem com Automato Finito

Este projeto consiste em um analisador lexico implementado em Python que utiliza a teoria de Automatos Finitos para reconhecer e classificar componentes de uma linguagem de programacao simples.

## Estrutura do Projeto

- automato.py: Codigo-fonte principal contendo a classe Automato e a interface de teste interativa.

## Requisitos

- Python 3.14.5 instalado.

## Como Executar

Para iniciar o analisador lexico interativo, execute o comando abaixo no terminal:

```bash
python automato.py
```

Apos executar, voce podera digitar sentencas de codigo diretamente no prompt. O programa exibira uma tabela com os tokens identificados. Para encerrar o programa, digite 'exit'.

## Elementos Reconhecidos

O automato esta programado para identificar as seguintes categorias:

- Palavras Reservadas: se, entao, senao, enquanto, faca, funcao, retorne.
- Identificadores: Nomes de variaveis ou funcoes que iniciam com letra.
- Numeros Inteiros: Sequencias de digitos (ex: 10, 500).
- Numeros Reais: Numeros com ponto flutuante (ex: 10.5, 3.1415).
- Literais: Textos entre aspas simples ou duplas (ex: "Ola Mundo").
- Operadores Matematicos: +, -, *, /, ^.
- Operadores Logicos e Especiais: <, >, =, !=, ~, !.

## Tratamento de Erros

O sistema possui mecanismos para lidar com:
- Literais nao fechados: Identifica quando uma aspa nao foi encerrada antes do fim da linha.
- Caracteres invalidos: Alerta sobre simbolos que nao pertencem ao alfabeto da linguagem sem interromper a execucao.
- Numeros malformados: Impede a leitura de numeros com mais de um ponto decimal como um unico token.

## Casos de Teste Sugeridos

Para validar as funcionalidades, voce pode testar as seguintes entradas no prompt interativo:

### 1. Codigo Valido Misto
Entrada: `se valor >= 100.5 entao resultado = "Sucesso"`
O que observar: O reconhecimento correto da palavra reservada 'se', do numero real '100.5' e do literal de texto.

### 2. Operadores Compostos e Negacao
Entrada: `status != ~verdadeiro`
O que observar: A diferenciacao entre o operador composto '!=' e o operador de negacao '~'.

### 3. Erro de Literal (String Aberta)
Entrada: `texto = "Este texto nao termina`
O que observar: A geracao do token 'ERRO_LITERAL_NAO_FECHADO' contendo a parte da string capturada.

### 4. Recuperacao de Caracteres Invalidos
Entrada: `valor = 50 @`
O que observar: A identificacao do numero 50 seguida do alerta 'CARACTERE AINDA NÃO TRATADO: @', sem interromper o fluxo.

### 5. Numeros Reais e Ambiguidade
Entrada: `10.5.2`
O que observar: O automato deve identificar '10.5' como um NUMERO_REAL e tratar o '.2' como uma nova sequencia (gerando um aviso de caractere nao tratado para o ponto inicial e colocar o numero como NUMERO_INTEIRO na tabela de analise).
