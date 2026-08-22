#/bin/python env
# Detect Port Easy
#
# Script by prince
import socket
import re
import concurrent.futures
import subprocess

def ssh_detect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_target = input("[~] Masukkan IP Target : ").strip()
    if not ip_target:
        print("[!] IP tidak Boleh Kosong")
        return

    port_range = input("[~] Masukkan Port Range Cnth:10-30 : ")

    try:
        s.connect(ip,target,port_range)


def main():
    while True:
        print("""
██████╗ ██████╗ ██╗███╗   ██╗ ██████╗███████╗███████╗███████╗ ██████╗
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
██████╔╝██████╔╝██║██╔██╗ ██║██║     █████╗  ███████╗█████╗  ██║     
██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██╔══╝  ╚════██║██╔══╝  ██║     
██║     ██║  ██║██║██║ ╚████║╚██████╗███████╗███████║███████╗╚██████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚══════╝ ╚═════╝
                TOOLS BY PRINCE @nama.disini                                                                     
              """)
        print("[~]PILIHAN OPSI YANG TERSEDIA:\n")
        print("1. SSH DETECTION")
        print("2. ANOTHER TOOLS")
        print("0. EXIT\n")

        pilihan = input("[~]Pilih Opsi Anda [1,2,0]: ") # Menangani Input
        match pilihan:
            case "1":
                ssh_detect()
            case "2":
                another()
            case "0":
                print("\n[~] Terima Kasih Telah menggunakan Tools Ini\n Bantu Support Di @nama.disini")
                break
            case "":
                print("[!]Input Tidak Boleh Kosong!")
            case _:
                print("\n[!] Input Tidak Valid, Ulangi")

        input("\n[~] Tekan Enter Untuk Melanjutkan")
if __name__ == "__main__":
    main()
