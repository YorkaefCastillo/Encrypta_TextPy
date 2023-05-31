import pyfiglet as glet
import random
from cryptography.fernet import Fernet


Font = ["slant", "3-d", "3x5", "5lineoblique", "alphabet", "banner3-D", "doh", "isometric1", "letters", "alligator", "dotmatrix", "bubble", "bulbhead", "digital"]
ador = ""
#<----------------------------------------------------------------
Titulo = glet.figlet_format("ENCRIPTA TEXT".center(50), font=f"{random.choice(Font)}")
print(Titulo)
#<----------------------------------------------------------------

def encryptador():
    #Se genera la clave de encryptacion
    clave = Fernet.generate_key()
    
    #Se almacena en un objeto
    clave_generada = Fernet(clave)

    #Texto que se va a encryptar
    text = input("Ingrese el texto que desea encryptar: ")

    #Se encrypta el texto
    text_encryptado = clave_generada.encrypt(text.encode())

    print(f"El texto encryptado es: {text_encryptado}")

    print(ador.center(50,"_"))

    #Desencryptar Texto
    texto_desencryptado = clave_generada.decrypt(text_encryptado)

    print(f"El texto desencryptado es: {texto_desencryptado}")

encryptador()
