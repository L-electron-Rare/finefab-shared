"""Auto-generated Pydantic v2 models from finefab-shared schemas.

DO NOT EDIT — regenerate with: python scripts/generate_types.py
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

class AgentCatalog(BaseModel):
    """Kill_LIFE Agent Catalog"""

    model_config = ConfigDict(extra='allow')

    contract_version: str
    updated_at: str
    repo: str
    agents: list[Any]
    legacy_runtime_aliases: dict[str, Any]
    write_set_conflict_resolution: list[dict[str, Any]] | None = None


class AgentHandoff(BaseModel):
    """Mesh Agent Handoff"""

    model_config = ConfigDict(extra='allow')

    lot_id: str
    owner_repo: str
    owner_agent: str
    write_set: list[str]
    preflight: list[str]
    validations: list[str]
    evidence: list[str]
    sync_targets: list[str]


class ApiBridgeGovernanceExecution(BaseModel):
    """Contract defining which fields may traverse the gateway between Kill_LIFE governance agents and Mascarade execution agents."""

    model_config = ConfigDict(extra='allow')

    metadata: dict[str, Any] = Field(..., alias="metadata", description="Contract metadata.")
    governance_payload_fields: list[str] = Field(..., alias="governance_payload_fields", description="Fields that belong only to the governance layer.")
    execution_payload_fields: list[str] = Field(..., alias="execution_payload_fields", description="Fields that may traverse to the execution layer.")
    bridge_rules: list[dict[str, Any]] = Field(..., alias="bridge_rules", description="Enforcement rules at gateway boundaries.")


class ArtifactWmsIndexRules(BaseModel):

    model_config = ConfigDict(extra='allow')


class BrowserScrape(BaseModel):
    """Browser Scrape Contract"""

    model_config = ConfigDict(extra='allow')

    request: dict[str, Any]
    response: dict[str, Any]


class FabPackage(BaseModel):
    """Fab Package"""

    model_config = ConfigDict(extra='allow')

    contract_version: str
    generated_at: str
    status: str
    board_id: str
    source_schematic: str | None
    source_board: str | None
    route_origin: str
    bom_file: str | None
    cpl_file: str | None
    gerber_dir: str | None
    drill_file: str | None
    drc_report: str | None
    review_artifacts: list[str]
    provenance: dict[str, Any]
    acceptance_gates: dict[str, Any]
    degraded_reasons: list[str] | None = None
    next_steps: list[str] | None = None
    artifacts: list[dict[str, Any]] | None = None


class InfraVps(BaseModel):
    """Infra VPS Inventory"""

    model_config = ConfigDict(extra='allow')

    contract_version: str
    generated_at: str
    component: str
    owner_repo: str
    owner_agent: str | None = None
    note: str | None = None
    services: list[Any]


class KillLifeAgentCatalog(BaseModel):

    model_config = ConfigDict(extra='allow')


class MachineRegistryMesh(BaseModel):

    model_config = ConfigDict(extra='allow')


class MachineRegistry(BaseModel):
    """Kill LIFE Machine Registry"""

    model_config = ConfigDict(extra='allow')

    generated_at: str
    default_profile: str
    profiles: list[str]
    targets: list[dict[str, Any]]


class MascaradeDispatchMesh(BaseModel):

    model_config = ConfigDict(extra='allow')


class MascaradeModelProfilesKxkmAi(BaseModel):

    model_config = ConfigDict(extra='allow')


class MascaradeModelProfilesTower(BaseModel):

    model_config = ConfigDict(extra='allow')


class OperatorLaneEvidence(BaseModel):
    """Full Operator Lane Evidence"""

    model_config = ConfigDict(extra='allow')

    generated_at: str
    status: str
    execution_path: str
    chat_url: str
    providers_url: str
    prompt: str
    provider: str
    model: str
    available_providers: list[str]
    completion: str
    summary: str
    error: str | None = None
    http_status: int | None = None
    usage: dict[str, Any] | None = None


class OpsKillLifeErpRegistry(BaseModel):

    model_config = ConfigDict(extra='allow')


class OpsMascaradeKillLifeContract(BaseModel):

    model_config = ConfigDict(extra='allow')


class PcbAiFabRegistry(BaseModel):

    model_config = ConfigDict(extra='allow')


class RepoSnapshot(BaseModel):
    """Mesh Repo Snapshot"""

    model_config = ConfigDict(extra='allow')

    machine: str
    repo: str
    branch: str
    sha: str
    remote: str
    dirty_set: list[str]
    required_script: str
    ssh_health: str


class RuntimeMcpIaGateway(BaseModel):
    """Runtime MCP IA Gateway"""

    model_config = ConfigDict(extra='allow')

    contract_version: str
    generated_at: str
    component: str
    owner_repo: str
    owner_agent: str
    owner_subagent: str | None
    write_set: list[str]
    status: str
    summary_short: str
    evidence: list[str]
    degraded_reasons: list[str] | None = None
    next_steps: list[str] | None = None
    surfaces: dict[str, Any]
    sources: dict[str, Any] | None = None


class SummaryShort(BaseModel):
    """Summary Short"""

    model_config = ConfigDict(extra='allow')

    contract_version: str
    generated_at: str
    component: str
    lot_id: str | None = None
    owner_repo: str
    owner_agent: str
    owner_subagent: str | None
    write_set: list[str]
    status: str
    summary_short: str
    evidence: list[str]
    degraded_reasons: list[str] | None = None
    next_steps: list[str] | None = None


class WorkflowHandshake(BaseModel):
    """Mesh Workflow Handshake"""

    model_config = ConfigDict(extra='allow')

    contract_version: str
    schema_version: str
    producer_repo: str
    consumer_repo: str
    compatibility: str
    workflow_fields: list[str] | None = None
    evidence: list[str]
    validations: list[str]
    sync_targets: list[str]
    ui_mappings: list[dict[str, Any]] | None = None


class YiacadActionRegistry(BaseModel):
    """Canonical internal registry for YiACAD transport commands, normalized action identifiers, supported surfaces, and engine boundaries."""

    model_config = ConfigDict(extra='allow')


class YiacadActionRegistry(BaseModel):
    """YiACAD Action Registry"""

    model_config = ConfigDict(extra='allow')

    contract_version: Any
    component: Any
    description: str | None = None
    actions: list[dict[str, Any]]


class YiacadContextBroker(BaseModel):
    """YiACAD Context Broker"""

    model_config = ConfigDict(extra='allow')

    component: str
    generated_at: str
    surface: str = Field(..., alias="surface", description="YiACAD client surface identifier, e.g. yiacad-desktop, yiacad-web, yiacad-api, tui")
    context_ref: str | None
    paths: dict[str, Any]
    runtime: dict[str, Any]


class YiacadUiuxOutput(BaseModel):
    """YiACAD UI UX Output Contract"""

    model_config = ConfigDict(extra='allow')

    component: str
    surface: str = Field(..., alias="surface", description="YiACAD client surface identifier, e.g. yiacad-desktop, yiacad-web, yiacad-api, tui")
    action: str
    execution_mode: str
    status: str
    severity: str
    summary: str
    details: str | None = None
    generated_at: str | None = None
    context_ref: str | None = None
    provider: str | None = None
    model: str | None = None
    latency_ms: int | None = None
    degraded_reasons: list[str]
    engine_status: dict[str, Any]
    artifacts: list[dict[str, Any]]
    next_steps: list[str]


__all__ = [
    "AgentCatalog",
    "AgentHandoff",
    "ApiBridgeGovernanceExecution",
    "ArtifactWmsIndexRules",
    "BrowserScrape",
    "FabPackage",
    "InfraVps",
    "KillLifeAgentCatalog",
    "MachineRegistryMesh",
    "MachineRegistry",
    "MascaradeDispatchMesh",
    "MascaradeModelProfilesKxkmAi",
    "MascaradeModelProfilesTower",
    "OperatorLaneEvidence",
    "OpsKillLifeErpRegistry",
    "OpsMascaradeKillLifeContract",
    "PcbAiFabRegistry",
    "RepoSnapshot",
    "RuntimeMcpIaGateway",
    "SummaryShort",
    "WorkflowHandshake",
    "YiacadActionRegistry",
    "YiacadActionRegistry",
    "YiacadContextBroker",
    "YiacadUiuxOutput",
]
