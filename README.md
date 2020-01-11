# PBS-KIDS Project README

# Goals

The goal of the project is to look for the drivers of children’s success on assessments in the PBS-KIDS Measure Up! application. The insights can inform teachers and parents on how 3-5-year old children learn. Our team will deliver a presentation documenting our findings and recommendations.

We acquired our data from the current Kaggle competition featured in Booz Allen Hamilton's Data Science Bowl. The writeup for the competition reads:

"The intent of the competition is to use the gameplay data to forecast how many attempts a child will take to pass a given assessment (an incorrect answer is counted as an attempt). Each application install is represented by an installation_id. This will typically correspond to one child, but you should expect noise from issues such as shared devices. In the training set, you are provided the full history of gameplay data. In the test set, we have truncated the history after the start event of a single assessment, chosen randomly, for which you must predict the number of attempts. Note that the training set contains many installation_ids which never took assessments, whereas every installation_id in the test set made an attempt on at least one assessment.

The learning path is designed as follows:

 Exposure(video clip) -> Exploration(activity) -> Practice(game) -> Demonstration(assessment). Users may follow the learning paths or choose their own at will.

The outcomes of the assessments are lumped into four groups (labeled accuracy_group in the data):

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

- Size of incoming train data (11341042, 9)

- Size of incoming train_labels data (17690, 7)

- Size of incoming specs data (386, 3)

- Size of incoming test data (1156414, 9)

## -> train.csv and test.csv

event_id - Randomly generated unique identifier for the event type. Maps to event_id column in specs table. **Each event_id is associated with only one event_code.**

    ‘Clip’ types all have the same event_id:  ‘27253bdc’

game_session - Randomly generated unique identifier grouping events within a single game or video play session.

timestamp - Client-generated datetime

event_data - Semi-structured JSON formatted string containing the events parameters. Default fields are: 

event_count, event_code, and - - game_time; otherwise fields are determined by the event type.

installation_id - Randomly generated unique identifier grouping game sessions within a single installed application instance.

event_count - Incremental counter of events within a game session (offset at 1). Extracted from event_data.

event_code - Identifier of the event 'class'. Unique per game, but may be duplicated across games. Extracted from event_data. **Each event_code is associated with multiple event_ids.**

    E.g. event_code(s)

    '2000' always identifies the 'Start Game' event for all games. Extracted from event_data.

    '4100' and '4110' identify assessment attempts. 

game_time - Time in milliseconds since the start of the game session. Extracted from event_data.

title - Title of the game or video.

type - Media type of the game or video. Possible values are: 'Game', 'Assessment', 'Activity', 'Clip'.

world - The section of the application the game or video belongs to. Helpful to identify the educational 
curriculum goals of the media. 

    Possible values are: 

    'NONE' (at the app's start screen)
    'TREETOPCITY' (Length/Height)
    'MAGMAPEAK' (Capacity/Displacement) 'CRYSTALCAVES' (Weight)

## -> train_labels.csv: 
This file demonstrates how to compute the ground truth for the assessments in the training set.

game_session - Randomly generated unique identifier grouping events within a single game or video play session.

installation_id - Randomly generated unique identifier grouping game sessions within a single installed application instance.

title - title of game, assessment, activity, or clip

num_correct - int number of correct responses on an assessment

num_incorrect - int number of incorrect responses on an assessment

accuracy - float between 0 and 1

accuracy_group - int 0, 1, 2, or 3 that denotes if the user passed the assessment in one (3), two (2), or three (1) times or never passed the assessment (0).

## -> specs.csv

event_id - Global unique identifier for the event 
type. Joins to event_id column in events table.

info - Description of the event.

args - JSON formatted string of event arguments. 
    
    Each argument contains:
    
    name - Argument name.
    type - Type of the argument (string, int, number, object, array).
    info - Description of the argument.
