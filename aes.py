from rtlsdr import RtlSdr
# chacha20


# 1. State inicialization

def create_matrix(key :bytes, nonce :bytes, count :int) -> List:

    c0 = 0x61707865
    c1 = 0x3320646e
    c2 = 0x79622d32
    c3 = 0x6b206574

    m_list = [c0, c1, c2, c3]

    # TODO: Optimalizuj 
    for i in range(0, len(key), 4):
        skupiny = key[i : i+4]
        prevod_cislo = int.from_bytes(skupiny, "little")
        m_list.append(prevod_cislo)

    m_list.append(count)

    for i in range(0, len(nonce), 4):
        skupiny = nonce[i : i+4]
        prevod_cislo = int.from_bytes( skupiny, "little")
        m_list.append(prevod_cislo)
    
    return m_list

# 2. Quarter round

def uprava_indexu(matice :list, index0 :int, index1 :int, index2 :int, index3 :int):

    # ARX 

    # a = (a + b) % 2^32, d je xor a 
    matice[index0] = (matice[index0] + matice[index1]) & 0xffffffff # uprava prvniho indexu
    matice[index3] = matice[index3] ^ matice[index0] # xor
    matice[index3] = rotl32(matice[index3], 16) # rotace bitů   
    
    # c = (c + b) % 2^32
    matice[index2] = (matice[index2] + matice[index3]) & 0xffffffff
    matice[index1] = matice[index1] ^ matice[index2]
    matice[index1] = rotl32(matice[index1], 12)

    matice[index0] = (matice[index0] + matice[index1]) & 0xffffffff 
    matice[index3] = matice[index3] ^ matice[index0] 
    matice[index3] = rotl32(matice[index3], 8)    
    
    matice[index2] = (matice[index2] + matice[index3]) & 0xffffffff
    matice[index1] = matice[index1] ^ matice[index2]
    matice[index1] = rotl32(matice[index1], 7)

# 3. chacha2 blockn

def chacha(key :bytes, nonce :bytes, count :int):

    matr = create_matrix(klic, nonce, count)
    matr_cp = list(matr)

    for i in range(0, 10):
        for x in range(4):
            # sloupce
            uprava_indexu(matr, x, x+4, x+8, x+12)

            # radky
            uprava_indexu(matr, x, 4+(x+1)%4, 8+(x+2)%4, 12+(x+3)%4)

    # secteni s puvodnimi hodnotami s modulem!

    for i in range(0, len(matr)):
        matr[i] = matr[i] + matr_cp[i] & 0xffffffff

        matr[i].to_bytes(4, "little")

    return matr

# 4. (De)sifrovani

klic = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f'
nonce = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02'

keystream = chacha(klic, nonce, 1)
print(f"Délka keystreamu: {len(keystream)} bajtů")
print(f"Keystream (hex): {keystream.hex()}")

