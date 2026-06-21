import customtkinter as ctk
from core.process_risk import get_process_risk

class ProcessPanel(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="#1E293B",
            corner_radius=15
        )

        self.title = ctk.CTkLabel(
            self,
            text="Process Monitor",
            font=("Segoe UI", 18, "bold")
        )

        self.title.pack(
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

        self.textbox.insert(
            "end",
            f"{'Process':<20}"
            f"{'PID':<10}"
            f"{'CPU':<8}"
            f"{'Risk'}\n"
        )

        self.textbox.insert(
            "end",
            "-" * 50 + "\n"
        )

    def update_processes(self, processes):
        print("UPDATE_PROCESSSES CALLED")
        self.textbox.delete(
            "1.0",
            "end"
        )

        self.textbox.insert(
            "end",
            f"{'Process':<20}"
            f"{'PID':<10}"
            f"{'CPU':<10}"
            f"{'Risk'}\n"
        )

        self.textbox.insert(
            "end",
            "-" * 50 + "\n"
        )

        for proc in processes:

            try:

                level, message = get_process_risk(proc)

                line = (
                    f"{proc['name'][:18]:<20}"
                    f"{proc['pid']:<10}"
                    f"{proc['cpu']:>6.1f}%"
                    f"    {level}\n"
                )

                self.textbox.insert(
                    "end",
                    line
                )

            except Exception as e:

                print("PROCESS PANEL ERROR:")
                print(e)