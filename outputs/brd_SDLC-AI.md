# Business Requirements Document: Developer Experience Portal for AI-Assisted SDLC

# 0. Header Information

- Project Name: Developer Experience Portal for AI-Assisted SDLC (SAP & non-SAP)

# 1. Executive Summary

- Build a unified Developer Experience Portal to orchestrate AI-assisted software development lifecycle (SDLC) across SAP and non-SAP platforms.
- Leverage a suite of AI agents to accelerate: requirements capture, design (functional/technical), build (code generation), testing (test case generation and execution), and training document generation.
- Enable a single front-end workflow with human-in-the-loop approvals, status management, and plug-and-play agent invocation per project type (SAP vs non-SAP).
- Reduce dependence on lengthy consulting cycles by using AI to reimagine and optimize business processes (e.g., order-to-cash) with expert validation.
- Architect for flexibility: evaluate SAP BTP and an open AI orchestration layer (McCain AI platform) to balance capability, cost, and scalability.
- Deliver a visual prototype for CIO review next week; target a working SDLC use case by end of March, iterate for 2–3 months, and be fully ready for Phase 2 in September.

# 2. Business Context & Problem Statement

- Background / context:
  - SAP program Phase 1 is a technical upgrade; Phase 2 intends to reimagine and optimize processes (e.g., order-to-cash).
  - Non-SAP work has progressed on multi-agent AI for SDLC; intention is to bring the same approach into SAP with one consistent methodology.
- Current state (if stated):
  - Manual, workshop-driven requirements capture documented as BRDs; downstream design, build, and testing largely manual or tool-based (e.g., Tosca).
  - A browser-based AI testing agent exists; thick-client GUI testing not supported yet.
- Problem / pain points:
  - Fragmented approaches across SAP and non-SAP; duplicative tooling and portals.
  - Lengthy consulting cycles to reimagine processes; slow, manual documentation and testing.
- Why now / business drivers:
  - Accelerate SDLC with AI to deliver productivity gains (estimated 20–60% depending on agent maturity).
  - Create a single, scalable developer experience across stacks; reduce cost by optimal LLM/provider selection.
  - Align with AI Labs reference architecture and prepare tooling for Phase 2 (target September).

# 3. Objectives & Success Metrics

- Objectives:
  - Design and implement a unified Developer Experience Portal for AI-assisted SDLC spanning SAP and non-SAP.
  - Operationalize multi-agent flow: requirements → gap analysis → design → build → test generation → test execution → training.
  - Establish human-in-the-loop review and approval gates that trigger downstream agents.
  - Evaluate and select architecture (SAP BTP vs McCain AI orchestration) and LLM/providers based on performance and cost.
  - Deliver a visual prototype next week and a working SDLC use case by end of March; iterate to full readiness for Phase 2.
- Success metrics / KPIs:
  - Productivity gains per agent (e.g., requirement/document generation, design, build, test). Target range discussed: 20–60%, to be validated.
  - LLM/model selection metrics: input/output tokens, total cost per artifact, and business user rating per output.
  - Portal adoption: number of projects/requirements processed via portal across SAP and non-SAP.
  - Cycle time reduction from requirements to tested build (baseline vs post-implementation).
- Baseline:
  - Not explicitly stated; to be established during early iterations (current manual/consulting-intensive process).
- Measurement cadence & owners (if stated):
  - Model experimentation and comparison to be run continuously as new LLMs become available; metrics include token usage, cost, and business ratings.

# 4. Scope

## 4.1 In Scope

- Unified Developer Experience Portal (single front-end) for initiating projects/requirements and orchestrating AI agents.
- Multi-agent flow:
  - Requirements document generation from workshop transcripts and supporting docs.
  - Gap assessment (standard SAP configuration coverage vs required enhancements).
  - Functional and technical design document generation for gaps.
  - Build/code generation from approved designs.
  - Test case generation from designs and As-Is process documentation.
  - AI-driven test execution (browser-based): prompt conversion, step execution, screenshots, report, defect creation on failure.
  - Training document generation (reusing test execution engine).
- Human-in-the-loop approvals at each stage; status management; edited document uploads to trigger next agent.
- LLM experimentation and model selection based on performance and cost.
- Architecture evaluation: SAP BTP vs McCain AI orchestration; plug-and-play support for SAP, Salesforce, and other stacks.
- Visual prototype (Figma/UX Pilot) for CIO review.

## 4.2 Out of Scope

- General project management tracking beyond AI-assisted development workflow (portal is not a full project tracker).
- Thick-client (SAP GUI) automated test execution (not supported currently).
- Full process reimagination deliverables (will be addressed via separate POCs aligned with leadership storyline).

## 4.3 Constraints (only what is stated)

- Test execution agent validated for browser-based applications only; thick-client GUI unsupported.
- Costs via intermediaries (e.g., BTP AI Core extended service) may be premium; preference to evaluate direct enterprise licenses.
- Human-in-the-loop expected at all stages due to current AI maturity; offline edits common (Word docs).
- Need for a single consistent front-end with flexible orchestration for agents across platforms.

# 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| CIO | Review visual prototype; provide strategic feedback | Portal overview | Present next week (Thu/Fri) |
| Product Owner | Initiate projects/requirements; approve BRDs and downstream deliverables | Portal access; approval workflows |  |
| Business Owner | Provide process requirements; review/approve BRDs and training docs | Portal access; human-in-loop reviews |  |
| Functional Engineer/Consultant | Facilitate workshops; review/approve BRDs, FDDs | Portal access; upload transcripts/docs; approvals |  |
| Technical Architect | Review/approve TDDs; oversee build agent outputs; prompt engineering guidance | Portal access; approvals |  |
| AI Engineering Team | Design portal and agent orchestration; build/integrate agents; model experimentation | Developer/admin access | Includes Ansh (100% allocated) and others (50–60%) |
| Piyush | Provide context on existing builds; support team enablement | As needed |  |
| Leadership (Program/IT) | Align Phase 2 storyline and POCs; approve architecture choices | Program dashboards |  |
| AI Labs Initiative | Define reference architecture; ensure cross-platform agent orchestration alignment | Architecture repositories |  |

# 6. Functional Requirements

1. FR-1 [Portal] The system shall provide a single landing page to initiate a new project or a new requirement within a project.
2. FR-2 [Portal] The system shall allow users to designate the project type (e.g., SAP or non-SAP) via a selectable control (e.g., drop-down), which determines agent templates and prompts used.
3. FR-3 [Portal] The system shall allow users to upload workshop transcripts and supporting documents for a requirement.
4. FR-4 [Requirements Agent] The system shall generate a Business Requirements Document (BRD) from uploaded transcripts and supporting documents.
5. FR-5 [Approvals] The system shall route the generated BRD for human-in-the-loop review and approval by the Business Owner and Functional Engineer.
6. FR-6 [Versioning] The system shall allow users to download, edit offline (e.g., Word), and re-upload revised BRDs, with the latest approved version stored and tracked.
7. FR-7 [Triggering] The system shall automatically trigger the next agent in the workflow upon approval of each artifact (e.g., BRD approval triggers gap assessment).
8. FR-8 [Gap Assessment Agent] The system shall evaluate approved BRDs to identify which requirements are covered by standard SAP configuration and which represent gaps requiring enhancements.
9. FR-9 [Design Agent] The system shall generate a Functional Design Document (FDD) and Technical Design Document (TDD) for identified gaps.
10. FR-10 [Approvals] The system shall route generated FDD/TDD for human-in-the-loop review and approval by the Functional Engineer and Technical Architect.
11. FR-11 [Build Agent] The system shall generate code artifacts from approved FDD/TDD and make them available for deployment.
12. FR-12 [Test Case Agent] The system shall generate test cases from approved FDD/TDD and from As-Is process documentation.
13. FR-13 [Test Execution Agent] The system shall read test cases in Word format, convert them into executable prompts, and perform browser-based test execution.
14. FR-14 [Test Reports] The system shall capture step-by-step screenshots during test execution and generate a test execution report.
15. FR-15 [Defect Handling] The system shall create a defect record when a test step fails, capturing relevant context (step, expected vs actual, screenshot).
16. FR-16 [Training Agent] The system shall generate end-user training documents leveraging the same engine used for test execution.
17. FR-17 [Notifications] The system shall notify relevant stakeholders when an artifact is ready for review or has been approved.
18. FR-18 [Status Management] The system shall track status per artifact (e.g., Draft, Under Review, Approved) and display workflow progression.
19. FR-19 [LLM Experimentation] The system shall support running multiple LLMs/providers for the same use case and capturing input/output tokens, total cost, and business user rating.
20. FR-20 [Model Selection] The system shall present comparative results to enable selection of best-fit LLM per use case, factoring cost vs performance.
21. FR-21 [Cross-Stack Orchestration] The system shall support invoking agents built on different technology stacks (e.g., SAP BTP, SAP Joule, Salesforce) via a common orchestration layer.
22. FR-22 [Human-in-the-Loop Everywhere] The system shall allow human review and approval at each stage before triggering the next agent.
23. FR-23 [Audit Trail] The system shall maintain an audit trail of uploads, generated artifacts, approvals, and agent execution logs.
24. FR-24 [Future Capability] The system shall be able to integrate a meeting agent that can join calls, track coverage of requirement dimensions (e.g., security, data), and nudge participants when gaps are detected.
25. FR-25 [Multi-Entry Paths] The system shall allow users to start the workflow at different stages (e.g., upload an FDD/TDD and generate test cases directly) when appropriate.

# 7. Non-Functional Requirements (NFRs)

1. NFR-1 [Performance] The system shall generate a BRD from transcripts within a reasonable time for typical workshop sizes (time target to be set during iteration).
2. NFR-2 [Performance] The system shall execute browser-based tests with minimal overhead relative to manual execution while capturing screenshots.
3. NFR-3 [Availability & Reliability] The system shall provide high availability for portal access during core business hours (exact SLA to be defined).
4. NFR-4 [Availability & Reliability] The system shall retry agent invocations on transient errors and log failures for support triage.
5. NFR-5 [Security & Access] The system shall enforce role-based access controls to limit who can create, view, edit, approve, and trigger agents.
6. NFR-6 [Security & Access] The system shall secure uploaded transcripts and documents, ensuring only authorized roles can access artifacts.
7. NFR-7 [Security & Access] The system shall support enterprise-compliant authentication and authorization mechanisms.
8. NFR-8 [Usability & UX] The system shall provide a clear, intuitive workflow visualization with status indicators and next-step prompts.
9. NFR-9 [Usability & UX] The system shall support offline edits and re-uploads seamlessly, reflecting the latest approved version.
10. NFR-10 [Auditability & Logging] The system shall log agent executions, inputs (model used, tokens), outputs, and triggered actions for audit and benchmarking.
11. NFR-11 [Auditability & Logging] The system shall log approvals, rejections, and version history for all artifacts.
12. NFR-12 [Compliance & Privacy] The system shall handle sensitive business data from transcripts and documents in compliance with enterprise policies.
13. NFR-13 [Compliance & Privacy] The system shall support data residency/compliance requirements when using external LLM providers (approach to be defined).
14. NFR-14 [Data Quality] The system shall provide mechanisms for business users to rate the quality of generated artifacts and capture feedback.
15. NFR-15 [Data Quality] The system shall enable iterative improvement of prompts/models based on feedback and benchmarking.
16. NFR-16 [Interoperability] The system shall support plug-and-play integration of agents built on SAP BTP, SAP Joule, and other stacks via a common orchestration layer.
17. NFR-17 [Cost Optimization] The system shall track model/token costs per artifact to inform provider selection and cost-performance trade-offs.
18. NFR-18 [Scalability] The system shall scale to support multiple concurrent projects and requirements across SAP and non-SAP.
19. NFR-19 [Maintainability] The system shall modularize agent definitions and configurations to allow easy updates and new agent additions.
20. NFR-20 [Extensibility] The system shall enable future integration of meeting agents and cross-system business agents (e.g., email-to-order) without major rework.

# 8. Data Requirements

- 8.1 Entities / Objects
  - Project; Requirement; Workshop Transcript; Supporting Document; BRD; Gap Analysis; FDD; TDD; Code Artifact; Test Case; Test Execution Report; Defect; Training Document; Approval; Status.
- 8.2 Key fields & validations (if stated)
  - Artifacts must be associated to a Project/Requirement; approvals must capture approver identity and timestamp; test execution must capture step logs and screenshots.
- 8.3 Data quality rules (if stated)
  - Store version history; ensure latest approved version is used to trigger downstream agents; capture business rating for generated outputs.

# 9. Integrations & Interfaces

- Systems involved:
  - SAP BTP (including AI Core extended service); SAP Joule; Salesforce (as example non-SAP); McCain AI orchestration platform; LLM providers (e.g., Gemini, GPT-5, Anthropic via chosen channels); Email/notification service; Browser-based application under test.
- Direction / triggers / frequency:
  - Agent invocation triggered by artifact approval; model experimentation triggered on-demand; test execution triggered per test cycle.
- Error handling:
  - Agent failures logged with retry where feasible; test failures generate defects with context.
- Future interface:
  - Meeting agent to join calls (Teams or similar) to monitor and nudge for coverage of requirement dimensions.

# 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Model comparison: input/output tokens, cost per artifact, business ratings.
  - Workflow status: artifact states (Draft/Review/Approved), agent execution logs.
  - Testing outcomes: pass/fail counts, defects created, screenshot availability.
- Filters/dimensions:
  - By project, requirement, platform (SAP vs non-SAP), agent, LLM/provider, date.
- Intended users:
  - Product Owners, Business Owners, Functional Engineers, Technical Architects, AI Engineering Team, Leadership.

# 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - Provide timely generation of artifacts and test execution; exact SLAs to be defined during iteration.
- Operational ownership/support model (if stated):
  - AI Engineering Team to build and enable access; alignment with AI Labs for architecture and with program leadership for storyline.

# 12. Risks, Dependencies, and Assumptions

- Risks:
  - LLM maturity may limit automation accuracy; human-in-the-loop remains essential.
  - Architecture choice could impact scalability and cost (platform lock-in risk).
  - Premium costs via intermediary services vs direct licenses; budget constraints.
  - Limited support for thick-client testing may constrain SAP GUI scenarios.
- Dependencies:
  - Access to Figma/UX Pilot for visual design.
  - Availability of workshop transcripts and supporting documentation.
  - Access to SAP BTP, SAP Joule, McCain AI orchestration, and LLM providers.
  - Leadership alignment on storyline and Phase 2 priorities.

# 13. Timeline & Milestones

- Key milestones/dates (if stated):
  - Next week (Thu/Fri): Visual prototype demonstration to CIO; Wednesday touchpoint for progress review.
  - End of March: Working SDLC use case ready.
  - Following 2–3 months: Iterate, test, and validate scenarios.
  - September (Phase 2): Tool fully ready, validated, and good-to-go.
- Release approach (if stated):
  - Iterative delivery: visual, architecture options, enable access, execution plan; continuous model experimentation.

# 14. Open Questions (to finalize BRD)

1. OQ-1: Which architecture will be selected: SAP BTP-based or McCain AI orchestration (or hybrid)?
2. OQ-2: What are the exact approval roles and gates per artifact (BRD, FDD, TDD, test cases, training)?
3. OQ-3: Which LLM providers will be licensed directly vs via intermediary services (and for which use cases)?
4. OQ-4: What defect management system will be integrated for automated defect creation?
5. OQ-5: What authentication/authorization mechanism will the portal use (enterprise SSO, RBAC policy specifics)?
6. OQ-6: What templates/formats will be standardized for BRD, FDD, TDD, test cases, and training documents (SAP vs non-SAP variants)?
7. OQ-7: How will data retention, privacy, and compliance be enforced for transcripts and generated artifacts?
8. OQ-8: Will browser-based test execution be extended to support thick-client (SAP GUI), and if so, how?
9. OQ-9: How will the portal handle multi-entry workflows (e.g., starting from FDD/TDD or test cases) and ensure downstream consistency?
10. OQ-10: What reporting dashboards are required for leadership, and what metric owners/cadence will be set?
11. OQ-11: How will email or “mindbox” notifications be integrated so approvals are reflected back into the portal reliably?
12. OQ-12: What is the definitive list of initial agents to be productionized vs kept in POC (e.g., order creation/change agents)?

# 15. Source Notes

- Primary notes used: INPUTS_TEXT [SOURCE: SAP-AI Transcript.txt]