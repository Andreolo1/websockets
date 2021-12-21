# -*- coding: utf-8 -*-

from socket import *
import webbrowser as wb
import requests


serverName = "localhost"
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)  # socket TCP
clientSocket.connect((serverName, serverPort))  # conexión con el servidor

while True:
    men = input("Escribe aquí la URL... ")  # url de la web que queremos abrir
    clientSocket.send(men.encode())  # enviamos la url al servidor
    if men == "*":
        break
    menmod = clientSocket.recv(2048).decode()  # recibimos el código de estado
    print(menmod)
clientSocket.close()
