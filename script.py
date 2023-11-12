def texto_a_binario(texto):
    binario = ' '.join(format(ord(caracter), '08b') for caracter in texto)
    return binario

def main():
    texto = input("Ingresa el texto que deseas convertir a binario: ")
    resultado = texto_a_binario(texto)
    print("El texto en binario es:", resultado)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        import sys
        sys.exit()
    except Exception as e:
        from tkinter import messagebox
        messagebox.showerror(title="texto a binario", message=f"{e}")
