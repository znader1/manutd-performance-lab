# 🔴 Man Utd Performance Lab (2026)

### Project Overview
A data science toolkit designed to optimize Manchester United's tactical transition under **Michael Carrick** (Jan 2026). This project automates the analysis of the "Front Four" (Bruno, Cunha, Mbeumo, Amad) to determine the most efficient 4-2-3-1 configuration.

### 🏗️ Modules
* **`scraper.py`**: Automated ETL pipeline fetching live 2025/26 season data (FBRef).
* **`analyzer.py`**: Calculates **Expected Threat (xT)** proxies using progressive actions and xG/xA.
* **`optimizer.py`**: Utilizes **Linear Sum Assignment (Scipy)** to mathematically solve the optimal starting XI based on positional suitability metrics.
* **`parser.py`**: Understat ETL for shot locations + xG (with on-disk caching).
* **`formation_analysis.py`**: Builds a match-by-match formation report (formation vs opponent + xG).
* **`visualizer.py`**: Generates danger-zone heatmaps + shotmaps from Understat shot data.

### 📊 Key Insight
By decoupling "Creativity" (xAG + Prog Passes) from "Threat" (xG + Carries), the model identifies that **Amad Diallo** creates higher system value as an Inverted LW, allowing **Bruno Fernandes** to operate centrally without spatial conflict.

### 🛠️ Tech Stack
* **Python:** Pandas, NumPy, Scipy
* **Visualization:** Matplotlib, mplsoccer
* **Data Engineering:** Automated Web Scraping (ETL)

---

## Quickstart

```bash
pip install -r requirements.txt
```

### 1) Fetch Understat shots (xG + locations)
Understat seasons use the start year (e.g. `2025` == `2025/26`).

```bash
python3 src/parser.py shots --team Manchester_United --season 2025
```

This writes a CSV to `data/understat_shots_Manchester_United_2025.csv` and caches the raw HTML in `data/cache/understat/`.
Use `--force` to refresh the cache.

### 2) Generate player danger zones + shot maps

```bash
python3 src/visualizer.py \
  --shots-csv data/understat_shots_Manchester_United_2025.csv \
  --top 6 \
  --out-dir data/plots \
  --mode both \
  --weight xg
```

To plot specific players:

```bash
python3 src/visualizer.py \
  --shots-csv data/understat_shots_Manchester_United_2025.csv \
  --players "Bruno Fernandes,Amad Diallo" \
  --out-dir data/plots
```

### 3) Build a formation report (formation vs opponent + xG)

```bash
python3 src/formation_analysis.py --team Manchester_United --season 2025
```

This writes:
- `data/understat_formation_report_Manchester_United_2025.csv`
- `data/understat_formation_summary_Manchester_United_2025.csv`
