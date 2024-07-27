# Herramienta de Conversión de Archivos

Este script en Python proporciona una interfaz de línea de comandos para convertir archivos de Microsoft Office a PDF y para convertir imágenes JPG a PNG. Utiliza `unoconv` para la conversión de archivos de Office y `Pillow` para la conversión de imágenes.

## Requisitos

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (para la conversión de imágenes)
- [unoconv](https://github.com/unoconv/unoconv) (para la conversión de archivos de Office a PDF)
- Colorama (para la gestión de colores en la terminal)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/CodingJAndres/convert.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd convert
    ```

3. **Instala las dependencias necesarias:**

    ```bash
    pip install Pillow colorama
    ```

4. **Asegúrate de que `unoconv` esté instalado en tu sistema.** Puedes instalarlo usando:

    ```bash
    sudo apt install unoconv
    ```

## Uso

1. **Ejecuta el script:**

    ```bash
    python convert_to_.py
    ```

2. **Selecciona el tipo de archivo que deseas convertir:**

    - **1. Microsoft Word (doc, docx)**
    - **2. Microsoft Excel (xls, xlsx)**
    - **3. Microsoft PowerPoint (ppt, pptx)**
    - **4. Imagen (JPG)**
    - **0. Salir**

3. **Proporciona la ubicación del archivo de entrada y el nombre del archivo de salida cuando se te solicite.**

## Descripción de Opciones

- **Microsoft Word/Excel/PowerPoint a PDF:** Convierte archivos de Office a PDF utilizando `unoconv`.
- **Imagen JPG a PNG:** Convierte archivos de imagen JPG a PNG utilizando `Pillow`.

## Manejo de Errores

- **Errores de Conversión:** El script mostrará mensajes de error en caso de que la conversión falle.
- **Opción No Válida:** Si se selecciona una opción no válida, el script mostrará un mensaje de error.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

¡Utiliza esta herramienta para convertir archivos y mejorar tu flujo de trabajo!
