from datetime import datetime

from wodi_mask import Identity, Context, Policy, DecisionEngine
from wodi_mask.identity import ExposureLevel, Stability
from wodi_mask.context import RiskProfile


def test_api_testing_rotates_ip():
    identity = Identity(
        mask_id="test",
        exposure=ExposureLevel.LOW,
        stability=Stability.STABLE,
        region_intent="us",
    )

    context = Context(
        app="api_testing",
        domain="example.com",
        timestamp=datetime.utcnow(),
        network="home",
        risk=RiskProfile.LOW,
    )

    engine = DecisionEngine(Policy.default())
    decision = engine.decide(identity, context)

    assert decision.rotate_ip is True
    assert decision.profile == "clean-dev"


def test_unknown_app_falls_back_to_default():
    identity = Identity(
        mask_id="test",
        exposure=ExposureLevel.MEDIUM,
        stability=Stability.STABLE,
        region_intent="",
    )

    context = Context(
        app="unknown",
        domain="example.com",
        timestamp=datetime.utcnow(),
        network="home",
        risk=RiskProfile.HIGH,
    )

    engine = DecisionEngine(Policy.default())
    decision = engine.decide(identity, context)

    assert decision.profile == "default"
    assert decision.risk_flag is True