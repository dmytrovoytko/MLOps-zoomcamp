import batch

import pandas as pd
pd.set_option('display.max_columns', None)


from datetime import datetime

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)


def test_prepare_data():
    
    data = [
        (None, None, dt(1, 1), dt(1, 10)),
        (1, 1, dt(1, 2), dt(1, 10)),
        (1, None, dt(1, 2, 0), dt(1, 2, 59)),
        (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]
    
    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)
    categorical = ['PULocationID', 'DOLocationID']
    
    actual_result = batch.prepare_data(df, categorical)
    print(f'Actual:\n{actual_result}')

    data1 = [
        ("-1", "-1", dt(1, 1), dt(1, 10), 9.0),
        ("1", "1", dt(1, 2), dt(1, 10), 8.0),
    ]
    
    columns1 = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime', 'duration']

    expected_result = pd.DataFrame(data1, columns=columns1)
    print(f'Expected:\n{expected_result}')

    assert (actual_result==expected_result).all(True).to_list()==[True, True]
    
