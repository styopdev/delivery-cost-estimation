
import re

from app.ingestion import create_vector_store
from app.retrieval import search_pricing_rules
from app.historical_data import find_similar_deliveries
from app.pricing import estimate_delivery_fee


def main():
    print("Building FAISS index...")
    create_vector_store()

    print("\nParcel Delivery Cost Estimator")

    question = input("\nAsk a question: ")

    # Keep FAISS retrieval as part of the project
    search_pricing_rules(question)

    # Extract origin, destination and weight
    match = re.match(
        r"^\s*(\S+)\s+(\S+)\s+(\d+(?:\.\d+)?)\s*kg\s*$",
        question,
        re.IGNORECASE
    )

    if not match:
        print("\nPlease use: Origin Destination Weight kg")
        return

    origin, destination, weight = match.groups()
    weight = float(weight)

    # Find historical deliveries using Pandas
    deliveries = find_similar_deliveries(
        origin, destination, weight
    )

    if not deliveries:
        print("\nNo historical data available for this route.")
        return

    closest = deliveries[0]
    difference = abs(closest["weight_kg"] - weight)

    if weight <= 0:
        print("\nWeight must be greater than zero.")
        return

    if difference > max(5, weight * 0.2):
        fee = estimate_delivery_fee(closest["distance_km"], weight)
        print("\nAssistant:")
        print(f"Estimated delivery fee: {fee:,} AMD")
        return

    print("\nAssistant:")
    print(f"Estimated delivery fee: {closest['fee_amd']:,.0f} AMD")
    print(
        f"Based on a historical delivery of "
        f"{closest['weight_kg']} kg."
    )


if __name__ == "__main__":
    main()
