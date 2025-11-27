import tkinter as tk

# =========================
# Window Setup
# =========================
window = tk.Tk()
window.geometry("700x500")
window.title("Test")

# ============
# Canvas Setup
# ============
canvas = tk.Canvas(window, bg="grey", scrollregion=(0, 0, 2800, 2000))
canvas.pack(expand = True, fill = "both")





window.mainloop()