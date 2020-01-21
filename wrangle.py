import pandas as pd 
import warnings
import os
warnings.filterwarnings("ignore")

def get_train():
    train = pd.read_csv('./train.csv')
    return train

def get_train_labels():
    train_labels = pd.read_csv('./train_labels.csv')
    return train_labels

def get_assessment_users(cache=True):
    csv_file_path = 'assessment_users.csv'
    if cache == True and os.path.exists(csv_file_path):
        assessment_users = pd.read_csv('assessment_users.csv')
        assessment_users.drop(columns = ['Unnamed: 0'], inplace = True)
        #assessment_users.head()
    else:
        train = get_train()
        train_labels = get_train_labels()
        
        df = pd.merge(train, train_labels, how = 'left', on = 'game_session')
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

def get_na_assessments(df):
    na_assessments = df[(df.type == 'Assessment') & (df.accuracy_group.isna())]
    return na_assessments.index

def get_iqr_users(df):
    assessments = df[df.type == 'Assessment'].groupby(['installation_id', 'game_session', 'accuracy_group']).count().reset_index()[['installation_id', 'game_session', 'accuracy_group']]
    assessments_count = pd.crosstab(assessments.installation_id, assessments.accuracy_group, margins = True)
    assessments_count.drop('All', inplace = True)
    q1 = assessments_count.All.quantile(0.25)
    q3 = assessments_count.All.quantile(0.75)
    iqr = q3-q1
    upper_fence = q3 + 3*iqr
    users = assessments_count[assessments_count.All <= upper_fence].index
    return users

def get_last_assessments(df):
    # sort the assessment types by timestamp
    assessments_df = df.sort_values(by=['installation_id', 'timestamp'])[df.type == 'Assessment']

    # look at the last value of the assessments_df to capture the last assessment taken ('game_session)
    assessments_df.drop_duplicates(subset = ['installation_id'], keep = 'last', inplace = True)

    last_game_sessions = assessments_df.game_session
    return last_game_sessions

def get_after_last_assessments_df(df, last_assessments):
    print('putting together after_last_assessment_df')
    print('index of items to print: ' + last_assessments.index[0] + 'to' + last_assessments.index[1])
    
    after_last_assessment_df = df[0:0]

    for i in last_assessments.index:
        after_last_assessment_df = after_last_assessment_df.append(df[(df.installation_id == last_assessments.loc[i].installation_id) & (df.timestamp > last_assessments.loc[i].timestamp)])
        print('index'+ i)
    
    return after_last_assessment_df


def prepare_df(cache=True):
    csv_file_path = 'train_maybe_final.csv'
    if cache and os.path.exists(csv_file_path):
        prepped_df = pd.read_csv(csv_file_path)
    else:
        df = get_assessment_users()
        df.timestamp = pd.to_datetime(df.timestamp)

        na_assessments = get_na_assessments(df)
        df.drop(na_assessments,inplace = True)

        #create new df1 that is only users who have <= 21 assessments.

        users = get_iqr_users(df)
        df1 = df[df.installation_id.isin(users)]

        # look at df1 that contain the 3523 installations capture the last game session information.
        last_game_sessions = get_last_assessments(df1)      
        last_assessments = df1[df1.game_session.isin(last_game_sessions)][['installation_id', 'game_session', 'timestamp', 'accuracy_group']].drop_duplicates(subset = ['installation_id'], keep = 'last') 
        last_assessments.to_csv('last_assessments.csv')

        # get a dataframe of types that happened after the last assessment.
        after_last_assessment_df = get_after_last_assessments_df(df1, last_assessments)

        # drop from the dataframe (df1) where the type happened after the last assessment
        df1.drop(after_last_assessment_df.index, inplace = True)
        df1.drop(last_assessments.index,inplace = True)

        df1.to_csv(csv_file_path)

        return df1
        
