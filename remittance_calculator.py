
import requests

API_URL = "https://open.er-api.com/v6/latest/USD"


def get_exchange_rates():
    """Fetch live exchange rates from the API."""
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data["result"] != "success":
            print("Error: Unable to fetch exchange rates.")
            return None

        return data["rates"]

    except requests.exceptions.RequestException as error:
        print("API connection error:", error)
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    """Convert an amount between supported currencies."""

    # Convert source currency into USD
    amount_in_usd = amount / rates[from_currency]

    # Convert USD into target currency
    converted_amount = amount_in_usd * rates[to_currency]

    return converted_amount


def main():
    print("=" * 40)
    print("       PKR REMITTANCE CALCULATOR")
    print("=" * 40)

    print("\nFetching live exchange rates...")

    rates = get_exchange_rates()

    if rates is None:
        return

    print("Exchange rates loaded successfully!")

    # Supported currencies
    currencies = ["PKR", "USD", "AED", "SAR"]

    print("\nSupported currencies:", ", ".join(currencies))

    try:
        amount = float(input("\nEnter amount: "))

        if amount <= 0:
            print("Please enter an amount greater than zero.")
            return

        from_currency = input(
            "Convert FROM (PKR/USD/AED/SAR): "
        ).upper().strip()

        to_currency = input(
            "Convert TO (PKR/USD/AED/SAR): "
        ).upper().strip()

        if from_currency not in currencies:
            print("Invalid source currency.")
            return

        if to_currency not in currencies:
            print("Invalid target currency.")
            return

        result = convert_currency(
            amount,
            from_currency,
            to_currency,
            rates
        )

        print("\n" + "=" * 40)
        print("           CONVERSION RESULT")
        print("=" * 40)

        print(f"From: {amount:,.2f} {from_currency}")
        print(f"To:   {result:,.2f} {to_currency}")

        print("\nExchange Rate:")
        print(
            f"1 {from_currency} = "
            f"{rates[to_currency] / rates[from_currency]:.4f} "
            f"{to_currency}"
        )

        print("\nSource: ExchangeRate-API")
        print("=" * 40)

    except ValueError:
        print("Invalid amount. Please enter a number.")


if __name__ == "__main__":
    main()
