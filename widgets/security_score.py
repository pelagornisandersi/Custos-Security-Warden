import customtkinter as ctk


class SecurityScoreCard(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(
            parent,
            corner_radius=15,
            fg_color="#1E293B"
        )

        self.title_label = ctk.CTkLabel(
            self,
            text="Security Score",
            font=("Segoe UI", 20, "bold")
        )

        self.score_label = ctk.CTkLabel(
            self,
            text="100",
            font=("Segoe UI", 40, "bold")
        )

        self.status_label = ctk.CTkLabel(
            self,
            text="Secure",
            font=("Segoe UI", 16)
        )

        self.title_label.pack(pady=(20, 10))
        self.score_label.pack()
        self.status_label.pack(pady=(10, 20))

    def update_score(self, score):

        self.score_label.configure(
            text=f"{score}/100"
        )

        if score >= 80:
            color = "#22C55E"
            status = "Secure"

        elif score >= 50:
            color = "#EAB308"
            status = "Needs Attention"

        else:
            color = "#EF4444"
            status = "High Risk"

        self.score_label.configure(
            text_color=color
        )

        self.status_label.configure(
            text=status,
            text_color=color
        )