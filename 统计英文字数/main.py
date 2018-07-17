# coding=utf-8
# author:GCS


from word_count import count_word
import add_words as ad


file_name = "test.txt"
count_word(file_name)
ad.add_words(file_name)
count_word(file_name)

file_names = ["test2.txt", "test3.txt"]
for file_name in file_names:
    count_word(file_name)