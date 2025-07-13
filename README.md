# Going-Beyond-Majority-Vote-Composite-Aware-Soft-Voting-in-Random-Forests

The provided code was shared via our Google Co-Lab.

Please see the lines below in our SWAV.pynb file for adjustments to dataset configuration, target columns, or any of the listed perameters.

# === User configuration ===
* FILE_PATH = "/content/personality_dataset.csv"  # Path to your data file (.csv or .data)
* TARGET_COLUMN = 'Personality'          # Name of the target column, or None to auto-detect
* TEST_SIZE = 0.2                    # Fraction of data to reserve for testing
* VAL_SIZE = 0.25                    # Fraction of train+val data to reserve for validation
* N_ESTIMATORS = 100                 # Number of trees in each Random Forest
* RANDOM_STATE = 42                  # Random seed for reproducibility
* TEMPERATURE = 1.0                  # Softmax temperature (<1 -> sharper; >1 -> smoother)
* COMPOSITE_WEIGHTS = [1.0, 1.0, 1.0, 1.0]  # [accuracy, precision, recall, f1]

Please note there are three python programs listed in the file we have shared. They vary in their preprocessing which allowed us to run our experiments on a wider variety of datasets.


You can replicate our noise results through our noisydata google drive or attempt your own using our noiseapply.py please see in file commments for instruction.

https://drive.google.com/drive/folders/1N4ucHox0WQkYBHVgoYM_BNhKUBm6fxw-?usp=drive_link

Important: Please note that you must replace the line for the BankMarketing.csv files

df = pd.read_csv('your_file.csv')
with
df = pd.read_csv('your_file.csv', sep=';')
