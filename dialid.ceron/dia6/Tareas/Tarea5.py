#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
#Cerón Rodríguez Lezly Dialid

import optparse
import sys
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
    opts,args = parser.parse_args()
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

#Imprime un mensaje en salida de errores, termina el programa si se le indica
def printError(msg, exit = False):
    sys.stderr.write('Error:\t%s\n' % msg)
    if exit:
        sys.exit(1)

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

#Para realizar peticiones HTTP al host especificado. Retorna true si se pudo autenticar a user con password. 
def makeRequest(host, user, password, verboso, digest):
    try:
        auth = HTTPDigestAuth(user, password) if digest else (user, password)
        response = get(host, auth=auth)
        if verboso:
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

#Condiciones de ejeución
if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port=opts.port, tls=opts.tls)
        usuarios = get_pass_users(opts.user, opts.user_list)
        passwords = get_pass_users(opts.password, opts.password_list)
        tipo = "Digest" if opts.digest else "Basic"
        s = ["URL destino: %s" % url, "Tipo de autenticación: %s" % tipo]
        if opts.verbose:
            print("\n".join(s))
        for u in usuarios:
            for p in passwords:
                if makeRequest(url, u, p, opts.verbose, opts.digest):
                    s.append('¡CREDENCIALES ENCONTRADAS!: %s\t%s' % (u,p))
                    if opts.verbose:
                        print(s[-1])
        if len(s) == 2:
            s.append("Ningún usuario y contraseña coincidió ")
        reportResults('\n'.join(s), opts.report, opts.stdout)
    except Exception as e:
        printError('Ocurrió un error inesperado')
        printError(e, True)