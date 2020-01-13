import pandas as pd 
import warnings
warnings.filterwarnings("ignore")

def get_train():
    train = pd.read_csv('./data/train.csv')
    return train

def get_train_labels():
    train_labels = pd.read_csv('./data/train_labels.csv')
    return train_labels

def get_assessment_users(cache=True):
    if cache == True:
        assessment_users = pd.read_csv('assessment_users.csv')
        assessment_users.drop(columns = ['Unnamed: 0'], inplace = True)
        #assessment_users.head()
    else:
        train = get_train()
        train_labels = get_train_labels()
        
        df = pd.merge(train_df, train_labels, how = 'left', on = 'game_session')
        df.drop(columns = ['installation_id_y', 'title_y'], inplace = True)
        df.rename(columns = {'installation_id_x': 'installation_id', 'title_x': 'title'}, inplace = True)
        
        assessment_users = df[df.installation_id.isin(train_labels.installation_id.unique())]

        # change object type of timestamp

        assessment_users.timestamp = pd.to_datetime(assessment_users.timestamp)
        assessment_users['date'] = assessment_users['timestamp'].dt.date
        assessment_users['hour'] = assessment_users['timestamp'].dt.hour
        assessment_users['weekday'] = assessment_users['timestamp'].dt.weekday_name

        assessment_users.to_csv('assessment_users.csv')

    return assessment_users

# assessment_users = get_assessment_users()