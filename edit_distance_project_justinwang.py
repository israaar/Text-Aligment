# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 20:58:37 2017

@author: justin
"""

"""
This program compares two text files (names of which provided by the user) and gives the edit distance, or minimum number of operations required to transform one string (from the text file) to another (from the other text file). The program also prints an optimal alignment diagram.

:return: the edit distance and optimal alignment between two strings (text files)
"""
import sys
import numpy as np

f1 = open(sys.argv[1], "r")
f2 = open(sys.argv[2], "r")
#f1 and f2 act as variables to allow the following functions to read text files (names of which are provided by the user)

def matching_or_not(a,b):
    if a==b:
        return 0
    else:
        return 1
#returns a 1 if two given elements are different, returning a 0 if they are the same


#THE MAIN FUNCTION
def optimal_alignment_and_edit_distance():
    
    data_1 = []
    data_2 = []
#creates two lists for two files

    for word in f1:
        for letter in word.replace("\n"," "):
            data_1.append(letter)
#appends each letter (character, including spaces and punctuation) from text files to the respective data lists, replacing line breaks with spaces
        
    for word in f2:
        for letter in word.replace("\n"," "):
            data_2.append(letter)

    
    length_data_1 = len(data_1)
    length_data_2 = len(data_2)
#length_data is the length of each string (text1 or text2)

    matrix = np.zeros(shape=(length_data_2,length_data_1))
#creates a matrix which will fit string length of text1 on y axis and text 2 on x axis

    for column_number in range(0, length_data_1):
        matrix[0, column_number] = column_number
#creates 0,1,2,3,4,5... etc on the first row and first column of matrix - initialization
    for row_number in range(0, length_data_2):
        matrix[row_number, 0] = row_number
        
    for i in range(1, length_data_2):
        for j in range(1, length_data_1):
            option_A = matrix[i - 1, j - 1] + matching_or_not(data_1[j], data_2[i])
            option_B = matrix[i - 1, j] + 1
            option_C = matrix[i, j - 1] + 1
            matrix[i, j] = min(option_A,option_B,option_C)
#dynamic programming algorithim, using recurrence relation above to fill in the matrix

    edit_distance = matrix[length_data_2 - 1, length_data_1 - 1]
#the bottom right corner of the filled-in-corner, or largest corner/furthest from [0,0] contains the value for edit distance


#CONSTRUCTING OPTIMAL ALIGNMENT 
    n = length_data_1 - 1
    m = length_data_2 - 1
#preparing variables for pulling elements from data lists

#start constructing alignment diagram 
    string_1 = ""
    string_2 = ""

#while loop in order to compare matrix values/backtrack to determine optimal operations made - adding either string elements or "-" to each growing alignment string accordingly
    while m >= 0 or n >= 0:
        if matrix[m, n] == (matrix[m, n - 1]) + 1:
            string_1 = data_1[n] + string_1
            string_2 = "-" + string_2
            n -= 1
        elif matrix[m, n] == (matrix[m - 1, n]) + 1:
            string_1 = "-" + string_1
            string_2 = data_2[m] + string_2
            m -= 1
        else:
            string_1 = data_1[n] + string_1
            string_2 = data_2[m] + string_2
            m -= 1
            n -= 1
 
    list_string_1= list(string_1)
    list_string_2= list(string_2)

#create middle line, "filler", to show which characters are same between text1 and text 2 in the alignment diagram
    filler = ""

#fills in the "filler" with "|" when the text1 and text2 match and a space when they don't match
    for i in range(len(string_1)):
        if list_string_1[i] == list_string_2[i]:
            filler += "|"
        else:
            filler += " "
    list_filler = list(filler)

#ensures that only 60 characters are printed on each line (60 from first string - including "-", 60 from filler line, and 60 from second string - inlcuding "-"). More than 60 characters in either text will result in more than one line of each (text1 string, text2 string, filler).    
    first_line = [list_string_1[i:i+60] for i in range(0, len(list_string_1), 60)]
    filler_line = [list_filler[i:i+60] for i in range(0, len(list_filler), 60)]
    second_line = [list_string_2[i:i+60] for i in range(0, len(list_string_2), 60)]

#prints the optimal alignment diagram and edit distance
    print "Optimal Alignment: \n"
    for i in range(len(first_line)):
        print "".join(first_line[i])
        print "".join(filler_line[i])
        print "".join(second_line[i])
    print "\n"
    print "Edit Distance =", edit_distance


optimal_alignment_and_edit_distance()
#runs the above function when program file is called 