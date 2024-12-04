import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
from datetime import datetime
import json


class ProjectStructureGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Estructura de Proyecto")
        self.root.geometry("800x600")

        # Configuración por defecto
        self.default_ignore = ['lib', 'vendor', 'node_modules', '.git', '__pycache__', 'tmp', 'logs']
        self.load_config()

        self.create_gui()

    def load_config(self):
        """Carga la configuración guardada o usa valores por defecto"""
        try:
            with open('structure_config.json', 'r') as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {
                'ignore_dirs': self.default_ignore,
                'last_directory': os.getcwd(),
                'emoji_folder': '📁',
                'emoji_file': '📄'
            }

    def save_config(self):
        """Guarda la configuración actual"""
        with open('structure_config.json', 'w') as f:
            json.dump(self.config, f)

    def create_gui(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Carpeta de proyecto
        ttk.Label(main_frame, text="Carpeta del Proyecto:").grid(row=0, column=0, sticky=tk.W)
        self.project_path = tk.StringVar(value=self.config['last_directory'])
        path_entry = ttk.Entry(main_frame, textvariable=self.project_path, width=50)
        path_entry.grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Examinar", command=self.browse_directory).grid(row=0, column=2)

        # Carpetas a ignorar
        ttk.Label(main_frame, text="Carpetas a ignorar:").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.ignore_text = tk.Text(main_frame, height=5, width=50)
        self.ignore_text.grid(row=1, column=1, columnspan=2)
        self.ignore_text.insert('1.0', '\n'.join(self.config['ignore_dirs']))

        # Personalización de emojis
        emoji_frame = ttk.LabelFrame(main_frame, text="Personalización", padding="5")
        emoji_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

        ttk.Label(emoji_frame, text="Emoji para carpetas:").grid(row=0, column=0)
        self.folder_emoji = tk.StringVar(value=self.config['emoji_folder'])
        ttk.Entry(emoji_frame, textvariable=self.folder_emoji, width=5).grid(row=0, column=1)

        ttk.Label(emoji_frame, text="Emoji para archivos:").grid(row=0, column=2, padx=10)
        self.file_emoji = tk.StringVar(value=self.config['emoji_file'])
        ttk.Entry(emoji_frame, textvariable=self.file_emoji, width=5).grid(row=0, column=3)

        # Resultado
        ttk.Label(main_frame, text="Estructura del Proyecto:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.result_text = tk.Text(main_frame, height=20, width=80)
        self.result_text.grid(row=4, column=0, columnspan=3)

        # Scrollbar para el resultado
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.result_text.yview)
        scrollbar.grid(row=4, column=3, sticky=(tk.N, tk.S))
        self.result_text['yscrollcommand'] = scrollbar.set

        # Botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=5, column=0, columnspan=3, pady=10)

        ttk.Button(button_frame, text="Generar Estructura", command=self.generate_structure).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Guardar en Archivo", command=self.save_to_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Limpiar", command=self.clear_result).pack(side=tk.LEFT, padx=5)

    def browse_directory(self):
        """Abre el diálogo para seleccionar directorio"""
        directory = filedialog.askdirectory(initialdir=self.project_path.get())
        if directory:
            self.project_path.set(directory)
            self.config['last_directory'] = directory
            self.save_config()

    def generate_structure(self, start_path=None, indent=''):
        """Genera la estructura del proyecto recursivamente"""
        if start_path is None:
            self.result_text.delete('1.0', tk.END)
            start_path = self.project_path.get()
            ignore_dirs = [d.strip() for d in self.ignore_text.get('1.0', tk.END).split('\n') if d.strip()]
            self.config['ignore_dirs'] = ignore_dirs
            self.save_config()

            self.result_text.insert(tk.END, "Estructura del Proyecto\n")
            self.result_text.insert(tk.END, "=====================\n\n")

        try:
            items = sorted(Path(start_path).iterdir())

            for item in items:
                if item.name in self.config['ignore_dirs'] or item.name.startswith('.'):
                    continue

                if item.is_dir():
                    self.result_text.insert(tk.END,
                                            f"{indent}{self.folder_emoji.get()} {item.name}/\n")
                    self.generate_structure(item, indent + '    ')
                else:
                    self.result_text.insert(tk.END,
                                            f"{indent}{self.file_emoji.get()} {item.name}\n")

        except PermissionError:
            messagebox.showerror("Error", f"Sin permisos para acceder a: {start_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al generar estructura: {str(e)}")

    def save_to_file(self):
        """Guarda la estructura en un archivo"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"project_structure_{timestamp}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.result_text.get('1.0', tk.END))
            messagebox.showinfo("Éxito", f"Estructura guardada en: {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar archivo: {str(e)}")

    def clear_result(self):
        """Limpia el área de resultado"""
        self.result_text.delete('1.0', tk.END)


def main():
    root = tk.Tk()
    app = ProjectStructureGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()