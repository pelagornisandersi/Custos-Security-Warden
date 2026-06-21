import customtkinter as ctk
import json
from widgets.security_score import SecurityScoreCard
from core.core_security_score import calculate_score
from core.monitor import (
    get_cpu_usage,
    get_ram_usage,
    get_disk_usage
)
from widgets.process_panel import ProcessPanel
from core.process_monitor import get_top_processes
from widgets.alert_panel import AlertPanel
from widgets.metric_card import MetricCard
from core.alerts import (
    raise_alert,
    clear_alert
)
from core.file_monitor import (
    build_baseline,
    check_changes
)
from tkinter import filedialog
from widgets.port_scanner_panel import PortScannerPanel
from core.port_scanner import scan_ports
from core.process_risk import get_process_risk
from core.network_monitor import get_connections
from widgets.network_panel import NetworkPanel


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


cpu = get_cpu_usage()
ram = get_ram_usage()
disk = get_disk_usage()


class SecurityDashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        try:

            with open("config.json") as f:

                config = json.load(f)

                self.watch_folder = config.get(
                    "watch_folder"
                )

        except:

            self.watch_folder = None

        
        

        self.title("Custos-Security Warden")
        self.geometry("1920x1080")

        self.configure(
            fg_color="#0F172A"
        )

        self.build_ui()

        self.watch_folder = None
        self.fim_baseline = {}

        self.update_metrics()

        open_ports = scan_ports(
            "127.0.0.1",
            [22, 80, 443, 3306, 8080]
        )

        self.port_panel.update_ports(
            open_ports
        )

    def scan_localhost(self):

            ports = [
                22,
                80,
                443,
                3306,
                5432,
                8080
            ]

            open_ports = scan_ports(
                "127.0.0.1",
                ports
            )

            self.port_panel.update_ports(
                open_ports
            )

            self.alert_panel.add_alert(
                "INFO",
                "Port scan completed"
            )

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.watch_folder = folder

            self.fim_baseline = build_baseline(
                folder
            )

            with open("config.json", "w") as f:

                json.dump(
                    {
                        "watch_folder": folder
                    },
                    f,
                    indent=4
                )

            self.alert_panel.add_alert(
                "INFO",
                f"Monitoring: {folder}"
            )

    def build_ui(self):


        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )



        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.port_panel = PortScannerPanel(
            self.main_frame,
            self.scan_localhost
        )

        self.port_panel.grid(
            row=4,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        for i in range(3):
            self.main_frame.grid_columnconfigure(
                i,
                weight=1
            )

        for i in range(6):
            self.main_frame.grid_rowconfigure(
                i,
                weight=1
            )

        header = ctk.CTkLabel(
            self.main_frame,
            text="Custos-Security Warden",
            font=("DM Sans", 30, "bold")
        )

        header.grid(
            row=0,
            column=0,
            columnspan=3,
            pady=(0, 20)
        )

        self.folder_button = ctk.CTkButton(
            self.main_frame,
            text="Select Folder",
            command=self.select_folder
        )

        self.folder_button.grid(
            row=4,
            column=0,
            columnspan=3,
            pady=10
        )

        card_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        
        self.cpu_card = MetricCard(
            self.main_frame,
            "CPU Usage"
        )

        self.cpu_card.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )


        self.ram_card = MetricCard(
            self.main_frame,
            "RAM Usage"
        )

        self.ram_card.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.disk_card = MetricCard(
            self.main_frame,
            "Disk Usage"
        )

        self.disk_card.grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.score_card = SecurityScoreCard(self.main_frame)

        self.score_card.grid(
            row=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.process_panel = ProcessPanel(self.main_frame)

        self.process_panel.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.alert_panel = AlertPanel(
            self.main_frame
        )

        self.network_panel = NetworkPanel(
           self.main_frame
        )

        self.network_panel.grid(
            row=5,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        self.alert_panel.grid(
            row=3,
            column=2,
            padx=10,
            pady=10,
            sticky="nsew"
        )

    def update_metrics(self):


        if self.watch_folder:

            alerts, self.fim_baseline = check_changes(
                self.watch_folder,
                self.fim_baseline
            )

            for level, message in alerts:

                alert_id = f"fim_{message}"

                if raise_alert(alert_id):

                    self.alert_panel.add_alert(
                        level,
                        message
                    )

        self.cpu_card.update_value(
            get_cpu_usage()
        )

        self.ram_card.update_value(
            get_ram_usage()
        )

        self.disk_card.update_value(
            get_disk_usage()
        )

        self.after(
            1000,
            self.update_metrics
        )

        alerts, self.fim_baseline = check_changes(
            "testfolder",
            self.fim_baseline
        )

        for level, message in alerts:

            self.alert_panel.add_alert(
                level,
                message
            )

        if cpu > 90:
            self.alert_panel.add_alert(
                "WARNING",
                f"High CPU Usage ({cpu:.0f}%)"
            )

        if ram > 90:
            self.alert_panel.add_alert(
                "WARNING",
                f"High RAM Usage ({ram:.0f}%)"
            )

        if cpu > 90:

            if raise_alert("cpu_high"):

                self.alert_panel.add_alert(
                    "WARNING",
                    f"High CPU Usage ({cpu:.0f}%)"
                )

        else:

            clear_alert("cpu_high")


        if ram > 90:

            if raise_alert("ram_high"):

                self.alert_panel.add_alert(
                    "WARNING",
                    f"High RAM Usage ({ram:.0f}%)"
                )

        else:

            clear_alert("ram_high")    

        if disk > 90:

            if raise_alert("disk_critical"):

                self.alert_panel.add_alert(
                    "HIGH",
                    f"Disk Usage Critical ({disk:.0f}%)"
                )

        else:

            clear_alert("disk_critical")
        
        for level, message in alerts:

            alert_id = f"fim_{message}"

            if raise_alert(alert_id):

                self.alert_panel.add_alert(
                    level,
                    message
                )

        score = calculate_score()

        self.score_card.update_score(score)

        processes = get_top_processes()

        for proc in processes:

            level, message = get_process_risk(proc)

            if level:

                alert_id = f"proc_{message}"

                if raise_alert(alert_id):

                    self.alert_panel.add_alert(
                        level,
                        message
                    )

        print("PROCESSES:", processes)

        self.process_panel.update_processes(
            processes
        )

        connections = get_connections()

        print("CONNECTIONS:", len(connections))

        self.network_panel.update_connections(
            connections
        )


if __name__ == "__main__":
    app = SecurityDashboard()
    app.mainloop()