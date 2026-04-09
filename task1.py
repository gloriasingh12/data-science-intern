# =================================================================
# PROJECT: Automated Data ETL Pipeline
# DESCRIPTION: Extract, Transform, and Load (ETL) using Pandas & Scikit-Learn.
# DELIVERABLE: Python script automating the end-to-end data flow.
# =================================================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

class DataPipeline:
    def __init__(self):
        print("⚙️  Initializing ETL Pipeline Engine...")
        self.scaler = StandardScaler()
        self.encoder = LabelEncoder()

    def extract(self):
        """STEP 1: EXTRACT - Loading Raw Data (Simulated CSV)"""
        print("\n📥 [EXTRACT] Loading raw data from sources...")
        raw_data = {
            'ID': [101, 102, 103, 104, 105],
            'Age': [25, np.nan, 35, 40, 28],
            'City': ['Noida', 'Delhi', 'Noida', 'Mumbai', 'Delhi'],
            'Salary': [50000, 60000, 75000, np.nan, 52000]
        }
        return pd.DataFrame(raw_data)

    def transform(self, df):
        """STEP 2: TRANSFORM - Data Cleaning & Scaling"""
        print("🔄 [TRANSFORM] Cleaning and processing data...")
        
        # 1. Handling Missing Values (Imputation)
        df['Age'] = df['Age'].fillna(df['Age'].mean())
        df['Salary'] = df['Salary'].fillna(df['Salary'].median())
        
        # 2. Feature Encoding (Converting Text to Numbers)
        df['City_Code'] = self.encoder.fit_transform(df['City'])
        
        # 3. Feature Scaling (Normalization)
        df[['Age', 'Salary']] = self.scaler.fit_transform(df[['Age', 'Salary']])
        
        print("✅ Transformation complete: Missing values handled & Features scaled.")
        return df

    def load(self, df):
        """STEP 3: LOAD - Saving Clean Data to 'Warehouse'"""
        print("📤 [LOAD] Saving processed data to 'clean_analytics_db'...")
        # In a real scenario, this would be: df.to_sql('table', engine)
        print("\n--- 💎 FINAL PROCESSED DATASET (ETL OUTPUT) ---")
        print(df.head())
        print("-" * 45)
        return True

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    pipeline = DataPipeline()

    # Run the ETL Flow (Deliverable)
    raw_df = pipeline.extract()
    processed_df = pipeline.transform(raw_df)
    pipeline.load(processed_df)

    print("\n✅ Task 45 Complete: Automated ETL Pipeline Verified.")
