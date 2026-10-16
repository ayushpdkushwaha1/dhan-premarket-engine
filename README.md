# Dhan API - Pre-Market Engine & Config Generator

## ⚠️ OS Compatibility
- **Linux:** Fully supported and ready to use out of the box (Requires `mpv` player for audio alerts).
- **macOS & Windows:** Requires manual code modifications to run properly (specifically the audio module).

## ⚠️ Disclaimer
**This is NOT an automated trading execution bot.** This script is designed strictly to automate the tedious pre-market setup process. It generates API keys, fetches Nifty 50 Security IDs, calculates expiry days, and prepares a JSON config file for your main execution engine (like a C++ backend). It does not execute trades.

## 🚀 Features (Automated Workflow)

- **Robust Dhan API Authentication:** Uses `pyotp` for TOTP generation and features a 5-attempt exponential backoff retry mechanism to ensure successful token generation.
- **C++ Backend Ready (`config.json`):** Automatically creates a structured `config.json` containing your Access Token, Client ID, Nifty Spot Security ID, Lot Size, and target CSV paths for fast I/O in other languages.
- **Smart Expiry & T-Day Tracker:** 
  - Calculates the current trading session relative to expiry (T1 for Expiry, T2, T3... T7).
  - Skips weekends and market holidays automatically while tracking days.
- **Automated CSV Downloads & Nifty 50 Filtering:** Fetches the latest master CSV from Dhan, filters it specifically for `OPTIDX` / `INDEX` (Nifty 50), and removes unnecessary garbage columns to give you a clean file.
- **Live NSE Holiday Scraper:** The `nse_holiday_updater.py` directly scrapes the official NSE website to find trading holidays (ignoring Feb 1st) and saves them in `nse_holidays.json`. It even catches sudden emergency holidays!
- **Live Spot Price Fetcher:** Uses `yfinance` in the background (`slow_ltp_update.py`) to fetch the latest Nifty Spot price and saves it to your excel sheet.
- **Audio Alerts:** Uses `mpv` to play background audio loops for task completion, errors, or holiday warnings.

---

## ⚙️ Configuration & Setup

1. **Install Dependencies:**
   Ensure you have `mpv` installed on your Linux system. Then install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Fill Your Credentials:**
   Open the `files/fix.xlsx` file and update ONLY these cells:
   - **Cell B2:** Enter your Dhan **Client ID**
   - **Cell B4:** Enter your **Fixed TOTP Secret** (The alphanumeric string from your Dhan QR code, NOT the daily 6-digit pin).
   - **Cell B5:** Enter your Dhan **Password**

   *(Note: Do not worry about `main.xlsx` or `config.json`, the script will auto-generate and fill them. Make sure your `.gitignore` is set up properly so you do not accidentally upload this Excel file).*

---

## 🛠️ HOW TO RUN

**STOP! Do not run multiple files.** You only need to run ONE file after filling in your credentials. The code is heavily linked and will execute everything automatically in the correct order.

Open your terminal in the project folder and run this single command:

```bash
python3 key.py
```

**What happens when you run `key.py`?**
1. It checks your internet connection.
2. It checks if today is a market holiday (If yes, it alerts you via audio and asks if you still want to proceed).
3. It updates the NSE holidays.
4. It logs into Dhan API and generates the daily token.
5. It downloads and parses the latest Nifty 50 CSVs.
6. It generates the `config.json` for your on-market trading bot.
7. It plays a success audio cue when everything is done.

## 📝 Author & License
- **Author:** Ayush Prasad Kushwaha ([@ayushhpdkushwaha1](https://github.com/ayushhpdkushwaha1))
- **License:** MIT License - Free to use and modify.