#!/usr/bin/env python3

def word_frequencies(filename):
    
    with open(filename, "r") as f:
        words_freq = {}
        for line in f:
            temp = line.split()
            for word in temp:
                word = clean(word)
                if word in words_freq:
                    words_freq[word] = words_freq[word] + 1
                else:
                    words_freq[word] = 1
        return words_freq
                
    
    
    return {}

def main():
    word_frequencies("src/alice.txt")

def clean(s):
    return s.strip("""!"#$%&'()*,-./:;?@[]_""")

if __name__ == "__main__":
    main()
