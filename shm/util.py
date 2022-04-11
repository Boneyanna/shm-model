import os
import pandas as pd

REQUIRED_DATA_COLUMNS = ['precipitation', 'temperature', 'global_radiation', 'wind_velocity', 'relative_humidity', 'discharge']


def read_data(path: int, integrity_check: bool = True) -> pd.DataFrame:
    """
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found")

    # read file
    df = pd.read_csv(path)

    if not integrity_check:
        return df
    
    # check file
    if not all([col in df.columns for col in REQUIRED_DATA_COLUMNS]):
        raise RuntimeError(f"Malformed data file: {path}.\nMake sure to have the follwoing columns available: {REQUIRED_DATA_COLUMNS}.\nFound: {df.columns}")

    return df


def run(data: pd.DataFrame, inplace: bool = False) -> None:
    """
    """
    # check if we need a copy
    if not inplace:
        df = data.copy()
    else:
        df = data
    
    # put your main code here

    # transpose to work on 'timestep objects'
    for it, row in df.iterrows():
        # boundary conditions
        if it == 0:
            continue

        # here it is > 0
        pass


    # finally return
    return df
