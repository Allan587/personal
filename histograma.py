def mostrar_histograma(n):
    print(f"{'Elemento':<10}{'Valor':<10}{'Histograma'}")
    print("-" * 30)

    for i in range(1, n + 1):
        print(f"{i:<10}{i:<10}{'*' * i}")
        
n = int(input("Introduce un número: "))

mostrar_histograma(n)
