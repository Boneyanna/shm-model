def fastflow(cat_qspout, cat_qfin, cat_quin, cat_qfout, cat_sf, cat_thres,cat_kf):
  # split outflow from snowmelt + rainfall into inflow to fastflow reservoir and unsaturated reservoir
  if cat_qspout > cat_thres: # outflow from snow + rainfall exceeds critical threshold
    cat_qfin = cat_qspout - cat_thres 
    cat_quin = cat_thres   
  else :
    cat_qfin = 0; 
    cat_quin = cat_qspout
  #add inflow to fast flow reservoir
  cat_sf = cat_sf + cat_qfin
  cat_qfout = cat_sf / cat_kf          # outflow from fastflow reservoir
  cat_qfout = min(cat_qfout,cat_sf)      # limit fast flow
  cat_sf = cat_sf - cat_qfout 
  
  return(cat_qfin, cat_quin, cat_qfout, cat_sf)
  
