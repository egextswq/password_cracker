import itertools
import hashlib

def brute_force_attack():
    target_hash = input("Kırmak istediğin SHA256 hash'i gir: ")
    characters = input("Kullanılacak karakterler (örn: abc123): ")
    max_length = int(input("Maksimum şifre uzunluğu: "))

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_word = ''.join(guess)
            guess_hash = hashlib.sha256(guess_word.encode()).hexdigest()
            if guess_hash == target_hash:
                print(f"[✔] Şifre bulundu: {guess_word}")
                return
    print("[✘] Şifre bulunamadı.")
