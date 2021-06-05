"""
html convert chinese to english

usage:
arg1: $filein

fileout write with $filein_tmp
"""
import sys
from google_trans_new import google_translator 
import re
import sys 

file=sys.argv[1] # "book.html"
fileout=file + '_tmp' #  "book_trans.html"

translator = google_translator()

f = open(fileout, "w")
line = 1
with open(file) as fp:
    while line:
        line = fp.readline()
        if re.search(u'[\u4e00-\u9fff]', line):
           line1 = line.replace('>','<').replace('"','<').replace('(','<').replace(')','<').replace(':','<').replace('/','<')
           line1 = line1.split('<')
           #line1 = line.split('<','>','"','(',')')
           for item in line1:
               if re.search(u'[\u4e00-\u9fff]', item):
                  print(item)
                  translate_text = translator.translate(item,lang_tgt='en')
                  # if you want to chinese
                  #translate_text = translator.translate(item,lang_tgt='zh-TW')
                  print(translate_text)
                  line = line.replace(u"%s"%item,u"%s"%translate_text)
                  new_or_not = True 
        f.write(line)

f.close()
