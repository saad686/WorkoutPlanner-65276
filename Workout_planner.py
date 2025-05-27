import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # convert cm to meters
    return weight / (height_m ** 2)

def suggest_plan(bmi):
    if bmi < 18.5:
        return ("🏋️ Workout: 20 mins light exercise\n🍽️ Diet: High-calorie diet, focus on protein and carbs")
    elif 18.5 <= bmi < 25:
        return ("🏋️ Workout: 30 mins moderate exercise\n🍽️ Diet: Balanced diet with veggies, protein, and healthy fats")
    elif 25 <= bmi < 30:
        return ("🏋️ Workout: 45 mins cardio + strength\n🍽️ Diet: Low-carb, high-protein meals")
    else:
        return ("🏋️ Workout: 60 mins intense cardio\n🍽️ Diet: Very low-carb, avoid sugar and processed food")

def suggest_plan(bmi):
    if bmi < 18.5:
        return (
            "🏋️ Workout: 20 mins light exercise\n"
            "📍 Location: Home\n"
            "🍽️ Diet: High-calorie diet, focus on protein and carbs"
        )
    elif 18.5 <= bmi < 25:
        return (
            "🏋️ Workout: 30 mins moderate exercise\n"
            "📍 Location: Home or Gym\n"
            "🍽️ Diet: Balanced diet with veggies, protein, and healthy fats"
        )
    elif 25 <= bmi < 30:
        return (
            "🏋️ Workout: 45 mins cardio + strength\n"
            "📍 Location: Gym recommended\n"
            "🍽️ Diet: Low-carb, high-protein meals"
        )
    else:
        return (
            "🏋️ Workout: 60 mins intense cardio\n"
            "📍 Location: Gym required for equipment\n"
            "🍽️ Diet: Very low-carb, avoid sugar and processed food"
        )



def on_submit():
    try:
        weight_input = weight_entry.get().strip()
        height_input = height_entry.get().strip()

        if not weight_input or not height_input:
            raise ValueError("Input fields cannot be empty.")

        weight = float(weight_input)
        height = float(height_input)

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = calculate_bmi(weight, height)
        bmi_label.config(text=f"📊 Your BMI is: {bmi:.2f}")

        plan = suggest_plan(bmi)
        plan_text.config(state="normal")
        plan_text.delete(1.0, tk.END)
        plan_text.insert(tk.END, plan)
        plan_text.config(state="disabled")

    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")

# Create main window
root = tk.Tk()
root.title("Workout Time Planner")
root.geometry("400x350")
root.resizable(False, False)

# Input Frame
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

tk.Label(frame, text="Enter your weight (kg):").grid(row=0, column=0, sticky="w")
weight_entry = tk.Entry(frame, width=20)
weight_entry.grid(row=0, column=1)

tk.Label(frame, text="Enter your height (cm):").grid(row=1, column=0, sticky="w", pady=10)
height_entry = tk.Entry(frame, width=20)
height_entry.grid(row=1, column=1, pady=10)

submit_btn = tk.Button(frame, text="Get Plan", command=on_submit)
submit_btn.grid(row=2, columnspan=2, pady=10)

# Output
bmi_label = tk.Label(root, text="", font=("Arial", 12))
bmi_label.pack()

plan_text = tk.Text(root, height=6, width=45, wrap="word", state="disabled", font=("Arial", 10))
plan_text.pack(pady=10)

root.mainloop()
