import customtkinter as ctk


class MetricCard(ctk.CTkFrame):
    def __init__(self, parent, title):

        super().__init__(
            parent,
            corner_radius=15,
            fg_color="#1E293B"
        )

        self.grid_propagate(False)
        super().__init__(
            parent,
            fg_color="#1E293B",
            corner_radius=15,
            height=170
        )


        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 16, "bold")
        )

        self.value_label = ctk.CTkLabel(
            self,
            text="0%",
            font=("Segoe UI", 28, "bold")
        )

        self.progress = ctk.CTkProgressBar(self)

        self.progress.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.progress.set(0)

        self.title_label.pack(pady=(15, 5))
        self.value_label.pack(pady=(0, 15))

    def update_value(self, value):

        self.value_label.configure(
            text=f"{value:.0f}%"
        )

        self.progress.set(value / 100)

        if value < 50:
            color = "#22C55E"

        elif value < 80:
            color = "#EAB308"

        else:
            color = "#EF4444"

        self.progress.configure(
            progress_color=color
        )