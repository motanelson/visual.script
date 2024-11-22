import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import csv


class ShellApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shell Command Executor")

        # Botão para carregar o arquivo .shell
        self.load_button = tk.Button(root, text="Load .list File", command=self.load_shell_file)
        self.load_button.pack(pady=10)

        # Frame para os botões criados
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(fill=tk.BOTH, expand=True)
        self.datas=[]

    def load_shell_file(self):
        shell_path = filedialog.askopenfilename(filetypes=[("Shell Files", "*.list")])
        if not shell_path:
            return

        try:
           


            # Adiciona os botões dinamicamente
            if 0==0:
                btn = tk.Button(
                    self.buttons_frame,
                    text=shell_path,
                    command=lambda cmd=shell_path: self.execute_command(cmd)
                )
                btn.pack(pady=5, padx=10, fill=tk.X)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load .list file: {e}")

    def execute_command(self, command):
        try:
             with open(command, "r") as file:
                reader = file.read()
                commands =reader.split("\n")
                for c in commands:
                    d =c.split(";")
                    for cc in d:
                        subprocess.run(cc, shell=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to execute command: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShellApp(root)
    root.mainloop()

