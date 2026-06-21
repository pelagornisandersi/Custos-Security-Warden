import customtkinter as ctk
from datetime import datetime

class AlertPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#1E293B",
            corner_radius=15
        )

        title = ctk.CTkLabel(
            self,
            text="Security Alerts",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=10
        )

        self.textbox = ctk.CTkTextbox(
            self,
            height=120,
            font=("Cascadia Code", 12)
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    def add_alert(self, level, message):

        timestamp = datetime.now().strftime(
            "%H:%M:%S"
        )

        self.textbox.insert(
            "1.0",
            f"[{timestamp}] [{level}] {message}\n"
        )