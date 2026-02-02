import sqlite3
import os
import sys
import time
import random


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_NAME = os.path.join(BASE_DIR, "portfolio.db")


class Asset:  # Asset class to represent a cryptocurrency asset
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


def create_table():  # Create the assets table if it doesn't exist
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS assets
                              (name TEXT, quantity REAL, price REAL)"""
        )


def add_asset(asset):  # Add a new asset to the portfolio
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO assets (name, quantity, price) VALUES (?, ?, ?)",
                (asset.name, asset.quantity, asset.price),
            )
            conn.commit()

            print("Asset added successfully!")
    except Exception as e:
        print(f"Error during asset addition: {e}")


def view_assets():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM assets")
            assets = cursor.fetchall()

            if assets:
                total_portfolio_value = 0.0
                print("\nYour Crypto Portfolio Assets:")
                print("-" * 60)

                for row in assets:

                    name = row[0]
                    quantity = row[1]
                    price = row[2]
                    current_value = quantity * price

                    total_portfolio_value += current_value

                    print(
                        f"Name: {name:<10} | Qty: {quantity:<10.4f} | Price: ${price:<10.2f} | Value: ${current_value:<12.2f}"
                    )

                print("-" * 60)
                print(f"GRAND TOTAL: ${total_portfolio_value:.2f}")
            else:
                print("\nNo assets found.")
    except Exception as e:
        print(f"Error during fetching assets: {e}")


def delete_all_assets():  # Delete all assets from the portfolio
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM assets")
            conn.commit()

            print("All assets deleted successfully!")
    except Exception as e:
        print(f"Error during deleting assets: {e}")


def main():
    create_table()
    while True:
        try:
            print(
                "\nWelcome to the Crypto Portfolio Manager, please wait for the menu to load..."
            )
            time.sleep(random.uniform(0.5, 1.5))
            print("1. Add Asset")
            time.sleep(random.uniform(0.5, 1.5))
            print("2. View Assets")
            time.sleep(random.uniform(0.5, 1.5))
            print("3. Delete All Assets")
            time.sleep(random.uniform(0.5, 1.5))
            print("4. Exit")
            time.sleep(random.uniform(0.5, 1.5))
            choice = input("Choose an option: ")
            time.sleep(random.uniform(0.5, 1.5))

            if choice == "1":
                try:
                    name = input("Enter asset name: ")
                    quantity = float(input("Enter quantity: "))
                    price = float(input("Enter price: "))
                    asset = Asset(name, quantity, price)
                    add_asset(asset)
                except ValueError:
                    print(
                        "Invalid input. Please enter valid numbers for quantity and price."
                    )
            elif choice == "2":
                view_assets()
            elif choice == "3":
                delete_all_assets()
            elif choice == "4":
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
