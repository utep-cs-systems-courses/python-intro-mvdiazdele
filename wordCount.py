#! /usr/bin/env python3

import sys
import os



def count(inputFile, outputFile):

    word_dict = dict()

    text = os.open(inputFile, os.O_RDONLY) #Open input file for reading only

    while text:
        line = os.read(text, 4096)
        if not line:
            break
        line = line.decode("utf-8").strip().lower()
        line = line.split()
        for word in line:
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1

    os.close(text)
    output = os.open(outputFile, os.O_RDWR | os.O_CREAT | os.O_TRUNC)

    sortedKeys = sorted(word_dict.keys())
    print(sortedKeys)
    for key in sortedKeys:
        value = word_dict[key]
        lineW = f"{key} {value}\n"
        os.write(output, lineW.encode())

    os.close(output)



count(sys.argv[1], sys.argv[2])


