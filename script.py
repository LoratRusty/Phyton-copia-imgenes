import os
from PIL import Image

def main():
    # Definir el directorio actual
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Definir la carpeta de salida para las imágenes duplicadas
    output_folder = os.path.join(current_directory, "nuevas_imagenes")
    os.makedirs(output_folder, exist_ok=True)

    # Obtener la lista de archivos de imagen en el directorio actual
    image_files = [f for f in os.listdir(current_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Salir si no hay archivos de imagen en el directorio
    if not image_files:
        print("No se encontraron archivos de imagen en el directorio.")
        return

    # Cargar la primera imagen de la lista
    image_filename = image_files[0]
    image_path = os.path.join(current_directory, image_filename)
    image = Image.open(image_path)

    # Generar imágenes duplicadas
    nombres = [i + 1 for i in range(len(image_files))]  # Generar nombres secuenciales
    for nombre, image_filename in zip(nombres, image_files):
        new_image = image.copy()

        # Guardar la imagen duplicada con el nombre en la carpeta de salida
        new_image_filename = f"{nombre}_{image_filename}"
        new_image_path = os.path.join(output_folder, new_image_filename)
        new_image.save(new_image_path)

    print("Imágenes generadas en la carpeta 'nuevas_imagenes'.")

    # Eliminar la imagen original si todas las duplicadas se generaron correctamente
    if all(os.path.exists(os.path.join(output_folder, f"{nombre}_{image_filename}")) for nombre, image_filename in zip(nombres, image_files)):
        try:
            os.remove(image_path)
            print("Imagen original eliminada.")
        except Exception as e:
            print("Error al eliminar la imagen original:", e)
    else:
        print("No se generaron todas las imágenes duplicadas correctamente.")
        print("La imagen original no se eliminará.")

if __name__ == "__main__":
    main()
