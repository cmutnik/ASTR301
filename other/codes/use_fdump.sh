  fdump NH_qso_rrlyrae_candidates_catalog.fits

  fdump NH_qso_rrlyrae_candidates_catalog.fits -n 2 > PS_data/rrqso.NH

  fdump NH_qso_rrlyrae_candidates_catalog.fits -n 2 | awk '{printf "%8.4f %8.4f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f\n", $1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13}' > PS_data/rrqso.reform

  fdump NH_qso_rrlyrae_candidates_catalog.fits -n 2 | awk '$6<16 && $7<16 &&$8<16{printf "%8.4f %8.4f %8.2f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f\n", $1,$2,$3,$4,$5,$6,$7,$8,$11,$12,$13}' > PS_data/rrqso.bright

  awk '$1>99 && $1<100 && $2>-1 && $2<0 && $11>0.5{print $0}' PS_data/rrqso.bright
