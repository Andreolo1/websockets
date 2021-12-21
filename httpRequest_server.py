# -*- coding: utf-8 -*-
import requests
import webbrowser as wb
import validators
from socket import *

"""
Web socket para practicar las conexiones TCP
El cliente pide a al servidor una web http(s). El servidor calcula el código de 
estado http con requests, lo devuelve al cliente y abre la web mediante la librería webbrowser.

El código podría variarse en caso de querer practicar sobre la librería requests:
devolver las cabeceras, el html de la página, etc.
"""

def comprueba(url):
    """
    Comprobar que la url es válida
    """
    return validators.url(url)


serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)  # socket TCP
serverSocket.bind(("", serverPort))          
serverSocket.listen(1)   # ponemos el servidor a escuchar (servidor pasivo)
print("El servidor está listo... ")

connectionSocket, addr = serverSocket.accept()  # el socket de conexión


while True:
    message = connectionSocket.recv(2048)  # recive la url
    u = message.decode()
    if comprueba(u) == True:
        r = requests.get(u)
        if u == "*":  # parar la conexión
            connectionServer.close() 
            break      
        
        elif r.status_code < 400:  # requesito, http debe tener un codigo de estado satisfactorio
            m = wb.open_new_tab(r.url)
            connectionSocket.send(f"status code: {r.status_code}".encode())  # envía el codigo de estado al cliente
            continue

        else:  # la conexión no es válida (código de estado http >= 400)
            m = "La URL no es válida"  
            connectionSocket.send(m.encode())
            print(m)
            continue
        
    else:  # la url no está bien escrita
        m = "La URL no es válida"
        connectionSocket.send(m.encode())
        print(m)
        
connectionSocket.close()
