#!/usr/bin/env python3
import os
import sys
import stat

def configurar_autostart():
    # 1. Obtener la ruta absoluta del script Codigo.py
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_codigo = os.path.join(dir_actual, "Codigo.py")
    
    if not os.path.exists(ruta_codigo):
        print(f"Error: No se encontró 'Codigo.py' en la carpeta actual: {dir_actual}")
        print("Por favor, ejecuta este script desde la misma carpeta donde está 'Codigo.py'.")
        return

    # 2. Asegurar que Codigo.py tenga permisos de ejecución en Linux
    try:
        st = os.stat(ruta_codigo)
        os.chmod(ruta_codigo, st.st_mode | stat.S_IEXEC)
        print("-> Se agregaron permisos de ejecución a Codigo.py")
    except Exception as e:
        print(f"Advertencia al dar permisos de ejecución: {e}")

    # 3. Determinar el ejecutable de Python a usar
    python_path = sys.executable

    # 4. Definir la ruta del directorio autostart del usuario en Linux (~/.config/autostart)
    home_dir = os.path.expanduser("~")
    autostart_dir = os.path.join(home_dir, ".config", "autostart")
    
    # Crear la carpeta si no existe
    if not os.path.exists(autostart_dir):
        os.makedirs(autostart_dir, exist_ok=True)
        print(f"-> Se creó la carpeta de autostart en: {autostart_dir}")
        
    desktop_file_path = os.path.join(autostart_dir, "wkk_hmi.desktop")

    # 5. Contenido del archivo .desktop
    # Path es el directorio de trabajo (working directory)
    contenido = f"""[Desktop Entry]
Type=Application
Name=WKK HMI
Comment=Inicio automático del Sistema SCADA WKK
Exec={python_path} {ruta_codigo}
Path={dir_actual}
Terminal=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
"""

    try:
        with open(desktop_file_path, "w", encoding="utf-8") as f:
            f.write(contenido)
        
        # Darle permisos de ejecución al archivo .desktop
        st = os.stat(desktop_file_path)
        os.chmod(desktop_file_path, st.st_mode | stat.S_IEXEC)
        
        print("\n=== ¡CONFIGURACIÓN COMPLETADA CON ÉXITO! ===")
        print(f"Se ha creado el archivo de inicio automático en:")
        print(f"  {desktop_file_path}")
        print(f"\nDetalles del inicio automático:")
        print(f"  - Ejecutable de Python: {python_path}")
        print(f"  - Script a ejecutar: {ruta_codigo}")
        print(f"  - Directorio de trabajo: {dir_actual}")
        print("\nEl programa se iniciará automáticamente en la pantalla de inicio la próxima vez que inicies sesión en la interfaz gráfica (Desktop).")
    except Exception as e:
        print(f"\nError al escribir el archivo de inicio automático: {e}")

if __name__ == "__main__":
    configurar_autostart()
