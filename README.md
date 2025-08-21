# 🎯 Adivinhe o Número  

Um joguinho simples feito em **Python** para treinar lógica de programação.  
O computador escolhe um número aleatório entre **1 e 100**, e o jogador tem **7 tentativas** para adivinhar.  

---

## 🚀 Como funciona
1. O programa gera um número aleatório entre 1 e 100.  
2. O jogador digita um palpite a cada rodada.  
3. O programa dá dicas se o número digitado é **maior** ou **menor** que o número secreto.  
4. O jogador vence se adivinhar o número dentro de 7 tentativas.  
5. Caso contrário, o programa revela o número correto.  

---

## 📌 Exemplo de execução

### ✅ Caso de vitória
```text
Tentativa 1 : 50
Seu número é maior
Tentativa 2 : 25
Seu número é menor
Tentativa 3 : 30
Os números são iguais, você venceu!!
```

### ❌ Caso de derrota
```text
Tentativa 1 : 10
Seu número é menor
Tentativa 2 : 90
Seu número é maior
Tentativa 3 : 70
Seu número é maior
Tentativa 4 : 60
Seu número é maior
Tentativa 5 : 40
Seu número é menor
Tentativa 6 : 50
Seu número é menor
Tentativa 7 : 55
Seu número é menor
Você perdeu, o número era 57
```

## 🛠️ Tecnologias utilizadas

- **Python 3**
- Módulo **random** (para gerar o número aleatório)

---

## 📚 Aprendizado
Esse projeto foi feito para treinar:
- Estruturas de repetição (`for`, `else`)  
- Condicionais (`if / elif / else`)  
- Entrada e saída de dados (`input`, `print`)  
- Uso do módulo **random**  

---

## ▶️ Como executar
1. Instale o **Python 3** na sua máquina.  
2. Baixe o arquivo `adivinhe.py`.  
3. No terminal, rode:  
   ```python
   python adivinhe.py
