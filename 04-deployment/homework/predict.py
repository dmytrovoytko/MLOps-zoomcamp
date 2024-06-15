import argparse

import pickle
import pandas as pd

# from flask import Flask, request, jsonify

with open('model.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)
categorical = ['PULocationID', 'DOLocationID']


# def prepare_features(ride):
#     features = {}
#     features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
#     features['trip_distance'] = ride['trip_distance']
#     return features


# def predict(features):
#     X = dv.transform(features)
#     preds = model.predict(X)
#     return float(preds[0])

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def main(args):
    year = args.year
    month = args.month
    df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet')

    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    res = y_pred.mean()
    print('y_pred.mean()=', res)
    
    return res

    # features = prepare_features(args)
    # pred = predict(features)

    # result = {
    #     'duration': pred
    # }

    # return jsonify(result)

# app = Flask('duration-prediction')


# @app.route('/predict', methods=['POST'])
# def predict_endpoint():
#     ride = request.get_json()

#     features = prepare_features(ride)
#     pred = predict(features)

#     result = {
#         'duration': pred
#     }

#     return jsonify(result)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Predict year month')

    parser.add_argument('--year', required=False, type=int, default=2023, help='year to process')
    parser.add_argument('--month', required=False, type=int, default=4, help='month to process')

    args = parser.parse_args()

    res = main(args)
    exit(res)

    # app.run(debug=True, host='0.0.0.0', port=9696)