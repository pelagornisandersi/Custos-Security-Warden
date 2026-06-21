import customtkinter as ctk


class PortScannerPanel(ctk.CTkFrame):

    def __init__(self, parent, scan_callback):

        super().__init__(
            parent,
            fg_color="#1E293B",
            corner_radius=15
        )

        self.scan_callback = scan_callback


        self.scan_button = ctk.CTkButton(
            self,
            text="Scan Localhost",
            command=self.scan_callback
        )

        self.scan_button.pack(
            pady=(0, 10)
        )



        title = ctk.CTkLabel(
            self,
            text="Port Scanner",
            font=("Segoe UI", 18, "bold")
        )

        title.pack(
            anchor="w",
            padx=15,
            pady=10
        )

        self.textbox = ctk.CTkTextbox(
            self,
            height=120
        )

        self.textbox.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15)
        )

    def update_ports(self, open_ports):

        SERVICES = {
            22: "SSH",
            80: "HTTP",
            443: "HTTPS",
            3306: "MySQL",
            5432: "PostgreSQL",
            8080: "HTTP-Alt"
        }

        self.textbox.delete(
            "1.0",
            "end"
        )

        if not open_ports:

            self.textbox.insert(
                "end",
                "No open ports found\n"
            )

            return

        for port in open_ports:

            service = SERVICES.get(
                port,
                "Unknown"
            )

            self.textbox.insert(
                "end",
                f"{port:<6} {service}\n"
            )