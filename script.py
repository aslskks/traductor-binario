def binario_a_texto(binario):
    binario = binario.split()  # Dividimos la cadena binaria en segmentos separados por espacios
    texto = ''
    for segmento in binario:
        try:
            # Convertimos el segmento binario a su equivalente en carácter ASCII y luego a texto
            caracter = chr(int(segmento, 2))
            texto += caracter
        except ValueError:
            # Si no podemos convertir el segmento, lo ignoramos
            pass
    return texto

def main():
    binario = input("Ingresa la cadena binaria que deseas convertir a texto: ")
    resultado = binario_a_texto(binario)
    print("El texto es:", resultado)

if __name__ == "__main__":
    main()
