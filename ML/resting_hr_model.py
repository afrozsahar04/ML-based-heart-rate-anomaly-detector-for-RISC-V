# Filter to likely resting heart rates (engineering assumption)
df_rest = df[(df['Heart rate'] >= 45) & (df['Heart rate'] <= 100)]

print("Original rows:", len(df))
print("Filtered resting rows:", len(df_rest))

Xr = np.column_stack([np.ones(len(df_rest)),
                      df_rest['Age'].values,
                      df_rest['Gender'].values])
yr = df_rest['Heart rate'].values

w_r, _, _, _ = np.linalg.lstsq(Xr, yr, rcond=None)
w0_r, w_age_r, w_gender_r = w_r

pred_r = Xr @ w_r
resid_r = yr - pred_r
mean_abs_r = np.mean(np.abs(resid_r))
std_abs_r = np.std(np.abs(resid_r))
threshold_r = mean_abs_r + 2*std_abs_r

print("\nRESTING HR MODEL")
print(" w0 =", w0_r)
print(" w_age =", w_age_r)
print(" w_gender =", w_gender_r)
print(" mean_abs =", mean_abs_r)
print(" std_abs =", std_abs_r)
print(" threshold =", threshold_r)
