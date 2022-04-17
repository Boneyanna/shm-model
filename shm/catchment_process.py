# state variables "state"
# cat_ss - fill level of snow reservoir, cat_sf- Fill level of fast reservoir
# cat_su - fill level of unsaturated zone, cat_si - fill level of interflow reservoir, cat_sb - fill level of baseflow reservoir
# Flux variables 
# cat_qsin - inflow to snow reseervoir , cat_qsout - outflow from snow reservoir, cat_qspout - outflow from snow reservoir + precipitation, cat_qfin- inflow to fastflow reservoir,
# cat_quin - inflow to unsat zone, cat_qfout - outflow from fastflow reservoir, cat_quout - outflowfrom unsaturated zone, cat_et- evapotranspiration, cat_qiin- inflow to interflow reserv
# cat_qiout - outflow from interflow reservoir, cat_qbin - inflow to baseflow reservoir, cat_qbout - outflow frombaseflow reservoir
#cat_qout - total outflow


from shm.snowpack_reservoir import snowpack
from shm.fastflow_reservoir import fastflow
from shm.unsaturated_reservoir import unsaturated
from shm.interflow_reservoir import interflow
from shm.baseflow_reservoir import baseflow
def prediction(data,state,flux,para, chara):
  # snowpack reservoir
  (flux.cat_qsin,flux.cat_qsout,flux.cat_qspout,state.cat_ss)= snowpack (data[0],data[1],flux.cat_qsin, flux.cat_qsout,flux.cat_qspout, state.cat_ss, para["t_crit"],para["cat_dd"])
  # fastflow reservoir
  (flux.cat_qfin,flux.cat_quin,flux.cat_qfout,state.cat_sf)= fastflow(flux.cat_qspout, flux.cat_qfin,flux.cat_quin,flux.cat_qfout,state.cat_sf,para["cat_thresh"],para["cat_kf"])
  # unsaturated zone
  (flux.cat_quout, flux.cat_et, state.cat_su)= unsaturated(flux.cat_quin, flux.cat_quout, flux.cat_et, state.cat_su,para["cat_beta"], para["cat_sumax"],data[1], chara["timestep"],data[2],data[3],data[4])
  # interflow reservoir
  (flux.cat_qiin,flux.cat_qiout, state.cat_si)= interflow(flux.cat_quout, flux.cat_qiin,flux.cat_qiout, state.cat_si,para["cat_perc"],para["cat_ki"]) 
  #baseflow reservoir
  (flux.cat_qbin,flux.cat_qbout, state.cat_sb) = baseflow(flux.cat_quout,flux.cat_qiin,flux.cat_qbin,flux.cat_qbout, state.cat_sb, para["cat_kb"])

  # total outflow (sum of fastflow, interflow and baseflow) 
  flux.cat_qout = flux.cat_qfout + flux.cat_qiout + flux.cat_qbout
  discharge = flux.cat_qout * chara["cat_area"] / chara["timestep"]
  return (discharge,state,flux)
