import os
import numpy as np
import pandas as pd

def add_gaussian_noise(
    df: pd.DataFrame,
    noise_pct: float,
    random_state: int = 42,
    target_col: str = None
) -> pd.DataFrame:

    rng = np.random.RandomState(random_state)
    df_noisy = df.copy()

    # pick only numeric columns, and drop the target if specified
    num_cols = df.select_dtypes(include=[np.number]).columns
    if target_col is not None and target_col in num_cols:
        num_cols = num_cols.drop(target_col)

    # compute per-column std-dev
    stds = df[num_cols].std(ddof=1)

    # draw noise for each feature column
    noise = rng.normal(
        loc=0.0,
        scale=stds * noise_pct,
        size=df[num_cols].shape
    )

    # inject noise into features only
    df_noisy[num_cols] = df[num_cols] + noise
    return df_noisy

# ----

input_path = 'new data/plane/train.csv'   # <- change this to your CSV’s path
df = pd.read_csv(input_path)

base_name = os.path.splitext(os.path.basename(input_path))[0]

# output directory exists
out_dir = 'new noise'                       
os.makedirs(out_dir, exist_ok=True)

for pct in [0.10, 0.15, 0.20]:
    df_noisy = add_gaussian_noise(
        df,
        noise_pct=pct,
        random_state=42,
        target_col='satsifaction'          # <- replace with your actual label column
    )
    out_fname = os.path.join(
        out_dir,
        f"plane_{base_name}-noise-{int(pct*100)}.csv"
    )
    df_noisy.to_csv(out_fname, index=False)
    print(f"Wrote {out_fname} (with {int(pct*100)}% noise)")
