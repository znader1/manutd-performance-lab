import pandas as pd
import time
import os

def scrape_united_data():
    """
    Scrapes 2025-2026 Manchester United stats from FBRef.
    Focuses on 'Possession' (Progression) and 'Standard' (Goals/Assists).
    """
    # 2025-2026 Season URL for Man Utd (Check if URL needs updating for '25/26' specifically)
    # Using the general 'current' page structure usually works, or specific season ID.
    # For safety in this demo, we use a generic placeholder URL logic or 'current'.
    # You might need to verify the exact FBRef ID for Man Utd in 2026.
    url = "https://fbref.com/en/squads/19538871/Manchester-United-Stats"

    print("⚽ Connecting to FBRef... (Please wait 5-10 seconds)")
    
    try:
        # 1. Read all tables on the page
        tables = pd.read_html(url, match="Standard Stats")
        std_df = tables[0]
        
        # 2. Clean the Multi-level Index (FBRef has double headers)
        std_df.columns = ['_'.join(col).strip() for col in std_df.columns.values]
        
        # 3. Filter for our key players (The Front Four + others)
        # Note: Adjust names if they appear differently on FBRef (e.g. "Bruno Fernandes")
        target_players = ["Bruno Fernandes", "Matheus Cunha", "Bryan Mbeumo", "Amad Diallo", "Marcus Rashford", "Kobbie Mainoo"]
        
        # Clean player names (remove the 'scout' link text if present)
        # FBRef often puts "Bruno Fernandes matches" -> we just want "Bruno Fernandes"
        # Usually checking 'contains' is safer.
        
        std_df['Player'] = std_df['Unnamed: 0_level_0_Player'].apply(lambda x: x.split('Matches')[0].strip() if isinstance(x, str) else x)
        
        # Filter
        df_filtered = std_df[std_df['Player'].isin(target_players)].copy()
        
        # 4. Select Key Columns for "Threat Analysis"
        # xG: Expected Goals, xAG: Expected Assisted Goals, PrgC: Progressive Carries
        # Note: Column names change slightly on FBRef, these are common defaults
        cols_to_keep = ['Player', 'Per 90 Minutes_xG', 'Per 90 Minutes_xAG', 'Per 90 Minutes_PrgC', 'Per 90 Minutes_PrgP']
        
        # Robust column selection (if column doesn't exist, fill 0)
        final_df = pd.DataFrame()
        final_df['Player'] = df_filtered['Player']
        
        for col in cols_to_keep[1:]:
            if col in df_filtered.columns:
                final_df[col] = df_filtered[col]
            else:
                final_df[col] = 0.0 # Placeholder if data missing

        # Rename for cleaner code later
        final_df.columns = ['Player', 'xG_p90', 'xA_p90', 'Prog_Carries_p90', 'Prog_Passes_p90']
        
        # Save to CSV so you don't get banned for scraping too much
        os.makedirs('data', exist_ok=True)
        final_df.to_csv('data/united_squad_2026.csv', index=False)
        print("✅ Data saved to data/united_squad_2026.csv")
        return final_df

    except Exception as e:
        print(f"❌ Error scraping: {e}")
        return None

if __name__ == "__main__":
    scrape_united_data()