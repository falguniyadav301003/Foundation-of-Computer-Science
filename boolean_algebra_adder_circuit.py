import tkinter as tk
from tkinter import messagebox


# ============================================================
# BOOLEAN INPUT VALIDATION
# ============================================================

def get_boolean(entry, name):
    value = entry.get().strip()

    if value not in ("0", "1"):
        messagebox.showerror(
            "Invalid Input",
            f"{name} must be either 0 or 1."
        )
        return None

    return int(value)


# ============================================================
# DRAWING FUNCTIONS
# ============================================================

def clear_canvas():
    canvas.delete("all")


def draw_input(x, y, label):
    canvas.create_text(
        x - 20, y,
        text=label,
        font=("Arial", 12, "bold")
    )

    canvas.create_line(
        x, y, x + 80, y,
        width=2
    )


def draw_output(x, y, label):
    canvas.create_line(
        x, y, x + 70, y,
        width=2
    )

    canvas.create_text(
        x + 90, y,
        text=label,
        font=("Arial", 12, "bold")
    )


def draw_and_gate(x, y, label="AND"):
    # AND gate body
    canvas.create_arc(
        x + 20, y - 50,
        x + 100, y + 50,
        start=270,
        extent=180,
        style=tk.ARC,
        width=2
    )

    canvas.create_line(
        x, y - 50,
        x + 50, y - 50,
        width=2
    )

    canvas.create_line(
        x, y + 50,
        x + 50, y + 50,
        width=2
    )

    canvas.create_line(
        x, y - 50,
        x, y + 50,
        width=2
    )

    canvas.create_text(
        x + 35, y,
        text=label,
        font=("Arial", 10, "bold")
    )

    return x + 100


def draw_or_gate(x, y, label="OR"):
    # OR gate
    points = [
        x, y - 50,
        x + 40, y - 45,
        x + 90, y,
        x + 40, y + 45,
        x, y + 50,
        x + 25, y,
        x, y - 50
    ]

    canvas.create_line(
        points,
        smooth=True,
        width=2
    )

    canvas.create_text(
        x + 40, y,
        text=label,
        font=("Arial", 10, "bold")
    )

    return x + 90


def draw_xor_gate(x, y, label="XOR"):
    # XOR gate body
    draw_or_gate(x + 10, y, label)

    # Extra XOR curve
    canvas.create_arc(
        x - 10, y - 50,
        x + 30, y + 50,
        start=270,
        extent=180,
        style=tk.ARC,
        width=2
    )

    return x + 100


def draw_not_gate(x, y):
    # Triangle
    canvas.create_polygon(
        x, y - 35,
        x, y + 35,
        x + 70, y,
        outline="black",
        fill="white",
        width=2
    )

    canvas.create_text(
        x + 25, y,
        text="NOT",
        font=("Arial", 10, "bold")
    )

    # NOT bubble
    canvas.create_oval(
        x + 68, y - 6,
        x + 80, y + 6,
        outline="black",
        width=2
    )

    return x + 80


def draw_nand_gate(x, y):
    end = draw_and_gate(x, y, "AND")

    # Bubble
    canvas.create_oval(
        end - 5, y - 6,
        end + 7, y + 6,
        outline="black",
        fill="white",
        width=2
    )

    return end + 2


def draw_nor_gate(x, y):
    end = draw_or_gate(x, y, "OR")

    # Bubble
    canvas.create_oval(
        end - 5, y - 6,
        end + 7, y + 6,
        outline="black",
        fill="white",
        width=2
    )

    return end + 2


def draw_gate_label(x, y, text):
    canvas.create_text(
        x, y,
        text=text,
        font=("Arial", 10, "bold")
    )


# ============================================================
# BASIC LOGIC CIRCUITS
# ============================================================

def draw_basic_circuit(operation):

    clear_canvas()

    canvas.create_text(
        350, 20,
        text=f"{operation} GATE",
        font=("Arial", 16, "bold")
    )

    if operation == "NOT":

        draw_input(80, 120, "A")

        draw_not_gate(180, 120)

        canvas.create_line(
            260, 120, 430, 120,
            width=2
        )

        canvas.create_text(
            460, 120,
            text="Y",
            font=("Arial", 12, "bold")
        )

    else:

        draw_input(80, 90, "A")
        draw_input(80, 160, "B")

        gate_x = 250
        gate_y = 125

        if operation == "AND":
            end = draw_and_gate(gate_x, gate_y)

        elif operation == "OR":
            end = draw_or_gate(gate_x, gate_y)

        elif operation == "NAND":
            end = draw_nand_gate(gate_x, gate_y)

        elif operation == "NOR":
            end = draw_nor_gate(gate_x, gate_y)

        elif operation == "XOR":
            end = draw_xor_gate(gate_x, gate_y, "XOR")

        elif operation == "XNOR":
            end = draw_xor_gate(gate_x, gate_y, "XOR")

            # XNOR bubble
            canvas.create_oval(
                end - 5, gate_y - 6,
                end + 7, gate_y + 6,
                outline="black",
                fill="white",
                width=2
            )

        # Input connections
        canvas.create_line(
            160, 90,
            250, 90,
            width=2
        )

        canvas.create_line(
            160, 160,
            250, 160,
            width=2
        )

        # Output
        canvas.create_line(
            end, gate_y,
            500, gate_y,
            width=2
        )

        canvas.create_text(
            525, gate_y,
            text="Y",
            font=("Arial", 12, "bold")
        )


# ============================================================
# HALF ADDER
# ============================================================

def draw_half_adder():

    clear_canvas()

    canvas.create_text(
        350, 20,
        text="HALF ADDER",
        font=("Arial", 16, "bold")
    )

    # ---------------- INPUTS ----------------

    canvas.create_text(
        50, 90,
        text="A",
        font=("Arial", 12, "bold")
    )

    canvas.create_text(
        50, 170,
        text="B",
        font=("Arial", 12, "bold")
    )

    # ---------------- XOR GATE ----------------

    draw_xor_gate(250, 90, "XOR")

    # A and B to XOR
    canvas.create_line(
        70, 90,
        250, 90,
        width=2
    )

    canvas.create_line(
        70, 170,
        180, 170,
        width=2
    )

    canvas.create_line(
        180, 170,
        180, 110,
        width=2
    )

    canvas.create_line(
        180, 110,
        250, 110,
        width=2
    )

    # XOR output
    canvas.create_line(
        350, 90,
        520, 90,
        width=2
    )

    canvas.create_text(
        550, 90,
        text="SUM",
        font=("Arial", 12, "bold")
    )

    # ---------------- AND GATE ----------------

    draw_and_gate(250, 250, "AND")

    # A to AND
    canvas.create_line(
        70, 90,
        150, 90,
        width=2
    )

    canvas.create_line(
        150, 90,
        150, 230,
        width=2
    )

    canvas.create_line(
        150, 230,
        250, 230,
        width=2
    )

    # B to AND
    canvas.create_line(
        70, 170,
        120, 170,
        width=2
    )

    canvas.create_line(
        120, 170,
        120, 270,
        width=2
    )

    canvas.create_line(
        120, 270,
        250, 270,
        width=2
    )

    # Carry output
    canvas.create_line(
        350, 250,
        520, 250,
        width=2
    )

    canvas.create_text(
        555, 250,
        text="CARRY",
        font=("Arial", 12, "bold")
    )


# ============================================================
# FULL ADDER
# ============================================================

def draw_full_adder():

    clear_canvas()

    canvas.create_text(
        350, 20,
        text="FULL ADDER",
        font=("Arial", 16, "bold")
    )

    # ========================================================
    # FIRST XOR
    # ========================================================

    draw_xor_gate(180, 100, "XOR")

    # Inputs A and B
    canvas.create_text(
        40, 70,
        text="A",
        font=("Arial", 12, "bold")
    )

    canvas.create_text(
        40, 130,
        text="B",
        font=("Arial", 12, "bold")
    )

    canvas.create_line(
        60, 70,
        180, 70,
        width=2
    )

    canvas.create_line(
        60, 130,
        130, 130,
        width=2
    )

    canvas.create_line(
        130, 130,
        130, 110,
        width=2
    )

    canvas.create_line(
        130, 110,
        180, 110,
        width=2
    )

    # ========================================================
    # SECOND XOR
    # ========================================================

    draw_xor_gate(400, 100, "XOR")

    # First XOR output to second XOR
    canvas.create_line(
        280, 100,
        400, 100,
        width=2
    )

    # Cin
    canvas.create_text(
        340, 150,
        text="Cin",
        font=("Arial", 12, "bold")
    )

    canvas.create_line(
        370, 150,
        370, 120,
        width=2
    )

    canvas.create_line(
        370, 120,
        400, 120,
        width=2
    )

    # SUM output
    canvas.create_line(
        500, 100,
        580, 100,
        width=2
    )

    canvas.create_text(
        610, 100,
        text="SUM",
        font=("Arial", 12, "bold")
    )

    # ========================================================
    # FIRST AND GATE: A AND B
    # ========================================================

    draw_and_gate(180, 260, "AND")

    canvas.create_line(
        80, 70,
        80, 235,
        width=2
    )

    canvas.create_line(
        80, 235,
        180, 235,
        width=2
    )

    canvas.create_line(
        100, 130,
        100, 285,
        width=2
    )

    canvas.create_line(
        100, 285,
        180, 285,
        width=2
    )

    # ========================================================
    # SECOND AND GATE: Cin AND (A XOR B)
    # ========================================================

    draw_and_gate(400, 300, "AND")

    # First XOR output
    canvas.create_line(
        280, 100,
        320, 100,
        width=2
    )

    canvas.create_line(
        320, 100,
        320, 275,
        width=2
    )

    canvas.create_line(
        320, 275,
        400, 275,
        width=2
    )

    # Cin
    canvas.create_line(
        340, 150,
        340, 325,
        width=2
    )

    canvas.create_line(
        340, 325,
        400, 325,
        width=2
    )

    # ========================================================
    # OR GATE
    # ========================================================

    draw_or_gate(570, 270, "OR")

    # First AND output
    canvas.create_line(
        280, 260,
        500, 260,
        width=2
    )

    canvas.create_line(
        500, 260,
        570, 250,
        width=2
    )

    # Second AND output
    canvas.create_line(
        500, 300,
        530, 300,
        width=2
    )

    canvas.create_line(
        530, 300,
        570, 290,
        width=2
    )

    # Carry output
    canvas.create_line(
        660, 270,
        700, 270,
        width=2
    )

    canvas.create_text(
        720, 270,
        text="CARRY",
        font=("Arial", 12, "bold")
    )


# ============================================================
# CALCULATION
# ============================================================

def calculate():

    operation = operation_var.get()

    # ---------------- BASIC OPERATIONS ----------------

    if operation in [
        "AND",
        "OR",
        "NOT",
        "NAND",
        "NOR",
        "XOR",
        "XNOR"
    ]:

        A = get_boolean(entry_A, "A")

        if A is None:
            return

        if operation == "NOT":

            result = int(not A)

            result_label.config(
                text=f"Output Y = {result}"
            )

        else:

            B = get_boolean(entry_B, "B")

            if B is None:
                return

            if operation == "AND":
                result = A & B

            elif operation == "OR":
                result = A | B

            elif operation == "NAND":
                result = int(not (A & B))

            elif operation == "NOR":
                result = int(not (A | B))

            elif operation == "XOR":
                result = A ^ B

            elif operation == "XNOR":
                result = int(not (A ^ B))

            result_label.config(
                text=f"Output Y = {result}"
            )

    # ---------------- HALF ADDER ----------------

    elif operation == "Half Adder":

        A = get_boolean(entry_A, "A")
        B = get_boolean(entry_B, "B")

        if A is None or B is None:
            return

        Sum = A ^ B
        Carry = A & B

        result_label.config(
            text=f"SUM = {Sum}     CARRY = {Carry}"
        )

    # ---------------- FULL ADDER ----------------

    elif operation == "Full Adder":

        A = get_boolean(entry_A, "A")
        B = get_boolean(entry_B, "B")
        Cin = get_boolean(entry_Cin, "Cin")

        if A is None or B is None or Cin is None:
            return

        Sum = A ^ B ^ Cin

        Carry = (A & B) | (Cin & (A ^ B))

        result_label.config(
            text=f"SUM = {Sum}     CARRY = {Carry}"
        )


# ============================================================
# OPERATION SELECTION
# ============================================================

def operation_changed(*args):

    operation = operation_var.get()

    # Enable/disable inputs
    if operation == "NOT":

        entry_B.config(state="disabled")
        entry_Cin.config(state="disabled")

    elif operation == "Full Adder":

        entry_B.config(state="normal")
        entry_Cin.config(state="normal")

    else:

        entry_B.config(state="normal")
        entry_Cin.config(state="disabled")

    # Draw selected circuit

    if operation == "Half Adder":

        draw_half_adder()

    elif operation == "Full Adder":

        draw_full_adder()

    else:

        draw_basic_circuit(operation)

    result_label.config(text="Output = ")


# ============================================================
# EXIT PROGRAM
# ============================================================

def exit_program():

    root.destroy()


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Boolean Algebra and Adder Circuits")

root.geometry("850x700")

root.resizable(False, False)


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    root,
    text="BOOLEAN ALGEBRA & ADDER CIRCUITS",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)


# ============================================================
# MENU
# ============================================================

operation_var = tk.StringVar()

operation_var.set("AND")

operation_var.trace_add(
    "write",
    operation_changed
)

tk.Label(
    root,
    text="Select Operation:",
    font=("Arial", 12, "bold")
).pack()

operation_menu = tk.OptionMenu(
    root,
    operation_var,

    "AND",
    "OR",
    "NOT",
    "NAND",
    "NOR",
    "XOR",
    "XNOR",
    "Half Adder",
    "Full Adder"
)

operation_menu.config(
    width=20,
    font=("Arial", 11)
)

operation_menu.pack(pady=5)


# ============================================================
# INPUT FRAME
# ============================================================

input_frame = tk.Frame(root)

input_frame.pack(pady=10)


# A
tk.Label(
    input_frame,
    text="A (0/1):",
    font=("Arial", 11)
).grid(row=0, column=0, padx=5)

entry_A = tk.Entry(
    input_frame,
    width=8
)

entry_A.grid(row=0, column=1, padx=5)


# B
tk.Label(
    input_frame,
    text="B (0/1):",
    font=("Arial", 11)
).grid(row=0, column=2, padx=5)

entry_B = tk.Entry(
    input_frame,
    width=8
)

entry_B.grid(row=0, column=3, padx=5)


# Cin
tk.Label(
    input_frame,
    text="Cin (0/1):",
    font=("Arial", 11)
).grid(row=0, column=4, padx=5)

entry_Cin = tk.Entry(
    input_frame,
    width=8
)

entry_Cin.grid(row=0, column=5, padx=5)


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(root)

button_frame.pack(pady=10)


calculate_button = tk.Button(
    button_frame,
    text="Calculate",
    command=calculate,
    font=("Arial", 11, "bold"),
    width=12
)

calculate_button.grid(
    row=0,
    column=0,
    padx=10
)


exit_button = tk.Button(
    button_frame,
    text="Exit",
    command=exit_program,
    font=("Arial", 11, "bold"),
    width=12
)

exit_button.grid(
    row=0,
    column=1,
    padx=10
)


# ============================================================
# RESULT
# ============================================================

result_label = tk.Label(
    root,
    text="Output = ",
    font=("Arial", 15, "bold")
)

result_label.pack(pady=5)


# ============================================================
# CIRCUIT CANVAS
# ============================================================

canvas = tk.Canvas(
    root,
    width=800,
    height=420,
    bg="white"
)

canvas.pack(pady=10)


# ============================================================
# START PROGRAM
# ============================================================

draw_basic_circuit("AND")

root.mainloop()
