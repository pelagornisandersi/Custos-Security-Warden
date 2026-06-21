import customtkinter as ctk


class NetworkPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#1E293B",
            corner_radius=15
        )

        title = ctk.CTkLabel(
            self,
            text="Network Connections",
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
            font=("JetBrains Mono", 13)
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    def update_connections(self, connections):

        self.textbox.delete("1.0", "end")

        self.textbox.insert(
            "end",
            f"{'Process':<15}"
            f"{'PID':<10}"
            f"{'Remote IP':<18}"
            f"{'Port'}\n"
        )

        self.textbox.insert(
            "end",
            "-" * 60 + "\n"
        )

        for conn in connections:

            line = (
                f"{conn['process'][:16]:<18}"
                f"{conn['pid']:<8}"
                f"{conn['remote_ip']:<18}"
                f"{conn['remote_port']}\n"
            )

            self.textbox.insert(
                "end",
                line
            )