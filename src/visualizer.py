import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch
from scipy.ndimage import gaussian_filter

def generate_synthetic_data(player_name, role="Creative"):
    """
    Generates MOCK event data (X, Y coordinates) to simulate a player's heatmap.
    This proves to the recruiter you can handle Event Data structures.
    """
    np.random.seed(42)
    n_events = 150 # Number of touches to simulate
    
    # Standard Pitch: 120x80 (StatsBomb Format)
    if player_name == "Bruno Fernandes":
        # Central + Left Half Space (Zone 14)
        x = np.random.normal(90, 10, n_events) # High up the pitch
        y = np.random.normal(40, 15, n_events) # Central
    
    elif player_name == "Amad Diallo":
        # Right Wing + Cutting Inside
        x = np.random.normal(95, 8, n_events) 
        y = np.random.normal(65, 10, n_events) # Right side (Y=80 is top)

    elif player_name == "Matheus Cunha":
        # Striker / False 9 (Drifting Left)
        x = np.random.normal(100, 10, n_events)
        y = np.random.normal(30, 12, n_events)
        
    elif player_name == "Bryan Mbeumo":
        # Right Wing / Wide Forward
        x = np.random.normal(85, 12, n_events)
        y = np.random.normal(70, 8, n_events)

    else:
        # Generic Midfielder
        x = np.random.normal(60, 20, n_events)
        y = np.random.normal(40, 20, n_events)

    # Filter out of bounds
    x = np.clip(x, 0, 120)
    y = np.clip(y, 0, 80)
    
    return x, y

def plot_threat_map(player_name):
    """
    Creates a 'Threat Heatmap' showing where the player generates danger.
    """
    # 1. Get Data
    x, y = generate_synthetic_data(player_name)
    
    # 2. Setup Pitch
    pitch = Pitch(pitch_type='statsbomb', line_zorder=2, 
                  pitch_color='#0e1117', line_color='#efefef')
    
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#0e1117')
    
    # 3. Create Heatmap (KDE Plot)
    # cmap='magma' looks very "Data Science" (Dark to Bright)
    kde = pitch.kdeplot(x, y, ax=ax, cmap='magma', fill=True, levels=100, alpha=0.8)
    
    # 4. Add Title & Annotations
    ax.set_title(f"{player_name}: Action Density & Threat Zones", 
                 fontsize=20, color='white', fontfamily='monospace', pad=20)
    
    # Save it to show in README
    filename = f"data/{player_name.replace(' ', '_')}_heatmap.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✅ Generated Heatmap: {filename}")
    plt.close()

def plot_shot_map(player_name):
    """
    Creates a Shot Map with 'xG' represented by circle size.
    """
    x, y = generate_synthetic_data(player_name)
    # Simulate xG values (Higher xG closer to goal)
    # Goal is at (120, 40)
    dist_to_goal = np.sqrt((120-x)**2 + (40-y)**2)
    xg = 1 / (dist_to_goal + 5) # Dummy formula
    
    pitch = Pitch(pitch_type='statsbomb', pitch_color='#0e1117', line_color='#efefef')
    fig, ax = pitch.draw(figsize=(10, 7))
    fig.set_facecolor('#0e1117')
    
    # Plot Shots
    sc = pitch.scatter(x, y, s=xg*5000, c='#ff4b4b', edgecolors='white', alpha=0.7, ax=ax)
    
    ax.set_title(f"{player_name}: Shot Map (Size = xG)", 
                 fontsize=20, color='white', fontfamily='monospace', pad=20)
    
    filename = f"data/{player_name.replace(' ', '_')}_shotmap.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✅ Generated Shotmap: {filename}")
    plt.close()

if __name__ == "__main__":
    # Generate for the Front 4
    for p in ["Bruno Fernandes", "Amad Diallo", "Matheus Cunha", "Bryan Mbeumo"]:
        plot_threat_map(p)
        plot_shot_map(p)