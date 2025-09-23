
![GitHub release downloads](https://img.shields.io/github/downloads/CyberiusCompany/Cyberius-Unzip-Cracker/latest/total)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![System](https://img.shields.io/badge/windows-x64-green)
![System](https://img.shields.io/badge/linux-x64-green)
![License](https://img.shields.io/badge/license-Private-red)
![Usage](https://img.shields.io/badge/usage-legal%20only-important)
![Python](https://img.shields.io/badge/python-3.7%2B-yellow)
![Tested on](https://img.shields.io/badge/tested%20on-Windows%2010%2F11%20%7C%20Ubuntu%2022.04-blue)


<p align="center">
  <a href="https://github.com/cyberiuscompany/CySortiFy">
    <img src="https://flagcdn.com/w40/es.png" alt="Español" title="Español">
    <strong>Español</strong>
  </a>
  &nbsp;|&nbsp;
  <img src="https://flagcdn.com/w40/us.png" alt="English" title="English">
  <strong>English</strong>
  &nbsp;|&nbsp;
  <a href="https://www.youtube.com/watch?v=xvFZjo5PgG0&list=RDxvFZjo5PgG0&start_radio=1&pp=ygUTcmljayByb2xsaW5nIG5vIGFkc6AHAQ%3D%3D">
    <img src="https://flagcdn.com/w40/jp.png" alt="日本語" title="Japanese">
    <strong>日本語</strong>
  </a>
</p>

# CySortiFy
CySortify is a lightweight **Python** tool that automatically organizes your **Downloads** folder on Windows, classifying files into **logical categories** (Docs, Pics, Movies, Setups, etc.) or by **extension** if they don't match any defined category.  

---

## 📝 Usage

- It starts with an icon in the tray (blue circle).  
- Every **30 seconds** it scans the **Downloads** folder and organizes files.  
- If it finds an unregistered extension, it moves it to its own `.ext` folder.  
- From the tray menu you can:
  - **Organize now**
  - **Open Downloads**
  - **Exit**

---

<p align="center">
  <img src="icono.png" alt="Banner" width="500"/>
</p

--- 

## 🎥 Demo

<p align="center">
  <img src="Imagenes/Video.gif" width="1200" alt="Demo of CyberiusUnzipCracker">
</p>

---

## Tool screenshots

<h2 align="center">Before and After Example</h2>
<div align="center">
  <img src="Imagenes/Foto Antes.png" alt="Photo 3.1" height="400px" style="display:inline-block; margin-right:10px; border: 1px solid #4f5354; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.5);"/>
  <img src="Imagenes/Foto Despues.png" alt="Photo 3.2" height="400px" style="display:inline-block; border: 1px solid #4f5354; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.5);"/>
</div>

<h2 align="center">Generating Random Files</h2>
<p align="center">
  <img src="Imagenes/Generando Ficheros Aleatorios.png" alt="Photo 1" width="500"/>
</p>

<h2 align="center">Tool Running in Background</h2>
<p align="center">
  <img src="Imagenes/Herrramienta Ejecutada y Ejecudad en Segundo Plano.png" alt="Photo 2" width="500"/>
</p>

<h2 align="center">Background Process</h2>
<p align="center">
  <img src="Imagenes/Proceso en Segundo Plano.png" alt="Photo 3" width="500"/>
</p>

<h2 align="center">Background Process Options</h2>
<p align="center">
  <img src="Imagenes/Opciones  Proceso Segundo Plano.png" alt="Photo 3" width="500"/>
</p>

## 🚀 Features

- ✔️ Automatic organization of files into folders by type.  
- ✔️ Very comprehensive predefined categories (Docs, Pics, Movies, Setups, Archives, Code, CAD, etc.).  
- ✔️ Unrecognized files are moved into a folder named by their extension (`.xyz`).  
- ✔️ New extensions are recorded in memory (`Unsorted`) without creating external files.  
- ✔️ Runs in the background with a tray icon.  
- ✔️ Windows notifications when a file is moved.  
- ✔️ Zero external configuration dependencies (`categories.json` is embedded in the code).  
- ✔️ Produces a **portable .exe** (no external JSON required).  


## 📑 Included categories

The program includes a very wide catalog of extensions, such as:

- **Docs** → `.pdf`, `.docx`, `.pptx`, `.xls`, `.txt`, `.epub`, `.mobi`, `.djvu`, `.odt`…  
- **Pics** → `.jpg`, `.png`, `.gif`, `.tiff`, `.heic`, `.raw`, `.cr2`, `.nef`, `.dng`…  
- **Audio** → `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`, `.mid`, `.opus`…  
- **Movies** → `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`, `.ts`…  
- **Setups** → `.exe`, `.msi`, `.iso`, `.apk`, `.deb`, `.rpm`, `.pkg`…  
- **Archives** → `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.xz`, `.cab`, `.tgz`…  
- **Code** → `.py`, `.sh`, `.bat`, `.ps1`, `.js`, `.html`, `.css`, `.sql`, `.cpp`, `.java`, `.go`, `.rs`, `.kt`, `.asm`…  
- **CAD/3D** → `.dwg`, `.dxf`, `.stl`, `.step`, `.fbx`, `.blend`, `.c4d`…  
- **Games** → `.iso`, `.nrg`, `.nds`, `.3ds`, `.gba`, `.smc`, `.nes`, `.sav`…  
- **Security** → `.pem`, `.crt`, `.cer`, `.pfx`, `.csr`, `.asc`, `.gpg`, `.jks`…  
- **Fonts** → `.ttf`, `.otf`, `.woff`, `.fon`…  
- **Backups** → `.bak`, `.old`, `.vhd`, `.vmdk`, `.gho`…  
- **Others** → `.log`, `.dat`, `.tmp`, `.url`, `.sys`…  

---

## 🧪 Test files generator

Use `Extesions_Generator.py` to quickly generate 50 test files in your Downloads folder with random extensions to validate behavior:

```bash
python Extesions_Generator.py
```

---

## 📁 Project structure

```bash
CYSORTIFY/
├── CySortify.py # main organizer (tray + notifications)
├── Extesions_Generator.py # test files generator with random extensions
├── README.md # this file (Spanish)
└── requirements.txt # Python dependencies
```
---

## 📄 Additional documentation

- [🤝 Code of Conduct](.github/CODE_OF_CONDUCT.md)
- [📬 How to Contribute](.github/CONTRIBUTING.md)
- [🔐 Security](.github/SECURITY.md)
- [⚠️ Legal Disclaimer](DISCLAIMER.md)
- [📜 License](LICENSE)
- [📢 Support](.github/SUPPORT.md)

---

## ⚙️ 1.1 Basic usage with clone 🪟 Windows

```bash
git clone https://github.com/cyberiuscompany/CySortiFy.git
cd CySortiFy
python -m venv venv (Not mandatory)
.\venv\Scripts\activate (Not mandatory)
pip install -r requirements.txt
python CySortiFy.py
```

## ⚙️ 1.1 Build heavy .exe 🪟 Windows

```bash
# Create the heavy binary .exe with everything included
git clone https://github.com/cyberiuscompany/CySortiFy.git
cd CySortiFy
python -m venv venv (Not mandatory)
.\venv\Scripts\activate (Not mandatory)
pip install pyinstaller
pyinstaller --clean --onefile --noconsole --version-file=version.txt --icon=cyberius.ico CySortify.py

# Run the program executable
CySortiFy/
├── dist/
│   └── CySortiFy/
│       └── CySortiFy.exe  ← THIS IS THE EXECUTABLE

⚠️ **Attention!**
You can move this binary anywhere because the .exe contains everything it needs to run,
but it will take longer to start because it loads more functions, libraries and DLLs.
