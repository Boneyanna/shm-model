def unsaturated(cat_quin, cat_quout, cat_et, cat_su, beta, cat_sumax, temp, time_step,rg,vel,rh):
  #unsaturated zone
  psi = (cat_su / cat_sumax) ** beta      # runoff coefficient - part fo rain becoming runoff
  cat_quout = cat_quin * psi                        # runoff [m/dt]                  
  cat_su = cat_su + cat_quin - cat_quout  # wetting of unsaturated zone [m]

  # limit unsaturated zone to sumax, excess becomes direct runoff
  if cat_su > cat_sumax:
    cat_quout = cat_quout + cat_su - cat_sumax   # [m/dt] add excess volume to runoff
    cat_su = cat_sumax               # [m] limit the fill level to sumax
  
  #landuse correction factor
  klu =0.5

  from Evapotranspiration import f_r_teta
  from Evapotranspiration import f_ETpo_Penman
  
  #soil moisture correction factor
  kteta = f_r_teta(cat_su,cat_sumax)

  #Potential evapotranspiration
  PET = f_ETpo_Penman(temp,time_step, rg, vel, rh)/1000

  #limit PET to zero
  PET = max(PET,0)

  cat_et = PET * klu * kteta   #Final ET
  cat_et = min(cat_et,cat_su) #limit etp

  #substracct et from unsaturated zone
  cat_su = cat_su - cat_et
  return (cat_quout, cat_et, cat_su)
