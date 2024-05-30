#!/bin/bash

echo "Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

echo "Instalando Pillow..."
pip3 install Pillow

echo "¡Instalación completada!"
