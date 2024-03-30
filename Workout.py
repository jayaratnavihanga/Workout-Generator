import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Function to generate the workout plan
def generate_workout():
    # Taking user input
    input_calories = int(calories_entry.get())
    if input_calories > 300:
        input_calories = 300

    predicted_workout = model.predict([[0, 0, input_calories]])  # Predict the workout

    selected_exercises = data[data['TotalCaloriesBurnt'] <= predicted_workout[0] + 10]  # Select exercises
    selected_exercises = selected_exercises.sample(n=5)  # Select 5 exercises

    # Display the workout plan
    workout_text.delete(1.0, tk.END)
    workout_text.insert(tk.END, "Exercise                                 Sets    Reps\n")
    for index, row in selected_exercises.iterrows():
        workout_text.insert(tk.END, f"{row['Exercise']: <40}{row['Sets']: <8}{row['Reps']: <6}\n")

# Load the dataset
file_path = "exercises - Easy Workouts.csv"
data = pd.read_csv(file_path)

# Initialize the model
model = RandomForestRegressor()
X = data[['Sets', 'Reps', 'ExerciseCaloriesBurnt']]
y = data['TotalCaloriesBurnt']
model.fit(X, y)

# Create the main window
root = tk.Tk()
root.title("FitFlow - Workout Generator")

# Create and place widgets
calories_label = ttk.Label(root, text="Desired Calorie Expenditure:")
calories_label.grid(row=0, column=0, padx=5, pady=5)

calories_entry = ttk.Entry(root)
calories_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = ttk.Button(root, text="Generate Workout", command=generate_workout)
generate_button.grid(row=0, column=2, padx=5, pady=5)

workout_text = tk.Text(root, height=10, width=50)
workout_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Run the application
root.mainloop()







