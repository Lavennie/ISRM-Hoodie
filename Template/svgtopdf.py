import os
import sys
import subprocess
from shutil import which

# check if inkscape command is available
if not which("inkscape"):
    input("\033[31mInkscape command is not available. Install Inkscape and add it to PATH.\033[0m")
    sys.exit(1)
    
# export all .svg files to .pdf
for f in os.listdir():
    if f.endswith(".svg"):
        command = [
            "inkscape",
            f"{f}",
            "--export-area-drawing",
            "--export-type=pdf",
            "--export-filename", 
            f"{f[:-4]}.pdf"
        ]
        print(command)
        try:
            subprocess.run(command, check=True)
            print(f"File successfully exported to \'{f[:-4]}.pdf\'.")
        except subprocess.CalledProcessError as e:
            print(f"\033[31mError during export: {e}.\033[0m")