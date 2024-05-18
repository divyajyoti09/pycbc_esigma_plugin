from gwnr.waveform import esigma_utils
from pycbc.types.timeseries import TimeSeries

def IMRESIGMAHM_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for IMRESIGMAHM waveform containing all (l,|m|) modes available.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
        -------

        hplus: PyCBC TimeSeries
            The plus-polarization of the waveform in time domain tapered from start to 0.4s.
        hcross: PyCBC TimeSeries
            The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    
    hp, hc = esigma_utils.get_imr_esigma_waveform(**input_params)
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)

def IMRESIGMA_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for IMRESIGMA waveform containing only the (l,|m|) = (2,2) mode.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
        -------

        hplus: PyCBC TimeSeries
            The plus-polarization of the waveform in time domain tapered from start to 0.4s.
        hcross: PyCBC TimeSeries
            The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    hp, hc = esigma_utils.get_imr_esigma_waveform(**input_params, modes_to_use=[(2, 2)])
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)

def InspiralESIGMAHM_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for InspiralESIGMAHM waveform containing all (l,|m|) modes available.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
        -------

        hplus: PyCBC TimeSeries
            The plus-polarization of the waveform in time domain tapered from start to 0.4s.
        hcross: PyCBC TimeSeries
            The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    _, hp, hc = esigma_utils.get_inspiral_esigma_waveform(**input_params)
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)

def InspiralESIGMA_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for InspiralESIGMA waveform containing only the (l,|m|) = (2,2) mode.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
        -------

        hplus: PyCBC TimeSeries
            The plus-polarization of the waveform in time domain tapered from start to 0.4s.
        hcross: PyCBC TimeSeries
            The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    hp, hc = esigma_utils.get_inspiral_esigma_waveform(**input_params, modes_to_use=[(2, 2)])
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    return(hp_ts, hc_ts)
