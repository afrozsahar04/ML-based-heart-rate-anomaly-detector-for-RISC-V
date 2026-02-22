# Interactive HR anomaly checker + regression plot
import numpy as np
import matplotlib.pyplot as plt

# --- Model constants from filtered resting HR training ---
w0 = 76.56197402980125
w_age = -0.040135531120197694
w_gender = -0.6671994780701134
threshold = 22.60455317973597  # bpm

# --- Step 1: Ask user for inputs ---
try:
    age = float(input("Enter Age (years): "))
    gender = input("Enter Gender (0 for Female, 1 for Male): ").strip()
    if gender.lower() in ['m','male','1']:
        gender = 1
    else:
        gender = 0
    measured_hr = float(input("Enter Measured Heart Rate (bpm): "))
except Exception as e:
    print("Invalid input! Use numbers only.")
    raise e

# --- Step 2: Compute predicted HR ---
predicted_hr = w0 + w_age * age + w_gender * gender
error = abs(measured_hr - predicted_hr)

# --- Step 3: Compare with threshold ---
is_anomaly = error > threshold
print("\nPredicted Resting HR: {:.2f} bpm".format(predicted_hr))
print("Measured HR: {:.2f} bpm".format(measured_hr))
print("Absolute difference: {:.2f} bpm".format(error))
print("Threshold: {:.2f} bpm".format(threshold))
if is_anomaly:
    print("⚠️ Anomaly detected!")
else:
    print("✅ Heart rate is normal (within expected range).")

# --- Step 4: Plot linear regression lines for sanity check ---
age_range = np.linspace(0, 100, 200)
hr_female = w0 + w_age * age_range + w_gender * 0
hr_male   = w0 + w_age * age_range + w_gender * 1

plt.figure(figsize=(8,5))
plt.plot(age_range, hr_female, label="Female (Gender=0)", color='pink')
plt.plot(age_range, hr_male, label="Male (Gender=1)", color='blue')
plt.scatter(age, measured_hr, color='red', s=80, label="Your HR")
plt.scatter(age, predicted_hr, color='green', s=80, label="Predicted HR")

plt.xlabel("Age (years)")
plt.ylabel("Heart Rate (bpm)")
plt.title("Resting HR Linear Regression")
plt.legend()
plt.grid(True)
plt.show()

