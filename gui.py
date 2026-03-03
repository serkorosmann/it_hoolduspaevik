import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from log_book import LogBook
from log_entry import LogEntry


class LogBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IT Hoolduspäevik")
        self.logbook = LogBook()
        self.logbook.load_from_file()

        self.build_ui()
        self.refresh_list()

    def build_ui(self):
        # Listbox kirjetega
        self.tree = ttk.Treeview(self.root, columns=("created_at", "status", "title", "description"), show="headings")
        self.tree.heading("created_at", text="Aeg")
        self.tree.heading("status", text="Staatus")
        self.tree.heading("title", text="Pealkiri")
        self.tree.heading("description", text="Kirjeldus")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Nupud
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X)

        tk.Button(frame, text="Lisa", command=self.add_entry).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame, text="Kustuta", command=self.delete_entry).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame, text="Muuda staatus", command=self.toggle_status).pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(frame, text="Salvesta", command=self.save).pack(side=tk.RIGHT, padx=5, pady=5)

    def refresh_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for entry in self.logbook.entries:
            self.tree.insert("", "end", values=(entry.created_at, entry.status, entry.title, entry.description))

    def add_entry(self):
        title = simpledialog.askstring("Pealkiri", "Sisesta töö pealkiri:")
        description = simpledialog.askstring("Kirjeldus", "Sisesta töö kirjeldus:")
        if not title or not description:
            messagebox.showerror("Viga", "Pealkiri ja kirjeldus peavad olema sisestatud")
            return
        try:
            entry = LogEntry(title, description)
            self.logbook.add_entry(entry)
            self.refresh_list()
        except ValueError as e:
            messagebox.showerror("Viga", str(e))

    def delete_entry(self):
        selected = self.tree.selection()
        if not selected:
            return
        created_at = self.tree.item(selected[0])["values"][0]
        self.logbook.delete_entry(created_at)
        self.refresh_list()

    def toggle_status(self):
        selected = self.tree.selection()
        if not selected:
            return
        created_at = self.tree.item(selected[0])["values"][0]
        self.logbook.change_status(created_at)
        self.refresh_list()

    def save(self):
        self.logbook.save_to_file()
        messagebox.showinfo("Salvestatud", "Andmed salvestatud!")


if __name__ == "__main__":
    root = tk.Tk()
    app = LogBookApp(root)
    root.mainloop()


"""
💡 Git commit + push:

git add gui.py
git commit -m "Added Tkinter GUI for LogBook (bonus)"
git push
"""