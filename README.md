# Stock Market Prediction Using BiLSTM

Predicts IBM stock closing prices using a **Bidirectional LSTM** neural network trained on historical price data enriched with technical indicators.

## How It Works

Standard LSTMs learn patterns by processing sequences forward in time. A **BiLSTM** processes the sequence in both directions — forward and backward — giving the model context from both past and future timesteps within the training window. For time-series prediction this captures momentum patterns that a unidirectional LSTM would miss.

### Data Pipeline

```
Alpha Vantage API
    ├── Daily OHLCV  (Open, High, Low, Close, Volume)
    ├── MACD         (Moving Average Convergence Divergence)
    └── MFI          (Money Flow Index — volume-weighted momentum)
            ↓
    stock_data_getter.py   — fetches and saves CSVs
    stock_data_formater.py — filters date range, merges features, min-max scales
            ↓
    BiLSTM_test_run.ipynb  — model training, evaluation, prediction
```

### Features Used

| Feature | Type | Why |
|---|---|---|
| Open, High, Low, Volume | Price / Volume | Raw market activity |
| MACD | Trend indicator | Detects momentum shifts and crossovers |
| MFI | Volume-weighted oscillator | Identifies overbought/oversold conditions |

All features are min-max scaled to `[0, 1]` before training.

## Tech Stack

- **Python 3** — pandas, numpy, scikit-learn
- **TensorFlow / Keras** — BiLSTM model
- **Alpha Vantage API** — historical stock data (free tier)
- **Jupyter Notebook** — model training and visualisation

## Project Structure

```
├── stock_data_getter.py      # Fetches OHLCV, MACD, MFI from Alpha Vantage
├── stock_data_formater.py    # Merges and normalises the feature set
└── BiLSTM_test_run.ipynb     # BiLSTM model — training, loss curves, predictions
```

## Setup

```bash
pip install pandas numpy requests tensorflow scikit-learn

# Fetch data (uses Alpha Vantage — replace apikey with your own free key)
python stock_data_getter.py

# Format features
python stock_data_formater.py

# Open notebook
jupyter notebook BiLSTM_test_run.ipynb
```

Get a free Alpha Vantage API key at [alphavantage.co](https://www.alphavantage.co/support/#api-key).
