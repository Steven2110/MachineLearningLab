import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the best model using pickle
with open('rf_model.pkl', 'rb') as model_file:
    best_model = pickle.load(model_file)

# Function to make predictions
def predict():
    try:
        season_1 = False
        season_2 = False
        season_3 = False
        season_4 = False

        holiday_0 = False
        holiday_1 = False

        workingday_0 = False
        workingday_1 = False

        weather_condition_1 = False
        weather_condition_2 = False
        weather_condition_3 = False

        year_0 = False
        year_1 = False

        # Get input values from the entry widget
        month = int(entry_month.get())
        weekday = int(entry_weekday.get())
        humidity = float(entry_humidity.get())
        temp = float(entry_temp.get())
        windspeed = float(entry_windspeed.get())
        # Categorical
        season = int(entry_season.get()) # 1, 2, 3, 4
        holiday = int(entry_holiday.get()) # 0, 1
        workingday = int(entry_workingday.get()) # 0, 1
        weather_condition = int(entry_weather_condition.get()) # 1, 2, 3
        year = int(entry_year.get()) # 0, 1
        

        if season == 1:
            season_1 = True
        elif season == 2:
            season_2 = True
        elif season == 3:
            season_3 = True
        elif season == 4:
            season_4 = True

        if holiday == 0:
            holiday_0 = True
        elif holiday == 1:
            holiday_1 = True

        if workingday == 0:
            workingday_0 = True
        elif workingday == 1:
            workingday_1 = True

        if weather_condition == 1:
            weather_condition_1 = True
        elif weather_condition == 2:
            weather_condition_2 = True
        elif weather_condition == 3:
            weather_condition_3 = True

        if year == 0:
            year_0 = True
        elif year == 1:
            year_1 = True

        # Make a prediction using the loaded model
        input_data = np.array([[month, weekday, humidity, temp, 
                                windspeed, season_1, season_2, 
                                season_3, season_4, holiday_0,
                                holiday_1, workingday_0, workingday_1,
                                weather_condition_1, weather_condition_2, 
                                weather_condition_3, year_0, year_1]])
        prediction = best_model.predict(input_data)
        # Display the prediction
        messagebox.showinfo('Prediction Result', f'The predicted number of rented bicycle is: {int(prediction[0])}')
        # messagebox.showinfo('Prediction Result', f'SUCCESS')

    except ValueError:
        messagebox.showerror('Error', 'Invalid input. Please enter numeric values.')

# GUI setup
app = tk.Tk()
app.title('Bicycle Rent Predictor')

# Entry widgets for user input
labels = ['Humidity', 'Temp', 'Windspeed', 'Year', 'Month', 'Weekday', 'Season', 'Holiday', 'Workingday', 'Weather Condition']
extra_labels = ['Month', 'Weekday', 'Season', 'Holiday', 'Workingday', 'Weather Condition', 'Year']

extra_labels_dict = {
    'Month': '1 - 12, where it represents the month in numerical',
    'Weekday': '0: Sun; 1: Mon; 2: Tue; 3: Wed; 4: Thu; 5: Fri; 6: Sat',
    'Season': '1: Winter; 2: Spring; 3: Summer; 4: Fall',
    'Holiday': '0: Non holiday; 1: Holiday',
    'Workingday': '0: Non workday; 1: Workday',
    'Weather Condition': '1: Clear; 2: Mist + Cloudy; 3: Light snow/rain; 4: Heavy rain/thunderstorm',
    'Year': '0: 2011; 1: 2012'
}

entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(app, text=label_text + ':')
    label.grid(row=i, column=0)
    entry = tk.Entry(app)
    entry.grid(row=i, column=1)
    entries.append(entry)
    if label_text in extra_labels:
        label = tk.Label(app, text=extra_labels_dict[label_text])
        label.grid(row=i, column=2)
    

# Assigning entry widgets to variables
(entry_humidity, entry_temp, entry_windspeed, entry_year, 
 entry_month, entry_weekday, entry_season, entry_holiday,
 entry_workingday, entry_weather_condition) = entries

# Button to trigger prediction
predict_button = tk.Button(app, text='Predict', command=predict)
predict_button.grid(row=len(labels), column=0, columnspan=2)

# Run the application
app.mainloop()