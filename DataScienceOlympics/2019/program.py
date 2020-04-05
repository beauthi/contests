import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
import io, math, requests

# Train sample
req = pd.read_csv('data/train_requests.csv', sep=',', low_memory=False, error_bad_lines=False)

X_additional = pd.read_csv('data/train_individuals.csv', sep=',', low_memory=False, error_bad_lines=False)
test_additional = pd.read_csv('data/test_individuals.csv', sep=',', low_memory=False, error_bad_lines=False)

# Test sample
test_requests = pd.read_csv('data/test_requests.csv', sep=',', low_memory=False, error_bad_lines=False)

ids = list(test_requests['request_id'])

# Only works in Python3, see comment below for Python2
def submit_prediction(df, sep=',', **kwargs):
    # TOKEN to recover on the platform: "Submissions"> "Submit from your Python Notebook"
    TOKEN='f728a718e71694ec2460748ca79b8bf13d9a006f37b8ab3672487631a8415661a511a834777bcd58eba2b2042fc4dee710cc306d8cf83659932896a562f32346'
    URL='https://qscore.datascience-olympics.com/api/submissions'
    #buffer = io.BytesIO() # Python 2
    buffer = io.StringIO() # Python 3
    df.to_csv(buffer, index=False, sep=sep, **kwargs)
    buffer.seek(0)
    r = requests.post(URL, headers={'Authorization': 'Bearer {}'.format(TOKEN)},files={'datafile': buffer})
    if r.status_code == 429:
        raise Exception('Submissions are too close. Next submission is only allowed in {} seconds.'.format(int(math.ceil(int(r.headers['x-rate-limit-remaining']) / 1000.0))))
    if r.status_code != 200:
        raise Exception(r.text)

def competition_scorer(y_true, y_pred):
    return log_loss(y_true, y_pred, sample_weight=10**y_true)


req = pd.merge(req, X_additional, on=['request_id'])
test_requests = pd.merge(test_requests, test_additional, on=['request_id'])

columns = ['district',
           'housing_situation_id',
           'group_composition_id',
           'housing_situation_2_id'
           #'group_composition_label',
           #'group_type'
           ]

X = req[columns]
y = req['granted_number_of_nights']

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.33, random_state=37)

X_train = X_train.fillna(0)
#X_train['group_composition_label'] = X_train['group_composition_label'].astype(str)
#X_train['group_type'] = X_train['group_type'].astype(str)
le = preprocessing.LabelEncoder()
le1 = preprocessing.LabelEncoder()
#le.fit(X_train['group_composition_label'])
#le1.fit(X_train['group_type'])

X_train = X_train[columns]
#X_train['group_composition_label'] = le.transform(X_train['group_composition_label'])
#X_train['group_type'] = le1.transform(X_train['group_type'])

model = RandomForestClassifier(n_estimators=10, class_weight="balanced")#solver='liblinear', multi_class='ovr')
model.fit(X_train, y_train)

x_val = X_val[columns]
#x_val['group_composition_label'] = le.transform(x_val['group_composition_label'])
#x_val['group_type'] = le1.transform(x_val['group_type'])

#print(competition_scorer(y_val, model.predict_proba(x_val)))

df = pd.concat([test_requests['request_id'], pd.DataFrame(model.predict_proba(test_requests[columns]))], axis=1)

submission = df.drop_duplicates(subset='request_id', keep="last")

submit_prediction(submission)
