import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext


class MultiTabTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("T4 Editor")

        # Create tab control
        self.tabControl = ttk.Notebook(root)
        self.tabControl.pack(expand=1, fill="both")

        # Create initial tab
        self.create_tab()

        # Menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New Tab", command=self.create_tab)
        self.file_menu.add_command(label="Close Tab", command=self.close_tab)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=root.quit)

    def create_tab(self):
        new_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(new_tab, text=f"Tab {self.tabControl.index('end')}")

        # Create a scrolled text widget inside the new tab
        text_area = scrolledtext.ScrolledText(new_tab, wrap=tk.WORD, width=40, height=10)
        text_area.pack(expand=True, fill="both")

        # Optionally, you can set initial text or do other configurations here

        self.tabControl.select(new_tab)

    def close_tab(self):
        if len(self.tabControl.tabs()) > 1:
            current_tab = self.tabControl.select()
            self.tabControl.forget(current_tab)
        else:
            messagebox.showinfo("Error", "Cannot close the last tab.")


def main():
    root = tk.Tk()
    editor = MultiTabTextEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
