import platform
import subprocess

def get_active_window():
    try:
        current_os = platform.system()

        if current_os == "Windows":
            import win32gui
            return win32gui.GetWindowText(win32gui.GetForegroundWindow())

        elif current_os == "Linux":
            result = subprocess.check_output(["xdotool", "getactivewindow", "getwindowname"])
            return result.decode("utf-8").strip()

        else:
            return "Unsupported OS"
    except Exception:
        return "Unknown Window"
