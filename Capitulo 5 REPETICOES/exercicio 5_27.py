#Não sabia resolver, então peguei esse código do site
s = input("Digite o número a verificar, sem espaços:")
i = 0
f = len(s) - 1
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print(f"{s} é palíndromo")
else:
    print(f"{s} não é palíndromo")
