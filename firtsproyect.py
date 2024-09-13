import os  
import glob  
import pandas as pd  

def renombrar_archivos_en_carpeta(carpeta, detalles):  
    """Renombra los archivos en la carpeta y guarda los detalles en la lista."""  
    # Obtiene el nombre de la carpeta  
    nombre_carpeta = os.path.basename(carpeta)  
    
    # Listar todos los archivos en la carpeta  
    archivos = glob.glob(os.path.join(carpeta, '*'))  
    
    # Contadores para archivos  
    contador_imagenes = 1  
    contador_videos = 1  
    
    for archivo in archivos:  
        # Obtiene la extensión del archivo  
        _, extension = os.path.splitext(archivo)  
        extension = extension.lower()  
        
        if extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:  
            # Es una imagen  
            nuevo_nombre = f"Foto_{nombre_carpeta}_{contador_imagenes}{extension}"  
            contador_imagenes += 1  
        elif extension in ['.mp4', '.avi', '.mov', '.mkv', '.flv']:  
            # Es un video  
            nuevo_nombre = f"Video_{nombre_carpeta}_{contador_videos}{extension}"  
            contador_videos += 1  
        else:  
            # Si no es ni imagen ni video, continuar  
            continue  
        
        # Define la nueva ruta del archivo  
        nueva_ruta = os.path.join(carpeta, nuevo_nombre)  
        
        # Renombra el archivo  
        os.rename(archivo, nueva_ruta)  
        print(f'Renombrado: {archivo} -> {nueva_ruta}')  
        
        # Añadir detalles del archivo al DataFrame  
        detalles.append([nombre_carpeta, os.path.basename(archivo), nuevo_nombre])  

def main():  
    """Función principal que recorre las carpetas y renombra los archivos."""  
    # Carpeta raíz donde se encuentran todas las subcarpetas  
    carpeta_raiz = 'F:/RESPALDO DISCO GRANDE/Pozos Calicheros AM8'  
    
    # Listar todas las subcarpetas en la carpeta raíz  
    carpetas = [f.path for f in os.scandir(carpeta_raiz) if f.is_dir()]  
    
    # Lista para almacenar los detalles de los archivos  
    detalles = []  
    
    for carpeta in carpetas:  
        renombrar_archivos_en_carpeta(carpeta, detalles)  
    
    # Crear un DataFrame de pandas con los detalles  
    df = pd.DataFrame(detalles, columns=['Nombre de Carpeta', 'Nombre Original', 'Nombre Nuevo'])  
    
    # Guardar el DataFrame en un archivo Excel  
    df.to_excel('detalles_archivos.xlsx', index=False, engine='openpyxl')  
    print("Detalles guardados en 'detalles_archivos.xlsx'")  

if __name__ == "__main__":  
    main()