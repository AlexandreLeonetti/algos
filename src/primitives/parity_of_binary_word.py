# compute parity of binary word
# parity is 1 if nuber of 1 is odd
# parity is 0 if number of 1 is even
def parity_O_n(word):
    parity = False
    while word:
        parity=parity ^ (word & 1)
        word >>= 1

    return parity 


a = 0b1010
print(parity_O_n(a))


def parity_O_k(word):

    parity = False
    while word:
        # python does not store leading zeroes explicitly, it stores integers
        # when the value of the integer is equal to zero, the loop stops
        # no need for shifting bits since the int value shrinks
        # in binary representation we just deleting ones right to left
        # in int representation we indeed shrinking number to zero
        print(bin(word))
        parity = parity ^ 1
        word = word & word-1
    return parity

print(parity_O_k(a))


def create_hash_table(n):
    hash = {}
    for i in range(0,n):
        hash[i]=parity_O_k(i)
    return hash

PRECOMPUTED_PARITY = create_hash_table(1<<16) 

def parity(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF  # 16-bit mask (65535 in decimal)

    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])



# Test cases for parity function
test_values = [0b1010, 0b1111, 0b1000000000000001, 0b0, 0b1, 0b1100110011001100]

for val in test_values:
    print(f"Parity of {bin(val)}: {parity(val)}")