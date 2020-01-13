import pandas as import pd 

def get_train():
    train = pd.read_csv('./data/train.csv')
    return train

def get_train_labels():
    train_labels = pd.read_csv('./data/train_labels.csv')
    return train_labels

def get_assessment_users(cache=True):
if cache:
    assessment_users = pd.read_csv('./data/assessment_users.csv')
else:
    print(0)