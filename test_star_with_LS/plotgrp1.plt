# Gnuplot script to plot sort star data
# Corey Mutnik 3/16/16

set terminal png nocrop enhanced size 900,700 font 'arial,18'
set out 'star1.png'

set xr [57452:57460]
set yr [8.5:12]

set title('Star 1')
set xlabel('Time [MJD]')
set ylabel('m')
set key off


plot "grp1.txt" u 3:9:10 with yerrorbars
