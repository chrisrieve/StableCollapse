#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:08:09 2016

@author: Christopher.Rieve
"""


import os
import sys

# TODO: Create command line interface
# TODO: Accept commandline argument to start program
# TODO: Create guardian statements 


#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)

os.chdir(r'C:\Users\christopher.rieve\Personal\Projects\StableCollapse')


# Read function in file function
def read_file(filename):
    with open(filename) as f:
        txt = f.readlines()
    return txt

# Remove '\n's from read in text
def strip_it(txt):
    new_txt = []
    for t in txt:
        new_t = t.rstrip('\n')
        new_txt.append(new_t)
    return new_txt
    
# Find Stata command
def find_stata_command(txt, cmd):
    cmd_lines = []
    for l in txt:
        if cmd in l:
            cmd_lines.append(l)
    return cmd_lines



# Find what was sorted by
def find_sort(collapse_line):
    by_start = collapse_line.find("by")
    end_by = collapse_line.find( r')', by_start)
    sort_list  =  collapse_line[by_start + 3:end_by]
    return sort_list.split()
    
# Add Stable sort
def sort_stably(sorted_by, cmd_line):
    new_sort = "sort " + " ".join(sorted_by) + ", stable"
    return (new_sort, cmd_line)
    
    

# Find original collapsed line in do file 
def find_cmd_line(cmd_line, do_c):
    return do_c.index(cmd_line)

# Insert sorted line
def insert_sort(do_c, stabalized, cmd_line_num):
    do_c.insert(cmd_line_num, stabalized[0])

# Leave a friendly comment
def create_friends(new_do, cmd_line_num):
    friendly_comment = '* Hey There! Just a friendly reminder to ALWAYS SORT STABLY.'
    new_do.insert(cmd_line_num, friendly_comment)

# Write out to file
def write_file(filename, txt):
    with open(filename, 'w') as f:
        for line in txt:
            f.write("%s\n" % line)

# Running
filename = 'Test do file.do'
outfile = 'Test do file - stabalized.do'
content = read_file(filename)
content = strip_it(content)
collapse_lines = find_stata_command(content, "collapse")
collapse_line = collapse_lines[0]
sorted_by = find_sort(collapse_line)
stabalized = sort_stably(sorted_by, collapse_line)
collapse_line_num = find_cmd_line(collapse_line, content)
insert_sort(content, stabalized, collapse_line_num)
create_friends(content, collapse_line_num)
write_file(outfile, content)


















