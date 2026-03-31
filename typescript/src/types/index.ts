// Auto-generated TypeScript interfaces from finefab-shared schemas.
// DO NOT EDIT — regenerate with: python scripts/generate_types.py

/** Kill_LIFE Agent Catalog */
export interface AgentCatalog {
  contract_version: string;
  updated_at: string;
  repo: string;
  agents: unknown[];
  legacy_runtime_aliases: Record<string, unknown>;
  write_set_conflict_resolution?: Record<string, unknown>[];
}

/** Mesh Agent Handoff */
export interface AgentHandoff {
  lot_id: string;
  owner_repo: string;
  owner_agent: string;
  write_set: string[];
  preflight: string[];
  validations: string[];
  evidence: string[];
  sync_targets: string[];
}

/** Contract defining which fields may traverse the gateway between Kill_LIFE governance agents and Mascarade execution agents. */
export interface ApiBridgeGovernanceExecution {
  /** Contract metadata. */
  metadata: Record<string, unknown>;
  /** Fields that belong only to the governance layer. */
  governance_payload_fields: string[];
  /** Fields that may traverse to the execution layer. */
  execution_payload_fields: string[];
  /** Enforcement rules at gateway boundaries. */
  bridge_rules: Record<string, unknown>[];
}

export interface ArtifactWmsIndexRules {
  [key: string]: unknown;
}

/** Fab Package */
export interface FabPackage {
  contract_version: string;
  generated_at: string;
  status: string;
  board_id: string;
  source_schematic: string | null;
  source_board: string | null;
  route_origin: string;
  bom_file: string | null;
  cpl_file: string | null;
  gerber_dir: string | null;
  drill_file: string | null;
  drc_report: string | null;
  review_artifacts: string[];
  provenance: Record<string, unknown>;
  acceptance_gates: Record<string, unknown>;
  degraded_reasons?: string[];
  next_steps?: string[];
  artifacts?: Record<string, unknown>[];
}

/** Infra VPS Inventory */
export interface InfraVps {
  contract_version: string;
  generated_at: string;
  component: string;
  owner_repo: string;
  owner_agent?: string;
  note?: string;
  services: unknown[];
}

export interface KillLifeAgentCatalog {
  [key: string]: unknown;
}

export interface MachineRegistryMesh {
  [key: string]: unknown;
}

/** Kill LIFE Machine Registry */
export interface MachineRegistry {
  generated_at: string;
  default_profile: string;
  profiles: string[];
  targets: Record<string, unknown>[];
}

export interface MascaradeDispatchMesh {
  [key: string]: unknown;
}

export interface MascaradeModelProfilesKxkmAi {
  [key: string]: unknown;
}

export interface MascaradeModelProfilesTower {
  [key: string]: unknown;
}

/** Full Operator Lane Evidence */
export interface OperatorLaneEvidence {
  generated_at: string;
  status: string;
  execution_path: string;
  chat_url: string;
  providers_url: string;
  prompt: string;
  provider: string;
  model: string;
  available_providers: string[];
  completion: string;
  summary: string;
  error?: string | null;
  http_status?: number | null;
  usage?: Record<string, unknown> | null;
}

export interface OpsKillLifeErpRegistry {
  [key: string]: unknown;
}

export interface OpsMascaradeKillLifeContract {
  [key: string]: unknown;
}

export interface PcbAiFabRegistry {
  [key: string]: unknown;
}

/** Mesh Repo Snapshot */
export interface RepoSnapshot {
  machine: string;
  repo: string;
  branch: string;
  sha: string;
  remote: string;
  dirty_set: string[];
  required_script: string;
  ssh_health: string;
}

/** Runtime MCP IA Gateway */
export interface RuntimeMcpIaGateway {
  contract_version: string;
  generated_at: string;
  component: string;
  owner_repo: string;
  owner_agent: string;
  owner_subagent: string | null;
  write_set: string[];
  status: string;
  summary_short: string;
  evidence: string[];
  degraded_reasons?: string[];
  next_steps?: string[];
  surfaces: Record<string, unknown>;
  sources?: Record<string, unknown>;
}

/** Summary Short */
export interface SummaryShort {
  contract_version: string;
  generated_at: string;
  component: string;
  lot_id?: string | null;
  owner_repo: string;
  owner_agent: string;
  owner_subagent: string | null;
  write_set: string[];
  status: string;
  summary_short: string;
  evidence: string[];
  degraded_reasons?: string[];
  next_steps?: string[];
}

/** Mesh Workflow Handshake */
export interface WorkflowHandshake {
  contract_version: string;
  schema_version: string;
  producer_repo: string;
  consumer_repo: string;
  compatibility: string;
  workflow_fields?: string[];
  evidence: string[];
  validations: string[];
  sync_targets: string[];
  ui_mappings?: Record<string, unknown>[];
}

/** Canonical internal registry for YiACAD transport commands, normalized action identifiers, supported surfaces, and engine boundaries. */
export interface YiacadActionRegistry {
  [key: string]: unknown;
}

/** YiACAD Action Registry */
export interface YiacadActionRegistry {
  contract_version: unknown;
  component: unknown;
  description?: string;
  actions: Record<string, unknown>[];
}

/** YiACAD Context Broker */
export interface YiacadContextBroker {
  component: string;
  generated_at: string;
  /** YiACAD client surface identifier, e.g. yiacad-desktop, yiacad-web, yiacad-api, tui */
  surface: string;
  context_ref: string | null;
  paths: Record<string, unknown>;
  runtime: Record<string, unknown>;
}

/** YiACAD UI UX Output Contract */
export interface YiacadUiuxOutput {
  component: string;
  /** YiACAD client surface identifier, e.g. yiacad-desktop, yiacad-web, yiacad-api, tui */
  surface: string;
  action: string;
  execution_mode: string;
  status: string;
  severity: string;
  summary: string;
  details?: string | null;
  generated_at?: string | null;
  context_ref?: string | null;
  provider?: string | null;
  model?: string | null;
  latency_ms?: number | null;
  degraded_reasons: string[];
  engine_status: Record<string, unknown>;
  artifacts: Record<string, unknown>[];
  next_steps: string[];
}
