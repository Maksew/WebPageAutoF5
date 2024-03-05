from cx_Freeze import setup, Executable
import sys

# Dépendances
build_exe_options = {
    "packages": ["os", "selenium", "tkinter", "logging", "re", "threading", "time"],  # vos packages ici
    "excludes": [],  # Excluez des packages non utilisés pour réduire la taille
    "include_files": ["src/", "drivers/", "img/"]  # Incluez d'autres dossiers si nécessaire
}

# Cible de l'exécutable
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Utilisez "Win32GUI" si vous voulez une application sans console

executables = [
    Executable("src/main.py", base=base)
]

setup(
    name="WebAutoF5",
    version="0.1",
    description="Application de rafraîchissement automatique de pages web",
    options={"build_exe": build_exe_options},
    executables=executables
)
