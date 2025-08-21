# Adivinhe o número 
import random
comp = random.randint(1,100)

for i in range(7):

    test = float(input(f"Tentativa {i + 1} : "))
    if comp > test:
        print("Seu numero é menor")
    elif test > comp:
        print("Seu número é maior")
    elif comp == test:
        print("Os números são iguais, você venceu!!")
        break
else:
    print(f"Você perdeu, o número era {comp}")

