#g
#02537
#r
#04822
#i
#06186
#field
#095+02
#-0.284
#N=
#417
#416
#RADec=
#95.4280
#2.3963
#f=
#0.10665
#P=
#9.376038
#logPr(rnd)=
#-0.991
#P2=
#4.77994
#Pr2/Pr=
#0.9525
#Star=
#02537

# Py script to make log prob rr histo

dfile = ascii.read('lsum_160419_awked.dat')


P = dfile['col19']
freq = dfile['col17']
logpr_rnd = dfile['col21']


def plots_with_titles():
	plt.figure(1)
	plt.clf()
	#plt.plot(P,logpr_rnd, '.')
	plt.plot(P,logpr_rnd, '*', color='k',fillstyle='none')
	plt.title('prob(f)')
	plt.xlabel('Period')
	plt.ylabel('logPr(rnd)')
	#plt.gca().invert_yaxis()
	plt.xlim(-10,350)# flip axis here rather than line above
	plt.ylim(-55,1.5)
	plt.grid()
	plt.savefig('log_period_empty.png')

	plt.figure(2)
	plt.clf()
	plt.plot(freq,logpr_rnd, 's', color='k',fillstyle='none')
	#plt.plot(freq,logpr_rnd, 'gs')
	plt.title('prob(f)')
	plt.xlabel('Frequency [$day^{-1}$]')
	plt.ylabel('logPr(rnd)')
	#plt.gca().invert_yaxis()
	plt.xlim(-0.5,25)
	plt.ylim(-55,1.5)
	plt.grid()
	plt.savefig('log_freq_empty.png')
plots_with_titles()

def plots_without_titles():
	plt.figure(1)
	plt.clf()
	plt.plot(P,logpr_rnd, 'D', color='k',fillstyle='none')
	plt.xlabel('Period')
	plt.ylabel('logPr(rnd)')
	plt.xlim(-10,350)
	plt.ylim(-55,1.5)
	plt.grid()
	plt.savefig('log_period_notitle_empty.png')

	plt.figure(2)
	plt.clf()
	plt.plot(freq,logpr_rnd, 'd', color='k',fillstyle='none')
	plt.xlabel('Frequency [$day^{-1}$]')
	plt.ylabel('logPr(rnd)')
	plt.xlim(-0.5,25)
	plt.ylim(-55,1.5)
	plt.grid()
	plt.savefig('log_freq_notitle_empty.png')
plots_without_titles()

'''
def plots_minus50_different_faile$d()^{-1}$]')
	plt.ylabel('logPr(rnd)')
	plt.xlim(-0.5,25)
	plt.ylim(-55,0)
	plt.savefig('log_freq_diff-50.png')
'''
def plots_minus50_different():
	foo = np.where(logpr_rnd == -50)
	logpr_minus50 = logpr_rnd[foo]
	P_minus50 = P[foo]
	freq_minus50 = freq[foo]

	logpr_notminus50 = logpr_rnd[np.where(logpr_rnd != -50)]
	P_notminus50 = P[np.where(logpr_rnd != -50)]
	freq_notminus50 = freq[np.where(logpr_rnd != -50)]

	plt.figure(1)
	plt.clf()
	#if logpr_rnd == -50:
	#	plt.plot(P,logpr_rnd, 'rh')
	#else:
	#	plt.plot(P,logpr_rnd, 'rH')
	plt.plot(P_minus50,logpr_minus50, '*', color='k',fillstyle='none')
	plt.plot(P_notminus50,logpr_notminus50, 'H', color='k',fillstyle='none')
	plt.title('prob(f)')
	plt.xlabel('Period')
	plt.ylabel('logPr(rnd)')
	plt.xlim(-10,350)
	plt.ylim(-55,1.5)
	plt.grid()
	plt.savefig('log_period_diff-50_empty.png')
	
	plt.figure(2)
	plt.clf()
	#if logpr_rnd == -50:
	#	plt.plot(freq,logpr_rnd, 'gH')
	#else:
	#	plt.plot(freq,logpr_rnd, 'gD')
	plt.plot(freq_minus50, logpr_minus50, 'h', color='k',fillstyle='none')
	plt.plot(freq_notminus50,logpr_notminus50, 'd', color='k',fillstyle='none')
	plt.title('prob(f)')
	plt.xlabel('Frequency [$day^{-1}$]')
	plt.ylabel('logPr(rnd)')
	plt.xlim(-0.5,25)
	plt.ylim(-55,1.5)
	plt.grid()
	plt.savefig('log_freq_diff-50_empty.png')
plots_minus50_different()




