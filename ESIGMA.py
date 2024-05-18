from gwnr.waveform import esigma_utils
from pycbc.types.timeseries import TimeSeries

try:
    # some versions of pycbc include td_taper in pycbc.waveform
    from pycbc.waveform import td_taper
except:
    # some other versions of pycbc include td_taper in pycbc.waveform.utils
    from pycbc.waveform.utils import td_taper

def taper_signal(signal, beta=5):
    """
    Returns tapered signal between start and start+0.4s.

    Parameters
    ----------

    signal : PyCBC TimeSeries
    beta : The beta parameter to use for the Kaiser window. See scipy.signal.kaiser for details. Default is 5.

    Returns
    -------

    signal_tapered : PyCBC TimeSeries
    """
    signal_tapered = td_taper(signal, signal.sample_times[0], signal.sample_times[0]+0.4, beta=beta)
    return(signal_tapered)

def IMRESIGMAHM_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for IMRESIGMAHM waveform containing all (l,|m|) modes available.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
    -------

    hplus : PyCBC TimeSeries
        The plus-polarization of the waveform in time domain tapered from start to 0.4s.
    hcross : PyCBC TimeSeries
        The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    
    hp, hc = esigma_utils.get_imr_esigma_waveform(**input_params)
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    
    hp_tapered = taper_signal(hp_ts)
    hc_tapered = taper_signal(hc_ts)
    return(hp_tapered, hc_tapered)

def IMRESIGMA_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for IMRESIGMA waveform containing only the (l,|m|) = (2,2) mode.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
    -------

    hplus : PyCBC TimeSeries
        The plus-polarization of the waveform in time domain tapered from start to 0.4s.
    hcross : PyCBC TimeSeries
        The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    hp, hc = esigma_utils.get_imr_esigma_waveform(**input_params, modes_to_use=[(2, 2)])
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    
    hp_tapered = taper_signal(hp_ts)
    hc_tapered = taper_signal(hc_ts)
    return(hp_tapered, hc_tapered)

def InspiralESIGMAHM_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for InspiralESIGMAHM waveform containing all (l,|m|) modes available.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
    -------

    hplus : PyCBC TimeSeries
        The plus-polarization of the waveform in time domain tapered from start to 0.4s.
    hcross : PyCBC TimeSeries
        The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    _, hp, hc = esigma_utils.get_inspiral_esigma_waveform(**input_params)
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    
    hp_tapered = taper_signal(hp_ts)
    hc_tapered = taper_signal(hc_ts)
    return(hp_tapered, hc_tapered)

def InspiralESIGMA_td(**input_params):
    """
    Returns tapered time domain gravitational polarizations for InspiralESIGMA waveform containing only the (l,|m|) = (2,2) mode.

    Parameters
    ----------

    Takes the same parameters as pycbc.waveform.get_td_waveform().
    
    Returns
    -------

    hplus : PyCBC TimeSeries
        The plus-polarization of the waveform in time domain tapered from start to 0.4s.
    hcross : PyCBC TimeSeries
        The cross-polarization of the waveform in time domain tapered from start to 0.4s.
    """
    hp, hc = esigma_utils.get_inspiral_esigma_waveform(**input_params, modes_to_use=[(2, 2)])
    hp_ts = TimeSeries(hp, input_params['delta_t'])
    hc_ts = TimeSeries(hc, input_params['delta_t'])
    
    hp_tapered = taper_signal(hp_ts)
    hc_tapered = taper_signal(hc_ts)
    return(hp_tapered, hc_tapered)
