
def baseflow(cat_quout,cat_qiin, cat_qbin, cat_qbout,cat_sb,cat_kf):  
  # inflow to baseflow reservoir 
  cat_qbin = cat_quout - cat_qiin

  # new storage in baseflow reservoir due to inflow 
  cat_sb = cat_sb + cat_qbin

  # outflow from baseflow reservoir 
  cat_qbout = cat_sb / cat_kf

  # limit outflow from baseflow reservoir
  cat_qbout = min(cat_qbout,cat_sb)

  # new storage in baseflow reservoir due to outflow
  cat_sb = cat_sb - cat_qbout
  return(cat_qbin, cat_qbout,cat_sb)
  
