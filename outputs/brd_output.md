# BRD: Edge Program – AI-Accelerated Developer Experience Portal for SDLC (SAP & Non-SAP)

# 0. Header Information

- Project Name: Developer Experience Portal for AI-assisted SDLC (SAP-first, extensible to non-SAP)
- Target Demonstrations: Visual prototype for CIO next week (Thu/Fri); internal touchpoint Wed
- Target Readiness: Working SDLC use case by end of March; iterate 2–3 months; ready for Phase 2 (around September)
- Status: Initiation and design visualization; multiple agents in POC/working state
- Document Owner: Program leadership and BA team (names not specified)
- Version: Initial draft from SAP-AI Transcript inputs

# 1. Executive Summary

- Build a unified Developer Experience Portal that orchestrates AI agents across the software development lifecycle (requirements to deployment) for SAP, with extensibility to non-SAP stacks.
- Standardize a single engineering approach across SAP and non-SAP; allow platform-specific variations via plug-and-play agents.
- Automate generation of BRDs, gap analysis, functional/technical designs, code, test cases, test execution, and training materials with human-in-the-loop approvals.
- Enable experimentation and selection of best-fit LLMs per task with cost/performance tracking.
- Deliver near-term value with a visual prototype for leadership, followed by a working use case by end of March to support Phase 2 process reimagination starting ~September.
- Anticipated productivity gains include 60%+ for auto test case generation (POC completed) and reduced cycle time via automated test execution (POC completed).

# 2. Business Context & Problem Statement

- Background / context:
  - Non-SAP world has ongoing work using AI agents across SDLC; intent is to bring a consistent approach to SAP without bifurcated methods.
  - Current SAP initiative is a technical upgrade (Phase 1); Phase 2 will reimagine/optimize processes (e.g., order-to-cash).
- Current state (if stated):
  - Manual workshops produce BRDs; functional/technical designs, code, tests, and training are largely manual; some agents already exist/POC’d (test case generation, test execution).
- Problem / pain points:
  - Duplicative approaches across platforms; manual, time-consuming SDLC artifacts; limited acceleration; reliance on long consulting cycles for process redesign.
- Why now / business drivers:
  - Accelerate SDLC for SAP Phase 2 timeline; reduce dependency on lengthy consulting; leverage AI maturity; unify developer experience; cost-effective LLM utilization.

# 3. Objectives & Success Metrics

- Objectives:
  - Deliver a single portal to initiate projects/requirements and orchestrate AI agents across SDLC with human-in-the-loop controls.
  - Standardize approach across SAP and non-SAP, enabling agent and model plug-and-play.
  - Automate generation of key SDLC artifacts (BRD, gap analysis, FDD/TDD, code, tests, training).
  - Provide model experimentation framework with cost and performance tracking to select optimal LLMs per use case.
- Success metrics / KPIs:
  - 60%+ productivity benefit for auto test case generation (POC completed).
  - Significant reduction in testing phase cycle time via automated test execution (POC completed).
  - Working SDLC use case available by end of March; readiness for Phase 2 by ~September.
- Baseline (if stated):
  - Baselines not numerically stated other than POC outcomes noted above.
- Measurement cadence & owners (if stated):
  - Not specified; human-in-the-loop reviews and leadership demos planned.

# 4. Scope

## 4.1 In Scope

- Developer Experience Portal: Single landing page to initiate a project/requirement (SAP or non-SAP) and orchestrate SDLC agents.
- Requirements phase: Upload transcripts and documents; AI agent generates BRD; business/functional review and approval.
- Gap assessment agent: Determine standard SAP config vs. gaps requiring enhancements.
- Design agents: Generate Functional Design Document (FDD) and Technical Design Document (TDD) for identified gaps.
- Build agent: Generate code/config from approved designs (SAP-first; validate SAP Joule for build acceleration).
- Testing agents: Auto test case generation (from FDD/TDD and as-is docs); automated test execution for browser-based apps with screenshot capture and defect creation.
- Training agent: Generate end-user training documents (reusing test automation engine).
- Human-in-the-loop: In-portal approvals; ability to upload edited artifacts; approval triggers next agent.
- LLM experimentation: Compare multiple models (e.g., via SAP BTP AI Core Extended or direct licenses), track input/output tokens and costs, capture business ratings, choose best-fit per use case.
- Architecture options analysis: SAP BTP vs. open AI orchestration platform; plug-and-play agent integration across stacks.
- Visual design: Figma/UX Pilot-driven prototype for end-to-end lifecycle visualization.
- Solution deployment support with AI agents for code deployment, quality checks, and security validation (as per roadmap).

## 4.2 Out of Scope

- Live-call copilot that joins workshops and nudges on missing topics (North Star; not included initially).
- Automated testing for thick client/GUI applications (current automation validated for browser-based only).
- Full process reimagination outputs (separate, more complex track; may run longer POCs).
- Procurement of enterprise licenses for LLMs/tools (decisioning included; contracting not covered).
- Comprehensive project management tracking (portal focuses on AI-assisted SDLC, not full PM tooling).

## 4.3 Constraints (only what is stated)

- Testing agent currently validated only for browser-based applications; GUI/thick client support uncertain.
- LLM maturity may limit accuracy; human-in-the-loop is required at each stage.
- Cost considerations: BTP AI Core Extended offers many models but adds premium vs. direct model access; need to manage trade-offs.
- Team members have partial allocations except for a subset; access to Figma/UX Pilot may require trials.

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| CIO / Leadership | Review visual prototype; provide directional feedback; sponsor timeline | View portal demos | CIO onsite next week for demo |
| Business Owner(s) | Provide requirements; review and approve BRDs and training outputs | Review/approve BRDs in portal; upload edits | Human-in-the-loop |
| Functional Engineers/Consultants | Lead workshops; validate BRDs; define FDD; review outputs | Create/approve artifacts in portal | SAP-first focus |
| Technical Architects/Developers | Review TDD; guide build agent prompts; oversee code generation and deployment | Approve designs; manage code outputs | Prompt engineering critical |
| Testing Team | Review generated test cases; run/monitor automated execution; manage defects | Access execution reports and screenshots | Testing agent POC completed |
| AI/ML Platform Team | Set up model experimentation; track token costs and performance; manage model access | Model dashboard and cost tracking | BTP AI Core Extended vs direct access |
| Architecture Team | Assess platform options; define integration patterns and orchestration | Design documentation | BTP vs open orchestration (Mechan AI platform) |
| AI Labs Initiative | Align business agents/use cases and reference architecture | Cross-platform coordination | Ensure storyline alignment |
| Program Team | Own end-to-end delivery plan; schedule touchpoints; enable tool access | Admin access | Coordinate access to Figma/UX Pilot |

# 6. Functional Requirements

Portal & Project Initiation

1. FR-1: The system shall provide a landing page to initiate a new project or a new requirement within a project.
2. FR-2: The system shall allow users to classify the initiative as SAP or non-SAP and route to the appropriate agent set.
3. FR-3: The system shall allow users to upload inputs for a requirement, including workshop transcripts and supporting documents.
4. FR-4: The system shall maintain status tracking for each lifecycle phase and artifact.

Requirements & BRD Generation

1. FR-5: The system shall generate a Business Requirements Document (BRD) from uploaded workshop transcripts and documents.
2. FR-6: The system shall enable designated business owners and functional engineers to review, edit (via file upload), and approve the BRD.
3. FR-7: The system shall trigger the next phase only upon BRD approval.

Gap Assessment (Standard Config vs Enhancements)

1. FR-8: The system shall analyze approved BRDs to identify requirements that can be met via standard SAP configuration versus gaps requiring enhancements.
2. FR-9: The system shall produce a gap summary report to feed design generation.

Design Generation (FDD/TDD)

1. FR-10: The system shall generate Functional Design Documents (FDD) and Technical Design Documents (TDD) for identified gaps.
2. FR-11: The system shall enable technical architects and functional engineers to review, edit (via upload), and approve FDD/TDD.
3. FR-12: Upon FDD/TDD approval, the system shall trigger the build agent.

Build & Code Generation

1. FR-13: The system shall generate code/configuration artifacts from approved FDD/TDD for SAP-targeted gaps.
2. FR-14: The system shall support use of SAP Joule (AI assistant) for build acceleration where applicable.
3. FR-15: The system shall allow technical users to review and approve generated code prior to deployment.

Testing (Test Case Generation & Execution)

1. FR-16: The system shall auto-generate test cases from FDD/TDD and as-is process documentation.
2. FR-17: The system shall execute test cases for browser-based applications by transforming steps into prompts, executing, and capturing step-wise screenshots.
3. FR-18: The system shall create a test execution report and log a defect when a test step fails.
4. FR-19: The system shall allow human adjustment of prompts prior to execution.

Training Artifact Generation

1. FR-20: The system shall generate end-user training documents by repurposing the test automation engine.

Human-in-the-Loop, Approvals, and Notifications

1. FR-21: The system shall support in-portal approvals for each artifact (BRD, FDD/TDD, code, tests, training).
2. FR-22: The system shall allow users to upload edited versions of artifacts and re-submit for approval.
3. FR-23: The system shall send notifications (e.g., email) to reviewers and update portal status upon approval or rejection.

LLM Experimentation, Selection, and Cost Tracking

1. FR-24: The system shall enable testing of multiple LLMs for a given use case and capture business ratings of output quality.
2. FR-25: The system shall track input and output tokens and compute per-run costs by model.
3. FR-26: The system shall allow selection of a default model per use case/agent based on cost-performance trade-offs.

Cross-Platform Orchestration

1. FR-27: The system shall orchestrate agents from different technology stacks (e.g., SAP BTP-based agents and agents on an open AI platform) through a plug-and-play framework.
2. FR-28: The system shall allow definition of deterministic and non-deterministic multi-agent flows through configuration.

# 7. Non-Functional Requirements (NFRs)

Performance

- NFR-1: The system shall trigger the next agent automatically upon approval without requiring re-entry of data.

Security & Access

- NFR-2: The system shall restrict artifact approval capabilities to designated reviewers (business owners, functional engineers, technical architects, as applicable).
- NFR-3: The system shall support capturing security/access requirements during requirements workshops and reflect them in generated artifacts.

Availability & Reliability

- NFR-4: The system shall allow offline edits of artifacts and subsequent upload without data loss.

Usability & UX

- NFR-5: The portal shall provide a single landing page and an end-to-end visual workflow for SDLC.
- NFR-6: The system shall clearly present status per phase and artifact with human-in-the-loop checkpoints.

Auditability & Logging

- NFR-7: The system shall maintain an audit trail of artifact generations, edits, approvals, and agent executions.
- NFR-8: The system shall log model selection and associated token/cost metrics for each run.

Data Quality

- NFR-9: The system shall preserve original transcripts and documents as immutable inputs linked to generated artifacts.

# 8. Data Requirements

## 8.1 Entities / Objects (if stated)

- Project
- Requirement (with type: SAP/non-SAP)
- Workshop (and Transcript)
- Supporting Document
- BRD
- Gap Analysis Report
- FDD
- TDD
- Code/Config Artifact
- Test Case
- Test Execution Report
- Defect
- Training Document
- Agent
- Model Run (LLM, tokens, cost, business rating)

## 8.2 Key fields & validations (if stated)

- Requirement: ID, title, project, platform (SAP/non-SAP), inputs (transcripts/documents), status.
- Transcript: source (e.g., workshop), date/time, participants (optional), file/link integrity.
- Model Run: model name, provider, input tokens, output tokens, computed cost, business rating, selected flag.
- Artifact (BRD/FDD/TDD/Code/Test/Training): version, author/agent, reviewer(s), approval status, linked inputs.

## 8.3 Data quality rules (if stated)

- All generated artifacts must reference the specific input transcripts/documents used.
- Approved artifacts must be version-stamped and immutable post-approval.

# 9. Integrations & Interfaces

- Systems involved:
  - SAP BTP (including AI Core Extended services); SAP Joule (AI assistant); Open AI orchestration platform (e.g., Mechan AI platform) for plug-and-play agents; Email/notification service; Browser-based test target systems.
- Direction:
  - Inbound: transcripts and documents into portal; approvals into portal.
  - Outbound: triggers to agents for generation/execution; notifications to reviewers; potential defect creation in target system (tool not specified).
- Triggers/events/frequency:
  - Approval of each artifact triggers the next agent; model experimentation can be invoked on demand.
- Error handling expectations:
  - Test execution agent shall produce failure reports and create defects when steps fail; portal shall log failures and allow re-run after prompt adjustments.

# 10. Reporting / Analytics

- Dashboards/reports required:
  - Model experimentation dashboard: runs by model, token usage, cost per run, business ratings, selected default.
  - Lifecycle status dashboard: artifact status per requirement (BRD, gap analysis, FDD/TDD, code, tests, training).
  - Testing summary: pass/fail rates, defects logged, execution screenshots availability.
- Filters/dimensions:
  - Project, requirement, platform (SAP/non-SAP), agent, model/provider.
- Intended users:
  - Program leadership, AI/ML platform team, architects, functional and testing teams.

# 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - Post-approval, the next agent should be invoked automatically (no manual re-entry).
- Operational ownership/support model (if stated):
  - Program team to enable platform/tool access (e.g., Figma/UX Pilot); AI/ML platform team to manage model access and costs.

# 12. Risks, Dependencies, and Assumptions

- Risks:
  - LLM accuracy variability may require significant human validation.
  - Cost overruns if using intermediary platforms with premiums (e.g., via BTP vs direct).
  - Timeline risk for end-of-March working use case if access/tooling is delayed.
  - Platform lock-in risk if portal is tightly coupled to a single stack.
- Dependencies:
  - Access to Figma/UX Pilot (or trials) for rapid visualization.
  - Decisions on architecture (BTP vs open orchestration) and LLM providers.
  - Availability of workshop transcripts and documents for BRD generation.
- Assumptions:
  - Human-in-the-loop remains mandatory across phases; leadership alignment continues through demos.

# 13. Timeline & Milestones

| Milestone | Target Date (if stated) | Notes |
| --- | --- | --- |
| Visual prototype (Figma/UX Pilot) for CIO | Next week Thu/Fri | Internal touchpoint Wed before demo |
| Architecture options (BTP vs open orchestration) – first draft | Not stated | Team to propose ETA after brainstorming |
| Working SDLC use case | End of March | Iterate/test for 2–3 months |
| Phase 2 readiness | Around September | Toolset validated for SAP program Phase 2 |

# 14. Open Questions (to finalize BRD)

1. Which platform will host the portal and orchestration: SAP BTP, open AI orchestration platform, or hybrid?
2. Which LLMs will be enterprise-licensed initially for each use case (e.g., BRD generation, coding)?
3. What are the approved templates/sections for BRD, FDD, and TDD to standardize generation?
4. Which notification channels are in scope (email only), and what is the approval routing configuration?
5. Where will defects be created and tracked (tool/system)?
6. What repository will store generated artifacts and version history (and retention requirements)?
7. What are the data privacy/security requirements for storing workshop transcripts and documents?
8. What specific metrics beyond the noted POC gains will be tracked for productivity and cycle time?
9. Will non-SAP flows be enabled in the initial release or deferred to a later phase?
10. What roles have final approval authority at each stage (business vs functional vs technical)?
11. Will the portal integrate with live-call transcripts (e.g., Teams) in phase 1 or rely on uploaded files only?
12. What is the approach and timeline for GUI/thick-client test automation support, if any?

# 15. Source Notes

- Primary notes used: INPUTS_TEXT (SAP-AI Transcript)
- Brownfield notes used: None provided