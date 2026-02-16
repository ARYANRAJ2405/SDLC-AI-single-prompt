# BRD: R&D Sensory UX Data Platform – Phase 2 Enhancements

# # 0. Header Information

- Project Name: R&D Sensory UX Data Platform (Stakeholder & Vendor Portals + Data Transformation Engine + Power BI)
- Date: 2026-02-16
- Status: Draft
- Document Owner: R&D Sensory UX Team (Angela Li, Jenn Soong)
- Version: 0.1

# # 1. Executive Summary

- Purpose: Enhance the R&D Sensory UX data platform to improve usability, data quality, and operational efficiency for sensory and analytical testing across global R&D.
- What is being built: Phase 2 improvements to the existing Power Apps solution (stakeholder portal, vendor portal, data transformation engine, SQL schemas, Power BI) including workflow, UX, data admin controls, and data validation enhancements.
- Who benefits: Sensory UX leads, line managers, sensory directors, R&D leads, analytical leads, vendors, and data admins.
- Intended outcomes: Faster, more accurate ingestion of sensory/analytical data; reduced manual effort; improved vendor collaboration; better search/reporting; stronger data quality; readiness for future predictive analytics.
- Drivers: Current UX challenges, limited editability, manual-heavy data transformation, lack of proactive monitoring/testing, and a roadmap to predictive analytics and expanded data coverage.
- Scope highlights: Pre-approval before RFP; post-completion data edits by data admins; support for non-product tests; bulk SIF operations; multi-user collaboration; improved search/filters; automated one-pagers; enforcement gates; dropdown/category hygiene.

# # 2. Business Context & Problem Statement

- Background / context:
  - Project initiated in 2024 to empower R&D Sensory UX and Data & Analytics with efficient, accurate, data-driven product and consumer insights.
  - Custom solution built with Power Apps; three main components: Stakeholder Portal, Vendor Portal, and Data Transformation Module.
  - Go-live: Early March 2025 (initial live in February; stabilized in March).
- Current state (if stated):
  - Global users (Europe, APAC, North America); laptop form factor; 50–100 expected users in year 1.
  - Internal users via AD; external vendors via separate email-based accounts (licenses required).
  - Vendor portal supports proposals, sample code mapping, data/report uploads; email notifications.
  - Data Transformation Engine (Python) processes heterogeneous vendor data to standardized schema for SQL and Power BI.
  - Two SQL schemas noted: R&D schema (app/holding tables) and Sensory schema (analytics/Power BI). ~35 tables total (initial ~19 sensory tables).
  - Support model: Past hypercare; two incident-focused vendor resources (Power Apps dev and Python engineer).
- Problem / pain points:
  - Historical data previously transactional; trend analysis difficult; platform now live but UX is poor (excessive scrolling, left-right navigation, hidden uploaded file visibility).
  - Data admins cannot edit after test completion (changes do not propagate to the Sensory schema/Power BI).
  - Data Transformation Engine matching performance inconsistent; vendor claimed ~95% but observed cases ~65%; promised learning over time did not materialize.
  - Bulk operations lacking (no bulk copy/paste for SIF; no SIF export).
  - Dropdowns not category-filtered (e.g., packaging types); data standardization issues (blanks, NA variants, duplicates).
  - Search/filter capabilities for completed tests are limited.
  - User/role constraints (only one user active per test step; line managers cannot complete workflows end-to-end).
  - Reactive operations: ~45 incidents tracked; no confirmed performance/security testing or proactive observability/monitoring.
- Why now / business drivers:
  - End-of-fiscal planning and need for Phase 2 resourcing and budget.
  - Roadmap to predictive analytics and innovation requires structured, high-quality data and streamlined processes.
  - Global adoption requires better UX, governance, and security posture.

# # 3. Objectives & Success Metrics

- Objectives:
  - Improve end-to-end usability and efficiency of sensory and analytical workflows.
  - Enable governance controls: pre-approval before RFP, gated test conclusion, and post-completion data edits by data admins.
  - Increase automation and standardization (bulk SIF operations, auto-populate study name, dropdown/category hygiene, file visibility).
  - Enhance data quality and transformation accuracy to support analytics.
  - Establish operational observability and complete security/performance testing suitable for external vendor access.
- Success metrics / KPIs (if stated or implied):
  - Data transformation matching rate approaches vendor’s stated 95% target (currently observed as low as ~65% in cases).
  - Reduction in incidents from the ~45 tracked to materially lower levels post-Phase 2.
  - Improved user satisfaction via UX outcomes (e.g., reduced manual steps, less scrolling, multi-user editing, bulk operations).
- Baseline (if stated):
  - ~28 proposals in the system at time of discussion; ~35 SQL tables (R&D + Sensory).
  - Live since early March 2025; ~45 incidents tracked.
  - Expected users: 50–100 in first year; global distribution.
- Measurement cadence & owners (if stated):
  - Not specified; to be defined (e.g., Data & Analytics with Sensory UX leadership).

# # 4. Scope

## ## 4.1 In Scope

- Workflow enhancements:
  - Pre-approval stage before RFP is sent to vendors (manager/director alignment).
  - Gated conclusion of tests pending DA confirmation of transformation completion.
  - Role capability: line managers able to complete test workflows where appropriate.
- Data admin capabilities:
  - Edit data after test completion with propagation to Sensory schema/Power BI and audit trail.
  - Manage holding protocol dropdown (streamline/cleanse terms).
- Data transformation & quality:
  - Improve transformation matching experience and workflow (review, feedback capture, propagation).
  - Standardize entries (blanks/NA), deduplicate, category-filtered dropdowns, enforce validations.
- UX & productivity:
  - Multi-user collaboration on active tests.
  - Bulk copy/paste for SIF; SIF export (Excel/PDF).
  - Improved search/filter for completed tests.
  - Better visibility of uploaded files and statuses.
  - Minimize scrolling; layout and readability improvements.
- Document generation:
  - Automated one-pager download (PowerPoint).
  - Create McCain report template (PowerPoint) from entered fields.
- Data model extensions:
  - Support non-product tests (allow projects without SIF, avoiding workflow breaks).
  - Auto-populate study name based on project number; request/approval for new study names.
- Operations & security:
  - Define and implement performance/security testing and basic observability/monitoring suited for external users.

## ## 4.2 Out of Scope

- Predictive analytics, formulation prediction, and broader product databases (materials/process attributes) beyond current scope.
- Building/owning supplier specifications and COAs management (e.g., TraceGains) within this phase.
- ERP integrations (e.g., SAP/Coupa for PO/vendor master) in Phase 2; considered future (Phase 3+).
- Re-platforming away from Power Apps in this phase.

## ## 4.3 Constraints (only what is stated)

- Power Apps platform UX limitations cited by prior vendor.
- External vendor users require licenses and separate email-based authentication.
- Internal access tied to AD; provisioning coordinated via platform team (Kaushal).
- Laptop-only usage due to data entry volume.
- Vendor data formats vary; transformation engine must accommodate heterogeneity.
- Data pushes to Sensory schema occur upon test completion; changes post-completion currently do not propagate.
- Support resources currently limited to incident resolution (Power Apps dev and Python engineer).
- Global user base (Europe/APAC/North America).

# # 5. Stakeholders & Roles

| Role/Group | Responsibilities | Access/View (if stated) | Notes |
| --- | --- | --- | --- |
| Sensory UX Lead | Initiate RFP; manage test setup; send SIF; coordinate with vendors; upload McCain report; conclude tests. | Access to own tests and peers’ completed tests; dashboard. | Primary process owner for sensory workflow. |
| Line Manager | Review/approve one-pager and final report; request changes. | Approval screens; dashboard. | Needs capability to complete tests when overseeing (Phase 2). |
| Sensory Director | Final approval authority; oversight; request changes. | Approval screens; dashboard. | Part of pre-approval and final approvals. |
| R&D Lead | Provide sample information (SIF); micro clearance date entry. | SIF pages and micro clearance form. | Receives notifications; returns SIF to sensory lead. |
| Vendor (External) | Submit proposals; enter sample codes; upload raw data/reports; view instructions. | Vendor portal; limited view; notifications. | Separate email-based login; license required. |
| Data Admin (Angela Li, Jenn Soong) | Administer data, dropdowns, vendors, users; bypass approvals; run transformation (intermediate/output); resolve incidents. | Admin features; view all tests; database access. | Requests: edit post-completion, better tools, reduce manual work. |
| Analytical Leads | Create analytical tests; upload instrument data (no approvals). | Analytical workflow screens. | Simpler workflow than sensory. |
| Platform/Access Manager (Kaushal) | Provision access and licenses for internal/external users. | NA | Must be notified for all new users; external licenses incur cost. |
| Vendor Support (Power Apps Dev, Python Eng) | Incident support for Power Apps and transformation engine. | NA | Incident-only; names referenced: Power Apps dev and Rahul (Python). |

# # 6. Functional Requirements

## Sensory Workflow & Approvals

1. FR-1: The system shall support a pre-approval step (by Line Manager and/or Sensory Director) before an RFP can be sent to vendors.
2. FR-2: The system shall allow creation of an RFP based on pre-approved information and transmit it to selected vendors via the Vendor Portal.
3. FR-3: The system shall allow multiple vendors to submit proposals for an RFP, and allow the Sensory Lead to select one for progression.
4. FR-4: The system shall capture manager/director approval of the selected vendor proposal and one-pager, including comments and approve/reject actions.
5. FR-5: The system shall allow the Sensory Lead to sign off on accepted proposals and proceed to test creation.
6. FR-6: The system shall generate and route the Sample Information Form (SIF) to the R&D Lead for completion and back to the Sensory Lead for vendor dispatch.
7. FR-7: The system shall capture Micro Clearance acknowledgment (date) for non-production samples.
8. FR-8: The system shall enable vendor uploads of raw data and reports to designated sections and notify the Sensory Lead upon submission.
9. FR-9: The system shall support submission of the McCain report by the Sensory Lead and route to Line Manager and Director for review/approval with comments.
10. FR-10: The system shall prevent test conclusion until the Data Admin confirms transformation completion (see Transformation requirements) or an explicit override is recorded.
11. FR-11: The system shall provide a read-only, completed-tests view for all stakeholders to review past test artifacts and statuses.
12. FR-12: The system shall allow Line Managers to complete the test workflow (not limited to the RFP/one-pager stage) where they oversee testing.

## Vendor Portal

1. FR-13: The system shall restrict vendors to their specific proposals/tests and display only necessary details for execution.
2. FR-14: The system shall allow vendors to view preparation instructions, equipment lists, and delivery/holding protocols, and to enter sample codes aligning to raw data.
3. FR-15: The system shall notify Sensory Leads via email when a vendor submits a proposal, SIF codes, raw data, or reports.
4. FR-16: The system shall support vendor authentication via separate email-based credentials (not AD).

## Data Transformation & Quality

1. FR-17: The system shall ingest heterogeneous vendor raw data and produce an Intermediate File for Data Admin review.
2. FR-18: The system shall display question-to-database mapping candidates with match scores and indicate poor/low-confidence matches.
3. FR-19: The system shall allow Data Admins to annotate mappings (remove/mismatch/new) and specify corrected Question IDs or new question definitions.
4. FR-20: The system shall generate an Output File in the target schema for ingestion to the Sensory database, restructuring data as required (e.g., stacking responses by product/respondent).
5. FR-21: The system shall capture Data Admin confirmation that transformation is complete for a test and expose this status to the workflow gate for test conclusion.
6. FR-22: The system shall enforce data standardization on entry (e.g., consistent "NA" handling, blanks normalization) and prevent duplicate master data entries where applicable.

## Data Admin & Post-Completion Editing

1. FR-23: The system shall allow Data Admins to edit test data and metadata after test completion.
2. FR-24: The system shall ensure post-completion edits propagate to the Sensory schema and downstream Power BI reports.
3. FR-25: The system shall log all post-completion edits with user, timestamp, fields changed, and rationale.

## UX, Productivity & Multi-User

1. FR-26: The system shall allow multiple assigned users to work on an active test’s data entry concurrently with appropriate conflict handling.
2. FR-27: The system shall provide bulk copy/paste capabilities for SIF data entry and support SIF export to Excel and/or PDF.
3. FR-28: The system shall improve visibility of uploaded files (e.g., clear indicators of file presence and status) on relevant screens.
4. FR-29: The system shall provide enhanced search and filter for completed tests (e.g., by region, test type, product).
5. FR-30: The system shall reduce excessive scrolling and reorganize forms to align with usability best practices within platform constraints.
6. FR-31: The system shall support automated generation and download of a one-pager PowerPoint slide populated from approved fields.
7. FR-32: The system shall support generating a McCain report template (PowerPoint) populated from approved fields.
8. FR-33: The system shall support tests without SIF (non-product research) without breaking workflow.
9. FR-34: The system shall auto-populate Study Name based on entered Project Number and allow request/approval flow for new Study Names.
10. FR-35: The system shall ensure dropdown contents are category-appropriate (e.g., primary packaging vs delivery vessels) to prevent mis-selection.

# # 7. Non-Functional Requirements (NFRs)

## Performance

1. NFR-1: The system shall undergo performance testing representative of expected usage (global users, laptop form factor) to validate acceptable response times for core workflows.
2. NFR-2: The system shall handle variable vendor file sizes and formats without undue degradation of transformation processing time.

## Security & Access

1. NFR-3: The system shall restrict access by role and ensure external vendors can only view/submit data for their assigned proposals/tests.
2. NFR-4: External users shall authenticate with separate email-based credentials; internal users via AD.
3. NFR-5: The solution shall undergo security testing commensurate with external access (e.g., vulnerability assessment) prior to Phase 2 release.
4. NFR-6: The system shall log authentication and authorization events for audit.

## Availability & Reliability

1. NFR-7: Implement basic observability/monitoring to detect availability issues and alert support (e.g., URL up/down checks, error alerts).
2. NFR-8: Define an incident response process aligned to current vendor support model (incident-only) with clear triage and resolution steps.

## Usability & UX

1. NFR-9: Form layouts shall minimize horizontal/vertical scrolling and provide clear grouping and progress indicators.
2. NFR-10: Uploaded file status shall be visibly indicated without requiring link-by-link inspection.
3. NFR-11: Search/filter controls shall be easily discoverable and performant for completed tests.

## Auditability & Logging

1. NFR-12: All approvals, bypasses, and status changes shall be logged with user and timestamp.
2. NFR-13: Data Admin post-completion edits and transformation mapping decisions shall be audit-logged.

## Compliance & Privacy

1. NFR-14: Vendor-submitted data and respondent-related data shall be protected in transit and at rest per organizational standards.

## Data Quality

1. NFR-15: Enforce standard representations for blanks/NA; prevent creation of duplicate master data entries via validations.
2. NFR-16: Ensure only approved and transformed data are propagated to the Sensory schema/Power BI.

# # 8. Data Requirements

## 8.1 Entities / Objects (if stated)

- Proposal, One-Pager, Test (Sensory, Analytical), Vendor, SIF (Sample Information Form), Micro Clearance Form
- Vendor Files (raw data, reports), McCain Report, Intermediate File, Output File
- Product (basic: SKU, log code), Study, Project Number
- Questions, Attributes, Answer Options, Respondent
- Equipment, Packaging (primary/secondary/delivery vessels), Holding/Delivery protocols
- Notifications, Budget/PO info (tracking only)
- Schemas: R&D (app/holding), Sensory (analytics/Power BI)

## 8.2 Key fields & validations (if stated)

- RFP and One-Pager: background, objectives, actions, project number, study name (auto-populate where possible).
- SIF: product details (SKU, log code), cooking instructions, holding/delivery protocols, equipment, sample codes (vendor).
- Micro clearance: date fields; applicability for pilot line samples.
- Vendor uploads: sectioned (raw data, descriptive/consumer, reports) with required formats/templates where applicable.
- Validations: category-appropriate dropdowns (e.g., package types), standard NA/blank handling, duplicate prevention for master data.

## 8.3 Data quality rules (if stated)

- Normalize NA/blanks and synonymous entries to prevent duplicate values.
- Restrict dropdown options by category (primary packaging vs delivery vessels).
- Only transformed/approved datasets flow into Sensory schema and Power BI.
- Audit trail for any post-completion edits.

# # 9. Integrations & Interfaces

- Systems involved:
  - Power Apps (Stakeholder & Vendor Portals).
  - SQL Database (R&D schema, Sensory schema).
  - Python-based Data Transformation Engine.
  - Power BI (reporting).
  - Email notifications.
- Direction (if stated):
  - Inbound: Vendor data/uploads to portal; internal entries (RFP, SIF, approvals).
  - Outbound: Transformed data to Sensory schema; Power BI consumption.
- Triggers/events/frequency (if stated):
  - Email notifications on vendor submissions, assignments, approvals, and key workflow transitions.
- Error handling expectations (if stated):
  - Bypass feature for approvals (admin-controlled) with audit; transformation review process with DA interventions.
- Future (Out of Scope Phase 2): ERP (SAP/Coupa) for PO/vendor master; TraceGains for supplier data maintenance.

# # 10. Reporting / Analytics (if applicable)

- Dashboards/reports required:
  - Power BI reports showing: products tested, test counts by region/test type, cleared/completed status, and selectable products.
- Filters/dimensions:
  - Region, test type (sensory vs analytical; consumer vs descriptive), product, status (active/completed).
- Intended users:
  - Internal stakeholders (Sensory Leads, Line Managers, Directors, R&D Leads, Data Admins).

# # 11. SLAs & Operational Expectations

- SLAs or processing expectations (if stated):
  - Not defined; performance/security testing and observability to be introduced in Phase 2.
- Operational ownership/support model (if stated):
  - Past hypercare; incident-only support by vendor resources (1 Power Apps dev, 1 Python engineer).
  - User provisioning coordinated with platform team (Kaushal); external licenses required.
  - Issue intake currently via online form and Excel tracker (~45 incidents).

# # 12. Risks, Dependencies, and Assumptions

- Risks:
  - Power Apps UX limitations may constrain improvements.
  - Data transformation matching may not improve without algorithmic changes (previous vendor declined learning capability).
  - Lack of proactive monitoring and unverified security posture with external access increases operational and security risk.
  - Manual admin workload (dropdowns, study master, user provisioning) reduces scalability.
  - Variable vendor data formats complicate standardization and increase DA workload.
- Dependencies:
  - Vendor support resources (Power Apps, Python).
  - Platform/access team for user provisioning and licensing.
  - SQL database schemas (R&D, Sensory); Power BI.
  - Email notifications for workflow routing.

# # 13. Timeline & Milestones

- Key milestones/dates (if stated):
  - Requirements finalized around Oct 2024; initial go-live Feb 2025; stabilized March 2025.
  - Phase 2 budgeting underway (end of fiscal); estimate requested within a week of meeting.
- Release approach (if stated):
  - Proposed delivery within 3–6 months (subject to resourcing and parallelization; per discussion).

# # 14. Open Questions (to finalize BRD)

1. OQ-1: Confirm target transformation matching rate (vendor stated 95%): what minimum acceptable threshold will be used and how will improvement be delivered?
2. OQ-2: Prioritize Phase 2 features (MoSCoW) and confirm any items that must be deferred.
3. OQ-3: Define scope of UX redesign feasible within Power Apps vs any needed alternative UI components.
4. OQ-4: Specify governance for post-completion edits (who can edit, what requires approval, audit requirements).
5. OQ-5: Define the exact gate criteria for concluding a test (what constitutes “DA transformation complete”: flags, checks, or sign-off).
6. OQ-6: Detail the non-product test workflow and required data fields when SIF is skipped.
7. OQ-7: Define multi-user editing rules and conflict resolution (locking, merge, latest-wins).
8. OQ-8: Confirm formats and templates for one-pager and report PPT generation (branding, fields).
9. OQ-9: Confirm search/filter dimensions for completed tests and any new Power BI report filters.
10. OQ-10: Define security testing scope and owner (e.g., vulnerability assessment, penetration testing) and timeline.
11. OQ-11: Define performance SLAs and expected load profile (concurrent users, target response times).
12. OQ-12: Clarify whether admin self-service user provisioning is in scope or if a request/approval mechanism is preferred.
13. OQ-13: Confirm timeline and scope for future ERP (SAP/Coupa) or TraceGains integrations.

# # 15. Source Notes

- Primary notes used: INPUTS_TEXT (meeting transcript RnD Sensory - Roadmap Discussion 2025-05-30).
- Brownfield notes used: None provided.

## Phase 2 Feature List & Indicative Priority (from discussion)

| Feature | Description | Indicative Priority (if stated) |
| --- | --- | --- |
| Pre-approval before RFP | Manager/Director approve info before sending RFP. | High |
| Post-completion data edits | DA edits propagate to Sensory schema/Power BI with audit. | High |
| Improve transformation UX/model | Enhance matching workflow and performance. | High |
| Support non-product tests | Allow tests without SIF; workflow does not break. | High |
| Multi-user collaboration | Allow multiple users to work on active tests. | High |
| Bulk SIF operations | Bulk copy/paste and SIF export (Excel/PDF). | High |
| Uploaded file visibility | Clear indicators of uploaded files/status. | Medium (raised from Low) |
| Improved search/filters | Better filtering for completed tests. | Medium |
| Automated one-pager (PPT) | Download one-pager populated from fields. | Medium |
| Report PPT generation | Generate McCain report template from fields. | Medium |
| Minimize scrolling | Form layout improvements. | Medium |
| Gate test conclusion | Block conclusion until DA confirms transformation. | High |
| Data quality standardization | Normalize NA/blanks; deduplicate. | High |
| Line Manager end-to-end capability | Enable LM to complete tests. | Medium |
| Manage holding protocol dropdown | Admin UI for protocol terms. | Medium |
| Auto-populate Study Name | Based on Project Number; new study request. | Medium |
| Dropdown category differentiation | Category-appropriate dropdown options. | Medium |
| Security/performance testing | Introduce testing and observability. | High |
| ERP integrations (SAP/Coupa) | Vendor/PO integration. | Out of Scope (Phase 3+) |
| TraceGains/supplier data | Leverage external supplier data management. | Out of Scope (Phase 3+) |