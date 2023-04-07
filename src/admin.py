import os
import sys
import ctypes

if len(sys.argv) != 2:
    print("Usage: admin.exe <app name>")
    sys.exit()

# Get the application file path
app_name = sys.argv[1]
app_file_path = os.path.abspath(app_name)

# Check if the file exists and if it has the .exe extension
if not os.path.exists(app_file_path) or not app_name.endswith(".exe"):
    print(f"Error: The file '{app_name}' is not a valid .exe file.")
    sys.exit()

# Get the current user token
user_token = ctypes.windll.shell32.IsUserAnAdmin()

# If the user is not an administrator, prompt for administrator privileges
if not user_token:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, app_name, 1)

# Run the application as an administrator
os.startfile(app_file_path, "runas")
