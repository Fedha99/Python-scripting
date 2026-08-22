#!/usr/bin/env python3
# Detect Port Easy
#
# Script by prince
import socket
import re
import concurrent.futures
import subprocess
import os

#--------------------------------------------------------

def port_single(target):
    while True:
        asc()
        port = input("[~] Masukkan Port Target : ")

        if not port:
            print("[!] IP Tidak Valid")
            input("[~] Tekan Enter Untuk Melanjutkan")
            continue
        print(target, port)
        input("[~] Ketik Enter Untuk Selesaikan Pengecekan")
        return port

#--------------------------------------------------------

def multi_port():
    print("Multi Port")
    input("Checklist Selesai")

#--------------------------------------------------------

def port_range():
    print("port range")
    input("Checklist Selesai")

#--------------------------------------------------------

def sambungan(): # Fungsi Socket agar bisa di reuse
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    return s

#--------------------------------------------------------

def input_user():
    while True:
        target = input("[~] Masukkan IP Target : ")

        if not target:
            print("[!] IP Tidak Valid")
            continue
        return target

#--------------------------------------------------------

def ssh_detect():
    target = input_user()
    while True:
        asc()
        print("\n[1] Single Port")
        print("[2] Multi Port")
        print("[3] Port Range")
        print("[0] Kembali Ke Menu utama\n")
        port_choice = input("[~] Pilih Opsi Port Scanning : ")

        match port_choice:
            case "1":
                port_single(target)
            case "2":
                multi_port()
            case "3":
                port_range()
            case "0":
                print("[~]Kembali Ke Menu")
                return
            case "":
                print("[!] Pilihan Tidak Boleh Kosong")
                input("[~] Tekan Enter Untuk Melanjutkan..")
                continue


#--------------------------------------------------------

def another():
    print("Fitur Dalam Pengembangan")

#--------------------------------------------------------

def asc():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
██████╗ ██████╗ ██╗███╗   ██╗ ██████╗███████╗███████╗███████╗ ██████╗
██╔══██╗██╔══██╗██║████╗  ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
██████╔╝██████╔╝██║██╔██╗ ██║██║     █████╗  ███████╗█████╗  ██║     
██╔═══╝ ██╔══██╗██║██║╚██╗██║██║     ██╔══╝  ╚════██║██╔══╝  ██║     
██║     ██║  ██║██║██║ ╚████║╚██████╗███████╗███████║███████╗╚██████╗
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚══════╝╚══════╝ ╚═════╝
                Tools By Prince @nama.disini
          """)

#--------------------------------------------------------

def main():
    while True:
        asc()
        print("[~]PILIHAN OPSI YANG TERSEDIA:\n")
        print("[1] SSH DETECTION")
        print("[2] ANOTHER TOOLS")
        print("[0] EXIT\n")

        pilihan = input("[~] Pilih Opsi Anda [1,2,0]: ") # Menangani Input
        match pilihan:
            case "1":
                ssh_detect()
            case "2":
                another()
            case "0":
                print("\n[~] Terima Kasih Telah menggunakan Tools Ini\n Bantu Support Di @nama.disini")
                break
            case "":
                print("[!] Input Tidak Boleh Kosong!")
            case _:
                print("\n[!] Input Tidak Valid, Ulangi")

        input("\n[~] Tekan Enter Untuk Melanjutkan")
        
if __name__ == "__main__":
#--------------------------------------------------------
    main()
