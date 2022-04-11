# state variables "state"
# state [0] - fill level of snow reservoir (cat_ss),  state [1]- Fill level of fast reservoir(cat_sf)
# state [2] - fill level of unsaturated zone (cat_su), state [0] - fill level of interflow reservoir (cat_si), state[4- fill level of baseflow reservoir
# Flux variables 
# flux [0] - inflow to snow reseervoir , flux[1] - outflow from snow reservoir, flux[2] - outflow from snow reservoir + precipitation, flux[3]- inflow to fastflow reservoir,
# flux[4] - inflow to unsat zone, flux[5] - outflow from fastflow reservoir, flux[6] - outflowfrom unsaturated zone, flux [7]- evapotranspiration, flux[8]- inflow to interflow reserv
# flux[9] - outflow from interflow reservoir, flux []
import pandas as pd
import numpy as np
from snowpack_reservoir import snowpack
from fastflow_reservoir import fastflow
from unsaturated_reservoir import unsaturated
from interflow_reservoir import interflow
from baseflow_reservoir import baseflow
def prediction(data,state,flux,para, chara):
  # snowpack reservoir
  flux[0],flux[1],flux[2],state[0]= snowpack(data[0],data[1],flux[0], flux[1],flux[2], state[0], para["t_crit"],para["cat_dd"])
  # fastflow reservoir
  flux[3],flux[4],flux[5],state[1]= fastflow(flux[2], flux[3],flux[4],flux[5],state[1],para["cat_thresh"],para["cat_kf"])
  # unsaturated zone
  flux[6], flux[7], state[2]= unsaturated(flux[4], flux[6], flux[7], state[2],para["cat_beta"], para["cat_sumax"],data[1], chara["timestep"],data[2],data[3],data[4])
  # interflow reservoir
  flux[8],flux[9], state[3]= interflow(flux[6], flux[8],flux[9], state[3],para["cat_perc"],para["cat_ki"]) 
  #baseflow reservoir
  flux[10],flux[11], state[4]= baseflow(flux[6],flux[8],flux[10],flux[11], state[4], para["cat_kb"])

  # total outflow (sum of fastflow, interflow and baseflow) 
  flux[12] = flux[5] + flux[9] + flux[11]
  discharge = flux[12] * chara["cat_area"] / chara["timestep"]
  return (discharge,state,flux)
