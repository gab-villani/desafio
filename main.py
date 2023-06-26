import sounddevice as sd
import time

def tocar_musica():
    filename = "../Cinco Patinhos.mp3"  # Caminho para o arquivo de áudio

    # Carrega o arquivo de áudio
    data, fs = sd.read(filename, dtype='float32')
    
    # Reproduz o áudio
    sd.play(data, fs)

def musica_patinhos():
    quantidade = int(input("Digite a quantidade inicial de patinhos: "))

    while quantidade > 0:
        print(f"{quantidade} patinhos foram passear")
        print("Além das montanhas para brincar")
        print("A mamãe gritou: 'Quá, quá, quá, quá!'")
        quantidade -= 1

        if quantidade > 0:
            print(f"Mas só {quantidade} patinhos voltaram de lá\n")
        else:
            print("E nenhum patinho voltou de lá\n")

        time.sleep(1)  # Atraso de 1 segundo entre as linhas

    sd.stop()

tocar_musica()
musica_patinhos()
