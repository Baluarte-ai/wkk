#!/bin/bash

# Obtener la ruta del directorio donde está este script
DIR_ACTUAL="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR_ACTUAL"

echo "=== WKK - INICIO Y ACTUALIZACIÓN AUTOMÁTICA ==="

# 1. Comprobar si hay conexión a internet intentando hacer un ping corto a github.com
# -c 1 (1 ping), -W 2 (tiempo de espera de 2 segundos)
if ping -c 1 -W 2 github.com >/dev/null 2>&1; then
    echo "Conexión a GitHub disponible. Actualizando repositorio..."
    # Descargar cambios y resetear el repositorio local para sincronizar con main
    # Esto elimina cambios locales accidentales en Codigo.py pero respeta la base de datos (.db)
    # y la configuración local (.json) ya que están gitignorados o no están rastreados.
    git fetch origin main && git reset --hard origin/main
    if [ $? -eq 0 ]; then
        echo "¡Repositorio actualizado correctamente!"
    else
        echo "Error al sincronizar con Git. Continuando con la versión local..."
    fi
else
    echo "Sin conexión a internet o GitHub inaccesible. Iniciando versión local..."
fi

# 2. Iniciar la aplicación
echo "Iniciando HMI SCADA..."
python3 Codigo.py
