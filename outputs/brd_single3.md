# Edge Program: Developer Experience Portal for AI‑Assisted SDLC (SAP & Non‑SAP)

# [Header Information]

| Field | Value |
| --- | --- |
| Project Name | Edge Program: Developer Experience Portal for AI‑Assisted SDLC (SAP & Non‑SAP) |
| Last Updated | 2026-02-16 |
| Status | Ready-for-Sign-off |
| Primary Objectives | 1) Establish a single Developer Experience Portal to orchestrate AI agents across the SDLC for SAP and non‑SAP with a consistent methodology and platform‑specific variations. 2) Use AI to reimagine and optimize core processes (e.g., Order‑to‑Cash) by ingesting as‑is process, pain points, KPIs, targeted improvements, and customizations to propose a future state with automation opportunities; human‑in‑loop validation. |
| Target Milestones | Visual UX flow for CIO demo by next week (Thu/Fri). Working SDLC use case by end of March. Iterate/validate for 2–3 months. Phase 2 program readiness around September. |
| Guiding Principles | One common front‑end across SAP and non‑SAP; plug‑and‑play agent orchestration; human‑in‑loop at every phase; cost/performance benchmarking and selection of LLMs; avoid toolchain lock‑in; support offline edits with re‑upload and versioning. |

# 1. Technology Platform and Tools

| Platform/Tool | Purpose in Solution | Notes |
| --- | --- | --- |
| Developer Experience Portal (Custom Front‑End) | Single landing page to initiate projects/requirements, upload transcripts/documents, trigger AI agents, manage approvals/status, and orchestrate SDLC end‑to‑end | Common front‑end for SAP and non‑SAP; project type selector drives agent variations |
| McCain AI Platform (Orchestration Layer) | Orchestrates multi‑agent workflows across heterogeneous stacks (SAP, Salesforce, open stack); reads config to invoke agents/tools | Plug‑and‑play design; avoids per‑stack silos; external to specific stacks when cross‑system actions are needed |
| SAP BTP (Business Technology Platform) | Option for building SAP‑centric agents/services and integrating SAP AI Core extended services | Architecture option; evaluate pros/cons vs open stack; must not restrict scale across non‑SAP |
| SAP AI Core Extended Service | Access to multiple LLM providers/models for experimentation and side‑by‑side evaluation | Offers ~7–8 providers/~40 models; carries premium vs direct provider licensing |
| SAP Discovery Center – Business AI Services | Catalog of SAP‑provided agents/services (e.g., dispute mgmt, future SAP agents) | Leverage where aligned with storyline and Edge objectives |
| SAP Joule (SAP Copilot) | Candidate for SAP‑native agents (e.g., order creation/change) | Use where agent objective is confined to SAP actions |
| Microsoft Teams | Meeting host for workshops; future ‘North Star’ live agent to monitor coverage (security/data) and nudge during calls | Initial scope uses recorded transcripts rather than live intervention |
| Figma / UX Pilot | Rapid prototyping and generation of visual workflows for the portal | Use transcripts/prompts to generate initial UX; trial access for team as needed |
| Cursor | Code development assistant for open technology stack; multi‑LLM access via a single license | Enables LLM flexibility without multiple direct contracts |
| LLMs: Gemini 3 / GPT‑5 / Anthropic (Claude) | Content generation across requirements, design, code, tests; benchmark for best fit per use case | Gemini 3 favored for requirements/user stories; coding parity observed across GPT/Gemini/Anthropic (to be validated); continuous benchmarking required |
| Test Execution AI Agent (Browser‑based) | Reads Word test cases, converts to prompts, executes steps in browser, captures screenshots, generates test report, raises defects on failure | Not supported for thick‑client/GUI in v1; validated for browser‑based systems |
| Microsoft Word (.docx) | Source format for test cases and generated documents | Primary input for test execution agent |
| Salesforce (Non‑SAP example) | Non‑SAP target for cross‑system orchestration use cases | Portal drop‑down to branch agent flows for non‑SAP projects |

# 2. User Roles/Responsibilities

| Role/Title | Responsibilities | Dashboard/View | Comments/Access Rights |
| --- | --- | --- | --- |
| CIO / Executive Stakeholder | Review high‑level UX flow and progress; sign‑off on architecture direction and milestones | Executive Overview (read‑only) | View all projects’ status and ROI snapshots |
| Product Owner / Business Owner | Provide business inputs; review and approve BRD; validate future‑state recommendations | My Approvals; Project Overview | Approve/Reject BRD and training materials; comment rights |
| Functional Engineer / Functional Consultant | Run workshops; upload transcripts/docs; review/edit BRD; co‑author FDD; validate test cases | My Projects; Requirements; Designs | Create/modify artifacts for assigned projects; trigger agents |
| Technical Architect | Review/author TDD; refine prompts; oversee build agent outputs; select architecture options | Designs; Build Pipeline; Model Benchmarks | Approve TDD; gate for code generation; manage model choices |
| AI/ML Engineer (Orchestration) | Configure multi‑agent flows; maintain config files; benchmark LLMs; track token/cost metrics | Orchestration & Benchmarking | Manage model access; switch models per use case; view all runs |
| QA Lead / Tester | Review generated test cases; supervise test execution; analyze reports; raise/triage defects | Testing Dashboard; Execution Reports | Execute/monitor tests; defect management rights |
| Developer / Dev Lead | Review and integrate generated code; unit tests; commit to repo; support fixes | Build Pipeline; Code Artifacts | View/modify generated code; mark build complete |
| SAP Functional Lead | Assess standard configuration vs enhancement gaps; advise on SAP feasibility | SAP Config & Gaps | Edit gap assessments; approve SAP config choices |
| Integration Lead | Design and monitor cross‑system agent flows (SAP, Salesforce, others) | Integration Orchestration | Configure inter‑platform steps; monitor run health |
| Security Lead | Ensure security/access requirements captured; review compliance in BRD/Design | Security Checklist | Approve security sections; require remediation if missing |
| Business Analyst (BA) | Owns end‑to‑end workflow integrity; ensures artifacts are complete and consistent | End‑to‑End Tracker | View all project artifacts; raise flags on inconsistencies |

# 3. Workflow Phases (Functional Requirements)

## Workflow 1: AI‑Assisted SDLC (SAP & Non‑SAP)

1. Phase 1.1: Requirement Capture & BRD Generation Agent
2. Phase 1.2: Human‑in‑Loop Approval & Versioning
3. Phase 1.3: Gap Assessment Agent (Standard Config vs Enhancement)
4. Phase 1.4: Functional Design (FDD) & Technical Design (TDD) Generation Agent
5. Phase 1.5: Build Agent (Code Generation)
6. Phase 1.6: Test Case Generation Agent
7. Phase 1.7: Test Execution Agent (Browser‑based)
8. Phase 1.8: Training Document Generation Agent
9. Phase 1.9: Project Initialization & Orchestration (Portal Flow)
10. Phase 1.10: Model Benchmarking & Cost Tracking
11. Phase 1.11: Architecture & Platform Selection
12. Phase 1.12: Security & Access Requirements Capture
13. Phase 1.13: Notifications & Offline Edits Handling

- Phase 1.1
  - ID: Req 1.1.1
  - Description: System ingests workshop transcripts and supporting documents to auto‑generate a Business Requirement Document (BRD).
  - Business Rule/Logic: IF project type = SAP THEN apply SAP BRD template and section taxonomy; ELSE apply non‑SAP template (user story oriented).
  - Business Rule/Logic: Inputs include multiple workshop transcripts and ancillary docs; concatenate and segment by topics.
  - Business Rule/Logic (North Star): IF security/data coverage not detected in transcript THEN agent flags missing sections and (future) nudges in live Teams session.
  - UI/UX Requirement: Upload area for transcripts (.vtt/.txt) and documents (.docx/.pdf); display processing status; show generated BRD preview with section outline.
  - ID: Req 1.1.2
  - Description: Support multiple workshops per requirement; maintain association to one requirement record.
  - Business Rule/Logic: IF additional workshop transcript uploaded AFTER initial BRD generation THEN mark BRD status = Needs Regeneration.
  - UI/UX Requirement: Badge shows count of linked workshops; button: Regenerate BRD.
- Phase 1.2
  - ID: Req 1.2.1
  - Description: Human‑in‑loop review and approval of BRD by Business Owner and Functional Engineer.
  - Business Rule/Logic: IF both Business Owner AND Functional Engineer approve THEN status = BRD Approved AND trigger Phase 1.3.
  - Business Rule/Logic: Offline edits allowed; IF edited .docx uploaded THEN create new version, preserve version history, and require re‑approval.
  - UI/UX Requirement: Approve/Reject with comments; version timeline; diff indicator between versions.
- Phase 1.3
  - ID: Req 1.3.1
  - Description: Gap assessment agent analyzes BRD to determine standard SAP configuration coverage vs enhancement gaps.
  - Business Rule/Logic: IF requirement can be met via standard config THEN mark as Config Item with reference; ELSE mark as Enhancement with gap description and rationale.
  - Business Rule/Logic: Confidence score per determination; low confidence requires SAP Functional Lead review.
  - UI/UX Requirement: Tabular gap list with columns: Item, Type (Config/Enhancement), Reference, Confidence, Reviewer, Status.
- Phase 1.4
  - ID: Req 1.4.1
  - Description: Generate Functional Design Document (FDD) and Technical Design Document (TDD) for each gap/enhancement.
  - Business Rule/Logic: IF Gap Type = Enhancement THEN auto‑generate FDD/TDD drafts linked to gap ID.
  - Business Rule/Logic: Approvals required: Functional Engineer for FDD; Technical Architect for TDD.
  - UI/UX Requirement: Document previews with anchors to BRD sections; approval workflow with status badges.
- Phase 1.5
  - ID: Req 1.5.1
  - Description: Build agent translates approved FDD/TDD into code artifacts.
  - Business Rule/Logic: IF FDD and TDD statuses = Approved THEN enable Generate Code; else disable.
  - Business Rule/Logic: Technical Architect selects preferred LLM/tooling (e.g., Cursor with chosen model).
  - UI/UX Requirement: Build pipeline view; artifact download; link to repository handoff.
- Phase 1.6
  - ID: Req 1.6.1
  - Description: Test case generation from FDD/TDD and from as‑is process documents.
  - Business Rule/Logic: IF FDD/TDD approved OR As‑Is doc provided THEN generate test cases mapped to requirements.
  - UI/UX Requirement: Table of test cases with Req ID linkage; export to .docx.
- Phase 1.7
  - ID: Req 1.7.1
  - Description: Test execution agent reads Word test cases, converts to prompts, executes browser steps, captures screenshots, generates execution report, and logs defects on failure.
  - Business Rule/Logic: IF step fails THEN create defect record with step index, screenshot, and error context.
  - Business Rule/Logic: Constraint: Only browser‑based UIs supported in v1; IF target = thick client (GUI) THEN mark Not Supported.
  - UI/UX Requirement: Execution progress bar; per‑step screenshot gallery; downloadable test report; defect list view.
- Phase 1.8
  - ID: Req 1.8.1
  - Description: Training document generation using the test execution engine adapted for end‑user training materials.
  - Business Rule/Logic: Input = Executable steps + screenshots; output = training guide .docx/.pdf.
  - UI/UX Requirement: Template selector; preview before export.
- Phase 1.9
  - ID: Req 1.9.1
  - Description: Portal project initialization with project type selector (SAP vs Non‑SAP) and requirement initiation.
  - Business Rule/Logic: IF project type = SAP THEN load SAP agent chain; ELSE load non‑SAP chain (e.g., user stories emphasis).
  - UI/UX Requirement: New Project wizard; Requirement dashboard with status lanes (Requirement, Design, Build, Test, Train).
  - ID: Req 1.9.2
  - Description: Config‑driven orchestration to support deterministic and non‑deterministic flows.
  - Business Rule/Logic: Orchestrator reads plain config (YAML/JSON): step order, agent bindings, required tools per step; executes accordingly.
  - UI/UX Requirement: View orchestration config; run logs; re‑run step capability.
- Phase 1.10
  - ID: Req 1.10.1
  - Description: Model benchmarking and token/cost tracking for each generation task.
  - Business Rule/Logic: Record input/output tokens, cost, model ID, and business rating per artifact; compare across models.
  - Business Rule/Logic: IF cheaper model yields acceptable quality (e.g., ~5% lower) but >=20% cheaper, allow selection per governance policy.
  - UI/UX Requirement: Benchmark dashboard with filters by phase/model; cost vs quality scatter plot.
- Phase 1.11
  - ID: Req 1.11.1
  - Description: Architecture decision framework to choose SAP BTP vs Open Stack with McCain AI Platform orchestration.
  - Business Rule/Logic: Evaluate pros/cons (cost, flexibility, agent availability, cross‑platform needs); document decision and rationale.
  - UI/UX Requirement: Architecture options page with decision log and attachments.
- Phase 1.12
  - ID: Req 1.12.1
  - Description: Explicit capture of security/access and data requirements within BRD.
  - Business Rule/Logic: IF BRD missing Security or Data sections THEN status = Incomplete and agent suggests prompts to fill gaps.
  - UI/UX Requirement: Checklist indicators for Security/Data; completeness meter.
- Phase 1.13
  - ID: Req 1.13.1
  - Description: Notifications and offline edit handling tied to portal status transitions.
  - Business Rule/Logic: IF Approve via portal THEN auto‑trigger next agent; IF edited doc re‑uploaded THEN reset approvals and notify reviewers.
  - UI/UX Requirement: Portal inbox for pending actions; email notifications optional; audit trail of status changes.

## Workflow 2: Process Reimagination via AI

1. Phase 2.1: As‑Is Intake & Objective Setting
2. Phase 2.2: AI‑Generated To‑Be and Automation Opportunities
3. Phase 2.3: Human Validation (Expert Review)
4. Phase 2.4: Targeted POCs (e.g., Order Creation/Change Agents)
5. Phase 2.5: Cross‑System Orchestration (SAP, Salesforce, Others)

- Phase 2.1
  - ID: Req 2.1.1
  - Description: Capture as‑is process (e.g., Order‑to‑Cash), pain points, KPIs, targeted improvements, and existing customizations.
  - Business Rule/Logic: Mandatory inputs: Process map, Pain Point list, KPIs (baseline and targets), Customization inventory.
  - UI/UX Requirement: Structured forms with attachments; KPI target fields.
- Phase 2.2
  - ID: Req 2.2.1
  - Description: AI proposes future‑state process and automation opportunities (including candidate agents).
  - Business Rule/Logic: Output includes suggested automations in SAP and via new agents; each suggestion has expected impact on KPIs.
  - UI/UX Requirement: To‑Be diagram preview; list of recommended agents with impact/effort tags.
- Phase 2.3
  - ID: Req 2.3.1
  - Description: Expert validation loop to accept/modify/reject AI recommendations.
  - Business Rule/Logic: IF recommendation approved THEN add to backlog; ELSE capture rationale.
  - UI/UX Requirement: Inline annotations and decision capture.
- Phase 2.4
  - ID: Req 2.4.1
  - Description: Execute minor POCs (e.g., email‑to‑order creation; order change) leveraging SAP Joule or Discovery Center agents where applicable.
  - Business Rule/Logic: POCs must align to leadership‑approved storyline; avoid misaligned use cases.
  - UI/UX Requirement: POC tracker with hypothesis, success criteria, and results.
- Phase 2.5
  - ID: Req 2.5.1
  - Description: Design orchestration for multi‑system actions (SAP, Salesforce, others) where a single agent spans multiple platforms.
  - Business Rule/Logic: IF action spans >1 platform THEN use external orchestration (McCain AI Platform) rather than intra‑platform agent chaining.
  - UI/UX Requirement: Cross‑system swimlane visualization; run logs per system.

# 4. Data Transformation & Mapping Logic

- Input Raw Data Formats
  - Workshop transcripts (.vtt/.txt), supporting docs (.docx/.pdf), as‑is process documents, FDD/TDD, Word test cases (.docx).
- Transformation Rules
  - Transcript ingestion: segment by topics; detect presence/absence of Security and Data sections.
  - IF ‘Security’ or ‘Data’ topics not detected THEN flag BRD as incomplete and prepare prompt suggestions for missing content.
  - BRD generation: map segmented topics to BRD template sections (SAP vs non‑SAP).
  - Gap detection: parse BRD requirements; for each requirement, classify as Standard Config vs Enhancement with confidence score.
  - FDD/TDD generation: template fill using gap context; embed references to BRD clauses.
  - Test case generation: derive cases from FDD/TDD OR as‑is docs; map each test case to requirement IDs.
  - Test execution: parse .docx steps → create structured prompts → drive browser automation; capture per‑step screenshots.
  - IF execution failure THEN assemble defect record with step index, screenshot, error text; link to test case and requirement.
  - Training doc generation: repurpose executed steps + screenshots into end‑user guide format.
- Versioning & Change Propagation
  - IF any upstream document is updated (BRD/FDD/TDD/test cases) THEN mark downstream artifacts as Outdated and require regeneration/approval.
  - Maintain version history with timestamps, editors, and diffs.
- Config‑Driven Orchestration
  - Plain config (YAML/JSON) defines: steps order, agents per step, required tools/models, retry policies.
  - IF deterministic flow THEN execute steps in sequence; ELSE allow branching based on artifact availability.
- Model Benchmarking Data
  - Capture per run: model ID, input/output tokens, cost, latency, evaluator rating (business/tech).
  - IF a new model is introduced THEN run A/B tests on representative samples and update preferred model per use case.
- Cross‑Platform Mapping
  - IF project type = SAP THEN use SAP templates/agents (BTP/AICore/Joule/Discovery Center); ELSE route via non‑SAP chain (e.g., Salesforce).
  - For cross‑system flows, map each action to a system‑specific adapter; orchestrator coordinates sequence and data handoff.

# 5. Non‑Functional Requirements (NFRs) & Data Quality

- Performance
  - Portal actions (upload, status transitions) should respond within typical enterprise UX expectations; batch agent runs may be asynchronous with progress indicators.
- Scalability
  - Support multiple concurrent projects and agent runs; orchestration must scale horizontally for parallel executions.
- Availability & Reliability
  - High availability for portal; retry policies for agent steps; idempotent re‑runs.
- Security & Access Control
  - Role‑based access to artifacts; approvals gated by roles; audit trail for all changes and approvals.
- Interoperability
  - Operate with SAP BTP and open stack; clean separation to allow cross‑system orchestration via McCain AI Platform.
- Cost Efficiency
  - Track token usage and cost per model; prefer direct enterprise licensing over aggregator premiums when feasible.
- Usability
  - Clear status lanes; minimal clicks to approve/regenerate; visibility into dependencies and downstream impact.
- Data Quality
  - Completeness checks (Security/Data sections); linkage integrity across BRD→FDD/TDD→Tests→Build; consistent IDs across artifacts.
- Test Execution Constraints
  - v1 supports browser‑based systems only; thick client (GUI) excluded.

# 6. Prioritization Matrix (MoSCoW)

| Priority | Requirement | Rationale |
| --- | --- | --- |
| Must | Single Developer Experience Portal with SAP/Non‑SAP selector (Req 1.9.1) | Common entry point and branching are foundational |
| Must | BRD generation from transcripts and docs (Req 1.1.1) | Core to reduce manual documentation time |
| Must | Human‑in‑loop approval and versioning (Req 1.2.1) | Governance and quality control |
| Must | Gap assessment (config vs enhancement) with confidence (Req 1.3.1) | Essential to plan design/build scope |
| Must | FDD/TDD generation and approvals (Req 1.4.1) | Bridges requirements to build |
| Must | Build agent for code generation gated by approvals (Req 1.5.1) | Accelerates development |
| Must | Test case generation and mapping to requirements (Req 1.6.1) | Traceability and coverage |
| Must | Browser‑based test execution with screenshots and defects (Req 1.7.1) | Removes need for separate automation tooling |
| Must | Training document generation (Req 1.8.1) | Completes SDLC with enablement |
| Must | Model benchmarking & cost tracking (Req 1.10.1) | Optimize quality/cost trade‑offs |
| Should | Config‑driven orchestration for deterministic/non‑deterministic flows (Req 1.9.2) | Flexibility and reuse across stacks |
| Should | Architecture decision framework (Req 1.11.1) | Right‑sizing platform choices |
| Should | Security/Data completeness checks and indicators (Req 1.12.1) | Data quality and auditability |
| Should | Notifications and portal inbox for actions (Req 1.13.1) | Operational efficiency |
| Could | Live Teams agent to nudge missing topics during workshops (North Star) | Future enhancement; higher complexity |
| Could | SAP Discovery Center/Joule agent integrations for targeted POCs (Req 2.4.1) | Accelerate specific use cases |
| Won't (v1) | Thick‑client (GUI) test automation | Current agent validated for browser only |
| Won't (v1) | Separate portals per tech stack | Violates single‑portal principle and increases maintenance |
| Won't (v1) | Aggregator‑only LLM access where premiums materially increase cost without benefit | Cost efficiency priority |

# 7. Project Scope (In/Out)

| Scope Item | In/Out | Phase/Timeline | Notes |
| --- | --- | --- | --- |
| UX Visual Prototype for Portal Workflow | In | Immediate (next week) | Figma/UX Pilot for CIO demo |
| End‑to‑End SDLC Agent Chain (Req→Design→Build→Test→Train) | In | Working by end of March; iterate 2–3 months | Human‑in‑loop at each step |
| Model Benchmarking & Cost Tracking | In | With initial agent runs | Token, cost, model, rating capture |
| Config‑Driven Orchestration | In | Initial release | Deterministic flows prioritized |
| Browser‑Based Test Execution Agent | In | Initial release | Screenshots and defects generation |
| Process Reimagination Framework & Initial POCs | In | Parallel, post‑visual demo | Align with leadership storyline |
| Thick‑Client (GUI) Test Automation | Out | Future (Phase 3+) | Requires separate validation |
| Full Project Management/Tracking Suite | Out | N/A | Portal focuses on AI‑assisted SDLC, not general PM |
| Multiple Separate Portals per Stack | Out | N/A | Single portal principle |
| Live Teams Nudge Agent | Out | Future (North Star) | Later enhancement after core stabilized |

# 8. Conflict Identification & Open Items

- Platform Decision: SAP BTP vs Open Stack with McCain AI Platform
  - Open Item: Produce pros/cons and cost implications; ensure non‑SAP scale is not hindered.
- LLM Access Strategy: Direct enterprise licenses vs SAP AI Core premium aggregator
  - Open Item: Define policy thresholds for quality vs cost trade‑offs and when to prefer direct access.
- Agent Readiness Inventory
  - Open Item: Document current maturity of test execution, test case generation, FDD/TDD generation agents; define acceptance gates.
- Security/Compliance for Teams Bot (North Star)
  - Open Item: Assess compliance and governance for live call participation and nudging.
- Integration Targets (Defect System, Repos)
  - Open Item: Select or integrate with defect tracking and source control; currently generic record inside portal.
- Access to Figma/UX Pilot
  - Open Item: Confirm licenses or trial access for design team.
- Non‑SAP Variations (e.g., Salesforce)
  - Open Item: Define minimal viable non‑SAP chain and templates for user stories.
- Timeline Risks
  - Open Item: Validate feasibility of end‑of‑March working chain; align resources (partial allocations).