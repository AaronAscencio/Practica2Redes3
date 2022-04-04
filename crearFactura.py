import os
import datetime

from ConsultaExterna import *

def crearFactura(hostname,version,comunidad,puerto,tcpin,tcpout,octin,octout):
        name = getConsulta(hostname,version,comunidad,puerto,'1.3.6.1.2.1.1.5.0')
        desc = getConsulta(hostname,version,comunidad,puerto,'1.3.6.1.2.1.1.1.0')
        tcpPassiveOpens = getConsulta(hostname,version,comunidad,puerto,'1.3.6.1.2.1.6.6.0')
        fecha = datetime.datetime.now()
        archivo = f'{hostname}.txt'
        f = open(archivo,'w')
        f.write(f'''
        device: {name}
        description: {desc}
        date: {fecha}
        defaultProtocol: radius
        rdate: {fecha}
        #NAS-IP-Address
        4: {hostname}
        #NAS-Port
        5: 22
        #NAS-Port-Type
        61: 2
        #User-Name
        1: ssh1
        #Acct-Status-Type
        40: 2
        #Acct-Delay-Time
        41: 14
        #Acct-Input-Octets
        42: {octin}
        #Acct-Output-Octets
        43: {octout}
        #Acct-Session-Id
        44: 185
        #Acct-Authentic
        45: 1
        #Acct-Session-Time
        46: 1238
        #Acct-Input-Packets
        47: {tcpin}
        #Acct-Output-Packets
        48: {tcpout}
        #Acct-Terminate-Cause
        49: 11
        #Acct-Multi-Session-Id
        50: 73
        #Acct-Link-Count
        51: 2
        #tcpPassiveOpens
        52: {tcpPassiveOpens}
        ''')
        f.write
        f.close()


if __name__ == '__main__':
    crearFactura()