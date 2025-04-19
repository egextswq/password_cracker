import hashlib

def crack_hash(hash_value, hash_type, wordlist_path="wordlist.txt"):
    with open(wordlist_path, 'r') as file:
        for word in file:
            word = word.strip()
            if hash_type == 'md5':
                hashed = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == 'sha1':
                hashed = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == 'sha256':
                hashed = hashlib.sha256(word.encode()).hexdigest()
            else:
                print("Desteklenmeyen hash türü.")
                return

            if hashed == hash_value:
                print(f"[✔] Şifre bulundu: {word}")
                return
    print("[✘] Şifre bulunamadı.")

def hash_cracker_menu():
    print("\n🔑 Hash Kırıcı")
    hash_value = input("Hash'i girin: ")
    print("Hash türünü seçin: md5, sha1, sha256")
    hash_type = input("Hash türü: ").lower()
    crack_hash(hash_value, hash_type)
