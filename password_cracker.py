import hashlib
import time

target_hash = input("Enter MD5 hash: ").strip()

if not target_hash:
    print("❌ No hash entered.")
    exit()

print("\n🔐 Starting Password Cracking...\n")

start_time = time.time()
found = False

# Count total lines (for progress %)
with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as f:
    total = sum(1 for _ in f)

with open("wordlist.txt", "r", encoding="utf-8", errors="ignore") as file:
    for i, line in enumerate(file, start=1):
        word = line.strip()
        hash_word = hashlib.md5(word.encode()).hexdigest()

        # Progress %
        percent = (i / total) * 100

        # Speed calculation
        elapsed = time.time() - start_time
        speed = i / elapsed if elapsed > 0 else 0

        if i % 100 == 0:
            print(f"[{percent:.2f}%] Speed: {speed:.2f} w/s")

        if hash_word == target_hash:
            print(f"\n✅ Password Found: {word}")
            found = True
            break

if not found:
    print("\n❌ Password not found in wordlist.")

end_time = time.time()
print(f"\n⏱️ Time taken: {end_time - start_time:.2f} seconds")
