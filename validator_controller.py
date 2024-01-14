import tkinter as tk
from tkinter import font
from subprocess import Popen
import os

# Define the groups of clients
ec_group = ("geth", "besu", "nethermind")
cc_group = ("teku", "nimbus", "prysm", "lighthouse")

# Define a variable to store data
saved_data = []

def start_clients():
    execution_client = execution_update_var.get()
    consensus_client = consensus_update_var.get()
    mevboost_option = mevboost_var.get()

    # Start the selected execution client
    if execution_client in ec_group:
        print(f"Starting {execution_client}...")
        Popen(['sudo', 'systemctl', 'start', execution_client])

    # Start the selected consensus client
    if consensus_client == "prysm":
        Popen(['sudo', 'systemctl', 'start', 'prysmbeacon'])
        Popen(['sudo', 'systemctl', 'start', 'prysmvalidator'])
    elif consensus_client == "lighthouse":
        Popen(['sudo', 'systemctl', 'start', 'lighthousebeacon'])
        Popen(['sudo', 'systemctl', 'start', 'lighthousevalidator'])
    elif consensus_client in cc_group:
        Popen(['sudo', 'systemctl', 'start', consensus_client])

    # Start MEV-Boost if selected
    if mevboost_option == "On":
        print("Starting MEV-Boost...")
        Popen(['sudo', 'systemctl', 'start', 'mevboost'])

def stop_clients():
    # Stop all execution clients
    for client in ec_group:
        print(f"Stopping {client}...")
        Popen(['sudo', 'systemctl', 'stop', client])

    # Stop all consensus clients
    for client in cc_group:
        if client == "prysm":
            Popen(['sudo', 'systemctl', 'stop', 'prysmbeacon'])
            Popen(['sudo', 'systemctl', 'stop', 'prysmvalidator'])
        elif client == "lighthouse":
            Popen(['sudo', 'systemctl', 'stop', 'lighthousebeacon'])
            Popen(['sudo', 'systemctl', 'stop', 'lighthousevalidator'])
        else:
            Popen(['sudo', 'systemctl', 'stop', client])

    # Always stop MEV-Boost
    print("Stopping MEV-Boost...")
    Popen(['sudo', 'systemctl', 'stop', 'mevboost'])

def show_journals():
    execution_client = execution_update_var.get()
    consensus_client = consensus_update_var.get()
    mevboost_option = mevboost_var.get()

    if execution_client in ec_group:
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', execution_client])

    if consensus_client == "prysm":
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', 'prysmbeacon'])
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', 'prysmvalidator'])
    elif consensus_client == "lighthouse":
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', 'lighthousebeacon'])
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', 'lighthousevalidator'])
    elif consensus_client in cc_group:
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', consensus_client])

    # Show MEV-Boost logs if it was on
    if mevboost_option == "On":
        Popen(['gnome-terminal', '--', 'journalctl', '-fu', 'mevboost'])

def service_file_exists(service_name):
    return os.path.exists(f"/etc/systemd/system/{service_name}.service")

def edit_service_file():
    execution_client = execution_update_var.get()
    consensus_client = consensus_update_var.get()

    if execution_client in ec_group and service_file_exists(execution_client):
        Popen(['gnome-terminal', '--', 'sudo', 'nano', f"/etc/systemd/system/{execution_client}.service"])

    if consensus_client in cc_group:
        if consensus_client == "prysm" and service_file_exists('prysmbeacon'):
            Popen(['gnome-terminal', '--', 'sudo', 'nano', '/etc/systemd/system/prysmbeacon.service'])
            if service_file_exists('prysmvalidator'):
                Popen(['gnome-terminal', '--', 'sudo', 'nano', '/etc/systemd/system/prysmvalidator.service'])
        elif consensus_client == "lighthouse" and service_file_exists('lighthousebeacon'):
            Popen(['gnome-terminal', '--', 'sudo', 'nano', '/etc/systemd/system/lighthousebeacon.service'])
            if service_file_exists('lighthousevalidator'):
                Popen(['gnome-terminal', '--', 'sudo', 'nano', '/etc/systemd/system/lighthousevalidator.service'])
        elif service_file_exists(consensus_client):
            Popen(['gnome-terminal', '--', 'sudo', 'nano', f"/etc/systemd/system/{consensus_client}.service"])

    # For MEV-Boost
    mevboost_option = mevboost_var.get()
    if mevboost_option == "On" and service_file_exists('mevboost'):
        Popen(['gnome-terminal', '--', 'sudo', 'nano', '/etc/systemd/system/mevboost.service'])

# Initialize Tkinter root
root = tk.Tk()
root.title("Validator Controller")
root.configure(background="#282C34")
root.geometry("1600x800")

execution_update_var = tk.StringVar()
consensus_update_var = tk.StringVar()
mevboost_var = tk.StringVar()

label_font = font.nametofont("TkDefaultFont").copy()
label_font.config(size=20)

# Dropdown for Execution Client
execution_update_label = tk.Label(root, text="Execution Client:", bg="#282C34", fg="#ABB2BF", font=label_font, anchor='e')
execution_update_label.grid(column=0, row=0, padx=30, pady=15, sticky='e')
execution_update_menu = tk.OptionMenu(root, execution_update_var, *ec_group)
execution_update_menu.config(bg="#2196F3", fg="#FFFFFF", activebackground="#64B5F6", activeforeground="#FFFFFF", font=label_font, takefocus=True)
execution_update_menu["menu"].config(bg="#2196F3", fg="#FFFFFF", activebackground="#64B5F6", activeforeground="#FFFFFF", font=label_font)
execution_update_menu.grid(column=1, row=0, padx=30, pady=15, ipadx=40, ipady=10)

# Dropdown for Consensus Client
consensus_update_label = tk.Label(root, text="Consensus Client:", bg="#282C34", fg="#ABB2BF", font=label_font, anchor='e')
consensus_update_label.grid(column=0, row=1, padx=30, pady=15, sticky='e')
consensus_update_menu = tk.OptionMenu(root, consensus_update_var, *cc_group)
consensus_update_menu.config(bg="#FF9800", fg="#FFFFFF", activebackground="#FFA726", activeforeground="#FFFFFF", font=label_font, takefocus=True)
consensus_update_menu["menu"].config(bg="#FF9800", fg="#FFFFFF", activebackground="#FFA726", activeforeground="#FFFFFF", font=label_font)
consensus_update_menu.grid(column=1, row=1, padx=30, pady=15, ipadx=40, ipady=10)

# Dropdown for MEV-Boost On/Off
mevboost_label = tk.Label(root, text="MEV-Boost On/Off:", bg="#282C34", fg="#ABB2BF", font=label_font, anchor='e')
mevboost_label.grid(column=0, row=2, padx=30, pady=15, sticky='e')
mevboost_options = ('On', 'Off')
mevboost_menu = tk.OptionMenu(root, mevboost_var, *mevboost_options)
mevboost_menu.config(bg="#4CAF50", fg="#FFFFFF", activebackground="#8BC34A", activeforeground="#FFFFFF", font=label_font, takefocus=True)
mevboost_menu["menu"].config(bg="#4CAF50", fg="#FFFFFF", activebackground="#8BC34A", activeforeground="#FFFFFF", font=label_font)
mevboost_menu.grid(column=1, row=2, padx=30, pady=15, ipadx=40, ipady=10)

# Start, Stop, Journals, and Service Files buttons
start_button = tk.Button(root, text="Start", command=start_clients, bg="#282C34", fg="#FFFFFF", activebackground="#28A745", activeforeground="#FFFFFF", font=label_font, takefocus=True)
start_button.grid(column=0, row=3, padx=30, pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_clients, bg="#282C34", fg="#FFFFFF", activebackground="#DC3545", activeforeground="#FFFFFF", font=label_font, takefocus=True)
stop_button.grid(column=1, row=3, padx=30, pady=10)

journals_button = tk.Button(root, text="Journals", command=show_journals, bg="#6C757D", fg="#FFFFFF", activebackground="#5A6268", activeforeground="#FFFFFF", font=label_font, takefocus=True)
journals_button.grid(column=0, row=4, padx=30, pady=20)

service_files_button = tk.Button(root, text="Service Files", command=edit_service_file, bg="#6C757D", fg="#FFFFFF", activebackground="#5A6268", activeforeground="#FFFFFF", font=label_font, takefocus=True)
service_files_button.grid(column=1, row=4, padx=30, pady=20)

root.mainloop()

