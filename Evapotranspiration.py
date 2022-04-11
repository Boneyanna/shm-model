
def f_r_teta(teta_act,teta_FC):
  teta_CRIT = 0.8 * teta_FC; # critial filling level. Above, water availability is no limitation

  if teta_act < teta_CRIT:
    r_teta = teta_act / teta_CRIT
  else:
    r_teta = 1
  return r_teta
  
def f_ETpo_Penman (T, dt, Rg, v2, RH):
  e_s = 6.11 * (2.718**( (17.62 * T) / (243.12 + T)))
  # inclination of the saturation vapor pressure curve
  # - s [hPa/K], e_s [hPa], T [°C]
  s = e_s * (4284 /((243.12 + T)**2))

  # specific latent heat of vaporizaton
  # - Lstar [J / kg]
  Lstar = 2088000    # 2088 kJ/kg

  # psychrometric constant
  # - gamma [hPa/K]
  gamma = 0.65

  # evaporation (eq. 6.15 in DVWK 238/1996)
  # - etp [mm/dt]
  etp = (s / (s + gamma) ) * (dt / Lstar) * (0.6 * Rg + 37.6 * (1 + 1.08 * v2) * (1 - (RH / 100) ) )
  return etp
