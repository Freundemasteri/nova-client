import os
import json
import subprocess
import customtkinter as ctk
from tkinter import messagebox

# NOVA BRANDING COLOR PALETTE
DARK_BG = "#0A0A0A"
CARD_BG = "#141414"
NOVA_RED = "#D31212"
NOVA_HOVER = "#960B0B"
TEXT_WHITE = "#FFFFFF"
TEXT_GRAY = "#888888"

# SPRACH-WÖRTERBUCH (Deutsch & Englisch)
TRANSLATIONS = {
    "DE": {
        "title": "Nova Client - Premium Utility",
        "subtitle": "MAXIMALER PERFORMANCE ACCELERATOR",
        "btn_perf": "ULTRA PERFORMANCE AKTIVIEREN",
        "btn_launch": "ROBLOX ÜBER NOVA STARTEN",
        "btn_discord": "STATUS DISCORD SERVER",
        "status_ready": "SYSTEM STATUS: BEREIT ZUM FLIEGEN",
        "status_engaged": "SYSTEM STATUS: ULTRA PERFORMANCE AKTIVIERT",
        "status_roblox": "SYSTEM STATUS: ROBLOX AKTIV",
        "err_roblox": "Roblox nicht gefunden!",
        "success_perf": "Ultra Performance erfolgreich injiziert!",
        "err_launch": "Roblox konnte nicht gestartet werden."
    },
    "EN": {
        "title": "Nova Client - Premium Utility",
        "subtitle": "MAXIMUM PERFORMANCE ACCELERATOR",
        "btn_perf": "ACTIVATE ULTRA PERFORMANCE",
        "btn_launch": "LAUNCH ROBLOX VIA NOVA",
        "btn_discord": "STATUS DISCORD SERVER",
        "status_ready": "SYSTEM STATUS: READY TO FLY",
        "status_engaged": "SYSTEM STATUS: NOVA ULTRA PERFORMANCE ENGAGED",
        "status_roblox": "SYSTEM STATUS: ROBLOX ACTIVE",
        "err_roblox": "Roblox not found!",
        "success_perf": "Ultra Performance successfully injected!",
        "err_launch": "Roblox could not be started."
    }
}

class NovaClientApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.current_lang = "DE" # Standard-Sprache auf Deutsch setzen

        # Fenster-Einstellungen
        self.title("Nova Client")
        self.geometry("580x460")
        self.resizable(False, False)
        self.configure(fg_color=DARK_BG)

        # Haupt-Container
        self.main_frame = ctk.CTkFrame(self, fg_color=CARD_BG, corner_radius=15, border_width=1, border_color="#222222")
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # SPRACH-AUSWAHL DROPDOWN
        self.lang_switch = ctk.CTkOptionMenu(
            self.main_frame,
            values=["DE", "EN"],
            command=self.change_language,
            fg_color="#222222",
            button_color=NOVA_RED,
            button_hover_color=NOVA_HOVER,
            dropdown_fg_color=CARD_BG,
            width=70,
            height=25
        )
        self.lang_switch.place(relx=0.95, rely=0.05, anchor="ne")

        # Titel-Label
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="NOVA CLIENT", 
            font=ctk.CTkFont(family="Impact", size=36, weight="bold"),
            text_color=NOVA_RED
        )
        self.title_label.pack(pady=(25, 2))

        # Untertitel
        self.subtitle_label = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            font=ctk.CTkFont(family="Arial", size=11, weight="bold"),
            text_color=TEXT_GRAY
        )
        self.subtitle_label.pack(pady=(0, 10))

        # Trennlinie
        self.line = ctk.CTkFrame(self.main_frame, height=2, width=420, fg_color="#333333")
        self.line.pack(pady=10)

        # Button 1: Ultra Performance
        self.fps_btn = ctk.CTkButton(
            self.main_frame, text="", command=self.enable_fps_unlocker, 
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            fg_color=NOVA_RED, hover_color=NOVA_HOVER, text_color=TEXT_WHITE,
            corner_radius=8, width=340, height=45
        )
        self.fps_btn.pack(pady=10)

        # Button 2: Roblox starten
        self.start_btn = ctk.CTkButton(
            self.main_frame, text="", command=self.start_roblox, 
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            fg_color="#222222", hover_color="#333333", text_color=TEXT_WHITE,
            border_width=1, border_color=NOVA_RED, corner_radius=8, width=340, height=45
        )
        self.start_btn.pack(pady=10)

        # Button 3: Discord Server (Für Status / Lags)
        self.discord_btn = ctk.CTkButton(
            self.main_frame, text="", command=self.open_discord_server, 
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            fg_color="#18191c", hover_color="#2f3136", text_color=TEXT_WHITE,
            border_width=1, border_color="#5865F2", corner_radius=8, width=340, height=40
        )
        self.discord_btn.pack(pady=10)

        # Status-Anzeige
        self.status_label = ctk.CTkLabel(
            self.main_frame, text="", 
            font=ctk.CTkFont(family="Arial", size=10, weight="bold"),
            text_color=TEXT_GRAY
        )
        self.status_label.pack(side="bottom", pady=15)

        # Texte initialisieren
        self.update_ui_text()

    def change_language(self, choice):
        self.current_lang = choice
        self.update_ui_text()

    def update_ui_text(self):
        lang = TRANSLATIONS[self.current_lang]
        self.title(lang["title"])
        self.subtitle_label.configure(text=lang["subtitle"])
        self.fps_btn.configure(text=lang["btn_perf"])
        self.start_btn.configure(text=lang["btn_launch"])
        self.discord_btn.configure(text=lang["btn_discord"])
        self.status_label.configure(text=lang["status_ready"])

    def open_discord_server(self):
        """Öffnet deinen Discord Server Link im Browser"""
        import webbrowser
        webbrowser.open("https://discord.gg/DEIN_SERVER_LINK")

    def get_roblox_path(self):
        local_app_data = os.getenv('LOCALAPPDATA')
        roblox_versions_path = os.path.join(local_app_data, "Roblox", "Versions")
        if os.path.exists(roblox_versions_path):
            for folder in os.listdir(roblox_versions_path):
                version_path = os.path.join(roblox_versions_path, folder)
                if os.path.isdir(version_path) and "RobloxPlayerBeta.exe" in os.listdir(version_path):
                    return version_path
        return None

    def enable_fps_unlocker(self):
        lang = TRANSLATIONS[self.current_lang]
        roblox_path = self.get_roblox_path()
        if not roblox_path:
            messagebox.showerror("Error", lang["err_roblox"])
            return

        settings_dir = os.path.join(roblox_path, "ClientSettings")
        os.makedirs(settings_dir, exist_ok=True)

        fflags_data = {
            "DFIntTaskSchedulerTargetFps": 9999,
            "FFlagTaskSchedulerLimitTargetFpsToScreenRefreshRate": "False",
            "FFlagDebugGraphicsDisableDirect3D11": "False", 
            "FIntRenderShadowMapBias": 0,                   
            "FFlagFastGPULightCulling3": "True",            
            "FIntFRMMinLevel": 1,                           
            "FFlagPreloadAllTextures": "True",              
            "FIntCSG3WorksetUpdateRate": 60,                
            "FFlagDebugDisablePostFX": "True",              
            "FFlagUserGpuSkinning2": "True"                 
        }

        settings_file = os.path.join(settings_dir, "ClientAppSettings.json")
        try:
            with open(settings_file, "w") as f:
                json.dump(fflags_data, f, indent=4)
            self.status_label.configure(text=lang["status_engaged"], text_color=NOVA_RED)
            messagebox.showinfo("Nova Client", lang["success_perf"])
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def start_roblox(self):
        lang = TRANSLATIONS[self.current_lang]
        roblox_path = self.get_roblox_path()
        if roblox_path:
            executable = os.path.join(roblox_path, "RobloxPlayerBeta.exe")
            subprocess.Popen([executable])
            self.status_label.configure(text=lang["status_roblox"], text_color="#00FF00")
        else:
            messagebox.showerror("Error", lang["err_launch"])

if __name__ == "__main__":
    app = NovaClientApp()
    app.mainloop()