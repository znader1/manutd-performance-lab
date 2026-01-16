import pandas as pd
import numpy as np
from scipy.optimize import linear_sum_assignment

def optimize_lineup():
    """
    Uses the Hungarian Algorithm to fit players into a 4-2-3-1
    based on their calculated ratings.
    """
    # 1. Mock Data based on Analyzer (or load real analysis)
    # Let's say the analyzer gave us these "Fitness Scores" for positions:
    # Rows: [Bruno, Cunha, Mbeumo, Amad]
    # Cols: [LW, AM, RW, ST]
    
    # Example logic: 
    # Bruno is elite at AM (0.95), good at RW (0.6)
    # Cunha is elite at ST (0.9), good at LW (0.7)
    # Mbeumo is elite at RW (0.9), okay at ST (0.6)
    # Amad is elite at LW/RW (0.85), okay at AM (0.7)
    
    players = ["Bruno", "Cunha", "Mbeumo", "Amad"]
    positions = ["LW", "AM", "RW", "ST"]
    
    # The 'Cost Matrix' (Higher is better, so we use negative for minimization)
    # [LW, AM, RW, ST]
    ratings = np.array([
        [0.50, 0.95, 0.60, 0.40], # Bruno
        [0.70, 0.60, 0.40, 0.90], # Cunha
        [0.40, 0.50, 0.90, 0.60], # Mbeumo
        [0.85, 0.70, 0.85, 0.30]  # Amad
    ])
    
    # Invert for Hungarian Algorithm (which finds lowest cost)
    cost_matrix = 1 - ratings 
    
    # 2. Run Optimization
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    
    print("\n🚀 --- OPTIMAL TACTICAL CONFIGURATION (4-2-3-1) ---")
    total_score = 0
    for i in range(len(row_ind)):
        player = players[row_ind[i]]
        pos = positions[col_ind[i]]
        score = ratings[row_ind[i], col_ind[i]]
        total_score += score
        print(f"📍 {pos}: {player} (Fit Score: {score})")
        
    print(f"🏆 System Efficiency: {round(total_score, 2)} / 4.00")

if __name__ == "__main__":
    optimize_lineup()