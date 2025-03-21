import statistics

def calcular_media(*numeros):
    #return sum(numeros) / len(numeros)
    return statistics.mean(numeros)


if __name__ == "__main__":
    print(calcular_media(3, 5, 8))