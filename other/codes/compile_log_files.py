# pull log files and use them to isolate which files are of RR Lyrae observations
# Corey Mutnik 3/9/16

#import matplotlib.pyplot as plt
#import numpy as np
from glob import glob
import os
from astropy.io import ascii

dir_path = u'/home/cmutnik/data/RR_data_160306/fulldata/'
globpath = os.path.join(dir_path, '*/*.log')#					use log files located in dir_path
filelist = glob(globpath)
filelist.sort() # unnecessary

#f = open('l202_bp5.t.txt', 'w')

data_dir = '/atlas/red/01p/'


'''
for i in range(len(dfile['Etime'])):
	if dfile['Etime'][i] == 20.0:
		print dfile['Observation'][i], '\t', dfile['Obj'][i]
'''

# makes a list of all the files were recorded for l=202^{\circ} @ b=+5^{\circ}
list_l202_bp5 = []
for j in range(len(filelist)):
	# make log file into astropy table
	dfile = ascii.read(filelist[j])
	#dfile.colnames
	# pull the directory numbers from log file number [:-4] takes off the '.log'
	dir_num = os.path.basename(filelist[j])[:-4]
	print 'directory_number\tfilename\tObs_ID'
	for i in range(len(dfile['Obj'])):
		if dfile['Obj'][i][:4] == '2021':
			print dir_num, '\t', dfile['Observation'][i], '\t', dfile['Obj'][i]
			# append files with full directories to empty list
			list_l202_bp5.append(data_dir+str(dir_num)+'/'+dfile['Observation'][i]+'.dph')
			#f.write(data_dir+str(dir_num)+'/'+str(dfile['Observation'][i])+'.dph'+'\n')
#f.close()

#####------------------------------------------------------------------------------------------------------------
cat = ascii.read('out.txt')



#for i in range(len(list_l202_bp5)):
	#startable = ascii.read(list_l202_bp5[i])

###
#Compile all data from all files in 'list_l202_bp5' into one file called "out.txt"
###
fout=open("out.t.txt","a")
# first file:
for line in open(list_l202_bp5[0]):
    fout.write(line)
# now the rest: try to skip line one so it doesnt print the header line 
for num in range(len(list_l202_bp5)):
    f = open(list_l202_bp5[num])
    print f
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()


'''
import pandas as pd
import numpy as np
all_data = pd.DataFrame()
#for f in glob('l202_bp5.txt'):
for f in glob(list_l202_bp5):
    #df = pd.read_excel(f)
    df = np.loadtxt(f, unpack=True)
    print df
    all_data = all_data.append(df,ignore_index=True)
'''

'''
def all_positive(column):
    if np.any(column < 0):
        return False
    return True
'''


