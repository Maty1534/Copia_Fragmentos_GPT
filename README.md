# Copia_Fragmentos_GPT

[Boton de Descarga: 💾](https://github.com/d69e8d1c-5358-4177-b537-be7ada3a564a)

El proyecto es una aplicación de escritorio simple que permite a los usuarios abrir archivos de texto o PDF y dividir su contenido en fragmentos de un tamaño especificado. Luego, los usuarios pueden copiar el fragmento actual al portapapeles para su uso, como entrada de texto en otro programa.

**Nombre del proyecto:** Copiador de Fragmentos de Texto

**Descripción general:**
El proyecto se basa en una interfaz gráfica de usuario (GUI) desarrollada con la biblioteca `tkinter` de Python. Proporciona una manera fácil de abrir archivos de texto o PDF, dividir su contenido en fragmentos y copiar esos fragmentos al portapapeles.

**Funcionalidades:**

1. **Abrir Archivo de Texto o PDF:**
   - Los usuarios pueden hacer clic en el botón "Abrir Archivo (Texto o PDF)" para seleccionar un archivo de texto o PDF desde su sistema de archivos.
   - El programa puede manejar tanto archivos de texto como PDF.

2. **Dividir Texto en Fragmentos:**
   - El contenido del archivo seleccionado se divide en fragmentos de un tamaño especificado (tamaño de bloque).
   - Los fragmentos se almacenan en una lista para su posterior procesamiento.

3. **Navegación por Fragmentos:**
   - Los usuarios pueden navegar por los fragmentos utilizando botones "Anterior" y "Siguiente", o mediante atajos de teclado (Ctrl+Shift+Izquierda y Ctrl+Shift+Derecha).
   - El fragmento actual se muestra en la interfaz gráfica.

4. **Copia de Fragmentos:**
   - Los usuarios pueden copiar el fragmento actual al portapapeles haciendo clic en el botón "Copiar (Ctrl+Shift+C)" o utilizando el atajo de teclado correspondiente (Ctrl+Shift+C).
   - Los fragmentos copiados pueden pegarse en otros programas como entrada de texto.

5. **Configuración del Tamaño del Bloque:**
   - Los usuarios pueden configurar el tamaño de bloque deseado haciendo clic en el botón "Configuración".
   - Se muestra un cuadro de diálogo para ingresar el nuevo tamaño de bloque, con una opción para restablecerlo al valor predeterminado.

6. **Mensajes de Bienvenida y Configuración:**
   - La aplicación muestra un mensaje de bienvenida la primera vez que se inicia para guiar a los usuarios.
   - Los mensajes de bienvenida y la configuración se almacenan en un archivo de configuración para que no se muestren repetidamente.

7. **Manejo de Errores:**
   - La aplicación maneja errores al abrir archivos, ya sea de texto o PDF, y muestra mensajes de error en caso de problemas.

**Uso típico del proyecto:**
- Un usuario abre la aplicación.
- Hace clic en "Abrir Archivo (Texto o PDF)" para seleccionar un archivo.
- La aplicación divide automáticamente el contenido en fragmentos.
- Utiliza los botones "Anterior" y "Siguiente" o atajos de teclado para navegar por los fragmentos.
- Cuando encuentra un fragmento deseado, hace clic en "Copiar (Ctrl+Shift+C)" o utiliza el atajo de teclado para copiarlo al portapapeles.
- Pega el fragmento copiado en otro programa o aplicación.

Este proyecto proporciona una forma sencilla y rápida de trabajar con fragmentos de texto de archivos largos, lo que puede ser útil en diversas situaciones, como la preparación de datos para procesamiento de lenguaje natural o la extracción de información de documentos extensos.
