import hashlib

def get_hash(word):
    """Get binary hash of the word (MD5 truncated to 8 bits)."""
    return bin(int(hashlib.md5(word.encode()).hexdigest(), 16))[2:].zfill(128)[:8]  # Use first 8 bits

def simhash(doc):
    """Generate an 8-bit SimHash for the document."""
    words = doc.split()
    vector = [0] * 8  # 8-bit vector
    
    for word in words:
        word_hash = get_hash(word)
        
        # Convert hash into +1/-1 weight vector
        for i, bit in enumerate(word_hash):
            if bit == '1':
                vector[i] += 1
            else:
                vector[i] -= 1
                
    # Generate the final SimHash
    simhash_value = ''.join(['1' if val > 0 else '0' for val in vector])
    return simhash_value

# Example usage
doc1 = "SimHash is a locality-sensitive hashing technique"
doc2 = "Hashing is useful in many document similarity applications"

hash1 = simhash(doc1)
hash2 = simhash(doc2)

print(f"SimHash of Document 1 (8-bit): {hash1}")
print(f"SimHash of Document 2 (8-bit): {hash2}")