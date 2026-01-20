import requests
import pandas as pd
import json
import re

def get_united_shots_2025():
    """
    Scrapes REAL 2025/2026 shot locations for Man Utd from Understat.
    """
    # 1. Find Man Utd's Team ID (United is usually ID '1')
    # For 2025/26, the URL structure remains the same.
    url = "https://understat.com/team/Manchester_United/2025"
    
    print(f"🌍 Connecting to Understat: {url}")
    response = requests.get(url)
    
    # 2. Extract the JSON hidden inside the HTML
    # Understat stores data in a script variable called 'playersData' or 'shotsData'
    match = re.search(r"var shotsData\s*=\s*JSON\.parse\('(.*?)'\)", response.text)
    
    if not match:
        print("❌ Could not find shot data. Understat might have changed format.")
        return None
        
    # Clean the hex string representation
    json_string = match.group(1).encode('utf-8').decode('unicode_escape')
    data = json.loads(json_string)
    
    # 3. Parse into DataFrame
    # Understat data is organized by 'h' (home) and 'a' (away) games
    all_shots = []
    
    for shot in data:
        all_shots.append({
            "Player": shot['player'],
            "X": float(shot['X']) * 120, # Convert 0-1 to StatsBomb 120 scale
            "Y": float(shot['Y']) * 80,  # Convert 0-1 to StatsBomb 80 scale
            "xG": float(shot['xG']),
            "Result": shot['result'], # 'Goal', 'Saved', 'Missed'
            "Minute": shot['minute'],
            "Type": "Shot"
        })
        
    df = pd.DataFrame(all_shots)
    
    # Filter for your Front 4
    target_players = ["Bruno Fernandes", "Matheus Cunha", "Bryan Mbeumo", "Amad Diallo"]
    df = df[df['Player'].isin(target_players)]
    
    # Save to CSV
    df.to_csv("data/real_shots_2026.csv", index=False)
    print(f"✅ Saved {len(df)} real shots to data/real_shots_2026.csv")
    return df

if __name__ == "__main__":
    get_united_shots_2025()