import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer import Radar, FontManager

def analyze_threat_profiles():
    # 1. Load Data
    try:
        df = pd.read_csv('data/united_squad_2026.csv')
    except:
        print("⚠️ Data not found. Run scraper.py first.")
        return

    # 2. Define our Metrics
    # 'Threat' = Goal Scoring Potential (xG) + Box Entry (Carries)
    # 'Creativity' = Assisting (xA) + Progression (Passes)
    
    # Simple Normalization (0-1 scale) so we can compare
    for col in ['xG_p90', 'xA_p90', 'Prog_Carries_p90', 'Prog_Passes_p90']:
        df[col + '_norm'] = df[col] / df[col].max()

    # 3. Create the "Best Position" Logic
    results = []
    for _, row in df.iterrows():
        # Scorer Score (Striker Suitability)
        striker_score = (row['xG_p90_norm'] * 0.7) + (row['Prog_Carries_p90_norm'] * 0.3)
        
        # Creator Score (No. 10 / Winger Suitability)
        creator_score = (row['xA_p90_norm'] * 0.6) + (row['Prog_Passes_p90_norm'] * 0.4)
        
        results.append({
            'Player': row['Player'],
            'Best_Role': 'Striker/Inside Forward' if striker_score > creator_score else 'Playmaker/Winger',
            'Striker_Rating': round(striker_score, 2),
            'Creator_Rating': round(creator_score, 2)
        })

    results_df = pd.DataFrame(results)
    print("\n📊 --- PLAYER ROLE ANALYSIS ---")
    print(results_df)
    
    # 4. (Optional) Generate a Radar Chart for Visuals
    # Select just Bruno and Cunha for comparison
    params = ['xG_p90', 'xA_p90', 'Prog_Carries_p90', 'Prog_Passes_p90']
    
    # Check if we have data to plot
    if len(df) >= 2:
        # ... Add mplsoccer radar code here (kept simple for now) ...
        print("\n✅ Analysis complete. Use these ratings for the Optimizer.")
    
    return results_df

if __name__ == "__main__":
    analyze_threat_profiles()