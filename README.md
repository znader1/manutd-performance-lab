# 🔴 Man Utd Performance Lab (2026)

### Project Overview
A data science toolkit designed to optimize Manchester United's tactical transition under **Michael Carrick** (Jan 2026). This project automates the analysis of the "Front Four" (Bruno, Cunha, Mbeumo, Amad) to determine the most efficient 4-2-3-1 configuration.

### 🏗️ Modules
* **`scraper.py`**: Automated ETL pipeline fetching live 2025/26 season data (FBRef).
* **`analyzer.py`**: Calculates **Expected Threat (xT)** proxies using progressive actions and xG/xA.
* **`optimizer.py`**: Utilizes **Linear Sum Assignment (Scipy)** to mathematically solve the optimal starting XI based on positional suitability metrics.

### 📊 Key Insight
By decoupling "Creativity" (xAG + Prog Passes) from "Threat" (xG + Carries), the model identifies that **Amad Diallo** creates higher system value as an Inverted LW, allowing **Bruno Fernandes** to operate centrally without spatial conflict.

### 🛠️ Tech Stack
* **Python:** Pandas, NumPy, Scipy
* **Visualization:** Matplotlib, mplsoccer
* **Data Engineering:** Automated Web Scraping (ETL)