# PKR Remittance Calculator 💱

A simple Python currency converter that converts Pakistani Rupees (PKR) to and from US Dollars (USD), UAE Dirhams (AED), and Saudi Riyals (SAR) using live exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/).

## 🚀 Features

- Fetches live exchange rates using the ExchangeRate-API.
- Converts between PKR, USD, AED, and SAR.
- Supports conversions in both directions.
- Displays the converted amount and exchange rate.
- Handles invalid amounts and unsupported currencies.
- Handles API connection errors.
- Uses Python's `requests` library.

## 🛠️ Technologies Used

- **Python 3**
- **Requests** – For fetching live exchange rate data from the API.
- **ExchangeRate-API** – For currency exchange rates.

## 📁 Project Structure

```text
pkr-remittance-calculator/
│
├── remittance_calculator.py
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/fahadrazzaqcsventures/pkr-remittance-calculator.git
```

### 2. Navigate to the project folder

```bash
cd pkr-remittance-calculator
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 4. Install the required library

```bash
pip install requests
```

### 5. Run the program

```bash
python remittance_calculator.py
```

## 💻 Example Usage

```text
========================================
       PKR REMITTANCE CALCULATOR
========================================

Fetching live exchange rates...
Exchange rates loaded successfully!

Supported currencies: PKR, USD, AED, SAR

Enter amount: 50000
Convert FROM (PKR/USD/AED/SAR): PKR
Convert TO (PKR/USD/AED/SAR): AED

========================================
           CONVERSION RESULT
========================================

From: 50,000.00 PKR
To:      653.00 AED

Exchange Rate:
1 PKR = 0.0131 AED

Source: ExchangeRate-API
========================================
```

*Note: The exchange rates and conversion amounts above are illustrative examples. Actual results depend on live API data.*

## 🌐 API Information

This project uses the following API endpoint:

```text
https://open.er-api.com/v6/latest/USD
```

The API returns exchange rates for different currencies relative to USD.

The program uses these rates to calculate conversions between PKR, USD, AED, and SAR.

## 🔄 Supported Currency Conversions

| From | To |
|---|---|
| PKR | USD, AED, SAR |
| USD | PKR, AED, SAR |
| AED | PKR, USD, SAR |
| SAR | PKR, USD, AED |

Same-currency conversions are also supported.

## ⚠️ Error Handling

The program handles:

- Invalid numerical input.
- Negative or zero amounts.
- Unsupported currency codes.
- API connection failures.
- HTTP request errors.

## 📌 Important Note

Exchange rates are fetched live when the program runs. Actual bank, exchange company, and remittance service rates may differ because of transaction fees, exchange spreads, and other charges.

This project is intended for educational purposes and currency conversion estimates, not official financial transactions.

## 👨‍💻 Author

**Fahad**

GitHub: [Your GitHub Profile](https://github.com/fahadrazzaqcsventures)

## 📄 License

This project is licensed under the MIT License.

---

⭐ If you find this project useful, consider giving it a star on GitHub!