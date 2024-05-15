import subprocess

def run_app():
    command = ["streamlit", "run", "configurator/app.py"]
    subprocess.run(command)