# python 01_generador_plantilla_proyecto_v0.1.py

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