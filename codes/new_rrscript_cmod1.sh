#!/bin/bash
# Q+D search for a periodic star

res1=$(date +%s.%N) # to calculate CPU time

# Desired FOV
a0=99 a1=100 d0=-1 d1=0 RAD=2.5 

eval $@

#mkdir tmp/rrsearchJT ; cd tmp/rrsearchJT
mkdir rrsearch.$a0.$a1.$d0.$d1 ; cd rrsearch.$a0.$a1.$d0.$d1

#All non-bad observations
  for m in {57396..57474} ; do
    awk '$5>=20 && $8<3 && $9>500 && $10>15 && $11!=0 && $12!=0{print $0}' /atlas/red/01p/$m/$m.log
  done > all.log

#Find the 882 observations that might overlap
  list=$(awk -v a0=$a0 -v a1=$a1 -v d0=$d0 -v d1=$d1 -v r=$RAD '$11>a0-r && $11<a1+r && $12>d0-r && $12<d1+r{print substr($1,1,14)}' all.log | sort | uniq)

#The idea is to rewrite all $obs.dpg files into these one degree chunks, not just this list. It does cost disk space, however.
  for obs in $list ; do
    echo $obs
    m=$(echo $obs | tr '[a-z]' ' ' | awk '{print $2}')
    mjd=$(grep ${obs}0 /atlas/red/01p/$m/$m.log | awk '{print $2}')
    awk -v obs=$obs -v mjd=$mjd -v a0=$a0 -v a1=$a1 -v d0=$d0 -v d1=$d1 \
     'NR>1 && $3>7 && $3<20 && $1>=a0 && $1<a1 && $2>=d0 && $2<d1 {printf "%s %11.5f %s\n", obs,mjd,$0}' \
      /atlas/red/01p/$m/$obs.dpg >> df.$a0.$a1.$d0.$d1.dat
  done

#dph files
#  for obs in $list ; do
#    echo $obs
#    m=$(echo $obs | tr '[a-z]' ' ' | awk '{print $2}')
#    mjd=$(grep ${obs}0 /atlas/red/01p/$m/$m.log | awk '{print $2}')
#    for dev in 0 1 ; do
#      awk -v obs=$obs -v dev=$dev -v mjd=$mjd -v a0=$a0 -v a1=$a1 -v d0=$d0 -v d1=$d1 \
#       'NR>1 && $3>7 && $3<20 && $1>=a0 && $1<a1 && $2>=d0 && $2<d1 {x=(dev==0?$6-2048:$6); y=$7-2048; \
#        a=int($1); d=$2>0?int($2):int($2-0.9999999); \
#        fname=sprintf("dfh%03d%+03d.dat",a,d); \
#        printf "%s%d %11.5f %s\n", obs,dev,mjd,$0 >> fname}' \
#      /atlas/red/01p/$m/$obs$dev.dph
#    done
#  done


# Group each filter's detections into a star list
  for filt in g r i ; do
    date +%s
    grep $filt df.$a0.$a1.$d0.$d1.dat | cm 4,3,5 - -max 5000000 -tol 0.001,d,m -grp -grpfmt "%8.4f" -grpfile grp.$filt > grpall.$filt
    awk -v nmin=12 '$2>nmin{print $0}' grp.$filt > star.$filt
  done
  date +%s

#Pick out the "real" stars: add a "variability" measure; sort by variability. The "real" star counts are
  for filt in g r i ; do
    awk -v nmin=100 '$2>100{q=($9<12) ? 2.4 : 0.2*$9; var=log($11-$10)/log(10)-q; printf "%s %7.3f\n", $0, var}' star.$filt | sort -k 12 -g -r > varstar.$filt
  done

# Pick the 1000 most variable from each list and intersect them
  for filt in g r i ; do
    head -1000 varstar.$filt > var.$filt
  done

  cm 3,6 var.g 3,6 var.r -tol 0.001,d | cm 3,6 - 3,6 var.i -tol 0.001,d > var.gri

# Test all stars that appear variable in gri
  mkdir VARLS ; cd VARLS
  fname=( g r i )
  for ((num=1; num<=$(wc ../var.gri | awk '{print $1}'); num++)) ; do
    n4=$(printf "%04d" $num)
    idx=( $(awk -v n=$num 'NR==n{print $1,$14,$27}' ../var.gri) )
    for fnum in 0 1 2 ; do
      awk -v idx=${idx[$fnum]} '$1==idx{print $0}' ../grpall.${fname[$fnum]} | awk -v filt=${fname[$fnum]} -v fnum=$fnum '{printf "%8.4f %8.4f %11.5f %s %c %d %7.1f %7.1f %6.3f %5.3f %05d\n", $4,$5,$3, $2, filt, fnum, $9,$10, $6,$12,$1}'
    done > grp.$n4
# run LS
    lsout=$(cat grp.$n4 | ayls out=lc.$n4 freq=freq.$n4)
    echo "$n4 $lsout" | tee -a lsum.dat
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

printf "Total runtime (days:hr:min:s): %d:%02d:%02d:%02.4f\n" $ddd $dh $dm $ds

exit 0
