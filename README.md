# Advanced Crypto Trading Bot

A sophisticated cryptocurrency trading bot with machine learning capabilities, technical analysis, and risk management.

## Features

- Multiple timeframe analysis
- Advanced technical indicators
- Machine learning ensemble
- Risk management
- Position sizing
- Real-time monitoring
- REST API
- Database integration

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```

3. Configure trading parameters in `src/config.py`

4. Run the bot:
   ```bash
   python main.py
   ```

5. Access the API dashboard:
   ```bash
   uvicorn src.api.main:app --reload
   ```

## Project Structure

- `src/`
  - `exchange/` - Exchange API integration
  - `indicators/` - Technical analysis
  - `ml/` - Machine learning models
  - `risk/` - Risk management
  - `models/` - Database models
  - `api/` - FastAPI endpoints

## Configuration

Edit `.env` file for:
- API credentials
- Risk parameters
- Trading limits
- Performance targets