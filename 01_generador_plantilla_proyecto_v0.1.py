import os
from tkinter import Tk, filedialog


def seleccionar_carpeta():
    """Abre un cuadro de diálogo para seleccionar la carpeta base."""
    root = Tk()
    root.withdraw()
    ruta = filedialog.askdirectory(
        title="Selecciona la carpeta base donde crear el proyecto"
    )
    return ruta


def crear_directorio_proyecto(nombre_proyecto, ruta_base):
    """
    Crea la estructura jerarquizada de carpetas para un proyecto
    desarrollado con scripts y Jupyter Notebooks, siguiendo el
    protocolo de organización y control de versiones.

    Parámetros
    ----------
    nombre_proyecto : str
        Nombre del proyecto (carpeta raíz).
    ruta_base : str
        Ruta donde se creará la carpeta del proyecto.

    Retorna
    -------
    None
    """

    # --------------------------------------------------
    # Ruta principal del proyecto
    # --------------------------------------------------
    ruta_proyecto = os.path.join(ruta_base, nombre_proyecto)
    os.makedirs(ruta_proyecto, exist_ok=True)

    # --------------------------------------------------
    # Estructura de carpetas (estándar del protocolo)
    # --------------------------------------------------
    estructura = {
        "00_config": [],
        "01_data": [
            "00_raw",
            "01_external",
            "02_processed",
            "03_metadata",
        ],
        "02_notebooks": [],
        "03_scripts": [],
        "04_utils": [],
        "05_results": [
            "00_figures",
            "01_tables",
            "02_reports",
        ],
    }

    for carpeta_principal, subcarpetas in estructura.items():
        ruta_principal = os.path.join(ruta_proyecto, carpeta_principal)
        os.makedirs(ruta_principal, exist_ok=True)

        for sub in subcarpetas:
            os.makedirs(os.path.join(ruta_principal, sub), exist_ok=True)

    # --------------------------------------------------
    # Contenido del archivo .gitignore
    # --------------------------------------------------
    gitignore_contenido = """
# ===============================
# Datos y resultados (NO versionar)
# ===============================
01_data/
05_results/

# ===============================
# Jupyter
# ===============================
.ipynb_checkpoints/

# ===============================
# Entornos virtuales
# ===============================
env/
venv/
.conda/

# ===============================
# Python
# ===============================
__pycache__/
*.pyc
*.pyo

# ===============================
# Sistema
# ===============================
.DS_Store
Thumbs.db

# ===============================
# Variables de entorno
# ===============================
.env
""".strip()

    # --------------------------------------------------
    # Contenido del README.md
    # --------------------------------------------------
    readme_contenido = f"""
# {nombre_proyecto}

## 1. Descripción
Breve descripción del objetivo del proyecto, su contexto y alcance general.

## 2. Estructura del proyecto
La organización del proyecto sigue el **Protocolo de Organización y Control de Versiones
para Proyectos con Scripts y Jupyter Notebooks**.

00_config/ # Configuración del proyecto
01_data/ # Datos (no versionados)
02_notebooks/ # Jupyter Notebooks
03_scripts/ # Scripts Python
04_utils/ # Utilidades
05_results/ # Resultados (no versionados)

## 3. Control de versiones
- El control de versiones se realiza con **Git y GitHub**.
- Solo se versiona código, configuración y documentación.
- Los datos y resultados están excluidos mediante `.gitignore`.

## 4. Entorno de trabajo
Las dependencias del proyecto se documentan en:
- `environment.yml` (Conda)
- `requirements.txt` (Pip)

## 5. Notas
- No modificar datos en `01_data/00_raw/`.
- Toda transformación debe documentarse en notebooks o scripts.
""".strip()

    # --------------------------------------------------
    # Archivos iniciales del proyecto
    # --------------------------------------------------
    archivos_iniciales = {
        "README.md": readme_contenido,
        ".gitignore": gitignore_contenido,
        "environment.yml": "# Dependencias del entorno Conda\n",
        "requirements.txt": "# Dependencias del entorno Pip\n",
    }

    for archivo, contenido in archivos_iniciales.items():
        with open(os.path.join(ruta_proyecto, archivo), "w", encoding="utf-8") as f:
            f.write(contenido)

    print(f"\n✅ Proyecto '{nombre_proyecto}' creado en:")
    print(os.path.abspath(ruta_proyecto))


# --------------------------------------------------
# Ejecución
# --------------------------------------------------
if __name__ == "__main__":
    nombre = input("Ingrese el nombre del proyecto: ").strip()

    # ----------------------------------------------
    # Validación del nombre del proyecto
    # ----------------------------------------------
    if not nombre:
        print("❌ El nombre del proyecto no puede estar vacío.")
        input("\nPresione cualquier tecla para salir...")
        raise SystemExit

    usar_actual = input(
        "¿Desea usar el directorio actual como ruta base? (s/n): "
    ).strip().lower()

    if usar_actual == "s":
        ruta = os.getcwd()
    else:
        ruta = seleccionar_carpeta()

    print(f"\nEl proyecto '{nombre}' se creará en:")
    print(os.path.abspath(ruta))

    confirmar = input("¿Desea continuar? (s/n): ").strip().lower()

    if confirmar == "s":
        crear_directorio_proyecto(nombre_proyecto=nombre, ruta_base=ruta)
    else:
        print("\n❌ Operación cancelada por el usuario.")

    input("\nPresione cualquier tecla para salir...")