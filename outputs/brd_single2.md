# R&D Sensory UX Data Platform BRD

# [Header Information]

| Field | Value |
| --- | --- |
| Project Name | R&D Sensory UX Data Platform (Stakeholder & Vendor Portals, Transformation Engine) |
| Last Updated | 2026-02-16 |
| Status | Ready-for-Sign-off |
| Project Objectives | - Empower R&D Sensory User Experience and Data teams to drive data-led product and consumer insights with efficiency and accuracy.- Centralize sensory testing (consumer + descriptive) and analytical instrument data into structured schemas for Power BI.- Support global users and external vendors with secure portals.- Establish foundation for predictive analytics and innovation (e.g., simulate 10% sodium reduction impact). |
| Baseline Metric | Sensory data constitutes ~94% of the current database content. |

# 1. Technology Platform and Tools

| Technology/Service | Purpose in Solution |
| --- | --- |
| Microsoft Power Apps (Power Platform) | Primary application layer for Stakeholder (internal) and Vendor (external) portals; forms, workflow UI, dashboards, admin screens. |
| Microsoft Power BI | Reporting and analytics dashboards (e.g., tests by region/type, product comparisons). Consumes data from Sensory schema. |
| SQL Database (R&D schema, Sensory schema) | R&D schema: app working/holding tables (drop-downs, notifications, SIF working data). Sensory schema: curated/normalized data for analytics and Power BI. |
| Python (Data Transformation Engine) | Implements ingestion, cleaning, question mapping, scoring, restructuring (wide-to-long), and output file generation for database ingestion. |
| Azure Active Directory (AAD) | Authentication and access control for internal McCain stakeholders. Internal users added via AAD; platform team provisions access. |
| External Vendor Accounts (email-based) | Separate credentials for vendor portal access; external licenses provisioned by Platform team. |
| Email Notifications | Workflow alerts (e.g., vendor submission, approvals, SIF requests) to Sensory Leads, R&D Leads, managers/directors, and Data Admins. |
| Excel (Admin Operations) | Interim bulk review/exports for large reference lists (e.g., questions/attributes) and incident tracking. |
| Visio (Process Architecture) | Architecture/workflow visualization (non-production). |
| Coupa / SAP (Future) | Target systems for future integrations (PO, vendor master). |
| TraceGains (Future Opportunity) | External solution for supplier and ingredient specification management and predictive use cases; not built in-house. |

# 2. User Roles/Responsibilities

| Role/Title | Responsibilities | Dashboard/View | Comments |
| --- | --- | --- | --- |
| Data Admin (e.g., Angela Li, Jenn Soong) | Administer app (vendors, users, drop-downs), manage category mapping, perform data transformation QA (intermediate/output), maintain SQL reference lists, bypass approvals when needed, incident triage. | Admin dashboard; View/Edit ALL tests (Active + Completed); Admin menus (Vendors, Drop-downs, Bypass, Category Mapping); Transformation module. | Can see all tests and admin menus; currently uses SQL/Excel for large list maintenance due to UI limitations. |
| Sensory UX Lead (Sensory Lead) | Initiate RFP; compile One-Pager; select vendor; coordinate SIF with R&D Lead; send SIF to vendor; receive vendor files; create McCain report; submit for approvals; conclude tests. | My Active Tests; Completed Tests; RFP screens; One-Pager; SIF links; Vendor file status; Report upload. | Receives email upon vendor submissions. Currently can only edit assigned tests; requires multi-collaborator capability in Phase 2. |
| Line Manager | Review/approve One-Pager/proposal; provide comments; may initiate RFPs. | My Approvals; RFP view; One-Pager; Completed Tests (peers). | Currently cannot complete full test workflow; Phase 2 to extend capability to complete tests when they oversee testing. |
| Sensory Director | Final approval of One-Pager/proposal and final report; provide comments; request changes. | My Approvals; Dashboard; Completed Tests. | Part of two approval cycles (pre-test and post-report). |
| R&D Lead | Complete Sample Information Form (SIF): product info (SKU, log code), cooking instructions, holding protocol, packaging; enter Micro Clearance date (when required). | Assigned SIF tasks; SIF forms; Completed SIF summaries. | Receives notifications for SIF assignment; returns SIF to Sensory Lead. |
| Analytical Lead (Internal Analytical Workflow) | Create analytical tests; plan sample info; upload instrument measurement data; no approvals. | My Active Tests (Analytical); Completed Tests. | Simplified workflow without vendor and approval steps. |
| Vendor (External Sensory Agency) | View RFP context; submit proposal and cost estimate; acknowledge accepted proposals; view SIF; enter sample codes/log codes; indicate equipment; upload test data and reports. | Vendor portal: Proposal submission; SIF (view + code entry); Files upload (by section). | External login via email; limited visibility to their engagements; triggers email notifications to Sensory Lead on submission. |
| Platform Admin (Kaushal’s Team) | Provision licenses (external), grant internal access, ensure application access configuration. | N/A (outside app). | External vendor licenses required; internal users added via AAD and platform provisioning. |
| Power Apps Support (Blackstraw) | Incident-only support for app workflow issues and defects. | N/A (support function). | Named engineer supports Power Apps; improvements deferred to Phase 2. |
| Python Support (Blackstraw) – Data Transformation | Incident-only support for transformation engine scripts and pipelines. | N/A (support function). | Named engineer (Rahul) supports Python pipeline; improvements deferred to Phase 2. |

# 3. Workflow Phases (Functional Requirements)

## Workflow 1: SensoryUX (External + Internal)

### Phase 1.1: Login & Role-Based Dashboard

- ID: Req 1.1.1 - Authenticate internal users via AAD; authenticate vendors via separate email-based credentials.
- Logic: IF user.type = internal THEN AAD authentication; IF user.type = vendor THEN external credential authentication.
- UI/UX Requirement: Role-specific dashboards: My Active Tests; Completed Tests; Admin Menus (Data Admin only). Status indicators (e.g., Proposal, Awaiting Approval, Approved, Test Created, SIF Pending, Vendor Data Pending, Transformation In Progress, Report Under Review, Completed) must display as visible badges in dashboards.
- ID: Req 1.1.2 - Email notifications for key events (vendor submission, approvals requested/completed, SIF assignment).
- Logic: IF vendor uploads any file THEN notify Sensory Lead by email; IF Sensory Lead requests SIF THEN notify R&D Lead; IF approval requested THEN notify Line Manager and Sensory Director.

### Phase 1.2: Pre-Approval Before RFP Dispatch (New)

- ID: Req 1.2.1 - Introduce pre-approval step for One-Pager prior to sending RFP to vendors.
- Logic: IF One-Pager NOT approved by Line Manager AND Sensory Director THEN block RFP dispatch to vendors.
- UI/UX Requirement: Pre-approval screen for One-Pager summary; approval buttons (Approve/Request Changes); comments capture; status badge 'Pre-Approval Pending'.
- ID: Req 1.2.2 - Support RFP field edits post-approval with change propagation to vendors.
- Logic: IF post-approval changes made to RFP-critical fields (Background/Request/Objective) THEN notify affected vendors and require their acknowledgement and proposal update.
- UI/UX Requirement: Change log showing field-level diffs; vendor-side notification banner with 'Acknowledge changes' action.

### Phase 1.3: RFP Creation & Dispatch

- ID: Req 1.3.1 - Sensory Lead creates RFP with fields: Background, Request, Objective, Business Strategy (e.g., stewardship, regional/global innovation), Category, Region/Country, minimal Product Info (SKU, log code, product type e.g., FRY product appetizer), Budget/PO Reminder.
- Logic: IF RFP dispatched to vendor THEN vendor portal displays RFP context; currently RFP is immutable without new workflow; Phase 2 enables controlled edit-propagation per Req 1.2.2.
- UI/UX Requirement: Single-column form layout to minimize left-right scrolling; required field indicators; tooltips for field definitions.
- ID: Req 1.3.2 - Support multiple vendors per RFP.
- Logic: IF multiple vendors invited THEN collect multiple proposal submissions for comparison and selection.
- UI/UX Requirement: Vendor comparison table (proposal cost, timeline, notes) for Sensory Lead.

### Phase 1.4: Vendor Proposal Submission

- ID: Req 1.4.1 - Vendor submits proposal & cost estimate; can upload proposal documents.
- Logic: IF proposal submitted THEN email Sensory Lead; proposal visible in RFP record.
- UI/UX Requirement: Vendor portal shows RFP details, upload controls with visible 'Uploaded' status and file counts; no need to click each link to confirm upload.

### Phase 1.5: One-Pager & Proposal Approval

- ID: Req 1.5.1 - Sensory Lead compiles One-Pager for management review (Line Manager and Sensory Director).
- Logic: IF LM/Director approve THEN proceed; ELSE return to Sensory Lead with comments for revision.
- UI/UX Requirement: Approval page with Approve/Request Changes; comment capture; status changes; email notifications.
- ID: Req 1.5.2 - Generate and download One-Pager PPT from entered fields.
- Logic: IF user selects 'Download One-Pager' THEN populate PPT template with RFP & One-Pager fields.
- UI/UX Requirement: Provide a standard McCain One-Pager PPT template mapping field-to-slide placeholders.

### Phase 1.6: Vendor Selection & Test Creation

- ID: Req 1.6.1 - Sensory Lead 'Signs Off' accepted proposal; system creates Test ID.
- Logic: IF vendor accepted THEN notify vendor; test status updates to 'Test Created'.
- UI/UX Requirement: Confirmation modal; Test ID displayed; audit trail recorded.

### Phase 1.7: Sample Information Form (SIF) Workflow

- ID: Req 1.7.1 - Sensory Lead assigns SIF to R&D Lead.
- Logic: IF SIF assigned THEN notify R&D Lead; SIF includes multi-page inputs: Product Information (SKU, log code, product category), Cooking Instructions, Holding Protocol (incl. delivery simulation details), Packaging (primary/secondary/delivery vessel).
- UI/UX Requirement: Multi-step form with progress; minimize lateral scrolling; summary page per sample; export SIF to Excel/PDF.
- ID: Req 1.7.2 - Vendor SIF View & Codes.
- Logic: Vendor enters product/sample codes and confirms log codes; vendor can add equipment entries if not present; equipment attributed to vendor account.
- UI/UX Requirement: Vendor view read-only for R&D-entered fields; editable code fields; equipment selection with 'Add New' inline.
- ID: Req 1.7.3 - Dropdown Category Differentiation.
- Logic: IF field = Primary Packaging Type THEN present only primary packaging options; IF field = Secondary/Delivery Vessel THEN present only appropriate options.
- UI/UX Requirement: Context-sensitive dropdowns to prevent data entry errors.
- ID: Req 1.7.4 - Bulk Data Entry to SIF.
- Logic: Allow bulk copy-paste for repetitive sample rows; support CSV/Excel import to populate SIF tables.
- UI/UX Requirement: Bulk paste grid; validation feedback; error row highlighting.
- ID: Req 1.7.5 - Support Non-Product Tests.
- Logic: IF test.type = Non-Product Research THEN allow skipping SIF without breaking workflow.
- UI/UX Requirement: Toggle to mark 'Non-Product Test'; skip SIF pages; status reflects accordingly.
- ID: Req 1.7.6 - Multi-Collaborator Editing.
- Logic: Allow multiple Sensory team members to edit active test records concurrently with optimistic locking or section-level locks.
- UI/UX Requirement: Show current editors; prevent overwrite conflicts; audit changes.

### Phase 1.8: Micro Clearance

- ID: Req 1.8.1 - R&D Lead enters Micro Clearance date for pilot-line samples.
- Logic: IF samples sourced from pilot line THEN Micro Clearance required prior to vendor testing.
- UI/UX Requirement: Date field; status indicator 'Micro Clearance Complete'; visible to vendor.

### Phase 1.9: Vendor Data Uploads

- ID: Req 1.9.1 - Vendor uploads raw data and reports by section (consumer, descriptive, other).
- Logic: IF file uploaded THEN show file count & 'Uploaded' badge; notify Sensory Lead.
- UI/UX Requirement: Clear per-section upload panels with visual status; filename list; download all button.

### Phase 1.10: Data Transformation (Intermediate & Output)

- ID: Req 1.10.1 - Intermediate File Review.
- Logic: System maps vendor questions to DB question IDs; assigns match score category (Exact, Check, Poor). IF score category = Poor THEN require Data Admin action; IF score category = Check THEN flag for review; IF score category = Exact THEN auto-accept.
- UI/UX Requirement: Intermediate file screen/table showing vendor question, candidate DB question ID, score, status flag.
- ID: Req 1.10.2 - Admin Actions on Questions.
- Logic: Admin comment values: blank = accept; 'remove' = exclude; 'mismatch <correctID>' = reassign; 'new' = create new question entry (requires new-sheet details).
- UI/UX Requirement: Inline editing of admin comment; add-new-question form to capture full metadata.
- ID: Req 1.10.3 - Category Mapping (Descriptive).
- Logic: IF test.type = Descriptive THEN select product category to load attribute list for mapping.
- UI/UX Requirement: Category selector; attribute list preview.
- ID: Req 1.10.4 - Output File Generation & Restructuring.
- Logic: Transform wide vendor data (questions as columns) into normalized long format by respondent and product; generate consumer and respondent tables; stage in R&D schema.
- UI/UX Requirement: Output preview panel showing row counts and sample records per destination table.
- ID: Req 1.10.5 - Continuous Improvement of Matching Model.
- Logic: IF admin corrections provided (supervised inputs) THEN system must learn to improve future match rates for similar questions/answer sets.
- UI/UX Requirement: Display historical match-rate KPI per vendor/test type; track before/after trends.
- ID: Req 1.10.6 - Publish to Sensory Schema upon completion.
- Logic: IF test.status = Completed AND output validated THEN push to Sensory schema for Power BI consumption.
- UI/UX Requirement: Publish job status with success/failure and timestamps.

### Phase 1.11: Report Creation & Approval

- ID: Req 1.11.1 - Sensory Lead uploads McCain report; LM/Director approve or request changes.
- Logic: IF approved THEN proceed to test conclusion.
- UI/UX Requirement: Report upload with versioning; approval screen; comments; notifications.
- ID: Req 1.11.2 - Generate McCain report PPT template populated from app fields.
- Logic: IF 'Generate Report PPT' THEN merge app fields into McCain report template placeholders.
- UI/UX Requirement: Downloadable PPT file with standardized branding and content sections.

### Phase 1.12: Test Conclusion & Locking

- ID: Req 1.12.1 - Gate conclusion on Data Transformation completion.
- Logic: IF Transformation status != Completed THEN block 'Conclude Test' and display blocking message.
- UI/UX Requirement: Modal warning citing pending transformation tasks; link to transformation module.
- ID: Req 1.12.2 - Post-Completion Edits by Data Admin with Propagation.
- Logic: IF role = Data Admin AND test.status = Completed THEN allow edits (e.g., SIF, raw data corrections) AND auto-propagate changes to Sensory schema and Power BI datasets.
- UI/UX Requirement: Admin-only edit controls with audit trail; 'Republish to Sensory Schema' action; confirmation dialogs.

## Workflow 2: Analytical (Internal Instrument Data)

- ID: Req 2.1.1 - Analytical Lead creates test, plans sample info, uploads instrument data (e.g., temperature, texture, oil).
- Logic: No LM/Director approvals; streamlined workflow from test creation to data upload.
- UI/UX Requirement: Analytical-specific forms; simpler dashboard; Completed Tests view; export capabilities.
- ID: Req 2.1.2 - Data Transformation applies restructuring rules where needed; publish to Sensory schema for Power BI.
- Logic: IF analytical data requires normalization THEN apply standard long-format transformation.
- UI/UX Requirement: Output preview and publish status analog to sensory workflow.

# 4. Data Transformation & Mapping Logic

- Input Raw Data Formats: Vendor-specific, non-uniform templates for consumer testing and descriptive analysis; system supports ingestion of multiple formats.
- Intermediate File: Displays vendor questions, candidate DB question IDs, match scores (Exact / Check / Poor), and admin comment field.
- Question Mapping Rules:
  - IF match score category = Exact THEN accept mapping; no admin action required.
  - IF match score category = Check THEN flag for review; Data Admin must review and confirm mapping.
  - IF match score category = Poor THEN Data Admin must choose: 'remove' (exclude), 'mismatch <correctID>' (assign corrected ID), or 'new' (create new question).
- Admin Comment Semantics:
  - blank = accept; 'remove' = exclude question from ingestion; 'mismatch <correctID>' = override mapping; 'new' = add a new question (requires new-sheet metadata).
- Answer Option Validation: Verify that answer options for mapped questions match DB definitions (e.g., age groups with different options).
- Category Mapping (Descriptive): Use product category to select attribute lists for mapping.
- Restructuring: Convert wide vendor datasets (questions as columns) into long, normalized tables by respondent and product.
- Output File: Contains curated records ready for insertion into consumer and respondent tables; staged in R&D schema pre-publish.
- Publish: On completion, push to Sensory schema for Power BI.
- Learning/Improvement: Incorporate supervised feedback from admin corrections to improve future matching performance over time.
- Data Standards & Cleaning:
  - Normalize blanks/NA as equivalent where applicable; enforce deduplication of logically identical reference values (e.g., packaging types, holding protocols).
  - Enforce dropdown category differentiation (primary vs secondary vs delivery vessel).
  - Reject ingestion if critical mappings remain unresolved (Poor without admin resolution).

# 5. Non-Functional Requirements (NFRs) & Data Quality

- Performance & Scalability:
  - Support forms and tables with 700+ questions and 500+ attributes without perceptible lag; target <3 seconds response for page loads under 20 concurrent users.
  - Enable bulk paste/import for SIF to reduce data entry time.
- Availability & Observability:
  - Implement uptime monitoring (URL health checks) and alerting for outages or degraded performance.
  - Track usage metrics (logins, active tests per region, vendor submissions).
- Security:
  - Conduct security testing (including for external vendor access): authentication hardening, rate-limiting, input validation, file upload scanning, and basic DDoS protection.
  - Ensure least-privilege role access; external vendor isolation; secure credential management.
- Globalization:
  - System supports global users (Europe, APAC, North America); consistent performance across regions.
- Data Integrity & Propagation:
  - Updates made post-completion by Data Admin must automatically reflect in Sensory schema (and downstream Power BI).
  - Prevent duplicates in reference lists via validation; normalize synonyms/variants (e.g., blanks/NA).
- Supportability:
  - Incident response by support engineers (Power Apps + Python); improvements handled via Phase 2 backlog.
- Auditability:
  - Audit trail for approvals, edits, bypasses, and post-completion changes (who, what, when).
- Device Form Factor:
  - Primary device: laptop/desktop (due to volume of data entry).

# 6. Prioritization Matrix (MoSCoW)

| Priority | Requirement | Rationale |
| --- | --- | --- |
| Must | Pre-approval workflow before RFP dispatch (Req 1.2.1) | Prevents rework and misalignment; requested by leadership. |
| Must | RFP edit propagation and vendor acknowledgement (Req 1.2.2) | Maintains data/process integrity when critical details change. |
| Must | Gate 'Conclude Test' on transformation completion (Req 1.12.1) | Avoids irreversible lock-in of incomplete data. |
| Must | Data Admin post-completion edits with propagation to Sensory schema (Req 1.12.2) | Ensures data quality and alignment of analytics datasets. |
| Must | Improve matching engine with supervised learning (Req 1.10.5) | Addresses low observed match rates (worst ~65%) and vendor promise for improvement. |
| Must | Dropdown category differentiation in SIF (Req 1.7.3) | Reduces data entry errors; critical for data quality. |
| Must | Bulk copy/paste and import for SIF (Req 1.7.4) | Eliminates time-consuming one-by-one entry; common user request. |
| Must | Vendor upload visibility (status badges, file counts) (Req 1.9.1 UI) | Fixes hidden-state pain point; reduces unnecessary clicks and confusion. |
| Must | Security testing and observability/monitoring setup | External vendor access mandates security validation and uptime monitoring. |
| Should | Multi-collaborator editing for active tests (Req 1.7.6) | Reflects real-world teamwork; improves throughput. |
| Should | Generate One-Pager PPT and McCain Report PPT from fields (Req 1.5.2; 1.11.2) | Standardization and time-savings for cross-functional sharing. |
| Should | Improved search and filter for completed tests | Faster retrieval and comparison; requested improvement. |
| Should | Minimize scrolling; restructure forms for better UX | Addresses layout and navigation issues raised by users. |
| Could | Non-Product Test support (skip SIF) (Req 1.7.5) | Expands use cases to research-only projects. |
| Could | Auto-populate Study Name from Project Number and approval to add new Study | Streamlines study master maintenance; reduces admin overhead. |
| Won't (Phase 2) | Integrations with Coupa/SAP (vendor master, PO) | Dependent on enterprise transformations; defer to Phase 3. |
| Won't (Phase 2) | Predictive analytics engine build-out (e.g., formulation success prediction) | Future roadmap; consider TraceGains integration; out of current scope. |

# 7. Project Scope (In/Out)

| In Scope (Phase 2) | Out of Scope (Future/Phase 3) |
| --- | --- |
| Pre-approval step; RFP change propagation to vendors. | SAP/Coupa integration for PO/vendor master. |
| Transformation engine improvements (matching, supervised learning); gating of test conclusion. | Predictive analytics/innovation modeling; TraceGains integrations. |
| Data Admin post-completion edits with auto-propagation to Sensory schema & Power BI. | Major data model expansions to include material/process parameter attributes beyond current capture. |
| SIF bulk paste/import; export to Excel/PDF; dropdown category differentiation; non-product test support. | Mobile/tablet form factors. |
| Multi-collaborator editing; improved vendor upload visibility; improved search/filter. | Replatforming or replacing Power Apps UI. |
| Generate One-Pager PPT and McCain Report PPT from app fields. | Advanced usage analytics or real-time telemetry dashboards (beyond basic monitoring). |
| Security testing and observability/monitoring. | Extensive performance load testing beyond agreed baseline unless required by monitoring outcomes. |

# 8. Conflict Identification & Open Items

- UI Table vs Performance: Stakeholders require table-format management for 700+ questions and 500+ attributes; vendor previously claimed table UI would be slow/unachievable within timeline. Requirement stands for Phase 2 to reduce reliance on direct SQL/Excel.
- Matching Model Commitment: Vendor promised supervised learning improvements during development; current behavior shows no improvement over time. Phase 2 must implement learning or equivalent rule-based enhancements to raise match rates.
- Security Testing: Unknown if any security testing was conducted; must be performed due to external vendor access.
- Observability: No proactive monitoring; currently reactive incident handling. Implement health checks and alerting.
- Performance Testing: No formal performance testing executed (e.g., 20 concurrent users, 2-3s targets). Define and execute baseline performance tests.
- Match Score Thresholds: Exact numeric thresholds for 'Exact', 'Check', 'Poor' not documented. Define and document thresholds; make configurable.
- Non-Product Test Flow: Define detailed behavior and data capture when SIF is skipped; ensure downstream analytics integrity.
- Multi-User Editing: Define locking strategy (optimistic vs section locks) and conflict resolution rules.
- Study Master Automation: Define approval workflow for new Study creation from Project Number, including email-based approval option.
- Vendor Authentication Strategy: Explore AAD B2B as alternative to separate credentials (if enterprise policy permits).

# Role-Specific Access Mapping (Standardized)

| Role/Title | View/Access Rights | Comments |
| --- | --- | --- |
| Data Admin | View/Edit ALL tests; Admin menus (Vendors, Drop-downs, Category Mapping, Bypass); Transformation module (full); Post-completion edits. | Can bypass approvals if approvers away; receives new Study requests; uses SQL/Excel for bulk lists pending UI enhancements. |
| Sensory UX Lead | View Personal Active Tests; Create RFP; One-Pager; Assign SIF; Send SIF to vendor; Receive vendor uploads; Create/Upload McCain report; Conclude tests (gated). | Receives email notifications upon vendor submissions. |
| Line Manager | View own approvals; Create RFP; Approve/Request changes on One-Pager and final report. | Phase 2: capability to complete tests when overseeing testing. |
| Sensory Director | View approvals; Approve/Request changes on One-Pager and final report. | Final approval authority. |
| R&D Lead | Access assigned SIF; Edit SIF pages; Enter Micro Clearance date. | Returns SIF to Sensory Lead; sees SIF summaries. |
| Vendor | Vendor portal only; Submit proposals; View SIF; Enter sample codes/log codes; Indicate equipment; Upload data/reports. | Separate credentials; limited information visibility. |
| Analytical Lead | Create tests; Sample planning; Data uploads; View Completed Tests. | No approvals; simplified forms. |
| Platform Admin | Provision access/licenses. | Outside app; email-based coordination. |

# Data Entities & Schemas (Reference)

- Schemas & Tables:
  - R&D schema: app-related tables (drop-down lists, notifications, SIF working data, holding tables for pre-completion).
  - Sensory schema: curated base sensory database tables powering Power BI; initial 19 tables; total ~35 tables across schemas.
- Key Artifacts: RFP, One-Pager, Test, SIF (Product Info, Cooking Instructions, Holding Protocol, Packaging), Micro Clearance, Vendor Files, Intermediate File, Output File, Study Master (Project Number ↔ Study Name).
- Data Flow: App captures → R&D schema (holding) → Transformation → Sensory schema (publish) → Power BI.