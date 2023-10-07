import pyperclip
import re
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import keyboard
import PyPDF2

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

# Función para abrir un archivo de texto


def open_file():
    global fragments, current_fragment
    file_path = filedialog.askopenfilename(
        filetypes=[("Archivos de Texto", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            contenido = file.read()
        fragments = split_text(contenido, CHUNK_SIZE)
        current_fragment = 0
        update_display(current_fragment)

# Función para abrir un archivo PDF y extraer su contenido de texto


def open_pdf():
    global fragments, current_fragment
    pdf_path = filedialog.askopenfilename(
        filetypes=[("Archivos PDF", "*.pdf")])
    if pdf_path:
        text = extract_text_from_pdf(pdf_path)
        if text:
            fragments = split_text(text, CHUNK_SIZE)
            current_fragment = 0
            update_display(current_fragment)

# Función para extraer texto de un archivo PDF


def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo PDF: {e}")
        return None

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


# Tamaño máximo por fragmento (constante)
CHUNK_SIZE = 4096

# Crear ventana de la interfaz gráfica
root = tk.Tk()
root.title("Copiar Fragmentos de Texto")

# Crear y configurar la interfaz gráfica con colores y estilos
root.configure(bg="#F0F0F0")  # Fondo de la ventana
text_widget = tk.Text(root, wrap=tk.WORD, bg="#FFFFFF",
                      fg="#000000")  # Color de fondo y texto
text_widget.pack()

# Crear un frame para centrar los botones
button_frame = tk.Frame(root, bg="#F0F0F0")
button_frame.pack()

open_button = tk.Button(button_frame, text="Abrir Archivo de Texto",
                        command=open_file, borderwidth=5, bg="#4CAF50", fg="#FFFFFF")  # Color de fondo y texto
open_button.pack(side=tk.LEFT, padx=10)

open_pdf_button = tk.Button(button_frame, text="Abrir Archivo PDF",
                            command=open_pdf, borderwidth=5, bg="#FF5722", fg="#FFFFFF")  # Color de fondo y texto
open_pdf_button.pack(side=tk.LEFT, padx=10)

copy_button = tk.Button(button_frame, text="Copiar (Ctrl+Shift+C)",
                        command=lambda: copy_fragment(current_fragment), borderwidth=5, bg="#008CBA", fg="#FFFFFF")  # Color de fondo y texto
copy_button.pack(side=tk.LEFT, padx=10)

previous_button = tk.Button(
    button_frame, text="Anterior (Ctrl+Shift+Izquierda)", command=previous_fragment, borderwidth=5, bg="#E57373", fg="#FFFFFF")  # Color de fondo y texto
previous_button.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(
    button_frame, text="Siguiente (Ctrl+Shift+Derecha)", command=next_fragment, borderwidth=5, bg="#2196F3", fg="#FFFFFF")  # Color de fondo y texto
next_button.pack(side=tk.LEFT, padx=10)

chunk_size_button = tk.Button(
    button_frame, text="Bloque", command=set_chunk_size, borderwidth=5, bg="#FF9800",
    fg="#FFFFFF")  # Color de fondo y texto
chunk_size_button.pack(side=tk.LEFT, padx=10)

status_label = tk.Label(root, text="", bg="#F0F0F0")  # Color de fondo
status_label.pack()

# Configura los atajos de teclado para avanzar y retroceder
keyboard.add_hotkey('ctrl+shift+c', lambda: copy_fragment(current_fragment))
keyboard.add_hotkey('ctrl+shift+left', previous_fragment)
keyboard.add_hotkey('ctrl+shift+right', next_fragment)

current_fragment = 0  # Índice del fragmento actual

root.iconify()  # Minimiza la ventana al inicio

root.mainloop()
