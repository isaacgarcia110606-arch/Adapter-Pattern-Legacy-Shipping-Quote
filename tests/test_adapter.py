from shipping_adapter.checkout import Checkout
from shipping_adapter.legacy_carrier import LegacyCarrier
from shipping_adapter.legacy_carrier_adapter import LegacyCarrierAdapter


def test_checkout_uses_legacy_carrier_through_adapter():
    # Arrange
    legacy_carrier = LegacyCarrier()
    adapter = LegacyCarrierAdapter(legacy_carrier)
    checkout = Checkout(shipping=adapter)
    
    destination = "45000"
    weight_kg = 5.0  # 5.0 * 2.20462 = 11.0231 lb
    
    # Act
    result = checkout.shipping_quote(destination, weight_kg)
    
    # Assert
    # LegacyCarrier formula para "45000" y 11.0231 lb: round(6.0 + (11.0231 * 1.25), 2) = 19.78
    expected_weight_lb = weight_kg * LegacyCarrierAdapter.KG_TO_LB
    expected_price = legacy_carrier.get_price(destination, expected_weight_lb)
    
    assert result == expected_price