import os
import json
import numpy as np
import pandas as pd

from shm.catchment_process import prediction


class SHM:
    STATE_NAMES = ['cat_ss','cat_sf','cat_su','cat_si','cat_sb']
    FLUX_NAMES = ['cat_qsin', 'cat_qsout', 'cat_qspout','cat_qfin','cat_quin','cat_qfout','cat_quout','cat_et','cat_qiin','cat_qiout','cat_qbin','cat_qbout','cat_qout']
    
    def __init__(self, cat_area: int, interval: str):
        """"""
        # set attributes
        self.cat_area = cat_area
        self.timedelta = pd.Timedelta(interval)
        self.interval_sec = self.timedelta.seconds

        # set parameter if there are any
        self._params = {}

    @classmethod
    def from_file(cls, path: str, **kwargs) -> 'SHM':
        """"""
        # check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f'{path} not found')

        # read config
        with open(path, 'r') as f:
            config = json.load(f)
        
        try:
            # mandatory attributes
            cat_area = config['attributes']['cat_area']
            interval = config['attributes']['interval']
            shm = SHM(cat_area, interval)

            if 'parameters' in config:
                shm.set_params(config['parameters'])
        except KeyError:
            raise RuntimeError(f'The config file {path} is invalid')

        # return 
        return shm

    @property
    def params(self) -> dict:
        return {**self._params}

    def get_params(self) -> dict:
        return self._params

    def set_params(self, params: dict) -> None:
        # TODO: validate and check the parameters
        self._params = params

    def get_cat_attributes(self) -> dict:
        return {
            'cat_area': self.cat_area,
            'timestep': self.interval_sec,
        }

    def fit(self, X: np.ndarray, y: np.ndarray) -> 'SHM':
        pass

    def transform(self, X: np.ndarray, **kwargs) -> np.ndarray:
        # TODO: make this nicer

        # TODO: do some validation to X
        # ie:
        if X.shape[1] != 6:
            raise ValueError('X must have shape (n, 6)')

        # make copy:
        _X = X.copy()

        # lengh of the data
        num_ts = X.shape[0]

        # get catchment attribtues and model parameters
        cat_attr = self.get_cat_attributes()
        params = self.get_params()

        # output container
        q = np.ones((1, num_ts)) * np.nan
        state = np.ones(num_ts, len(SHM.STATE_NAMES)) * np.nan
        flux = np.ones((num_ts, len(SHM.FLUX_NAMES))) * np.nan

        # accept boundary conditions
        # TODO: rework this into an attribute
        if 'boundary_conditions' in kwargs:
            boundary_conditions = kwargs['boundary_conditions']
        else:
            boundary_conditions = [0 ,0 ,0.15 ,0 ,0.027]
        state[0] = boundary_conditions
        flux[0] = [0] * len(SHM.FLUX_NAMES)

        # TODO: Cython this
        # main loop
        for t in range(1, num_ts):
            q[0,t], state[t, :], flux[t, :] = prediction(_X, state, flux, params, cat_attr)

        # save the states
        self._state = state
        self._flux = flux

        return q

    def tensor_transform(self, input_tensor):
        pass