# Carpeta Descargas del usuario
$downloads = Join-Path $env:USERPROFILE "Downloads"

# Lista de extensiones comunes en Windows
$extensions = @(
    "exe","dll","bat","cmd","txt","log","ini","sys","dat","bin",
    "vbs","js","html","css","xml","json","yml","cfg","reg","inf",
    "doc","docx","xls","xlsx","ppt","pptx","pdf","rtf","csv","sql",
    "png","jpg","jpeg","gif","bmp","ico","mp3","wav","mp4","avi",
    "zip","rar","7z","gz","tar","iso","msi","lnk","url","scr"
)

# Crear 50 ficheros aleatorios
for ($i = 1; $i -le 50; $i++) {
    # Generar nombre aleatorio de 8 caracteres
    $name = -join ((48..57 + 65..90 + 97..122) | Get-Random -Count 8 | ForEach-Object {[char]$_})

    # Escoger extensión aleatoria
    $ext = Get-Random -InputObject $extensions

    $filename = "$name.$ext"
    $filepath = Join-Path $downloads $filename

    # Escribir contenido en el fichero
    "Fichero de prueba $i con extensión .$ext" | Out-File -FilePath $filepath -Encoding utf8
}

Write-Host "Se han creado 50 ficheros de prueba en: $downloads"
