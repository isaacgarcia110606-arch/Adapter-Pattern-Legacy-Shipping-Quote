from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.shipping_quote_provider import ShippingQuoteProvider


class LegacyCarrierAdapter(ShippingQuoteProvider):
    # Factor de conversión estándar: 1 kg ≈ 2.20462 lb
    KG_TO_LB = 2.20462

    def __init__(self, legacy_carrier: LegacyCarrier):
        self.legacy_carrier = legacy_carrier

    def quote(self, destination: str, weight_kg: float) -> float:
        weight_lb = weight_kg * self.KG_TO_LB
        return self.legacy_carrier.get_price(
            postal_code=destination, 
            weight_lb=weight_lb
        )