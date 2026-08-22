#!/usr/bin/env python3
# Detect Port Easy
#
# Script by prince
import socket
import re
import concurrent.futures
import subprocess
import os
import time

#--------------------------------------------------------

def scan_port(target,port):
    s = sambungan()
    connection = s.connect_ex((target, port))
    if connection == 0:
        print(f"[+] Port {port} koneksi terhubung")
        input("Tekan Enter Untuk Melanjutkan")
    else:
        print(f"[-] Port {port} Koneksi Tidak Ada")

    s.close()


#--------------------------------------------------------

def port_single(target):
    while True:
        asc()
        port = input("[~] Masukkan Port Target : ")
        if not port:
            print("[!] IP Tidak Valid")
            input("[~] Tekan Enter Untuk Melanjutkan")
            continue
        port_int = int(port)
        scan_port(target,port_int)

        return

#--------------------------------------------------------

def multi_port(target):
    while True:
        asc()
        print(f"[~] IP Target Terkonfirmasi {target}")
        r_input = input("[~] Masukkan Port Range (example:10-40) : ").strip()

        # Validasi tanda "-"
        if "-" not in r_input:
            print(f"[!] IP Range Salah! Gunakan Format 12-30\n")
            input("Tekan Enter Untuk Melanjutkan")

        try:
            port_awal, port_akhir = r_input.split("-")
            start = int(port_awal)
            end = int(port_akhir)

            if start > end: # Pengecekan Port
                print("[!] Angka Awal Harus Lebih Kecil\n")
                input("Tekan Enter Untuk Melanjutkan")
                continue

            print(f"[*] Memulai Pengecekan Port Pada Target {target} {start} -> {end}...")

            for port in range(start, end + 1):
                scan_port(target, port)
                time.sleep(0.1)

            input("\n[+] Pemindaian Selesai Tekan Enter Untuk Melanjutkan")
            return
            
        except ValueError:
            print("[!] Format Port Harus Berupa Angka")
            input("Tekan Enter Untuk Melanjutkan")
            continue

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
                multi_port(target)
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
