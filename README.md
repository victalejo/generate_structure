# Documentación: Generador de Estructura de Proyectos

## Índice
1. [Descripción General](#descripción-general)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Guía de Usuario](#guía-de-usuario)
5. [Características](#características)
6. [Configuración](#configuración)
7. [Referencia Técnica](#referencia-técnica)
8. [Solución de Problemas](#solución-de-problemas)

## Descripción General

El Generador de Estructura de Proyectos es una aplicación de escritorio que permite visualizar y documentar la estructura de directorios y archivos de cualquier proyecto de software. Especialmente útil para proyectos CakePHP y otros frameworks que tienen estructuras de directorios complejas.

### Características Principales
- Interfaz gráfica intuitiva
- Personalización de visualización
- Exportación de resultados
- Configuración persistente
- Soporte para ignorar directorios específicos

## Requisitos del Sistema

- Python 3.6 o superior
- Sistema operativo: Windows, macOS, o Linux
- Módulos Python requeridos:
  - tkinter (incluido en la instalación estándar de Python)
  - pathlib
  - json (incluido en la instalación estándar de Python)

## Instalación

1. Clone o descargue el archivo `project_structure_gui.py`
2. Asegúrese de tener Python instalado
3. Ejecute el script:
```bash
python project_structure_gui.py
```

## Guía de Usuario

### Interfaz Principal

La interfaz se divide en varias secciones:

1. **Selector de Carpeta**
   - Muestra la ruta actual del proyecto
   - Botón "Examinar" para seleccionar una carpeta

2. **Configuración de Carpetas a Ignorar**
   - Campo de texto para especificar directorios a excluir
   - Un directorio por línea

3. **Personalización de Emojis**
   - Emoji para carpetas (por defecto: 📁)
   - Emoji para archivos (por defecto: 📄)

4. **Área de Resultados**
   - Muestra la estructura generada
   - Incluye barra de desplazamiento

5. **Botones de Acción**
   - Generar Estructura
   - Guardar en Archivo
   - Limpiar

### Uso Básico

1. Seleccione la carpeta del proyecto usando el botón "Examinar"
2. Modifique la lista de carpetas a ignorar si es necesario
3. Personalice los emojis si lo desea
4. Haga clic en "Generar Estructura"
5. Use "Guardar en Archivo" para exportar los resultados

## Características

### Gestión de Carpetas a Ignorar
Por defecto, se ignoran:
- lib (CakePHP)
- vendor
- node_modules
- .git
- __pycache__
- tmp
- logs

### Personalización Visual
- Emojis configurables para archivos y carpetas
- Indentación clara y consistente
- Formato de texto legible

### Exportación
- Guarda la estructura en archivos de texto
- Incluye marca de tiempo en el nombre del archivo
- Formato UTF-8 para soporte completo de caracteres

### Persistencia
- Guarda la última carpeta visitada
- Mantiene la configuración entre sesiones
- Archivo de configuración: `structure_config.json`

## Configuración

### Archivo de Configuración
```json
{
    "ignore_dirs": ["lib", "vendor", "node_modules", ...],
    "last_directory": "/ruta/ultimo/proyecto",
    "emoji_folder": "📁",
    "emoji_file": "📄"
}
```

### Personalización Manual
Puede editar `structure_config.json` directamente para:
- Modificar directorios ignorados por defecto
- Cambiar emojis predeterminados
- Establecer directorio inicial

## Referencia Técnica

### Clases Principales

#### ProjectStructureGenerator
```python
class ProjectStructureGenerator:
    def __init__(self, root)
    def load_config(self)
    def save_config(self)
    def create_gui(self)
    def generate_structure(self, start_path=None, indent='')
    def save_to_file(self)
    def clear_result(self)
```

### Métodos Importantes

- `load_config()`: Carga configuración desde archivo JSON
- `save_config()`: Guarda configuración actual
- `generate_structure()`: Genera estructura recursivamente
- `save_to_file()`: Exporta resultados a archivo

## Solución de Problemas

### Problemas Comunes

1. **Error de Permisos**
   - Causa: Sin acceso a ciertos directorios
   - Solución: Ejecutar con permisos adecuados

2. **Caracteres Incorrectos**
   - Causa: Problemas de codificación
   - Solución: Verificar que el sistema use UTF-8

3. **Directorios No Visibles**
   - Causa: Directorio en lista de ignorados
   - Solución: Revisar configuración de ignorados

### Contacto y Soporte

Para reportar problemas o sugerir mejoras:
1. Crear un issue en el repositorio
2. Incluir:
   - Descripción del problema
   - Sistema operativo
   - Versión de Python
   - Pasos para reproducir el error