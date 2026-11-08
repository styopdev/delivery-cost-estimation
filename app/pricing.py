BASE_FEE_AMD = 500
PRICE_PER_KILOMETER_AMD = 100
WEIGHT_SURCHARGE_PER_KG_AMD = 50
WEIGHT_SURCHARGE_START_KG = 2
MINIMUM_FEE_AMD = 700


def estimate_delivery_fee(distance_km: float, weight_kg: float) -> int:
    """Estimate a delivery fee using the published pricing rules."""
    if distance_km < 0:
        raise ValueError("Distance must not be negative.")
    if weight_kg <= 0:
        raise ValueError("Weight must be greater than zero.")

    weight_surcharge = (
        max(0, weight_kg - WEIGHT_SURCHARGE_START_KG)
        * WEIGHT_SURCHARGE_PER_KG_AMD
    )
    fee = (
        BASE_FEE_AMD
        + distance_km * PRICE_PER_KILOMETER_AMD
        + weight_surcharge
    )
    return max(MINIMUM_FEE_AMD, round(fee))
