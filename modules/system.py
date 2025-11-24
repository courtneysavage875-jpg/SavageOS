import os

def shutdown():
    return "Shutting down system..."

def update_system():
    os.system("pkg update -y && pkg upgrade -y")
    return "System updated."
