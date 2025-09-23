import os
import random
import string

# Carpeta de Descargas del usuario en Windows
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Lista variada de extensiones comunes en Windows
extensions = [
    "exe", "dll", "bat", "cmd", "txt", "log", "ini", "sys", "dat", "bin",
    "vbs", "js", "html", "css", "xml", "json", "yml", "cfg", "reg", "inf",
    "doc", "docx", "xls", "xlsx", "ppt", "pptx", "pdf", "rtf", "csv", "sql",
    "png", "jpg", "jpeg", "gif", "bmp", "ico", "mp3", "wav", "mp4", "avi",
    "zip", "rar", "7z", "gz", "tar", "iso", "msi", "lnk", "url", "scr"
]

# Crear 50 ficheros aleatorios
for i in range(50):
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    ext = random.choice(extensions)
    filename = f"{name}.{ext}"
    filepath = os.path.join(downloads, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Fichero de prueba {i+1} con extensión .{ext}\n")

print(f"Se han creado 50 ficheros de prueba en: {downloads}")
