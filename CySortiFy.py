import os
import time
import threading
import shutil
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
from win10toast import ToastNotifier

# --- CONFIG ---
DOWNLOADS = os.path.join(os.environ.get("USERPROFILE", ""), "Downloads")
INTERVAL = 30
IGNORE_EXTS = {".crdownload", ".part", ".download", ".tmp"}
RUNNING = True

# --- Notificador ---
toaster = ToastNotifier()

# --- Categorías embebidas (de tu JSON gigante) ---
DEFAULT_CATEGORIES = {
  "Docs": [
    ".pdf",".doc",".docx",".dot",".dotx",".ppt",".pptx",".pps",".ppsx",
    ".xls",".xlsx",".xlsm",".csv",".tsv",".txt",".rtf",".odt",".ods",".odp",
    ".epub",".chm",".mobi",".azw3",".djvu",".pages",".numbers",".key",".abw",
    ".sxw",".uot",".wpd",".wks"
  ],
  "Pics": [
    ".jpg",".jpeg",".png",".gif",".bmp",".tiff",".tif",".webp",".heic",".heif",
    ".ico",".jfif",".raw",".arw",".cr2",".nef",".orf",".sr2",".dng",".raf",
    ".pef",".rw2",".srw",".3fr"
  ],
  "AudioFiles": [
    ".mp3",".wav",".flac",".aac",".ogg",".oga",".m4a",".wma",".aiff",".aif",
    ".mid",".midi",".amr",".opus",".caf",".dsd",".ra",".au",".snd"
  ],
  "Movies": [
    ".mp4",".m4v",".avi",".mkv",".mov",".wmv",".flv",".mpeg",".mpg",".3gp",".3g2",
    ".webm",".ts",".m2ts",".vob",".ogv",".rm",".rmvb",".asf",".f4v",".divx",".xvid"
  ],
  "Setups": [
    ".exe",".msi",".iso",".img",".dmg",".apk",".deb",".rpm",".pkg",".msu",
    ".cab",".appx",".nupkg",".flatpak",".snap"
  ],
  "Archives": [
    ".zip",".rar",".7z",".tar",".gz",".bz2",".xz",".lz",".lzma",".z",".cab",
    ".ace",".arj",".sit",".sitx",".tgz",".txz",".cpio",".rpm",".deb"
  ],
  "Code": [
    ".py",".pyw",".pyc",".sh",".bash",".bat",".ps1",".cmd",".pl",".pm",".rb",".php",
    ".js",".ts",".jsx",".tsx",".html",".htm",".css",".scss",".sass",".less",
    ".sql",".xml",".json",".yaml",".yml",".toml",".ini",".cfg",".conf",".reg",
    ".c",".h",".hpp",".cpp",".cc",".cxx",".cs",".vb",".java",".class",".jar",
    ".swift",".go",".rs",".kt",".kts",".scala",".lua",".erl",".ex",".exs",".hs",
    ".r",".m",".mat",".jl",".for",".f90",".asm",".s"
  ],
  "Data": [
    ".db",".sqlite",".sqlite3",".mdb",".accdb",".bak",".dump",".sqlitedb",
    ".xml",".json",".parquet",".feather",".h5",".hdf5",".sav",".dta",
    ".sas7bdat",".xpt",".arff",".mat",".spf"
  ],
  "Executables": [
    ".bin",".com",".scr",".elf",".o",".so",".dll",".ocx",".drv",".efi"
  ],
  "Design": [
    ".psd",".ai",".svg",".xd",".sketch",".fig",".indd",".cdr",".qxd",".afdesign",
    ".afphoto",".afpub",".ase",".abr"
  ],
  "Fonts": [
    ".ttf",".otf",".woff",".woff2",".pfb",".pfa",".fnt",".eot",".fon"
  ],
  "CAD_3D": [
    ".dwg",".dxf",".stl",".step",".stp",".iges",".igs",".obj",".3ds",".fbx",
    ".blend",".max",".ma",".mb",".dae",".c4d",".lwo",".lws",".ply"
  ],
  "Games": [
    ".iso",".nrg",".bin",".cue",".gcm",".wbfs",".nds",".3ds",".gba",".gb",
    ".gbc",".smc",".sfc",".nes",".z64",".v64",".wad",".pak",".pk3",".xp3",
    ".rpgsave",".sav",".map",".lvl"
  ],
  "Backups": [
    ".bak",".old",".tmp",".bk",".backup",".gho",".vhd",".vhdx",".vmdk",".ova",".ovf",
    ".cab",".qic"
  ],
  "Torrents": [
    ".torrent"
  ],
  "Security": [
    ".pem",".crt",".cer",".key",".pfx",".der",".csr",".asc",".gpg",".pgp",
    ".keystore",".jks"
  ],
  "Virtualization": [
    ".vdi",".vhd",".vhdx",".vmdk",".qcow2",".ova",".ovf",".pvm"
  ],
  "Scripts_Macros": [
    ".vbs",".jsm",".wsf",".hta",".lnk",".scpt",".applescript",".wsh",".gadget"
  ],
  "Spreadsheets": [
    ".xls",".xlsx",".xlsm",".ods",".numbers"
  ],
  "Presentations": [
    ".ppt",".pptx",".odp",".key"
  ],
  "Ebooks": [
    ".epub",".mobi",".azw",".azw3",".fb2",".lit",".prc"
  ],
  "Logs": [
    ".log",".err",".out",".trace",".dmp"
  ],
  "Configs": [
    ".ini",".cfg",".conf",".cnf",".yaml",".yml",".toml",".properties"
  ],
  "Datasets": [
    ".csv",".tsv",".sav",".dta",".sas7bdat",".arff",".h5",".npz",".mat"
  ],
  "Others": [
    ".idx",".dat",".tmp",".part",".crdownload",".swp",".bak1"
  ],
  "Unsorted": [
    ".inf",".url",".sys"
  ]
}

# Normalizamos a minúsculas
CATEGORIES = {k: [e.lower() for e in v] for k, v in DEFAULT_CATEGORIES.items()}

# --- Icono bandeja ---
def create_image():
    img = Image.new('RGB', (64, 64), color=(40, 40, 40))
    d = ImageDraw.Draw(img)
    d.ellipse((8, 8, 56, 56), fill=(100, 180, 255))
    return img

# Evitar colisiones
def unique_dest(dest_dir, filename):
    base, ext = os.path.splitext(filename)
    candidate = os.path.join(dest_dir, filename)
    i = 1
    while os.path.exists(candidate):
        candidate = os.path.join(dest_dir, f"{base} ({i}){ext}")
        i += 1
    return candidate

# Buscar carpeta destino según categorías
def get_category_folder(ext):
    ext = ext.strip().lower()
    if not ext:
        return "[sin_extension]"
    for category, ext_list in CATEGORIES.items():
        if ext in ext_list:
            return category
    if ext and ext not in CATEGORIES["Unsorted"]:
        CATEGORIES["Unsorted"].append(ext)  # solo en RAM
    return ext

def organize_files():
    if not os.path.isdir(DOWNLOADS):
        return

    for name in os.listdir(DOWNLOADS):
        src = os.path.join(DOWNLOADS, name)
        if not os.path.isfile(src):
            continue

        ext = os.path.splitext(name)[1].lower().strip()
        if ext in IGNORE_EXTS:
            continue

        folder_name = get_category_folder(ext)
        dest_dir = os.path.join(DOWNLOADS, folder_name)

        try:
            os.makedirs(dest_dir, exist_ok=True)
            dst = unique_dest(dest_dir, name)
            shutil.move(src, dst)
            msg = f'Movido: \"{name}\" → {folder_name}'
            print("📂", msg)
            toaster.show_toast("Organizador de Descargas", msg, duration=3, threaded=True)
        except Exception as e:
            print(f"⚠️ No se pudo mover {name}: {e}")

def background_worker():
    while RUNNING:
        organize_files()
        time.sleep(INTERVAL)

# --- Menú bandeja ---
def organize_now(icon, item):
    organize_files()

def open_downloads(icon, item):
    try:
        os.startfile(DOWNLOADS)
    except Exception:
        pass

def quit_action(icon, item):
    global RUNNING
    RUNNING = False
    icon.stop()

def main():
    t = threading.Thread(target=background_worker, daemon=True)
    t.start()

    icon = Icon("OrganizadorDescargas", create_image(), "Organizador de Descargas",
                Menu(
                    MenuItem("Organizar ahora", organize_now),
                    MenuItem("Abrir Descargas", open_downloads),
                    MenuItem("Salir", quit_action)
                ))
    icon.run()

if __name__ == "__main__":
    main()
