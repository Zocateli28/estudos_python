N = int(input())

for i in range(N):
    a = input()
    b = input()
   
    if len(b) <= len(a) and a[-len(b):] == b:
        print("encaixa")
    else:
        print("nao encaixa")
