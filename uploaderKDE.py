import os
import os.path

from datetime import datetime
from uuid import uuid4

from subprocess import Popen, PIPE

import notify2

def copy_clipboard(msg):
    ''' Copy `msg` to the clipboard '''
    with Popen(['xclip','-selection', 'clipboard'], stdin=PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))     

def mostrarNotificacion(title, message):
    notify2.init("Test")
    notice = notify2.Notification(title, message)
    notice.show()
    return

# CONFIGURACION
ruta_imagenes = "/home/miguel/Documentos/dev/imagenes-publicas-24-25/"
prefijoGithub = "https://raw.githubusercontent.com/miguelbayon/imagenes-publicas-24-25/main/"           
extensionCaptura = ".png"
# FIN CONFIGURACION

os.chdir(ruta_imagenes)
print("Cambiado a la carpeta de las imágenes");
nombreCaptura = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())

print("La captura se guardará en " + ruta_imagenes + nombreCaptura)
print("Iniciando capturador de imagenes...")

orden = "spectacle -r -n -b -o " + ruta_imagenes + nombreCaptura + extensionCaptura
os.system(orden)

rutaAlArchivo = ruta_imagenes + nombreCaptura + extensionCaptura
print(rutaAlArchivo)
existeArchivo = os.path.isfile(ruta_imagenes + nombreCaptura + extensionCaptura)

if (not existeArchivo) :
    print("Captura abortada porque ya existe un archivo con este nombre")

else :
    print("La captura se creo correctamente")
    orden = "git add " + nombreCaptura + extensionCaptura
    os.system(orden)
    orden = "git commit -m 'Nueva imagen " + nombreCaptura + extensionCaptura + "'"
    os.system(orden)
    orden = "git push origin main"
    os.system(orden)
    textoMarkdown = "![Imagen](" + prefijoGithub + nombreCaptura + extensionCaptura + ")" 
    copy_clipboard(textoMarkdown)
    print("Texto copiado al portapapeles: " + textoMarkdown)
    mostrarNotificacion("Uploaderkde: captura subida", textoMarkdown);



