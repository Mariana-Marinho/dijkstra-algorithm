import subprocess


def install_dependencies():
    subprocess.run(['pip', 'install', 'tkinter'])
    subprocess.run(['pip', 'install', 'networkx'])
    subprocess.run(['pip', 'install', 'matplotlib.pyplot'])
    subprocess.run(['pip', 'install', 'random'])