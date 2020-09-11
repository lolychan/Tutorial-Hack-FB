import os
os.system("clear")
def banner():
    print("""
    #############
    Turorial 01
    #############
    """)

def main():
    os.system("clear")
    banner()
    print("1.Hack Facebook")
    print("2.Install Bahan")
    print("0.Exit")
    pilih = input("Pilih Nomor: ")
    if pilih == "1":
        os.system("git clone https://github.com/Icam-ULLAS/MBF")
        os.system("cd MBF")
        os.system("python2 MBF.py")
    elif pilih == "2":
        os.system("pip2 install requests")
        os.system("pip2 install mechanize")
    elif pilih == "0":
        exit()

main()
