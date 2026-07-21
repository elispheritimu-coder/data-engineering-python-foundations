# ============================================
# EMPLOYEE ATTRITION ANALYSIS
# Analyst: Elispher N. | BSc Statistics
# Dataset: Employee Attrition Survey
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ── Load the data ────────────────────────────
df = pd.read_csv('Employee Attrition.csv')

# ── Question 1: Statistical Summary ──────────
print("=" * 55)
print("QUESTION 1 — DATASET OVERVIEW & SUMMARY")
print("=" * 55)
print(f"\nTotal Employees: {df.shape[0]}")
print(f"Total Variables: {df.shape[1]}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nMissing Values:\n{df.isnull().sum()}")
print(f"\nStatistical Summary:")
print(df.describe())
