import os
import threading

from Monitor import *
from graph import *
from ConsultaExterna import *
from crearFactura import *


class Menu():


    def Accion(opcion,host,minutos):
        if(opcion=='s'):
            print('Creando reporte')
            hostname = host[0][0]
            version = host[0][1]
            comunidad = host[0][2]
            puerto = host[0][3]
            tcpin = obtenerDatos(minutos,hostname,'tcpin')
            tcpout = obtenerDatos(minutos,hostname,'tcpout')
            octin = obtenerDatos(minutos,hostname,'octin')
            octout = obtenerDatos(minutos,hostname,'octout')
            crearFactura(hostname,version,comunidad,puerto,tcpin,tcpout,octin,octout)
            print(f'Se ha creado el reporte de: {hostname}')


        elif(opcion=='n'):
            print('Saliendo')
            os.system ("clear")
            quit()

    def Opciones(host,minutos):
        r = input('Deseas crear el reporte de contabilidad (s/n): ')
        Menu.Accion(r,host,minutos)

    def __init__(self):
        agente = []
        host = []
        print('*** PRACTICA 2 ***')
        hostname = input('Introduce el nombre del hostname: ')
        version = int(input('Introduce la version: '))
        comunidad = input('Introduce la comunidad: ')
        puerto = int(input('Introduce el puerto: '))
        minutos = int(input('Introduce la cantidad de minutos para obtener los datos: '))
        minutos = minutos*60
        agente.append(hostname)
        agente.append(version)
        agente.append(comunidad)
        agente.append(puerto)
        host.append(agente)
        #print(host)
        m = Monitor(host)
        m.CrearCarpetas()
        m.CrearRRD()
        hilo = threading.Thread(target=m.Update,)
        hilo2 = threading.Thread(target=Menu.Opciones,args=(host,minutos),)
        hilo.start()
        hilo2.start()

if(__name__=='__main__'):
    Menu()