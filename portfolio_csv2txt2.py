#!/usr/bin/python
# Usage: portfolio_csv2txt.py -i Portfolio.csv -o Portfolio.yml
# This prints out a yaml format data file (without the ---) to be included in front-matter of a .md file.
# The input file to process defaults to "Porfolio.csv" if not specified in the argument calling this program.
# The output is to STDOUT if an -o (output file) is not specified.
# The output rewrites any existing file of the same name.


# Get argument list using sys module:
import sys, getopt
def program(*args):
    # do whatever
    pass
# Provide default file_in name argument if not provided:
if __name__ == "__main__":
#def main(argv):
   try:
      arg1 = sys.argv[1]
      file_in = sys.argv[1]
   except IndexError: # getopt.GetoptError:
      # print "Usage: " + sys.argv[0] + ' -i <inputfile> -o <outputfile>'
      # sys.exit(2)
      file_in = 'Portfolio.csv'

# Provide default file_out name argument if not provided:
if __name__ == "__main__":
#def main(argv):
   try:
      arg1 = sys.argv[2]
      file_out = sys.argv[2]
   except IndexError: # getopt.GetoptError:
      file_out = file_in + '.txt'
# Send STDOUT to a file:
sys.stdout=open( file_out,"w")


# Print in yml format:
import csv
# 'rU' means open in universal-newline mode needed on Macs:
#with open('./Portfolio.csv', 'rU') as f:
with open(file_in, 'rU') as f:
    reader = csv.reader(f, delimiter=',')
    first_line = f.readline() # pull out first line - do not print 
    for i in reader:
        # print row
         print \
         '  - '+'image_file: '+i[7] + \
         '\n    thumb_file: '+i[12] + \
         '\n    thumb_width: '+i[13] + \
         '\n    thumb_height: '+i[14] + \
         '\n    title: '+i[1] + \
         '\n    year: '+i[2] + \
         '\n    media_type: '+i[3] + \
         '\n    media_width: '+i[4] + \
         '\n    media_height: '+i[5] + \
         '\n    status: '+i[6] + \
         '\n    notes: '+i[16] + \
         '\n    tags: '+i[17] 
    for i in reader:
        print '# allrowcount='+ str( sum(1 for _ in f) )

# Close the file every time:
sys.stdout.close()
