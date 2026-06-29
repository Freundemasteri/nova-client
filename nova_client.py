import os
import json
import subprocess
import customtkinter as ctk
from tkinter import messagebox

# NOVA BRANDING COLOR PALETTE (Passend zum Logo)
DARK_BG = "#0A0A0A"       # Tiefschwarz für den Hintergrund
CARD_BG = "#141414"       # Etwas helleres Schwarz für Boxen
NOVA_RED = "#D31212"      # Das aggressive Nova-Rot für Buttons
NOVA_HOVER = "#960B0B"    # Dunkleres Rot für den Hover-Effekt
TEXT_WHITE = "#FFFFFF"    # Reines Weiß für Titel
TEXT_GRAY = "#888888"     # Grau für Untertitel

ctk.set_appearance_mode("Dark") 

class NovaClientApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Fenster-Einstellungen
        self.title("Nova Client - Premium Utility")
        self.geometry("550x400")
        self.resizable(False, False)
        self.configure(fg_color=DARK_BG)

        # Haupt-Container für das moderne "Card"-Design
        self.main_frame = ctk.CTkFrame(self, fg_color=CARD_BG, corner_radius=15, border_width=1, border_color="#222222")
        self.main_frame.pack(pady=25, padx=25, fill="both", expand=True)

        # Titel-Label (Nova Red)
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="NOVA CLIENT", 
            font=ctk.CTkFont(family="Impact", size=36, weight="bold"),
            text_color=NOVA_RED
        )
        self.title_label.pack(pady=(20, 2))

        # Untertitel
        self.subtitle_label = ctk.CTkLabel(
            self.main_frame, 
            text="MAXIMUM PERFORMANCE ACCELERATOR", 
            font=ctk.CTkFont(family="Arial", size=11, weight="bold"),
            text_color=TEXT_GRAY
        )
        self.subtitle_label.pack(pady=(0, 15))

        # Trennlinie mit Glüheffekt-Farbe
        self.line = ctk.CTkFrame(self.main_frame, height=2, width=400, fg_color="#333333")
        self.line.pack(pady=10)

        # Button 1: Ultra Performance (Jetzt in Nova-Rot)
        self.fps_btn = ctk.CTkButton(
            self.main_frame, 
            text="ACTIVATE ULTRA PERFORMANCE", 
            command=self.enable_fps_unlocker, 
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            fg_color=NOVA_RED,
            hover_color=NOVA_HOVER,
            text_color=TEXT_WHITE,
            corner_radius=8,
            width=320, 
            height=45
        )
        self.fps_btn.pack(pady=15)

        # Button 2: Roblox starten (Dezenteres Design, das sich einfügt)
        self.start_btn = ctk.CTkButton(
            self.main_frame, 
            text="LAUNCH ROBLOX VIA NOVA", 
            command=self.start_roblox, 
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            fg_color="#222222", 
            hover_color="#333333",
            text_color=TEXT_WHITE,
            border_width=1,
            border_color=NOVA_RED,
            corner_radius=8,
            width=320, 
            height=45
        )
        self.start_btn.pack(pady=10)

        # Status-Anzeige im edlen Look
        self.status_label = ctk.CTkLabel(
            self.main_frame, 
            text="SYSTEM STATUS: READY TO FLY", 
            font=ctk.CTkFont(family="Arial", size=10, weight="bold"),
            text_color=TEXT_GRAY
        )
        self.status_label.pack(side="bottom", pady=15)

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
        roblox_path = self.get_roblox_path()
        if not roblox_path:
            messagebox.showerror("Fehler", "Roblox nicht gefunden!")
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
            self.status_label.configure(text="SYSTEM STATUS: NOVA ULTRA PERFORMANCE ENGAGED", text_color=NOVA_RED)
            messagebox.showinfo("Nova Client", "Ultra Performance erfolgreich injiziert!")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler: {e}")

    def start_roblox(self):
        roblox_path = self.get_roblox_path()
        if roblox_path:
            executable = os.path.join(roblox_path, "RobloxPlayerBeta.exe")
            subprocess.Popen([executable])
            self.status_label.configure(text="SYSTEM STATUS: ROBLOX ACTIVE", text_color="#00FF00")
        else:
            messagebox.showerror("Fehler", "Roblox konnte nicht gestartet werden.")

if __name__ == "__main__":
    app = NovaClientApp()
    app.mainloop()