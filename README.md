# PBS-KIDS Project README

# Goals

The goal of the project is "to gain insights into how media can help children learn important skills for success in school and life" (Kaggle, 2019). We have been invited "to predict scores on in-game assessments and create an algorithm that will lead to better-designed games and improved learning outcomes" (Kaggle).

Information from Kaggle:

"The intent of the competition is to use the gameplay data to forecast how many attempts a child will take to pass a given assessment (an incorrect answer is counted as an attempt). Each application install is represented by an installation_id. This will typically correspond to one child, but you should expect noise from issues such as shared devices. In the training set, you are provided the full history of gameplay data. In the test set, we have truncated the history after the start event of a single assessment, chosen randomly, for which you must predict the number of attempts. Note that the training set contains many installation_ids which never took assessments, whereas every installation_id in the test set made an attempt on at least one assessment.

The outcomes in this competition are grouped into 4 groups (labeled accuracy_group in the data):

    3: the assessment was solved on the first attempt

    2: the assessment was solved on the second attempt

    1: the assessment was solved after 3 or more attempts

    0: the assessment was never solved

# Deliverables

1. Presentation with slide show
2. Jupyter notebook documenting our process
3. Modules containing any functions needed to run our notebook
4. A csv file with the installation_id (unique user identifier) and the prediction of the accuracy_group (number of attempts to pass an assessment).
5. A brochure with process and tool diagrams

# Data Dictionary

- Size of train data (11341042, 9)

- Size of train_labels data (17690, 7)

- Size of specs data (386, 3)

- Size of test data (1156414, 9)

## -> train.csv and test.csv

event_id - Randomly generated unique identifier for the event type. Maps to event_id column in specs table.

game_session - Randomly generated unique identifier grouping events within a single game or video play session.

timestamp - Client-generated datetime

event_data - Semi-structured JSON formatted string containing the events parameters. Default fields are: 

event_count, event_code, and - - game_time; otherwise fields are determined by the event type.

installation_id - Randomly generated unique identifier grouping game sessions within a single installed application instance.

event_count - Incremental counter of events within a game session (offset at 1). Extracted from event_data.

event_code - Identifier of the event 'class'. Unique per game, but may be duplicated across games. E.g. event 

code '2000' always - - - - identifies the 'Start Game' event for all games. Extracted from event_data.

game_time - Time in milliseconds since the start of the game session. Extracted from event_data.

title - Title of the game or video.

type - Media type of the game or video. Possible values are: 'Game', 'Assessment', 'Activity', 'Clip'.

world - The section of the application the game or video belongs to. Helpful to identify the educational 

curriculum goals of the media. Possible values are: 'NONE' (at the app's start screen), TREETOPCITY' (Length/Height), 'MAGMAPEAK' (Capacity/Displacement), 'CRYSTALCAVES' (Weight).

## -> specs.csv

event_id - Global unique identifier for the event 
type. Joins to event_id column in events table.


info - Description of the event.

args - JSON formatted string of event arguments. 
    
Each argument contains:
    
    name - Argument name.

    type - Type of the argument (string, int, number, object, array).

    info - Description of the argument.

Each argument contains:
name - Argument name.

type - Type of the argument (string, int, number, object, array).

info - Description of the argument.
