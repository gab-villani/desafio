import sounddevice as sd
import time

# def tocar_musica():
#     filename = "../Cinco Patinhos.mp3"  # Caminho para o arquivo de áudio

#     Carrega o arquivo de áudio
#     data, fs = sd.read(filename, dtype='float32')
    
#     Reproduz o áudio
#     sd.play(data, fs)

def musica_patinhos():
    quantidade = int(input("Digite a quantidade inicial de patinhos: "))
    qtd = quantidade
    while qtd > 0:
        
        print(f"\n{qtd} patinhos foram passear")
        print("Além das montanhas para brincar")
        print("A mamãe gritou: 'Quá, quá, quá, quá!'")
        qtd -= 1

        if qtd > 0:
            print(f"Mas só {qtd} patinhos voltaram de lá\n")
        else:
            print(f"\nA mamãe patinha foi procurar \nAlém das montanhas onde foi parar\nA mamãe gritou: 'Quá, quá, quá, quá!'\nE os {quantidade} patinhos voltaram de lá")

        time.sleep(6)  # Atraso de 1 segundo entre as linhas

    # sd.stop()

# tocar_musica()
musica_patinhos()
