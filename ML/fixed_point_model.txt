# ============================
# FIXED-POINT MODEL (Q10.6)
# ============================
SCALE = 64  # 2^6

w0_fx = 4900
w_age_fx = -3
w_gender_fx = -43
threshold_fx = 1447


def predict_hr_fixed(age, gender):
    """
    Fixed-point prediction
    """
    acc = w0_fx
    acc += w_age_fx * age
    acc += w_gender_fx * gender
    return acc  # still scaled


# ============================
# USER INPUT
# ============================
age = int(input("Enter Age: "))
gender = int(input("Enter Gender (0=Female, 1=Male): "))
measured_hr = float(input("Enter Measured HR: "))

# Fixed-point prediction
pred_fx = predict_hr_fixed(age, gender)

# Convert back to float (for comparison only)
pred_float_from_fx = pred_fx / SCALE

error_fx = abs(measured_hr * SCALE - pred_fx)

print("\n===== FIXED-POINT RESULT =====")
print(f"Predicted HR (fixed->float): {pred_float_from_fx:.2f} bpm")
print(f"Measured HR                : {measured_hr:.2f} bpm")
print(f"Error (fixed)              : {error_fx / SCALE:.2f} bpm")
print(f"Threshold                  : {threshold_fx / SCALE:.2f} bpm")

if error_fx > threshold_fx:
    print("❌ ANOMALY DETECTED (fixed-point)")
else:
    print("✅ Normal (fixed-point)")
