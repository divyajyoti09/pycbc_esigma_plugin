from gwnr.waveform import esigma_utils
from pycbc.types.timeseries import TimeSeries

def IMRESIGMAHM_td(**input_params):
    hp, hc = esigma_utils.get_imr_esigma_waveform(**input_params)
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)

def IMRESIGMA_td(**input_params):
    hp, hc = esigma_utils.get_imr_esigma_waveform(**input_params, modes_to_use=[(2, 2)])
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)

def InspiralESIGMAHM_td(**input_params):
    _, hp, hc = esigma_utils.get_inspiral_esigma_waveform(**input_params)
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)

def InspiralESIGMA_td(**input_params):
    hp, hc = esigma_utils.get_inspiral_esigma_waveform(**input_params, modes_to_use=[(2, 2)])
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)
