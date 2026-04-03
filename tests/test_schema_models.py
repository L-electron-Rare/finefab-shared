from finefab_shared.models import AgentCatalog
from pydantic import ValidationError


def test_agent_catalog_instantiation_minimal() -> None:
    model = AgentCatalog(
        contract_version="v1",
        updated_at="2026-04-03T00:00:00Z",
        repo="finefab-shared",
        agents=[],
        legacy_runtime_aliases={},
    )
    assert model.contract_version == "v1"
    assert model.repo == "finefab-shared"


def test_agent_catalog_requires_contract_version() -> None:
    try:
        AgentCatalog(
            updated_at="2026-04-03T00:00:00Z",
            repo="finefab-shared",
            agents=[],
            legacy_runtime_aliases={},
        )
        assert False, "ValidationError expected when contract_version is missing"
    except ValidationError:
        assert True
