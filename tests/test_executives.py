"""
Tests for Chamber Executive Network engine
"""

from chamber_executive_network import search_executives
from genesis_core import EpistemicStatus

def test_search_executives():
    contract = search_executives("383474814")
    assert contract.confidence > 0.9
    assert len(contract.result.get("executives")) >= 2
    assert contract.evidence[0].status == EpistemicStatus.FACT
