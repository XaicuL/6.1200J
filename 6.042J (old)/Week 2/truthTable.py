import tkinter as tk
from tkinter import messagebox
import itertools
import re


def solve():
    expr = entry.get().upper()
    if not expr: return

    vars_found = sorted(list(set(re.findall(r'[A-Z]', expr))))
    n = len(vars_found)

    clean_expr = expr.replace('AND', ' and ').replace('OR', ' or ').replace('NOT', ' not ')
    clean_expr = clean_expr.replace('->', ' <= ').replace('<->', ' == ')

    text_result.delete('1.0', tk.END)
    header = "  ".join(vars_found) + "  |  Result\n"
    text_result.insert(tk.END, header + "-" * (len(header) + 5) + "\n")

    try:
        for vals in itertools.product([True, False], repeat=n):
            v_map = dict(zip(vars_found, vals))
            res = eval(clean_expr, {"__builtins__": None}, v_map)
            row = "  ".join("T" if v else "F" for v in vals)
            text_result.insert(tk.END, f"{row}  |  {'T' if res else 'F'}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid Expression: {e}")


root = tk.Tk()
root.title("Truth Table Calculator")
root.geometry("400x500")

tk.Label(root, text="Logic Expression:", font=('Arial', 10, 'bold')).pack(pady=5)
tk.Label(root, text="(Use AND, OR, NOT, ->, <->)", font=('Arial', 8)).pack()

entry = tk.Entry(root, width=40, justify='center')
entry.pack(pady=5)
entry.insert(0, "(P AND Q) -> R")

tk.Button(root, text="Generate Table", command=solve, bg='#2196F3', fg='white').pack(pady=10)

text_result = tk.Text(root, width=45, height=18, font=('Courier New', 10))
text_result.pack(pady=10)

root.mainloop()
