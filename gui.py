import tkinter as tk
from tkinter import ttk, messagebox
from service import add_record, get_all_records, delete_record

class FinanceApp:

    def __init__(self, root):
        self.root = root
        self.root.title("财务管理系统")
        self.root.geometry("900x600")

        self.create_widgets()
        self.refresh_table()

    def create_widgets(self):
        columns = ("id", "date", "type", "amount", "category", "description")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        self.tree.pack(fill="both", expand=True)

        frame = tk.Frame(self.root)
        frame.pack(fill="x")

        tk.Button(frame, text="添加收入", command=lambda: self.open_add_window("收入")).pack(side="left")
        tk.Button(frame, text="添加支出", command=lambda: self.open_add_window("支出")).pack(side="left")
        tk.Button(frame, text="删除选中", command=self.delete_selected).pack(side="left")

    def refresh_table(self):
        self.tree.delete(*self.tree.get_children())
        records = get_all_records()
        for row in records:
            self.tree.insert("", "end", values=row)

    def open_add_window(self, rec_type):
        top = tk.Toplevel(self.root)
        top.title("添加记录")

        tk.Label(top, text="金额").pack()
        entry_amount = tk.Entry(top)
        entry_amount.pack()

        tk.Label(top, text="分类").pack()
        entry_category = tk.Entry(top)
        entry_category.pack()

        tk.Label(top, text="描述").pack()
        entry_desc = tk.Entry(top)
        entry_desc.pack()

        def save():
            add_record(
                rec_type,
                float(entry_amount.get()),
                entry_category.get(),
                entry_desc.get()
            )
            self.refresh_table()
            top.destroy()

        tk.Button(top, text="保存", command=save).pack()

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected[0])
        record_id = item["values"][0]

        delete_record(record_id)
        self.refresh_table()