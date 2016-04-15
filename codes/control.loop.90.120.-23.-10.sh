#!/bin/bash
# Q+D control loop tosearch 1deg x 1deg FOVs

res1=$(date +%s.%N) # to calculate CPU time

sr=90
fr=119
d0=-23
d1=-11

eval $@

# run loop that generates 1x1 FOV for 90 < RA < 120
    for (( i=$sr;i<=$fr;i++ )) ; do
        (( ts = i))
        (( tf = ts + 1 ))
        # run loop that generates 1x1 FOV for -1 < Dec < 15 at each 1x1 RA
        for (( j=$d0;j<=$d1;j++ )) ; do
        	(( dects = j ))
        	(( dectf = dects + 1 ))
            #echo $ts.$tf.$dects.$dectf
            ~/new_rrscript_cmod1.sh a0=$ts a1=$tf d0=$dects d1=$dectf
        done
    done
# to calculate CPU time
res2=$(date +%s.%N)
dt=$(echo "$res2 - $res1" | bc)
ddd=$(echo "$dt/86400" | bc)
dt2=$(echo "$dt-86400*$ddd" | bc)
dh=$(echo "$dt2/3600" | bc)
dt3=$(echo "$dt2-3600*$dh" | bc)
dm=$(echo "$dt3/60" | bc)
ds=$(echo "$dt3-60*$dm" | bc)

printf "Control loop runtime (days:hr:min:s): %d:%02d:%02d:%02.4f\n" $ddd $dh $dm $ds

exit 0
