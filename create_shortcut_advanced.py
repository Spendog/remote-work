import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def create_shortcut(target_path, shortcut_path, icon_path=None):
    """
    Creates a Windows shortcut using PowerShell.
    """
    script = f'''
    $WshShell = New-Object -comObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
    $Shortcut.TargetPath = "{target_path}"
    $Shortcut.WorkingDirectory = "{os.path.dirname(target_path)}"
    '''
    
    if icon_path and os.path.exists(icon_path):
        script += f'$Shortcut.IconLocation = "{icon_path}"\n'
    
    script += '$Shortcut.Save()'
    
    # Run PowerShell command
    cmd = ["powershell", "-Command", script]
    subprocess.run(cmd, check=True)
    return shortcut_path

def convert_png_to_ico(png_path, ico_path):
    """
    Converts a PNG file to an ICO file using Pillow.
    """
    try:
        img = Image.open(png_path)
        img.save(ico_path, format='ICO', sizes=[(256, 256)])
        return True
    except Exception as e:
        print(f"Error converting image: {e}")
        return False

def select_file():
    root = tk.Tk()
    root.withdraw() # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select PNG Icon",
        filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")]
    )
    return file_path

def main():
    # 1. Setup paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_bat = os.path.join(current_dir, "run.bat")
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    shortcut_name = "Remote Keyboard.lnk"
    shortcut_path = os.path.join(desktop, shortcut_name)
    
    print("--- Remote Keyboard Shortcut Creator ---")
    print("Opening file selector...")

    # 2. Get PNG via GUI
    png_path = select_file()
    
    icon_path = None
    if png_path:
        print(f"Selected Icon: {png_path}")
        icon_name = "custom_icon.ico"
        icon_path = os.path.join(current_dir, icon_name)
        if not convert_png_to_ico(png_path, icon_path):
            print("Warning: Could not convert PNG. Using default icon.")
            icon_path = None
    else:
        print("No icon selected. Using default.")

    # 3. Create Shortcut
    try:
        create_shortcut(target_bat, shortcut_path, icon_path)
        print(f"\n[SUCCESS] Shortcut created on Desktop!")
        print(f"Path: {shortcut_path}")
        
        msg = "Shortcut created on your Desktop!\n\nTo add to Taskbar:\n1. Go to Desktop.\n2. Right-click 'Remote Keyboard'.\n3. Select 'Pin to taskbar'."
        print(f"\n{msg}")
        
        # Show success message box
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Success", msg)
        
    except Exception as e:
        print(f"\n[ERROR] Could not create shortcut: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
