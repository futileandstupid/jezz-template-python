"""Pure settlement fee calculus with closed Pydantic schemas and Z3-provable contracts."""

from typing import Annotated, Final

import icontract
from pydantic import BaseModel, ConfigDict, Field, validate_call

CALL_CONFIG: Final[ConfigDict] = ConfigDict(
    extra="forbid",
    frozen=True,
    strict=True,
    allow_inf_nan=False,
)

type AccountIdStr = Annotated[str, Field(min_length=3, max_length=64, pattern=r"^[A-Za-z0-9_-]+$")]
type PositiveCents = Annotated[int, Field(ge=1, le=1_000_000_000)]
type NonNegativeCents = Annotated[int, Field(ge=0, le=1_000_000_000)]
type BasisPoints = Annotated[int, Field(ge=0, le=10_000)]


class SettlementRequest(BaseModel):
    """Closed wire schema representing an inbound settlement quote request."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True, allow_inf_nan=False)

    account_id: AccountIdStr
    gross_cents: PositiveCents
    fee_bps: BasisPoints


class SettlementQuote(BaseModel):
    """Closed wire schema representing a conserved settlement fee quote."""

    model_config = ConfigDict(extra="forbid", frozen=True, strict=True, allow_inf_nan=False)

    account_id: AccountIdStr
    gross_cents: PositiveCents
    fee_cents: NonNegativeCents
    net_cents: NonNegativeCents


@validate_call(config=CALL_CONFIG, validate_return=True)
@icontract.require(
    lambda gross_cents, fee_bps: 1 <= gross_cents <= 1_000_000_000 and 0 <= fee_bps <= 10_000
)
@icontract.ensure(lambda gross_cents, result: 0 <= result <= gross_cents)
def net_after_fee(gross_cents: PositiveCents, fee_bps: BasisPoints) -> NonNegativeCents:
    """Compute net integer cents after deducting integer basis-point fees."""
    fee_cents = (gross_cents * fee_bps) // 10_000
    return gross_cents - fee_cents


@validate_call(config=CALL_CONFIG, validate_return=True)
def build_settlement_quote(request: SettlementRequest) -> SettlementQuote:
    """Construct a conserved SettlementQuote from a validated SettlementRequest."""
    net_cents = net_after_fee(request.gross_cents, request.fee_bps)
    fee_cents = request.gross_cents - net_cents
    return SettlementQuote(
        account_id=request.account_id,
        gross_cents=request.gross_cents,
        fee_cents=fee_cents,
        net_cents=net_cents,
    )
