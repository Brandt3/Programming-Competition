# =============================================================================
# Problem 5 — Secret Message (Vigenère Cipher Decode)
# =============================================================================
#Needs adjustment
def solve_secret():
    keyword = input().strip().lower()
    k = len(keyword)
    n = int(input())

    def decrypt_char(ch, key_char):
        """Reverse Vigenère: find original letter given encrypted letter and key."""
        # Encryption: plain_pos shifted forward by key_offset (mod 26) = cipher
        # Row for key_char 'a'=0 shifts by 1, 'b' shifts by 2, ... 'z' shifts by 0
        # From table: row 1 (key 'a'): a->b, b->c, ..., z->a (shift +1)
        # So cipher = (plain + shift) mod 26 where shift = ord(key_char)-ord('a')+1
        # Decrypt: plain = (cipher - shift) mod 26
        shift = ord(key_char) - ord('a')
        if ch.isupper():
            plain_idx = (ord(ch) - ord('A') - shift) % 26
            return chr(plain_idx + ord('A'))
        else:
            plain_idx = (ord(ch) - ord('a') - shift) % 26
            return chr(plain_idx + ord('a'))

    for _ in range(n):
        line = input()
        result = []
        key_pos = 0  # position in keyword (only advances on letters)
        for ch in line:
            if ch.isalpha():
                key_char = keyword[key_pos % k]
                result.append(decrypt_char(ch, key_char))
                key_pos += 1
            else:
                result.append(ch)
        print(''.join(result))

solve_secret()