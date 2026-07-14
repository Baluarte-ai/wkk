#!/usr/bin/env python3
import os
import sys
import stat

def crear_acceso_directo():
    # 1. Obtener la ruta absoluta del script Codigo.py
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_codigo = os.path.join(dir_actual, "Codigo.py")
    ruta_logo = os.path.join(dir_actual, "assets", "Logo WKK.png")
    
    if not os.path.exists(ruta_codigo):
        print(f"Error: No se encontró 'Codigo.py' en la carpeta actual: {dir_actual}")
        return

    # 2. Asegurar permisos de ejecución a Codigo.py
    try:
        st = os.stat(ruta_codigo)
        os.chmod(ruta_codigo, st.st_mode | stat.S_IEXEC)
    except Exception as e:
        print(f"Advertencia al dar permisos de ejecución a Codigo.py: {e}")

    # 3. Determinar el directorio del Escritorio (en inglés o español)
    home_dir = os.path.expanduser("~")
    posibles_escritorios = ["Desktop", "Escritorio"]
    desktop_dir = None
    
    for folder in posibles_escritorios:
        path_test = os.path.join(home_dir, folder)
        if os.path.exists(path_test) and os.path.isdir(path_test):
            desktop_dir = path_test
            break
            
    if not desktop_dir:
        desktop_dir = home_dir  # Caída de respaldo al home si no se encuentra ninguno

    desktop_file_path = os.path.join(desktop_dir, "wkk_hmi.desktop")
    python_path = sys.executable

    # 4. Contenido del acceso directo (.desktop)
    contenido = f"""[Desktop Entry]
Type=Application
Name=WKK HMI
Comment=Iniciar Sistema SCADA WKK
Exec={python_path} {ruta_codigo}
Path={dir_actual}
Icon={ruta_logo}
Terminal=false
NoDisplay=false
"""

    try:
        with open(desktop_file_path, "w", encoding="utf-8") as f:
            f.write(contenido)
        
        # Darle permisos de ejecución al archivo .desktop en el Escritorio
        st = os.stat(desktop_file_path)
        os.chmod(desktop_file_path, st.st_mode | stat.S_IEXEC)
        
        print("\n=== ACCESO DIRECTO CREADO CON ÉXITO ===")
        print(f"Se ha creado el archivo ejecutable en tu Escritorio:")
        print(f"  {desktop_file_path}")
        print("\nNota: La primera vez que le des doble click en el Escritorio de la Raspberry Pi,")
        print("selecciona 'Mark Executable' o 'Trust and Launch' (Confiar e Iniciar) para habilitar el icono.")
    except Exception as e:
        print(f"\nError al crear el acceso directo en el Escritorio: {e}")

if __name__ == "__main__":
    crear_acceso_directo()
