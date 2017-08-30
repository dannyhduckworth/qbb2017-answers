#!/usr/bin/env python

import sys

#Goal: Clean-up the fly data.
#Include Swiss-Prot ID & Flybase AC (Columns 3 & 5)

#USAGE
#cat Raw_Fly_File.txt | ./day2-homework-part1.py 


fh = sys.stdin 

#Make a dict for the desired columns
gene_dict = {} 

#Find all the lines that contain DROME
#If contain "DROME," find the last column and second-to-last column
#Label those columns fb_id and ac. Add to the dictionary.
for line in fh: 
    if "DROME" in line:
        fields = line.rstrip("\r\n").split() 
        
        if len(fields[-1]) == 11 and len(fields[-2]) == 6: #Search for last column, which has 
            fb_id = fields[-1]                              #11 characters. Second-to-last
            ac = fields[-2]                                 #has 6 characters
            gene_dict[fb_id] = ac                          #Write these to fb_id and ac
                
#Write dictionary to file
file_object = open("gene_parsed.txt", "w")

#Write the fb_id and ac separated by a tab and new line
for key, value in gene_dict.items():
    str_out = key + '\t' + value + '\r\n' #Add a tab between and a new line
    file_object.write(str_out)

file_object.close()
      