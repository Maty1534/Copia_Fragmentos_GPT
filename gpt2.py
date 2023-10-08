import pyperclip
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import keyboard
import requests
import zipfile
import os
import shutil
from PyPDF2 import PdfReader  # Importa la clase PdfReader desde PyPDF2

# Función para dividir el texto en fragmentos de un tamaño dado


def split_text(text, chunk_size):
    text = re.sub(r'\s+', ' ', text)  # Elimina espacios innecesarios
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Función para copiar el fragmento actual


def copy_fragment(current_fragment):
    if current_fragment < len(fragments):
        fragment = fragments[current_fragment]
        pyperclip.copy(fragment)
        update_display(current_fragment)
        if current_fragment == len(fragments) - 1:
            messagebox.showinfo(
                "Finalizado", "Todos los fragmentos han sido copiados.")
        next_fragment()  # Avanzar automáticamente al próximo fragmento

# Función para actualizar la pantalla con el fragmento actual


def update_display(current_fragment):
    if current_fragment < len(fragments):
        fragment = fragments[current_fragment]
        text_widget.delete(1.0, tk.END)  # Borra el contenido anterior
        text_widget.insert(
            tk.END, f"Fragmento {current_fragment + 1}:\n\n{fragment}")
        status_label.config(
            text=f"Fragmento {current_fragment + 1}/{len(fragments)}")

# Función para avanzar al próximo fragmento


def next_fragment():
    global current_fragment
    if current_fragment < len(fragments) - 1:
        current_fragment += 1
        update_display(current_fragment)

# Función para retroceder al fragmento anterior


def previous_fragment():
    global current_fragment
    if current_fragment > 0:
        current_fragment -= 1
        update_display(current_fragment)

# Función para abrir un archivo (PDF o texto) y realizar las acciones adecuadas


def open_file():
    global fragments, current_fragment
    file_path = filedialog.askopenfilename(
        filetypes=[("Archivos de Texto y PDF", "*.txt;*.pdf")])  # Permite seleccionar tanto archivos de texto como PDF

    if file_path:
        _, file_extension = os.path.splitext(file_path)

        if file_extension.lower() == '.pdf':
            try:
                pdf_reader = PdfReader(file_path)
                contenido = ""
                for page in pdf_reader.pages:
                    contenido += page.extract_text()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo abrir el archivo PDF: {e}")
                return
        else:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    contenido = file.read()
            except Exception as e:
                messagebox.showerror(
                    "Error", f"No se pudo abrir el archivo de texto: {e}")
                return

        fragments = split_text(contenido, CHUNK_SIZE)
        current_fragment = 0
        update_display(current_fragment)

# Función para establecer el tamaño del bloque


def set_chunk_size():
    global CHUNK_SIZE
    new_chunk_size = simpledialog.askinteger(
        "Modificar Tamaño de Bloque", "Nuevo tamaño de bloque (0 para predeterminado):", initialvalue=CHUNK_SIZE)
    if new_chunk_size is not None:
        if new_chunk_size <= 0:
            CHUNK_SIZE = 4096  # Valor predeterminado
        else:
            CHUNK_SIZE = new_chunk_size

# Función para mostrar el mensaje de bienvenida


def mostrar_bienvenida():
    messagebox.showinfo(
        "Bienvenido", "Bienvenido al programa de copia de fragmentos de texto.\n\nHaga clic en 'Abrir Archivo de Texto' o 'Abrir Archivo PDF' para comenzar.")


def abrir_configuracion():
    configuracion_window = tk.Toplevel(root)
    configuracion_window.title("Configuración")
    configuracion_window.geometry("300x150")
    configuracion_window.configure(bg="#F0F0F0")

    # Etiqueta para el tamaño del bloque
    chunk_label = tk.Label(
        configuracion_window, text="Tamaño del Bloque:", bg="#F0F0F0")
    chunk_label.pack()

    # Cuadro de entrada para el tamaño del bloque
    chunk_entry = tk.Entry(configuracion_window)
    chunk_entry.insert(0, str(CHUNK_SIZE))
    chunk_entry.pack()

    # Botón para aplicar el cambio de tamaño de bloque
    apply_button = tk.Button(configuracion_window, text="Aplicar",
                             command=lambda: aplicar_configuracion(int(chunk_entry.get())))
    apply_button.pack()

    # Función para aplicar el cambio de tamaño de bloque

    def aplicar_configuracion(nuevo_tamano):
        global CHUNK_SIZE
        CHUNK_SIZE = nuevo_tamano
        messagebox.showinfo(
            "Configuración", f"Tamaño del Bloque actualizado a {CHUNK_SIZE}.")

    configuracion_window.mainloop()

# Función para guardar configuraciones


def guardar_configuracion(nombre, valor):
    try:
        with open('config.txt', 'w') as archivo_config:
            archivo_config.write(f"{nombre}:{valor}")
    except Exception as e:
        print(f"Error al guardar configuración: {e}")

# Función para obtener configuraciones


def obtener_configuracion(nombre):
    try:
        with open('config.txt', 'r') as archivo_config:
            for linea in archivo_config:
                if linea.startswith(nombre):
                    return linea.split(":")[1].strip()
    except Exception as e:
        print(f"Error al obtener configuración: {e}")
    return ""


# Tamaño máximo por fragmento (constante)
CHUNK_SIZE = 4096

# Crear ventana de la interfaz gráfica
root = tk.Tk()
root.title("Fragmentos de textos para GPT")

# Crear y configurar la interfaz gráfica con colores y estilos
root.configure(bg="#F0F0F0")  # Fondo de la ventana
text_widget = tk.Text(root, wrap=tk.WORD, bg="#FFFFFF",
                      fg="#000000")  # Color de fondo y texto
text_widget.pack()

# Crear un frame para centrar los botones
button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack()

open_file_button = tk.Button(button_frame, text="Abrir Archivo (Texto o PDF)",
                             command=open_file, borderwidth=5, bg="#4CAF50", fg="#FFFFFF")
open_file_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copiar (Ctrl+Shift+C)",
                        command=lambda: copy_fragment(current_fragment), borderwidth=5, bg="#008CBA", fg="#FFFFFF")
copy_button.pack(side=tk.LEFT, padx=10)

previous_button = tk.Button(
    button_frame, text="Anterior (Ctrl+Shift+Izquierda)", command=previous_fragment, borderwidth=5, bg="#E57373", fg="#FFFFFF")
previous_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(
    button_frame, text="Siguiente (Ctrl+Shift+Derecha)", command=next_fragment, borderwidth=5, bg="#2196F3", fg="#FFFFFF")
next_button.pack(side=tk.LEFT, padx=10)

config_button = tk.Button(
    button_frame, text="Configuración", command=abrir_configuracion, borderwidth=5, bg="#FF5722", fg="#FFFFFF")
config_button.pack(side=tk.LEFT, padx=10)

status_label = tk.Label(root, text="", bg="#F0F0F0")
status_label.pack()

# Configura los atajos de teclado para avanzar y retroceder
keyboard.add_hotkey('ctrl+shift+c', lambda: copy_fragment(current_fragment))
keyboard.add_hotkey('ctrl+shift+left', previous_fragment)
keyboard.add_hotkey('ctrl+shift+right', next_fragment)

current_fragment = 0  # Índice del fragmento actual

# Verifica si el usuario ya ha visto el mensaje de bienvenida y la solicitud de actualizaciones
if not obtener_configuracion("bienvenida"):
    mostrar_bienvenida()
    guardar_configuracion("bienvenida", "visto")


root.iconify()  # Minimiza la ventana al inicio

root.mainloop()
