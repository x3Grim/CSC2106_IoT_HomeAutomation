from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def model_training(x,y):
    # Assume X contains your feature data, and y contains your labels (asleep or awake)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Initialize and train the model (example with Random Forest)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')


#based on pressure sensor data, predict if user is moving or stationary & sleeping
#can use for plotting movement over time graph in dashboard
def movement_prediction():
    # get pressure sensor data from database

    #if no change over a certain period, then count as stationary
    #if change in pressure sensor value detected, then count as moved

    return


def sleep_state_prediction():
    # get heart rate data
    # use movement_prediction data

    # train model to predict sleep state
    # if not moving, do heart rate AI stuff 
    model_training()

    pass


def main():
    # Call the movement prediction function
    movement_prediction()

    # define nominal sleep state
    # sleep_state = ["awake", "light", "deep", "rem"]

    # return sleep state
    # return nominal_sleep_state

    sleep_state_prediction()

    pass