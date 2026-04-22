# test du moteur de recherche de dirigeants
from chamber_executive_network.search import search_executives

def test_recherche_dirigeants_airbus():
    contract = search_executives("airbus")
    assert contract is not None
    assert contract.result["total_executives"] >= 1
    assert len(contract.evidence) >= 1
