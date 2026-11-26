import pandas as pd
from src.logger import logger


def data_ingestion():
    try:

        '''
        * Problem Statements : To  predict the preventive maintainance for Coal Mine application 

        * Independent Columns(X) :  'vibration_rms', 'vibration_peak', 'vibration_kurtosis',
        'vibration_crest_factor', 'bpfo_amplitude', 'bpfi_amplitude',
        'bsf_amplitude', 'ftf_amplitude', 'bearing_temperature',
        'acoustic_level', 'rotational_speed', 'ambient_temperature', 'humidity',
        'dust_concentration', 'moisture_level', 'operating_hours',
        'conveyor_load', 'belt_speed', 'motor_current', 'lubrication_age_hours',
        'last_maintenance_hours', 'previous_failure_count',
        'seal_condition_score', 'bearing_age_months'

        * Target Columns(y) : 'failure_within_7_days'

        
        '''
        df = pd.read_csv(r'C:\mlops_prediction\data\raw\preventative_maintainance_dataset.csv')
        logger.info(f'Data Ingestion Completed Successfully with {df.shape}')
        logger.info(f'Dataset Columns ....{df.columns}')
        return df
    except FileNotFoundError as e:
        logger.exception(f'Exception Occurs ....{e}')
        raise 