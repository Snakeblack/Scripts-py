import os, shutil

extenciones = {
    "Imagenes": ['.jpg', '.png', '.jpeg', '.gif', '.webp', '.bmp', '.ico', '.svg', '.psd', '.heic', '.nef', '.crw', '.ai', '.id', '.raw'],
    "Videos": ['.mkv', '.mov', '.avi', '.mp4', '.wmv', 'webm', '.flv', '.divx', '.mpg', '.wpl'],
    "Documentos": ['.docx', '.doc', '.txt', '.dic', '.diz', '.dochtml', '.exc', '.log', '.pdf', '.rtf', '.scp', '.wri', '.wtx', '.sgl', '.sdw', '.sds', '.sdd', '.sdc', '.sda', '.sgl', '.stc', '.sti', '.sxc', '.sxi', '.sxm', '.pot', '.ppa', '.pps', '.ppt', '.ppthtml', '.dot', '.wbk', '.wiz', '.wbk', '.xlc', '.xlm', '.xls', '.xlw', '.xlt'],
    "Ejecutables": ['.exe', '.msi', '.lnk'],
    "Subtitulos": ['.srt', '.sub'],
    "ImagenesDeSistema": ['.div', '.iso', '.ova', '.ovf', '.vhd', '.vmdk','.vbox-extpack'],
    "Musica": ['.mp3', '.acc', '.flac', '.m3u', '.wav', '.aiff', '.wma', '.ogg', '.opus', '.pcm', '.alac', '.aac', '.m4a', '.caf', '.oga', '.mogg', '.3gp', '.m4r'],
    "Comprimidos": ['.zip', '.rar', '.7z', '.tar', '.rar5', '.winrar'],
    "ExtensionesBrave": ['.csv'],
    "Code": ['.html', '.css', '.js', '.c', '.sh', '.php', '.scss', '.json', '.jar', '.java', '.cpp', '.asp', '.hta', '.htm', '.htt', '.jse', '.jsp', '.mht', '.mhtml', '.shtm', '.url', '.class', '.vbs'],
    "ArchivosDeSistema": ['.bat', '.com', '.ps1', '.dll', '.sys', '.ini', '.scr', '.ani', '.bfc', '.bkf', '.theme', '.tmp'],
    "Certificados": ['.cer'],
    "Fuentes": ['.ttf', '.otf'],
    "Torrent": ['.torrent']
}

def crearCarpetas(path):
    exts = obtenerExtenciones(path)
    for i in extenciones.keys():
        for k in exts:
            if k in extenciones[i] and not os.path.exists(path+i):
                os.mkdir(path+i)

def obtenerExtenciones(path):
    extenciones = []
    for i in os.listdir(path):
        ext = os.path.splitext(i)[1]
        if ext not in extenciones and ext !="":
            extenciones.append(ext)
    return extenciones

def ordenar(path, archivo, ext):
    for i in extenciones.keys():
        if ext in extenciones[i]:
            try:
                shutil.move(path+archivo, path+i)
            except:
                print(f"Ocurrio un error, no se pudo mover el archivo {archivo}")


def proceso(path):
    crearCarpetas(path)
    for archivo in os.listdir(path):
        ext = os.path.splitext(archivo)[1]
        ordenar(path, archivo, ext)


while True:
    path = input("Ingrese la direccion de la carpeta a ordenar: ")
    if os.path.exists(path):
        path += "/"
        break
    else:
        print("Error, el path ingresado no existe")

proceso(path)
print("Proceso finalizado")
