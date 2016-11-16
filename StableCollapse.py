#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 17:08:09 2016

@author: Christopher.Rieve
"""


import os
import sys

# TODO: Check if data is already sorted
# TODO: Work with bysort statements
# TODO: Work with gsort statements
# TODO: Add more usage statistics

do_file = sys.argv[1]

# Guardians
if not do_file.endswith('.do'):
    print 'Stable Collapse only works on Stata .do files.'
    sys.exit(0)

if not os.path.isfile(do_file):
    print "File '", do_file, "' does not exist"
    sys.exit(0)


def read_file(filename):
    with open(filename) as f:
        txt = f.readlines()
    return txt


def strip_it(txt):
    new_txt = []
    for t in txt:
        new_t = t.rstrip('\n')
        new_txt.append(new_t)
    return new_txt


def find_stata_command(txt, cmd):
    cmd_lines = []
    for l in txt:
        if cmd in l:
            cmd_lines.append(l)
    return cmd_lines


def find_sort(line_num, cmd):
    if cmd == 'collapse':
        by_start = line_num.find("by")
        end_by = line_num.find(r')', by_start)
        sort_list = line_num[by_start + 3:end_by]
    if cmd == 'sort':
        start = line_num.find(' ')
        sort_list = line_num[start + 1:]
    return sort_list.split()


def sort_stably(sort_order, cmd_line):
    new_sort = "sort " + " ".join(sort_order) + ", stable"
    return (new_sort, cmd_line)


def find_cmd_line(cmd_line, do_c):
    return do_c.index(cmd_line)


def insert_sort(do_c, stable, cmd_line_num, cmd):
    if cmd == "collapse":
        do_c.insert(cmd_line_num, stable[0])
    if cmd == "sort":
        do_c[cmd_line_num] = stable[0]
    return do_c


def create_friends(new_do, cmd_line_num):
    friendly_comment = '* Hey There! Just a friendly reminder to ALWAYS SORT STABLY.'
    new_do.insert(cmd_line_num, friendly_comment)


def write_file(filename, txt):
    with open(filename, 'w') as f:
        for line in txt:
            f.write("%s\n" % line)


def big_league(command, dcont):
    command_lines = find_stata_command(dcont, command)
    for command_line in command_lines:
        sorted_by = find_sort(command_line, command)
        stabalized = sort_stably(sorted_by, command_line)
        command_line_num = find_cmd_line(command_line, dcont)
        dcont = insert_sort(dcont, stabalized, command_line_num, command)
        create_friends(dcont, command_line_num)
    return dcont

# Running
content = read_file(do_file)
content = strip_it(content)
content = big_league("sort", content)
content = big_league("collapse", content)


write_file(do_file, content)

print 'Everything should be stable now'
