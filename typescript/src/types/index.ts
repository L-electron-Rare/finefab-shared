// Auto-generated TypeScript interfaces from finefab-shared schemas.
// DO NOT EDIT — regenerate with: python scripts/generate_types.py

/** Kill_LIFE Agent Catalog */
export interface AgentCatalog {
  contract_version: string;
  updated_at: string;
  repo: string;
  agents: unknown[];
  legacy_runtime_aliases: Record<string, unknown>;
  write_set_conflict_resolution?: {
    paths: string[];
    agents: string[];
    rule: string;
    owner_by_path?: Record<string, unknown>;
  }[];
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
  metadata: {
    version: string;
    date: string;
    owner_repo: string;
    status: string;
  };
  /** Fields that belong only to the governance layer. */
  governance_payload_fields: string[];
  /** Fields that may traverse to the execution layer. */
  execution_payload_fields: string[];
  /** Enforcement rules at gateway boundaries. */
  bridge_rules: {
    rule_id: string;
    from: string;
    to: string;
    action: string;
    target_fields: string[];
    description?: string;
  }[];
}

export interface ArtifactWmsIndexRules {
  [key: string]: unknown;
}

/** Browser Scrape Contract */
export interface BrowserScrape {
  request: {
    url: string;
    selector?: string | null;
    timeout_ms?: number;
  };
  response: {
    url: string;
    title: string;
    content: string;
  };
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
  provenance: {
    producer: string;
    tool: string;
    mode: string;
    route_origin: string;
  };
  acceptance_gates: {
    erc_ok: boolean;
    drc_ok: boolean;
    bom_review_ok: boolean;
    artifacts_complete: boolean;
  };
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
  targets: {
    id: string;
    target: string;
    host: string;
    port: number;
    role: string;
    priority: number;
    placement: string;
    enabled_profiles: string[];
    critical_repos: string[];
    non_essential_policy?: string;
    reserve_only: boolean;
    load_order_bias?: number;
    notes?: string;
  }[];
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
  surfaces: {
    runtime: unknown;
    mcp: unknown;
    ia: unknown;
    firmware_cad?: unknown;
    web_platform?: unknown;
    langfuse?: unknown;
    infra_vps?: unknown;
  };
  sources?: {
    intelligence?: unknown;
    mesh?: unknown;
    mascarade?: unknown;
    firmware_cad?: unknown;
    web_platform?: unknown;
    langfuse?: unknown;
    infra_vps?: unknown;
  };
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
  ui_mappings?: {
    field: string;
    ui_surface: string;
    notes?: string;
  }[];
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
  actions: {
    transport_command: string;
    action_id: string;
    display_name: string;
    description: string;
    supported_surfaces: string[];
    required_inputs: string[];
    accepted_inputs: string[];
    engine_families: string[];
    produced_artifacts: string[];
    default_next_steps: string[];
    intent_aliases?: string[];
    native_handler: string;
  }[];
}

/** YiACAD Context Broker */
export interface YiacadContextBroker {
  component: string;
  generated_at: string;
  /** YiACAD client surface identifier, e.g. yiacad-desktop, yiacad-web, yiacad-api, tui */
  surface: string;
  context_ref: string | null;
  paths: {
    source_path: string | null;
    board: string | null;
    schematic: string | null;
    freecad_document: string | null;
    artifacts_dir: string | null;
  };
  runtime: {
    root: string;
    artifacts_root: string;
    fusion_status_path: string | null;
    engine_baseline: {
      kicad?: string;
      freecad?: string;
      kibot?: string;
      kiauto?: string;
    };
    integrated_engines: {
      kicad?: unknown;
      freecad?: unknown;
      kibot?: unknown;
      kiauto?: unknown;
    };
  };
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
  engine_status: {
    kicad?: unknown;
    freecad?: unknown;
    kibot?: unknown;
    kiauto?: unknown;
  };
  artifacts: {
    kind: string;
    path: string;
    label?: string | null;
  }[];
  next_steps: string[];
}
