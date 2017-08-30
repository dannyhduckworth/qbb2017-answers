#!/usr/bin/env python


#Goal: Find matching gene IDs to the protein AC. 
#Add the protein AC to the data column


import sys

# USAGE
# ./day2-homework-part1.py MAP_FILE C_TAB [DEFAULT]


#Show formatting if wrong usage in command line
if len(sys.argv) < 3:
    print("USAGE: day2-homework-part1.py MAP_FILE C_TAB [DEFAULT]")
    sys.exit(0)
 
#Set command line default/blank prompt   
if len(sys.argv) == 4:
    default = sys.argv[3] #If [DEFAULT] supplied, swap in
else:
    default = None  #Else label as None
    
    
#Open the parsed fly file
map_file = open(sys.argv[1], 'r')


#Make a new dictionary
mapping_dict = {}

#Loop over map_file to extract values
for line in map_file:
    key, value = line.rstrip("\r\n").split('\t') #Strip the return
    mapping_dict[key] = value #Add these values to the keys (ac --> fb_id)
    
#Close map_file
map_file.close()

#Open the c_tab file
c_tab = open(sys.argv[2], 'r')


#Add header to column
#Read first line of c_tab and strip
original_head = c_tab.readline().rstrip("\r\n") #Read first line and strip return
print original_head + "\tAC" #Add AC header to original headers



#Iterate over c_tab and find matching genes 
#Add protein AC to that line
for line in c_tab:
    columns = line.rstrip("\r\n").split('\t') #Split columns
    gene_name_column = columns[8]             #Find gene names
    if gene_name_column in mapping_dict:        #If gene name is in dictionary:
        ac_id = mapping_dict[gene_name_column]  #Add the ac value to it
    elif default is not None:           #Add in default value for no match
        ac_id = default                 
    else:                               #If no default value and no match, skip line
        continue
    columns.append(ac_id)               #Append the ac_id to the list
    print '\t'.join(columns)            #Convert list to string, separated by tabs    
        
#Close c_tab file
c_tab.close()


    


    