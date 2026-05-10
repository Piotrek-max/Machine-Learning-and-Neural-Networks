import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.graphics.gofplots import qqplot


def analyze_normality(df, columns):
    results = []
    fig, axes = plt.subplots(len(columns), 2, figsize=(12, 4 * len(columns)))

    for i, col in enumerate(columns):
        # Shapiro-Wilk
        stat, p = stats.shapiro(df[col].sample(min(len(df), 5000)))
        skew_val = stats.skew(df[col].dropna())
        results.append({'Feature': col, 'Shapiro-Stat': stat, 'p-value': p, 'Skewness': skew_val})

        # QQ-Plot
        stats.probplot(df[col].dropna(), dist="norm", plot=axes[i, 0])
        axes[i, 0].set_title(f"QQ Plot: {col}")

        # Histogram
        axes[i, 1].hist(df[col].dropna(), bins=30, color='skyblue', edgecolor='black')
        axes[i, 1].set_title(f"Histogram: {col} (Skew: {skew_val:.2f})")

    plt.tight_layout()
    plt.show()
    return pd.DataFrame(results)