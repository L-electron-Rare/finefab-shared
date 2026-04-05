from pathlib import Path

from finefab_shared.models import AgentCatalog, BrowserScrape
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


def test_browser_scrape_uses_nested_models() -> None:
    model = BrowserScrape(
        request={
            "url": "https://example.com",
            "selector": None,
            "timeout_ms": 15000,
        },
        response={
            "url": "https://example.com",
            "title": "Example",
            "content": "Hello",
        },
    )

    assert model.request.url == "https://example.com"
    assert model.request.timeout_ms == 15000
    assert model.response.title == "Example"


def test_browser_scrape_typescript_output_keeps_nested_fields() -> None:
    ts_types = (
        Path(__file__).resolve().parents[1] / "typescript" / "src" / "types" / "index.ts"
    ).read_text()

    assert "export interface BrowserScrape {" in ts_types
    assert "request: {" in ts_types
    assert "timeout_ms?: number;" in ts_types
    assert "response: {" in ts_types
    assert "content: string;" in ts_types
