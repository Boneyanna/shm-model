def interflow(cat_quout,cat_qiin,cat_qiout, cat_si,cat_perc,cat_ki):  
  # inflow to interflow reservoir
  cat_qiin = cat_quout * cat_perc

  # new storage in interflow reservoir due to inflow
  cat_si = cat_si + cat_qiin

  # outflow from interflow reservoir 
  cat_qiout = cat_si / cat_ki

  # limit outflow from interflow reservoir
  cat_qiout = min(cat_qiout,cat_si)

  # new storage in interflow reservoir due to outflow
  cat_si = cat_si - cat_qiout
  return(cat_qiin, cat_qiout, cat_si)
  
