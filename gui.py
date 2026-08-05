import customtkinter as ctk
import tkinter as tk
import webbrowser
from tkinter import Canvas
from PIL import Image, ImageTk
from pathlib import Path
from backend.screenshot import capture_canvas
from backend.hpc_client import solve_image
from tkinter import messagebox

from config import (
    ASSETS_DIR,
    BLACK_BUTTON,
    BLUE_BUTTON,
    BRUSH_BUTTON,
    CALCULATE_BUTTON,
    CLEAR_BUTTON,
    DRAWING_BACKGROUND,
    ERASER_BUTTON,
    GREEN_BUTTON,
    LOAD_BUTTON,
    RED_BUTTON,
    SAVE_BUTTON,
    TOOLBAR_IMAGE,
    WHITE_BUTTON,
    YELLOW_BUTTON,
)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")


class CalciSketchApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("CalciSketch")
        self.geometry("1920x1080")
        self.minsize(1280, 720)
        self.configure(fg_color="white")

        self.load_assets()

        self.container = ctk.CTkFrame(self, fg_color="white")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        self.create_navbar()

        for Page in (HomePage, AboutPage, DrawingPage):
            page = Page(self.container, self)
            self.frames[Page.__name__] = page
            page.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def load_assets(self):

        self.bg_photo = ImageTk.PhotoImage(
            Image.open(ASSETS_DIR / "bg img.png").resize((1920, 1080))
        )

        self.logo = ImageTk.PhotoImage(
            Image.open(ASSETS_DIR / "logo.png").resize((40, 40))
        )

        self.about_photo = ImageTk.PhotoImage(
            Image.open(ASSETS_DIR / "ABOUT US!!.png").resize((280, 75))
        )

        self.start_photo = ImageTk.PhotoImage(
            Image.open(ASSETS_DIR / "START DRAWING.png").resize((280, 75))
        )

        self.drawing_background = ImageTk.PhotoImage(
            Image.open(DRAWING_BACKGROUND).resize((1920, 1080))
        )
        self.toolbar_photo = ImageTk.PhotoImage(
            Image.open(TOOLBAR_IMAGE).resize((1600, 102))
        )

        button_assets = {
            "red": RED_BUTTON,
            "yellow": YELLOW_BUTTON,
            "green": GREEN_BUTTON,
            "blue": BLUE_BUTTON,
            "white": WHITE_BUTTON,
            "black": BLACK_BUTTON,
            "eraser": ERASER_BUTTON,
            "brush": BRUSH_BUTTON,
            "calculate": CALCULATE_BUTTON,
            "clear": CLEAR_BUTTON,
            "save": SAVE_BUTTON,
            "load": LOAD_BUTTON,
        }
        self.toolbar_buttons = {}
        button_sizes = {
            "red": (56, 56), "yellow": (56, 56), "green": (56, 56),
            "blue": (56, 56), "white": (56, 56), "black": (56, 56),
            "eraser": (58, 58), "brush": (56, 56),
            "calculate": (68, 68), "clear": (50, 50),
            "save": (50, 50), "load": (50, 50),
        }
        for name, path in button_assets.items():
            with Image.open(path) as image:
                self.toolbar_buttons[name] = ctk.CTkImage(
                    # Convert LA files (Save and Load) to RGBA.  This keeps
                    # their transparent areas transparent instead of black.
                    light_image=image.convert("RGBA"),
                    dark_image=image.convert("RGBA"),
                    size=button_sizes[name],
                )

    def create_navbar(self):

        border = ctk.CTkFrame(
            self,
            fg_color="black",
            height=72
        )

        border.place(relx=0, rely=0, relwidth=1)

        navbar = ctk.CTkFrame(
            border,
            fg_color="white",
            height=70
        )

        navbar.place(relx=0, rely=0, relwidth=1)

        center = ctk.CTkFrame(navbar, fg_color="transparent")
        center.place(relx=0.5, rely=0.5, anchor="center")

        logo = tk.Label(
            center,
            image=self.logo,
            bg="white",
            cursor="hand2",
            bd=0
        )

        logo.pack(side="left", padx=(0, 10))

        logo.bind(
            "<Button-1>",
            lambda e: self.show_frame("HomePage")
        )

        title = tk.Label(
            center,
            text="CalciSketch",
            bg="white",
            fg="black",
            font=("Helvetica Neue", 20, "bold")
        )

        title.pack(side="left")

    def show_frame(self, name):

        for frame in self.frames.values():
            frame.place_forget()

        self.frames[name].place(
            relwidth=1,
            relheight=1
        )


class HomePage(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent, fg_color="white")

        self.controller = controller

        self.canvas = Canvas(
            self,
            highlightthickness=0,
            bd=0
        )

        self.canvas.pack(
            fill="both",
            expand=True
        )

        self.canvas.create_image(
            0,
            0,
            image=controller.bg_photo,
            anchor="nw"
        )

        self.canvas.create_text(
            960,
            430,
            text="CalciSketch",
            font=("Helvetica Neue", 48, "bold"),
            fill="black"
        )

        self.canvas.create_text(
            960,
            500,
            text="Draw. Solve. Understand.",
            font=("Helvetica Neue", 24),
            fill="black"
        )

        about_btn = self.canvas.create_image(
            880,
            580,
            image=controller.about_photo
        )

        start_btn = self.canvas.create_image(
            1040,
            580,
            image=controller.start_photo
        )

        self.canvas.tag_bind(
            about_btn,
            "<Button-1>",
            lambda e: controller.show_frame("AboutPage")
        )

        self.canvas.tag_bind(
            start_btn,
            "<Button-1>",
            lambda e: controller.show_frame("DrawingPage")
        )


# ============================================================
# AboutPage
# (Next Part)
# ============================================================

class AboutPage(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent, fg_color="white")

        self.controller = controller
        self.card_images = []

        bg = tk.Label(
            self,
            image=controller.bg_photo,
            bd=0
        )
        bg.place(relwidth=1, relheight=1)

        title = ctk.CTkLabel(
            self,
            text="Meet the Team",
            font=("Helvetica Neue", 36, "bold"),
            text_color="black",
            fg_color="transparent"
        )

        title.place(relx=0.5, y=120, anchor="center")

        members = [

            {
                "image": "amal_Card.png",
                "description":
                    "Expert in model training and execution, ensuring robust machine learning performance.",
                "linkedin":
                    "https://www.linkedin.com/in/raainal/"
            },

            {
                "image": "shib_card.png",
                "description":
                    "Full Stack Developer responsible for backend integration and application architecture.",
                "linkedin":
                    "https://www.linkedin.com/in/shibsobhan-mohanty-53957b252/"
            },

            {
                "image": "dharsh_Card.png",
                "description":
                    "Frontend developer focused on UI/UX and desktop application development.",
                "linkedin":
                    "https://www.linkedin.com/in/dharshini-guruprasath/"
            }

        ]

        card_width = 300
        card_height = 370
        spacing = 120

        total_width = len(members) * card_width + (len(members)-1) * spacing
        start_x = (1920 - total_width) // 2

        y = 250

        for i, member in enumerate(members):

            x = start_x + i * (card_width + spacing)

            self.create_member_card(
                x,
                y,
                card_width,
                card_height,
                member
            )

    def create_member_card(
        self,
        x,
        y,
        width,
        height,
        member
    ):

        frame = ctk.CTkFrame(
            self,
            width=width,
            height=height,
            corner_radius=25,
            fg_color="white",
            border_width=1,
            border_color="#DDDDDD"
        )

        frame.place(x=x, y=y)

        img = Image.open(
            ASSETS_DIR / member["image"]
        ).resize((240, 240))

        photo = ImageTk.PhotoImage(img)

        self.card_images.append(photo)

        image_label = tk.Label(
            frame,
            image=photo,
            bd=0
        )

        image_label.pack(pady=(15, 0))

        desc = ctk.CTkLabel(
            frame,
            text=member["description"],
            width=250,
            wraplength=240,
            justify="center",
            text_color="gray20",
            font=("Helvetica",12)
        )

        desc.pack(pady=(0, 8))

        button = ctk.CTkButton(

            frame,

            text="LinkedIn",

            width=120,

            command=lambda url=member["linkedin"]:
            webbrowser.open(url)

        )

        button.pack(pady=12)

# ============================================================
# DrawingPage
# (Next Part)
# ============================================================

class DrawingPage(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent, fg_color="white")

        self.controller = controller

        self.brush_color = "black"
        self.brush_size = 3
        self.eraser = False

        self.drawing_actions = []
        self.solution_box = None

        self.create_canvas()
        self.create_toolbar()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    # ----------------------------------------------------
    # Canvas
    # ----------------------------------------------------

    def create_canvas(self):

        self.canvas = tk.Canvas(
            self,
            bg="white",
            highlightthickness=0,
            bd=0
        )

        self.canvas.place(
            x=0,
            y=70,
            relwidth=1,
            height=830
        )
        self.canvas.create_image(
            0,
            0,
            image=self.controller.drawing_background,
            anchor="nw",
            tags="background",
        )

    # ----------------------------------------------------
    # Toolbar
    # ----------------------------------------------------

    def create_toolbar(self):

        toolbar = ctk.CTkFrame(
            self,
            fg_color="transparent",
            height=102,
            corner_radius=0
        )
        # Keep a reference so result widgets can never cover the drawing
        # controls.  The result box is created after the toolbar, so without
        # explicitly raising this frame it can sit on top of the buttons.
        self.toolbar = toolbar

        toolbar_background = tk.Label(
            toolbar,
            image=self.controller.toolbar_photo,
            bg="white",
            bd=0,
        )
        toolbar_background.place(relx=0.5, rely=0.5, anchor="center")

        controls = ctk.CTkFrame(toolbar, fg_color="transparent")
        controls.pack(fill="both", expand=True, padx=120)

        toolbar.pack(
            side="bottom",
            fill="x",
            padx=25,
            pady=15
        )

        # ---------------- Colors ----------------

        colors = ["red", "yellow", "green", "blue", "white", "black"]

        for color in colors:

            btn = ctk.CTkButton(
                controls,
                image=self.controller.toolbar_buttons[color],
                width=56,
                height=56,
                text="",
                fg_color="transparent",
                hover_color="#E6E6E6",
                command=lambda c=color:
                self.change_color(c)
            )

            btn.pack(
                side="left",
                padx=6,
                pady=10
            )

        # ---------------- Brush ----------------

        brush_btn = ctk.CTkButton(
            controls,
            image=self.controller.toolbar_buttons["brush"],
            width=56,
            height=56,
            text="",
            fg_color="transparent",
            hover_color="#E6E6E6",
            command=self.use_brush
        )

        brush_btn.pack(
            side="left",
            padx=16
        )

        # ---------------- Eraser ----------------

        eraser_btn = ctk.CTkButton(
            controls,
            image=self.controller.toolbar_buttons["eraser"],
            width=58,
            height=58,
            text="",
            fg_color="transparent",
            hover_color="#E6E6E6",
            command=self.use_eraser
        )

        eraser_btn.pack(
            side="left",
            padx=4
        )

        # ---------------- Slider ----------------

        self.slider = ctk.CTkSlider(
            controls,
            from_=1,
            to=12,
            command=self.change_size,
            width=180
        )

        self.slider.set(3)

        self.slider.pack(
            side="left",
            padx=20
        )

        # ---------------- Clear ----------------

        clear_btn = ctk.CTkButton(
            controls,
            image=self.controller.toolbar_buttons["clear"],
            width=50,
            height=50,
            text="",
            fg_color="transparent",
            hover_color="#E6E6E6",
            command=self.clear_canvas
        )

        clear_btn.pack(
            side="right",
            padx=6
        )

        # ---------------- Save ----------------

        save_btn = ctk.CTkButton(
            controls,
            image=self.controller.toolbar_buttons["save"],
            width=50,
            height=50,
            text="",
            fg_color="transparent",
            hover_color="#E6E6E6",
            command=self.save_work
        )

        save_btn.pack(
            side="right",
            padx=6
        )

        # ---------------- Load ----------------

        load_btn = ctk.CTkButton(
            controls,
            image=self.controller.toolbar_buttons["load"],
            width=50,
            height=50,
            text="",
            fg_color="transparent",
            hover_color="#E6E6E6",
            command=self.load_work
        )

        load_btn.pack(
            side="right",
            padx=6
        )

        # ---------------- Calculate ----------------

        calculate_btn = ctk.CTkButton(
            controls,
            image=self.controller.toolbar_buttons["calculate"],
            width=68,
            height=68,
            text="",
            fg_color="transparent",
            hover_color="#E6E6E6",
            command=self.on_calculate_click
        )

        calculate_btn.pack(
            side="right",
            padx=10
        )

    # ----------------------------------------------------
    # Drawing
    # ----------------------------------------------------

    def paint(self, event):

        x1 = event.x - self.brush_size
        y1 = event.y - self.brush_size
        x2 = event.x + self.brush_size
        y2 = event.y + self.brush_size

        color = "white" if self.eraser else self.brush_color

        self.canvas.create_oval(
            x1,
            y1,
            x2,
            y2,
            fill=color,
            outline=color
        )

        self.drawing_actions.append({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2,
            "color": color,
            "size": self.brush_size
        })

    def reset(self, event):

        pass

    # ----------------------------------------------------
    # Brush
    # ----------------------------------------------------

    def change_color(self, color):

        self.brush_color = color
        self.eraser = False

    def use_brush(self):

        self.eraser = False

    def use_eraser(self):

        self.eraser = True

    def change_size(self, value):

        self.brush_size = int(value)

    # ----------------------------------------------------
    # Canvas Operations
    # ----------------------------------------------------

    def clear_canvas(self):

        self.canvas.delete("all")
        self.canvas.create_image(
            0,
            0,
            image=self.controller.drawing_background,
            anchor="nw",
            tags="background",
        )
        self.drawing_actions.clear()

        if self.solution_box:
            self.solution_box.destroy()
            self.solution_box = None

    # ----------------------------------------------------
    # Backend Hooks
    # ----------------------------------------------------
    def on_calculate_click(self):
        try:
            image_path = capture_canvas(self.canvas)
            response = solve_image(image_path)

            if response["success"]:
                self.display_solution(
                    response["steps"],
                    response["answer"]
                    )
            else:
                messagebox.showerror(
                    "Server Error",
                    response["error"]
                    )
        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
                )

        print("Calculate button clicked.")

    def save_work(self):

        print("Save Drawing")

    def load_work(self):

        print("Load Drawing")

    # ----------------------------------------------------
    # Result Box
    # ----------------------------------------------------

    def display_solution(self, steps, answer):

        if self.solution_box:
            self.solution_box.destroy()

        self.solution_box = ctk.CTkTextbox(
            self,
            width=1750,
            height=170,
            font=("Helvetica",18)
        )

        self.solution_box.place(
            relx=0.5,
            rely=0.68,
            relwidth=0.9,
            anchor="center",
        )

        for step in steps:

            self.solution_box.insert(
                "end",
                step + "\n"
            )

        self.solution_box.insert(
            "end",
            "\nFinal Answer:\n"
        )

        self.solution_box.insert(
            "end",
            answer
        )

        self.solution_box.configure(
            state="disabled"
        )

        # A solution is added after the toolbar and would otherwise be the
        # topmost widget.  Raise the toolbar so Calculate, Clear, and the
        # other controls remain clickable for the next calculation.
        self.toolbar.lift()


if __name__ == "__main__":

    app = CalciSketchApp()
    app.mainloop()
