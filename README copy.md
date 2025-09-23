# CySortify

CySortify es una herramienta ligera en **Python** que organiza automáticamente tu carpeta de **Descargas** en Windows.  
Clasifica los archivos por **categorías lógicas** (Docs, Pics, Movies, Setups, etc.) o por **extensión** si no encajan en ninguna categoría definida.  

Incluye:
- **CySortify.py** → organizador principal (ejecución en segundo plano con icono en bandeja).
- **Extesions_Generator.py** → generador de ficheros de prueba con extensiones aleatorias.
- **categories.json** → archivo de configuración editable con categorías y extensiones.

---

## 🚀 Características

- ✔️ Clasifica archivos en carpetas lógicas o por extensión.
- ✔️ Evita colisiones (`archivo (1).pdf`, `archivo (2).pdf`).
- ✔️ Notificaciones en Windows con el archivo movido y destino.
- ✔️ Aprendizaje automático: extensiones nuevas se añaden a `"Unsorted"` en `categories.json`.
- ✔️ Menú en bandeja:
  - **Organizar ahora**
  - **Abrir Descargas**
  - **Salir**
- ✔️ Configurable mediante `categories.json`.

---

## 📂 Estructura del proyecto

CySortify/
├── CySortify.py # Organizador principal
├── Extesions_Generator.py # Generador de archivos de prueba
├── categories.json # Categorías y extensiones configurables
└── README.md # Este archivo

pip install pyinstaller
pyinstaller --clean --onefile --noconsole CySortify.py
pyinstaller --clean --onefile --noconsole --version-file=version.txt CySortify.py
pyinstaller --clean --onefile --noconsole --version-file=version.txt --icon=cyberius.ico CySortify.py

dist/CySortify.exe
