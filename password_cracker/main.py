from hash_cracker import hash_cracker_menu
from brute_force import brute_force_attack

def main():
    while True:
        print("\n🔐 Şifre Kırıcı Sistemi")
        print("1. Hash Kırıcı (MD5, SHA1, SHA256)")
        print("2. Brute Force")
        print("3. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            hash_cracker_menu()
        elif choice == '2':
            brute_force_attack()
        elif choice == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
