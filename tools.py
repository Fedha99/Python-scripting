#/bin/python env
# Detect Port Easy
#
# Script by prince
import socket
import re
import concurrent.futures
import subprocess

def another():
    print("Another")
    pass

def ssh_detect(): # Fungsi SSH Detect
    ip = input("Masukkan IP Target : ")
    target_port = input("Masukkan Range Port example:1-10 : ")
    split_port = target_port.split("-") # Pemberi target dari IP range
    port_awal = int(split_port[0])
    port_akhir = int(split_port[1])
    print(f"Confirmed Port Awal {port_awal}, Dan Port Akhir {port_akhir}")
    for port in range(port_awal,port_akhir + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket AF_INET untuk IP ADDRESS dan SOCK_STREAM Di butuhkan untuk koneksi TCP 
        s.settimeout(1.0) # Session Timeout 

        try: # Looping per port
            s.connect((ip,port))



def main(): # Fungsi Main
    print("""
██████╗ ██████╗ ██╗███╗   ██╗ ██████╗███████╗███████╗███████╗ ██████╗
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
██████╔╝██████╔╝██║██╔██╗ ██║██║     █████╗  ███████╗█████╗  ██║     
██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██╔══╝  ╚════██║██╔══╝  ██║     
██║     ██║  ██║██║██║ ╚████║╚██████╗███████╗███████║███████╗╚██████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚══════╝ ╚═════╝
                TOOLS BY PRINCE                                                                     
          """)
    print("OPSI TOOLS YANG TERSEDIA\n")
    print("1.SSH DETECTION\n")
    choice = input("Pilih Opsi Yang Tersedia : ")
    if choice == "1":
        ssh_detect()
    elif choice == "2":
        another()
    else:
        return 0

main()
