import subprocess
from PIL import Image
from colorama import init, Fore, Style

# Inicializar Colorama para estilos de texto en la terminal
init(autoreset=True)

def convert_office_to_pdf(input_file, output_file):
    try:
        subprocess.run(["unoconv", "-f", "pdf", "-o", output_file, input_file], check=True)
        print(Fore.GREEN + f"File {input_file} converted to PDF: {output_file}")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error converting {input_file} to PDF: {e}")

def convert_jpg_to_png(input_file, output_file):
    try:
        img = Image.open(input_file)
        img.save(output_file, "PNG")
        print(Fore.GREEN + f"File {input_file} converted to PNG: {output_file}")
    except Exception as e:
        print(Fore.RED + f"Error converting {input_file} to PNG: {str(e)}")

def display_menu():
    print(Fore.CYAN + Style.BRIGHT + "Seleccione el tipo de archivo que desea convertir:")
    print("1. Microsoft Word (doc, docx)")
    print("2. Microsoft Excel (xls, xlsx)")
    print("3. Microsoft PowerPoint (ppt, pptx)")
    print("4. Imagen (JPG)")
    print("0. Salir")

def convert_file(option):
    if option == "1":
        input_office_file = input(Fore.YELLOW + "Ingrese la ubicación del archivo de Word: ")
        output_pdf_file = input(Fore.YELLOW + "Ingrese el nombre del archivo PDF de salida: ")
        convert_office_to_pdf(input_office_file, output_pdf_file)

    elif option == "2":
        input_office_file = input(Fore.YELLOW + "Ingrese la ubicación del archivo de Excel: ")
        output_pdf_file = input(Fore.YELLOW + "Ingrese el nombre del archivo PDF de salida: ")
        convert_office_to_pdf(input_office_file, output_pdf_file)

    elif option == "3":
        input_office_file = input(Fore.YELLOW + "Ingrese la ubicación del archivo de PowerPoint: ")
        output_pdf_file = input(Fore.YELLOW + "Ingrese el nombre del archivo PDF de salida: ")
        convert_office_to_pdf(input_office_file, output_pdf_file)

    elif option == "4":
        input_image_file = input(Fore.YELLOW + "Ingrese la ubicación del archivo de imagen JPG: ")
        output_png_file = input(Fore.YELLOW + "Ingrese el nombre del archivo PNG de salida: ")
        convert_jpg_to_png(input_image_file, output_png_file)

    elif option == "0":
        print(Fore.YELLOW + "Saliendo del programa...")
        exit()

    else:
        print(Fore.RED + "Opción no válida.")

if __name__ == "__main__":
    while True:
        display_menu()
        option = input(Fore.YELLOW + "Ingrese el número de la opción deseada: ")
        convert_file(option)
