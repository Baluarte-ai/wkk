#!/usr/bin/env python3
import os
import sys
import stat

def configurar_autostart():
    # 1. Obtener la ruta absoluta de Codigo.py y del script bash de inicio
    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_codigo = os.path.join(dir_actual, "Codigo.py")
    ruta_sh = os.path.join(dir_actual, "arrancar_hmi.sh")
    
    if not os.path.exists(ruta_sh):
        print(f"Error: No se encontró 'arrancar_hmi.sh' en la carpeta actual: {dir_actual}")
        return

    # 2. Asegurar que Codigo.py y arrancar_hmi.sh tengan permisos de ejecución en Linux
    try:
        st = os.stat(ruta_codigo)
        os.chmod(ruta_codigo, st.st_mode | stat.S_IEXEC)
        print("-> Se agregaron permisos de ejecución a Codigo.py")
    except Exception as e:
        print(f"Advertencia al dar permisos de ejecución a Codigo.py: {e}")

    try:
        st = os.stat(ruta_sh)
        os.chmod(ruta_sh, st.st_mode | stat.S_IEXEC)
        print("-> Se agregaron permisos de ejecución a arrancar_hmi.sh")
    except Exception as e:
        print(f"Advertencia al dar permisos de ejecución a arrancar_hmi.sh: {e}")

    # 3. Definir la ruta del directorio autostart del usuario en Linux (~/.config/autostart)
    home_dir = os.path.expanduser("~")
    autostart_dir = os.path.join(home_dir, ".config", "autostart")
    
    # Crear la carpeta si no existe
    if not os.path.exists(autostart_dir):
        os.makedirs(autostart_dir, exist_ok=True)
        print(f"-> Se creó la carpeta de autostart en: {autostart_dir}")
        
    desktop_file_path = os.path.join(autostart_dir, "wkk_hmi.desktop")

    # 4. Contenido del archivo .desktop para lanzar el script bash
    contenido = f"""[Desktop Entry]
Type=Application
Name=WKK HMI
Comment=Inicio automático y actualización del Sistema SCADA WKK
Exec=/bin/bash {ruta_sh}
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
        print(f"  - Script de arranque: {ruta_sh}")
        print(f"  - Directorio de trabajo: {dir_actual}")
        print("\nEl programa se actualizará y se iniciará automáticamente la próxima vez que inicies sesión en la interfaz gráfica (Desktop).")
    except Exception as e:
        print(f"\nError al escribir el archivo de inicio automático: {e}")

if __name__ == "__main__":
    configurar_autostart()
