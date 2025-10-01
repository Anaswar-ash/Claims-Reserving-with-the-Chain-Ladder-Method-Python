

import chainladder as cl
import matplotlib.pyplot as plt

print("chain-Ladder Analysis Initialized (Python)")

# --- 1. LOAD DATA ---
# The python 'chainladder' library also comes with sample datasets.
# We will use the same `raa` dataset for consistency.
print("Step 1: Loading sample data (RAA dataset)")
raa = cl.load_dataset('raa')

# Print the original claims development triangle.
# The data is stored in a Triangle object, which is built on pandas.
print("Original Claims Development Triangle:")
print(raa)
print("\n")

# --- 2. APPLY THE CHAIN-LADDER MODEL ---
# The process is object-oriented. We create a Chainladder model
# and then fit it to our data.
print("Step 2: Applying the Chain-Ladder model")

# Instantiate and fit the model
cl_model = cl.Chainladder()
cl_model.fit(raa)

# The model object now contains all the results.

# --- 3. ANALYZE AND SUMMARIZE RESULTS ---
# You can access different pieces of the analysis directly from the fitted model.

# Print the completed triangle with projections
print("Completed Claims Triangle (with Projections):")
print(cl_model.full_triangle_)
print("\n")

# Print the summary table
print("Chain-Ladder Model Summary:")
print(cl_model.summary_)
print("\n")

# Explanation of Summary Columns:
# - Latest: The most recent diagonal of known claims.
# - Ultimate: The projected total claims for each origin year.
# - IBNR: Incurred But Not Reported reserve (Ultimate - Latest).

# Get the total IBNR (reserve) estimate
total_ibnr = cl_model.ibnr_.sum()

print("..................................................")
print(f"Total IBNR (Reserve) Estimate: {total_ibnr:,\.2f}")
print("..................................................")

# --- 4. VISUALIZE MODEL FIT AND RESULTS ---
# The library has a built-in plot method that uses matplotlib.
print("Step 3: Generating and saving model diagnostic plots")

# The plot() method creates a figure with multiple useful subplots.
fig = cl_model.plot()

# Save the entire figure to a file
plt.savefig("Python_ChainLadder_Plots.png")

print("\n--- Analysis Complete ---")
print("Plots have been saved to the file: Python_ChainLadder_Plots.png")
