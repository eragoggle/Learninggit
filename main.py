# DSC 510
# Week 9
# Programming Assignment Week 9
# Author Era Ebhodaghe
# Date: 31-Oct-2021

# The purpose of this program is to count the number of words in the gettysburg text file
# Each word will be displayed in a table with the respective count in descending order to a new text file as opposed to the screen
# The program will prompt the user for the name of the text file

import string  # importing string library to remove punctuation


# function to process line
def process_line(line, word_dict):
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    word = line.split()
    add_word(word, word_dict)


# function to add words to the dictionary
def add_word(words, word_dict):
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1


# function to process file and write to the file
def process_file(word_dict, new_file):
    with open(new_file, 'w') as text_file:
        text_file.write(f'Length of the dictionary: {len(word_dict)} words\n'
                        f"{'Word':20}{'Count'}\n"
                        f"{'':-<26}\n")
        for key, value in sorted(word_dict.items(), key=lambda item: item[1], reverse=True):
            text_file.write(f"{key:20}{value}\n")


# main program
def main():
    word_dict = {}
    with open('gettysburg.txt', 'r') as text_file:
        for line in text_file:
            process_line(line, word_dict)
    new_file = str(input('Please enter the new text file name: ')).rstrip()
    if new_file.endswith('.txt'):  # error handling to make sure the file is created as a text file
        new_file = new_file
    else:
        new_file = new_file + '.txt'
    process_file(word_dict, new_file)
    print(f"The new file '{new_file}' has been created ")


if __name__ == '__main__':
    main()
