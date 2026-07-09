# HMI SCADA - Control de Prensa WKK

Este repositorio contiene la aplicación HMI SCADA para el control y monitoreo de la prensa, desarrollada en Python con Tkinter.

## Archivos Principales
*   **`Codigo.py`**: Versión de producción optimizada para correr en Raspberry Pi (Linux) con pantalla completa, conectándose mediante `snap7` al PLC Siemens LOGO!.
*   **`Codigo_demo.py`**: Versión demo optimizada para Windows que emula el comportamiento de comunicación del PLC localmente para pruebas rápidas y desarrollo de UI.

## Requisitos de Instalación
Para instalar las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Ejecución
Para iniciar la versión de prueba en Windows:
```bash
python Codigo_demo.py
```
Para iniciar la versión de producción en Linux:
```bash
python Codigo.py
```
