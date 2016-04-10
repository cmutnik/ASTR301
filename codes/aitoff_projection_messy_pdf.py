# code to make aioff projection of all rr lyrae
# Python script to make projection mapping of RR candidates from lsum.dat files
# observed data and PS data
# Corey Mutnik 4/7/16

from astropy.io import fits, ascii
import numpy as np
import matplotlib.pyplot as plt
from astropy import coordinates as coord
from astropy import units as u
from glob import glob
import os

dfile1 = np.genfromtxt('/ay303/atlas/rr_lyrae/tmp/compare_var_cat/first3000.99.100.-1.0/JTscript.RA.Dec.99.100.-1.0.txt')
RA1 = dfile1[:,0]
Dec1 = dfile1[:,1]
c = coord.FK5(RA1, Dec1, unit=(u.deg, u.deg))
c_gal = c.galactic

# PS var star list
PSdat = fits.open('/home/rr_lyrae/ref/NH_qso_rrlyrae_candidates_catalog.fits')
PS_rr_candidates = PSdat[1].data

# for PS var candidates >=0.05
mask = PS_rr_candidates['p_RRLyrae'] >= 0.05
newtbdata = PS_rr_candidates[mask]
PS = coord.FK5(newtbdata['ra'], newtbdata['dec'], unit=(u.deg, u.deg))
PS_gal = PS.galactic

# for PS var candidates >=0.2
mask_tac2 = PS_rr_candidates['p_RRLyrae'] >= 0.2
newtbdata_tac2 = PS_rr_candidates[mask_tac2]
PS_tac2 = coord.FK5(newtbdata_tac2['ra'], newtbdata_tac2['dec'], unit=(u.deg, u.deg))
PS_gal_tac2 = PS_tac2.galactic

def plot_map_with_tac05_tac2_PSdata_lsum():
	plt.clf()
	fig = plt.figure(1)
	ax = fig.add_subplot(1,1,1, aspect='equal')
	ax.scatter(PS_gal.l.degree, PS_gal.b.degree, s=1, color='blue', alpha=0.025, label='PS >= 0.05')
	ax.scatter(PS_gal_tac2.l.degree, PS_gal_tac2.b.degree, s=1, color='green', alpha=0.025, label='PS >= 0.2')
	# alpha zero so it doesnt show, only there for the label
	ax.scatter(c_gal.l.degree, c_gal.b.degree, s=1, color='red', alpha=0.0, label='Observed')
	ax.set_xlim(360., 0.)
	ax.set_ylim(-90., 90.)
	ax.set_xlabel("Galactic Longitude")
	ax.set_ylabel("Galactic Latitude")
	ax.legend()

#Make an Aitoff projection map of the sources in Galactic coordinates
l_rad = c_gal.l.radian
l_rad[l_rad > np.pi] -= 2. * np.pi
b_rad = c_gal.b.radian

# do same for PS data: rr candidates >= 0.05
l_rad_PS = PS_gal.l.radian
l_rad_PS[l_rad_PS > np.pi] -= 2. * np.pi
b_rad_PS = PS_gal.b.radian

def aitoff_with_tac05_tac2_PSdata_lsum():
	# do same for PS data: rr candidates >= 0.2
	l_rad_PS2 = PS_gal_tac2.l.radian
	l_rad_PS2[l_rad_PS2 > np.pi] -= 2. * np.pi
	b_rad_PS2 = PS_gal_tac2.b.radian

	# plot
	plt.clf()
	fig = plt.figure(2)
	ax = fig.add_subplot(1,1,1, projection='aitoff')
	ax.scatter(l_rad_PS, b_rad_PS, s=1, color='blue', alpha=0.025)
	ax.scatter(l_rad_PS2, b_rad_PS2, s=1, color='green', alpha=0.025)
	#ax.scatter(l_rad, b_rad, s=1, color='red', alpha=0.05)
	ax.grid()
	#plt.savefig('PS_obs_atioff_proj_tac05_tac2_lsum.png')







dir_path = u'/ay303/atlas/rr_lyrae/*/VARLS/'

globpath = os.path.join(dir_path, 'lsum.dat')
filelist = glob(globpath)
filelist.sort() # so we are know which file we are working with

def aitoff_square(RA, Dec, fn='testsquare.png'):
	c = coord.FK5(RA, Dec, unit=(u.deg, u.deg))
	c_gal = c.galactic
	#plt.clf()
	fig = plt.figure(1)
	ax = fig.add_subplot(1,1,1, aspect='equal')
	ax.scatter(c_gal.l.degree, c_gal.b.degree, s=1, color='red', alpha=0.025, label='Observed')
	#plt.colorbar()
	#ax.set_xlim(360., 0.)
	#ax.set_ylim(-90., 90.)
	#ax.set_xlabel("Galactic Longitude")
	#ax.set_ylabel("Galactic Latitude")
	#ax.legend()
	#plt.savefig(fn)


def aitoff_map(RA,Dec,fn='testmap.png'):
	'''
	Make an Aitoff projection map 
	of the sources in Galactic coordinates
	'''
	# convert coordinates to galactic and wrap them
	c = coord.FK5(RA, Dec, unit=(u.deg, u.deg))
	c_gal = c.galactic
	l_rad = c_gal.l.radian
	l_rad[l_rad > np.pi] -= 2. * np.pi
	b_rad = c_gal.b.radian

	# plot
	fig = plt.figure(2)
	ax = fig.add_subplot(1,1,1, projection='aitoff')
	ax.scatter(l_rad, b_rad, s=1, color='red', alpha=0.025)
	#ax.colorbar()
	#ax.grid()
	#plt.savefig(fn)

# Plot PS data first, so observed data shows ontop
plot_map_with_tac05_tac2_PSdata_lsum()
for i in range(len(filelist)):
	dfile = ascii.read(filelist[i])
	RA_lsum = dfile['col6']
	Dec_lsum = dfile['col7']
	aitoff_square(RA=RA_lsum, Dec=Dec_lsum, fn='Obs_lsum_aitoff_xy.png')
plt.savefig('Obs_PS_lsum_aitoff_xy.pdf')

# Plot PS data first, so observed data shows ontop
aitoff_with_tac05_tac2_PSdata_lsum()
for j in range(len(filelist)):
	dfile = ascii.read(filelist[j])
	RA_lsum = dfile['col6']
	Dec_lsum = dfile['col7']
	# call plotting function
	aitoff_map(RA_lsum, Dec_lsum, fn='Obs_lsum_aitoff_map.png')
plt.savefig('Obs_PS_lsum_aitoff_map.pdf')

