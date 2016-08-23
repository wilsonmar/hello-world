#!/usr/bin/python
# This prints out a whole md (markdown) file (with the --- front-matter) so Snapcart can reference it.
# This is the "Parser" described in https://wilsonmar.github.io/jam-stack-website-project-plan/
# Usage: python portfolio_csv2md.py  _Portfolio.csv 
# The input file to process defaults to "Porfolio.csv" if not specified in the argument calling this program.
# The Portfolio.csv is a spreadsheet containing one row for each work of art.
# The output is to STDOUT if an output file is not specified.
# The output rewrites any existing file of the same name.
# This is stored in https://github.com/wilsonmar/python-batch
# A description of Python features used in this program: https://github.com/wilsonmar/python-templates/blob/master/README.md

# Begin timer (used by all my Python batch programs):
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
            outrowcount = sum(1 for _ in f)
            print '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+" "+sys.argv[0]+' START: outrowcount='+ str( outrowcount ) +'.'
else:
    print '# '+time.strftime('%Y-%m-%d-%H:%M (local time)')+' '+sys.argv[0]+" ABORTED. Either file "+file_in+" is missing or is not readable."
    exit(2)

# Provide default file_out name argument if not provided:
if __name__ == "__main__":
#def main(argv):
   try:
      arg1 = sys.argv[2]
      path_out = sys.argv[2]
   except IndexError: # getopt.GetoptError:
      path_out = 'http://www.ghmgallery.com/images'

# Send STDOUT to a file:
# stdout = sys.stdout  # remember the handle to the real standard output.
# sys.stdout=open( file_out,"w")


# Print in yml format:
import csv
# 'rU' means open in universal-newline mode needed on Macs:
#with open('./Portfolio.csv', 'rU') as f:
with open(file_in, 'rU') as f:
    reader = csv.reader(f, delimiter=',')
    first_line = f.readline() # pull out first line - do not print 
    for i in reader: # iterate:
        file_out = i[11] + '.md' # blank entries are ignored by Python.
        fo = open(file_out,"w") # in current folder.
        fo.write( '---' + \
        '\n name: '+i[1] + \
        '\n price: '+i[22] + \
        '\n slug: '+i[11] + \
        '\n sku: '+i[11] + \
        '\n image: '+ path_out +'/'+ i[7] + \
        '\n layout: productdetails' + \
        '\n---' + \
        '\n<strong>'+i[1]+'</strong><br />' \
        '\n '+i[2]+'. '+i[3]+'. '+i[4]+'x'+i[5]+' inches.'+'<br />' + \
        '\n '+i[6]+'<br />' + \
        '\n ' + \
        '\n '+i[16] + \
        '\n ' + \
        '\n '+i[17] + \
        '\n#END') # last item in string.
        fo.close()
        # notes: '+i[16] + \
        # tage: i[17]

# Close the file every time:
# sys.stdout.close()
# sys.stdout = stdout # Restore regular stdout.

# End timer:
elapsed = (timeit.default_timer() - start_time) * 1000
print "# "+ time.strftime('%Y-%m-%d-%H:%M (local time)') +' '+ sys.argv[0] +" END: ran for "+ "{:.2f}".format(elapsed)+ ' secs.'
# https://mkaz.tech/python-string-format.html

print "# "+ time.strftime('%Y-%m-%d-%H:%M (local time)') +' '+ sys.argv[0] +" Secs per item: "+ "{:.2f}".format(elapsed / outrowcount )+ ' secs.'
