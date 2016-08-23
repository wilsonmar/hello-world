#!/usr/bin/python
# This prints out a file (without the ---) to be included in front-matter yml of a .md file.
# as the "Parser" described in https://wilsonmar.github.io/jam-website-project-plan/
# Usage: python portfolio_csv2txt.py  Portfolio.csv  Portfolio.yml
# The input file to process defaults to "_Porfolio.csv" if not specified in the argument calling this program.
# The output is to STDOUT if an -o (output file) is not specified.
# The output rewrites any existing file of the same name.
# This is store in https://github.com/wilsonmar/python-batch

# Begin timer:
import timeit
start_time = timeit.default_timer()

# Get argument list using sys module:
import sys, os.path
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
      file_in = '_Portfolio.csv'

# Exit if file_in not found:
if os.path.exists(file_in) and os.access(file_in, os.R_OK):
    import csv, time
    with open(file_in, 'rU') as f:
        reader = csv.reader(f, delimiter=',')
        for i in reader:
            print '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+" "+sys.argv[0]+' START: outrowcount='+ str( sum(1 for _ in f) ) +'.'
else:
    print '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+' '+sys.argv[0]+" ABORTED. Either file "+file_in+" is missing or is not readable."
    exit(2)

# Provide default file_out name argument if not provided:
if __name__ == "__main__":
#def main(argv):
   try:
      arg1 = sys.argv[2]
      file_out = sys.argv[2]
   except IndexError: # getopt.GetoptError:
      file_out = file_in + '.txt'

# Send STDOUT to a file:
stdout = sys.stdout  # remember the handle to the real standard output.
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

# Close the file every time:
sys.stdout.close()


sys.stdout = stdout # Restore regular stdout.
# End timer:
elapsed = timeit.default_timer() - start_time
print "# "+ time.strftime('%Y-%m-%d-%H:%M (local time)') +' '+ sys.argv[0] +" END: ran for "+ "{:.2f}".format(elapsed * 1000 )+ ' secs.'

