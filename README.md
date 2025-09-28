# Claims-Reserving-with-the-Chain-Ladder-Method-Python

This project demonstrates a fundamental actuarial technique—claims reserving using the Chain-Ladder method. It is implemented in Python using the `chainladder` library, a popular choice for actuarial analysis.

## Objective

The goal is to analyze a claims development triangle to project the ultimate cost of claims and determine the Incurred But Not Reported (IBNR) reserve. This is the Python equivalent of the R project.

## Files in this Repository

- `chain_ladder_analysis.py`: The main Python script that performs the analysis.
- `requirements.txt`: A file listing the necessary Python packages (`chainladder`, `pandas`, `matplotlib`).
- `README.md`: This file, providing an overview and instructions for the Python project.
- `.gitignore`: A standard Python gitignore file.
- `Python_ChainLadder_Plots.png`: A PNG file that is **generated** by the script, containing model diagnostic plots.

## Prerequisites

- **Python 3**: You must have Python 3 installed on your system.
- **pip**: Python's package installer, which typically comes with Python.

## How to Run the Analysis

1.  **Navigate to the Project Directory**: Open your terminal or command prompt and navigate to the `Python_ChainLadder_Project` folder.
    ```bash
    cd path/to/your/Python_ChainLadder_Project
    ```

2.  **Create a Virtual Environment (Recommended)**: It is best practice to create a virtual environment to manage project dependencies.
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**: Install the required packages using pip and the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Script**: Execute the main Python script.
    ```bash
    python chain_ladder_analysis.py
    ```

## Understanding the Output

When you run the script, the console will display:

1.  **Original Claims Triangle**: The raw input data.
2.  **Completed Claims Triangle**: The data with future claims projected by the model.
3.  **Chain-Ladder Model Summary**: A table showing the `Ultimate` cost, `Latest` paid claims, and `IBNR` reserve for each origin year.
4.  **Total IBNR Estimate**: The final, total reserve required.

A file named `Python_ChainLadder_Plots.png` will also be saved in the project directory with several diagnostic plots.