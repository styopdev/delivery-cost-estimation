import pandas as pd


def find_similar_deliveries(origin, destination, weight_kg):
    df = pd.read_csv("data/deliveries.csv")

    # Match the exact route
    matches = df[
        (df["origin"].str.lower() == origin.lower()) &
        (df["destination"].str.lower() == destination.lower())
    ].copy()

    if matches.empty:
        return []

    # Find deliveries with similar parcel weights
    matches["weight_difference"] = abs(
        matches["weight_kg"] - weight_kg
    )

    matches = matches.sort_values("weight_difference")

    return matches.head(5).to_dict(orient="records")