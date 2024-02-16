import subprocess
import os

main_script = 'game.py'
resource_folder = 'resources'
config_file = 'config.txt'

# Build the PyInstaller command
pyinstaller_cmd = [
    'pyinstaller',
    '--onefile',
    '--add-data', f'{resource_folder}/;{resource_folder}',
    '--add-data', f'{config_file};.',
    main_script
]

# Run the command
subprocess.run(pyinstaller_cmd)
