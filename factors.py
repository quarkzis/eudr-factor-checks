"""Company-type factors used by the EUDR Due Diligence Costs Calculator."""

S1_FACTORS = {
    "Upstream operator (non-SME)": 1.00,
    "Upstream operator (SME)": 1.00,
    "Downstream operator (non-SME)": 0.75,
    "Downstream operator (SME)": 0.50,
    "Trader (non-SME)": 0.75,
    "Trader (SME)": 0.25,
}


def adjusted_days(base_days, company_type):
    """Return base effort in days scaled by the S1 company-type factor."""
    if company_type not in S1_FACTORS:
        raise ValueError(f"Unknown company type: {company_type}")
    return round(base_days * S1_FACTORS[company_type], 2)
