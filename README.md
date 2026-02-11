# Jogo de Adivinhação Numérica

Este é um projeto de estudo desenvolvido em **Python** que implementa um jogo interativo de adivinhação. O diferencial deste código é a atualização dinâmica do intervalo de palpites, Seguindo a logida de uma binary search.

##  Sobre o Projeto

O objetivo é descobrir um número secreto gerado aleatoriamente entre 1 e 100. O programa utiliza conceitos fundamentais de programação para garantir uma experiência de usuário fluida e sem erros.

###  Lógica de Funcionamento
O jogo não apenas diz se o palpite foi alto ou baixo, mas também:
1.  **Restringe o intervalo:** Se você chuta 50 e o sistema diz "Muito alto", o próximo intervalo exibido será entre 1 e 49.
2.  **Valida a entrada:** Impede que o usuário insira números fora do intervalo sugerido ou caracteres inválidos (letras/símbolos).

##  Funcionalidades

* **Geração Aleatória:** Uso da biblioteca `random` para definir o número secreto.
* **Tratamento de Exceções:** Bloco `try-except` para capturar erros de digitação (ValueError).
* **Feedback em Tempo Real:** Mensagens claras sobre a proximidade do número e contador de tentativas.
* **Interface via Console:** Interação direta e simples pelo terminal.

##  Tecnologias

* [Python 3.x](https://www.python.org/)
* Biblioteca `random` (Nativa)

## 📖 Como Rodar o Jogo

1.  **Clonar o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    ```
2.  **Entrar na pasta:**
    ```bash
    cd seu-repositorio
    ```
3.  **Executar o script:**
    ```bash
    python nome_do_seu_arquivo.py
    ```

##  Exemplo de Execução

```text
Adivinhação inicializada!
Digite um palpite entre 1 e 100: 50
Muito baixo!
Digite um palpite entre 51 e 100: 80
Muito alto!
Digite um palpite entre 51 e 79: 65
Parabéns! Você acertou o número 65 em 3 tentativas.
