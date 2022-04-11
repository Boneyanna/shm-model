def snowpack(prec,temp,cat_qsin, cat_qsout, cat_qspout,cat_ss, t_crit,cat_dd ):
  
  if temp > t_crit :
    cat_qsin = 0  # prec falls as rain
   
    #calculate snowmelt from snow reservoir
    cat_qsout = cat_dd * (temp - t_crit)
    cat_qsout = min(cat_qsout,cat_ss)  #limit snowmelt

    #subtract snowmelt from snow reservoir
    cat_ss = cat_ss - cat_qsout

    #flow from rainfall and snowmelt
    cat_qspout = prec + cat_qsout

  else:
    cat_qsin = prec                     #precip falls as snow
    cat_ss = cat_ss + cat_qsin # add snowfall to snow reservoir
    cat_qsout = 0                          #no melting
    cat_qspout = 0                         # no flow from precip or snowmelt
  return(cat_qsin,cat_qsout,cat_qspout, cat_ss)
  
