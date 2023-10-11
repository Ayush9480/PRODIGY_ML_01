import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('train.csv')

# Initialize the model
model = LinearRegression()
X = data[['OverallQual', 'OverallCond', 'YearBuilt']]
y = data['SalePrice']
model.fit(X, y)

def predict_price():
    try:
        overall_quality = int(quality_entry.get())
        overall_condition = int(condition_entry.get())
        year_built = int(year_entry.get())
        
        new_data = pd.DataFrame({'OverallQual': [overall_quality], 'OverallCond': [overall_condition], 'YearBuilt': [year_built]})
        predicted_price = model.predict(new_data)
        result_label.config(text=f'Predicted Price: ${predicted_price[0]:,.2f}')
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("House Price Predictor")

frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Overall Quality (1-10):").grid(column=0, row=0, sticky=tk.W)
quality_entry = ttk.Entry(frame)
quality_entry.grid(column=1, row=0)

ttk.Label(frame, text="Overall Condition (1-10):").grid(column=0, row=1, sticky=tk.W)
condition_entry = ttk.Entry(frame)
condition_entry.grid(column=1, row=1)

ttk.Label(frame, text="Year Built:").grid(column=0, row=2, sticky=tk.W)
year_entry = ttk.Entry(frame)
year_entry.grid(column=1, row=2)

predict_button = ttk.Button(frame, text="Predict Price", command=predict_price)
predict_button.grid(column=0, row=3, columnspan=2)

result_label = ttk.Label(frame, text="")
result_label.grid(column=0, row=4, columnspan=2)

root.mainloop()
