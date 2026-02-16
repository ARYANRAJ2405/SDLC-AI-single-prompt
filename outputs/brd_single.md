[Header Information]
Project Name: R&D Sensory UX & Analytical Data App (Stakeholder Portal + Vendor Portal + Transformation Module)
Last Updated: 2026-02-16
Status: Ready-for-Sign-off

Project Objectives
- Systematize sensory user experience and analytical test data to enable efficient, accurate insights and future predictive analytics for product development.
- Centralize external sensory (consumer testing and descriptive analysis) and internal analytical instrument measures in a structured database.
- Reduce cycle time to find and leverage historical data (remediate “transactional-only” histories).
- Ensure global, vendor-inclusive workflow with role-based access and auditability.
- Transformation Engine objective: reliably ingest heterogeneous vendor raw files, clean, map questions/attributes, and restructure to the database schema for Power BI analytics.
- Scale target: 50–100 global users in Year 1 across Europe, APAC, North America.
- Data volume: 700+ survey questions and 500+ sensory attributes must be manageable in admin UI and reporting.
- Current data composition: Sensory UX data represents ~94% of total database content.

1. Technology Platform and Tools
- Microsoft Power Apps
  - Purpose: Front-end application for Stakeholder Portal (internal users) and Vendor Portal (external users).
  - Functions: Workflow forms (RFP, One-Pager, SIF, Micro Clearance), role-specific dashboards, vendor submissions, approvals.
- Microsoft Power BI
  - Purpose: Reporting/analytics layer on finalized sensory schema.
  - Functions: Product/test dashboards (e.g., tests by region, type, product comparisons), data slicing.
- Azure SQL Database (Schemas: RND schema, Sensory schema)
  - Purpose: System of record.
  - RND schema: App-facing “holding”/staging and functional tables (dropdowns, notifications, approvals, holding tables pre-completion).
  - Sensory schema: Finalized data for reporting; receives data post-completion through controlled push from the app/transformation.
  - Current footprint: ~35 total tables (19 original sensory tables; additional app/RND tables added during development).
- Python (Pandas)
  - Purpose: Data Transformation Engine (intermediate and output files), question mapping, scoring, wide-to-long reshaping, code legend generation.
  - Maintained by: Python engineer (Rahul).
- Azure Active Directory (Internal users)
  - Purpose: Internal user authentication/authorization. Internal users added via AD with approvals from platform team.
- External User Access/Licensing
  - Purpose: Vendor access via separate, email-based IDs; licensing managed by Platform Team (Kaushal).
- Email Notifications
  - Purpose: Workflow alerts (e.g., vendor submission, approvals). Current implementation sends emails when vendors submit and at key workflow steps.

2. User Roles/Responsibilities
Role/Title | Responsibilities | Dashboard/View | Comments
- Data Admin (e.g., Angela Li, Jenn Soong) | Full lifecycle oversight; manage users/vendors; manage dropdowns; manage category mapping for transformation; run intermediate/output file steps; coordinate push to sensory schema; bypass approvals when needed; incident triage | View/Edit ALL tests (active and completed); Admin menus (vendors, users, dropdowns, bypass, category mapping); All dashboards | Currently cannot edit finalized data in sensory schema post-completion; requested in Phase 2.
- Sensory UX Lead | Create RFP; compile One-Pager; select vendor; submit for approval; sign off vendor acceptance; route SIF to R&D Lead; send SIF to vendor; receive and QC vendor files; compile McCain report; submit report for approval; conclude test | Own Active Tests; Completed Tests (read-only); notifications on vendor submissions | Receives email when vendor submits; can only work tests assigned to them; currently only one active editor per test (Phase 2: allow multi-editor).
- Line Manager | Approve/return One-Pager/proposal with comments; optionally create RFP (current capability) | Own dashboard with tests awaiting approval | Phase 2 ask: allow completing entire test workflow when they oversee testing (parity with Sensory Lead).
- Sensory Director | Approve/return One-Pager/proposal with comments | Own dashboard with tests awaiting approval | Approval authority at proposal/One-Pager and final report stages.
- R&D Lead | Complete Sample Information Form (SIF): product info, cooking instructions, holding/delivery protocols; complete Micro Clearance acknowledgement | Own tasks (SIF, Micro Clearance) | Sends SIF back to Sensory Lead; vendor sees SIF read-only and adds codes/equipment.
- Analytical Lead | Create analytical tests; plan sample info; upload analytical data; no approvals | Own Active/Completed Analytical Tests | Simplified workflow vs Sensory UX.
- Vendor (External) | View RFP details; submit proposals; view SIF; enter sample blinding codes and equipment; upload raw data/reports | Vendor Portal with limited views; Upload sections; Notifications to Sensory Lead | Auth via separate email-based IDs; license required per vendor user.
- Platform Admin (Kaushal team) | Provision licenses; grant external/internal access | N/A | Gatekeeper for external vendor licensing and internal user access enablement (email-driven).
- Support (Blackstraw) | Power Apps dev (Azure) for incidents; Python (Rahul) for transformation incidents | N/A | Incident-only remit per current contract; change requests deferred to Phase 2.

3. Workflow Phases (Functional Requirements)

Workflow 1: Sensory UX (External + Internal)
Phase 1.1: Login & Role-Based Dashboard
- ID: Req 1.1.1
- Description: Users authenticate and land on role-specific dashboard (Active Tests, Completed Tests, Approvals).
- Business Rule/Logic:
  - IF Role = Data Admin THEN show Admin menus (Vendors, Users, Dropdowns, Bypass approvals, Category Mapping, Table views).
  - IF Role = Sensory Lead THEN show Active Tests assigned; Completed Tests (read-only); vendor submission notifications.
- UI/UX Requirement:
  - Status badges for each test phase (proposal pending, approval pending, SIF pending, vendor upload pending, report approval pending, completed).
  - Minimal horizontal scrolling; responsive grid layouts.

Phase 1.2: Pre-Approval (New) Before RFP Submission to Vendors
- ID: Req 1.2.1
- Description: Introduce a pre-approval One-Pager step by Line Manager and Sensory Director before issuing the RFP to vendors.
- Logic:
  - IF One-Pager (background/objectives/products/plan) approved by both roles THEN enable RFP dispatch.
  - IF One-Pager returned with comments THEN Sensory Lead must update and resubmit; version history maintained.
  - IF updates post-approval change any field that impacts RFP scope (e.g., objectives, products) THEN invalidate previously sent RFPs and notify impacted vendors; require vendor re-acknowledgment.
- UI/UX Requirement:
  - “Download One-Pager” as PPT export (Phase 2 feature) with mapped fields.
  - Visual indicator when any One-Pager field differs from the last vendor-notified version.

Phase 1.3: RFP Creation and Dispatch
- ID: Req 1.3.1
- Description: Sensory Lead creates RFP with project background, objectives, products, test type (consumer vs descriptive), region, category, etc.
- Logic:
  - IF Pre-Approval status != Approved THEN RFP Dispatch = Disabled.
  - Multi-vendor support: allow selection of one or more vendors for solicitation.
- UI/UX Requirement:
  - Multi-select vendor picker; summary of dispatched vendors; audit trail.

Phase 1.4: Vendor Proposal Submission
- ID: Req 1.4.1
- Description: Vendors submit proposals in Vendor Portal; can upload proposal docs and cost estimates.
- Logic:
  - Notification: On proposal submission, email Sensory Lead.
  - IF multiple proposals received THEN Sensory Lead selects a proposal for advancement.
- UI/UX Requirement:
  - For Sensory Lead, side-by-side proposal comparison view; visible “Uploaded” flags on files (no click-to-discover).

Phase 1.5: One-Pager Compilation & Approval
- ID: Req 1.5.1
- Description: Consolidate vendor selection and project details into One-Pager; line manager and director review and approve.
- Logic:
  - Approvers may Approve or Return with comments.
  - Approved One-Pager locks inputs that drive vendor scope; subsequent changes trigger vendor re-ack per Req 1.2.1.
- UI/UX Requirement:
  - Track approvals with timestamps and comments; show approval status on dashboard.

Phase 1.6: Vendor Acceptance Sign-Off
- ID: Req 1.6.1
- Description: Sensory Lead triggers sign-off to selected vendor, indicating test starts.
- Logic:
  - Sign-off notification emailed to vendor.
  - IF sign-off not sent THEN vendor cannot upload test results.
- UI/UX Requirement:
  - Show “Vendor Accepted” badge.

Phase 1.7: Sample Information Form (SIF) – R&D Lead
- ID: Req 1.7.1
- Description: R&D Lead completes multi-page SIF: product info, cooking instructions, holding/delivery protocols.
- Logic:
  - SIF required for product-based tests.
  - Validation rules to prevent duplicates (e.g., NA/blank normalization) and ensure completeness (see Data Quality).
  - Bulk operations (Phase 2): copy/paste from Excel for batch entries.
  - Export (Phase 2): SIF downloadable as Excel and PDF.
- UI/UX Requirement:
  - Tabbed pages; progressive disclosure; dropdowns filtered by category (Primary vs Secondary vs Delivery vessels must be isolated).

Phase 1.8: Vendor Codes & Equipment
- ID: Req 1.8.1
- Description: Vendor views SIF, enters sample blind codes that will match raw data, and records equipment used.
- Logic:
  - Code Legend must map to raw data keys; system validates code coverage vs expected samples.
  - Vendors can add equipment not in list; new equipment entries flagged for admin review.
- UI/UX Requirement:
  - Clear code-to-sample mapping table with completeness indicator.

Phase 1.9: Micro Clearance Acknowledgement
- ID: Req 1.9.1
- Description: R&D Lead records date of microbiological clearance for pilot-line samples.
- Logic:
  - IF Micro Clearance required AND not completed THEN prevent test start in vendor portal.
- UI/UX Requirement:
  - Simple date picker and status badge “Cleared/Not Cleared”.

Phase 1.10: Vendor File Uploads (Raw Data/Reports)
- ID: Req 1.10.1
- Description: Vendors upload raw test data and reports into designated sections.
- Logic:
  - Email notification to Sensory Lead upon each upload.
  - Enforce allowed file types (e.g., CSV/XLSX for raw data; PDF/PPT for reports).
- UI/UX Requirement:
  - Show section-level “Uploaded / Missing” icons; file names and timestamps inline.

Phase 1.11: Data Transformation – Intermediate & Output
- ID: Req 1.11.1
- Description: Data Admin validates and finalizes transformation from raw to database-ready format.
- Logic:
  - Intermediate File:
    - Auto-generate Code Legend to decode products from vendor codes.
    - Reformatted tab: Map submitted questions to DB Question IDs; calculate match score.
    - Score thresholds (to be defined): 
      - IF score >= Exact_Threshold THEN auto-accept; status “Exact Match”.
      - IF score in [Review_Low, Review_High) THEN status “Check”.
      - IF score < Poor_Threshold THEN status “Poor Match”.
    - Data Admin Actions:
      - Leave blank to accept.
      - Enter “remove” to drop a question.
      - Enter “mismatch” and specify corrected Question ID.
      - Enter “new” and add a new sheet with question definition for creation.
  - Output File:
    - Restructure wide vendor format to long format per respondent per product per question.
    - Populate Consumer, Respondent, and related target tables with resolved Question IDs.
  - Audit:
    - Capture who performed mappings, timestamps, and decisions.
- UI/UX Requirement:
  - Admin-facing validation screen showing mapping statuses, scores, filters by status (Exact/Check/Poor), and bulk actions.

Phase 1.12: McCain Report Creation & Approval
- ID: Req 1.12.1
- Description: Sensory Lead compiles internal report; submits for line manager/director approval.
- Logic:
  - Approvers can Approve or Return with comments.
  - Phase 2 Output: Auto-generate report PPT sections from entered fields (objectives, background, action standards).
- UI/UX Requirement:
  - “Generate Report PPT” button with post-editable template.

Phase 1.13: Test Conclusion (Gated)
- ID: Req 1.13.1
- Description: Sensory Lead concludes test, moving it to Completed view.
- Logic:
  - IF Transformation status != Completed (intermediate validated + output loaded to sensory schema) THEN block Conclusion; display blocking message.
  - IF concluded THEN freeze writes to RND staging, push finalized records to Sensory schema.
  - Phase 2: Allow Data Admin to edit select fields post-completion with audit trail; on save, auto-propagate to Sensory schema.
- UI/UX Requirement:
  - Confirmation dialog references transformation status; show links to unresolved items.

Workflow 2: Analytical (Internal)
Phase 2.1: Create Analytical Test
- ID: Req 2.1.1
- Description: Analytical Lead creates test with minimal background data.
- Logic:
  - No vendor or management approval steps.
- UI/UX Requirement:
  - Simplified form; defaults for standard instrument tests.

Phase 2.2: Plan Sample Info
- ID: Req 2.2.1
- Description: Enter sample details analogous to SIF (reduced scope).
- Logic:
  - Basic validations (no duplicate entries; required fields).
- UI/UX Requirement:
  - Streamlined layout.

Phase 2.3: Upload Analytical Data
- ID: Req 2.3.1
- Description: Upload instrument measurement data; transform to database format.
- Logic:
  - Apply transformation to normalize structure for Power BI.
- UI/UX Requirement:
  - Upload status and data quality checks.

Cross-Workflow Admin Functions
Phase A.1: Vendor & User Administration
- ID: Req A.1.1
- Description: Data Admin manages vendor users and internal users.
- Logic:
  - Vendor adds require license request to Platform Admin (Kaushal) and activation.
  - Internal users created via AD; Platform Admin approval required.
- UI/UX Requirement:
  - Self-service request queue and status; reduce email-only dependencies (Phase 2 enhancement).

Phase A.2: Dropdown & Category Management
- ID: Req A.2.1
- Description: Admin manages dropdowns and three-level dependent lists (e.g., Country/Region; Primary/Secondary/Delivery types).
- Logic:
  - IF field = Primary Package Type THEN only show Primary Package entries; similarly for Secondary/Delivery.
- UI/UX Requirement:
  - Table editor for bulk updates (must support 700+ questions, 500+ attributes) with filters and search.

Phase A.3: Bypass Approvals (Existing)
- ID: Req A.3.1
- Description: Admin can bypass approval steps when approvers are unavailable.
- Logic:
  - Capture reason and timestamp; notify approvers of bypass event.
- UI/UX Requirement:
  - Bypass button visible only to Admin with warning dialog.

4. Data Transformation & Mapping Logic

Input Raw Data Formats
- Vendor-submitted files in varied structures (CSV/XLSX). Standard template encouraged but not enforced due to vendor diversity and test types.

Core Transformation Steps
- Code Legend:
  - Decode vendor sample codes to product/sample identifiers as specified in SIF; error if codes do not cover all expected samples.
- Question Mapping:
  - Compare incoming question text and answer options to master Question DB.
  - Compute match score (string similarity and option-set compatibility).
  - Status classification:
    - Exact Match: score ≥ Exact_Threshold → auto-accept.
    - Check: Review_Low ≤ score < Review_High → flag for admin check.
    - Poor Match: score < Poor_Threshold → likely remove or add as new.
- Admin Overrides:
  - IF Decision = “remove” THEN exclude question from output.
  - IF Decision = “mismatch” AND CorrectedID provided THEN map to CorrectedID.
  - IF Decision = “new” THEN create a New-Question definition (sheet) with:
    - Question text, answer options, scale, category, language, effective date.
    - On approval, new Question ID generated and mapping updated.
- Category Mapping:
  - IF Test Type = Descriptive Analysis AND Product Category = X THEN use attribute list (panelist attributes) defined for Category X.
- Restructuring Wide → Long:
  - For each Respondent and Product: pivot responses from columns into rows.
  - Populate:
    - Consumer table (test-level info)
    - Respondent table (participant-level)
    - Response table (question-level long format)
  - Preserve foreign keys (TestID, RespondentID, ProductID, QuestionID).
- Finalization:
  - On Data Admin “Transform Complete,” generate Output File and push to Sensory schema.
- Data Quality Normalization:
  - Normalize NA/Blank entries; unify casing; trim whitespace; deduplicate entries.

Input Raw Data to Question Mapping Logic (Explicit Rules)
- IF MatchStatus = “Poor Match” THEN Data Admin must choose:
  - remove OR mismatch + CorrectedID OR new + New-Question definition.
- IF MatchStatus = “Check” THEN Data Admin must confirm accept or treat as mismatch/new.
- IF Answer Option Set Mismatch = True THEN force mismatch or new (cannot auto-accept).
- IF Vendor code not found in Code Legend THEN raise error; require SIF code correction or legend update.
- IF SIF missing (non-product tests) THEN:
  - Current behavior: workflow breaks (not allowed).
  - Phase 2 requirement: allow SIF-optional tests with alternate minimal metadata and transformation path.

5. Non-Functional Requirements (NFRs) & Data Quality

Performance & Scalability
- The system must support:
  - Admin table editors with 700+ questions and 500+ attributes without perceptible lag (target <2 seconds for filter/search, <3 seconds for save).
  - 20 concurrent users with page responses <3 seconds for common actions (form load, save, list paging).
  - Vendor uploads up to 50 MB per file with upload completion <30 seconds on standard corporate network.
- Availability & Observability
  - Target uptime ≥ 99.5% monthly.
  - Implement availability monitoring of app endpoints and alerting to support and Data Admins on outages.
  - Capture performance telemetry (page load times, API durations), error logs, and user action audit logs.
- Security
  - Mandatory security testing prior to next release:
    - OWASP Top 10 vulnerability assessment for the Power Apps front-end and any custom connectors.
    - Authentication and authorization review for external vendor access (consider Azure AD B2B or hardened external identity).
    - Rate limiting and file upload scanning (antivirus, type/size enforcement).
    - Penetration testing including brute-force and DDoS simulation (as feasible for platform).
  - Role-based access control enforcing least privilege.
  - Audit trail for approvals, bypasses, data edits, and transformation decisions.
  - Secure data at rest (Azure SQL TDE) and in transit (TLS).
- Data Integrity & Quality
  - Post-completion edits by Data Admin must automatically and reliably propagate to Sensory schema with versioning and audit.
  - Enforce normalization (NA/blank standardization) and deduplication on controlled domains (e.g., dropdown values).
  - Referential integrity across TestID, RespondentID, ProductID, QuestionID; reject inconsistent loads.
  - Validate SIF completeness; prevent invalid dropdown cross-category selections (primary vs secondary vs delivery).
- Internationalization
  - Support global usage (timezone-aware timestamps, locale-agnostic parsing for numeric and date fields in uploads).

6. Prioritization Matrix (MoSCoW)

Priority | Requirement | Rationale
- Must | Pre-Approval before RFP (Req 1.2.1) | Prevents rework and vendor misalignment; addresses governance gap.
- Must | Gate Test Conclusion on Transformation Complete (Req 1.13.1) | Prevents loss of ability to correct raw data; safeguards data integrity.
- Must | Post-Completion Admin Edits with Propagation | Corrects discovered data issues; aligns reporting with ground truth.
- Must | Improve Data Transformation QA (score thresholds, UI, admin actions) (Req 1.11.1) | Current matching rate observed as low as 65%; time-consuming manual checks.
- Must | Dropdown category filtering (Primary/Secondary/Delivery) | Prevents frequent data entry errors; reduces cleanup.
- Must | Data quality validations (NA/blank normalization, dedupe) | Avoids duplicates and schema pollution.
- Must | Security testing & Observability (monitoring/alerts) | External vendor access mandates security posture and uptime visibility.
- Should | Multi-user editing on Active Tests | Reflects real-world collaboration; reduces bottlenecks.
- Should | SIF bulk copy/paste and SIF export (Excel/PDF) | Significant time saver and transparency for R&D teams.
- Should | Improved search/filter for Completed Tests | Speeds retrieval.
- Should | Visible file upload status indicators | Eliminates “click-to-discover” frustration; clarity.
- Should | One-Pager PPT export; Report PPT generation | Standardizes stakeholder communications.
- Could | Internal user/vendor self-service access requests | Reduces platform team emails; streamlines onboarding.
- Could | Integration with SAP/Coupa (Vendor master/PO linkage) | Future automation; dependent on enterprise transformations.
- Won’t (Phase 2) | Predictive analytics/product formulation prediction | Requires broader product/process/material datasets; slated for future phases.
- Won’t (Phase 2) | Supplier ingredient/COA master data (TraceGains integration) | Outside current scope; separate platform better suited.

7. Project Scope (In/Out Table)

In-Scope (Phase 2)
- Sensory UX workflow enhancements: pre-approval gating, vendor re-acknowledgment on changes, conclude-test gating.
- Admin post-completion edit and automatic propagation to Sensory schema with audit.
- Transformation Engine UI and logic enhancements (score thresholds, bulk review, audit trail).
- Dropdown/category filtering corrections for packaging types.
- SIF bulk copy/paste; SIF export (Excel/PDF); manage non-product tests (SIF-optional path).
- Multi-user collaboration on active tests.
- UX improvements: reduce horizontal scrolling, structured page layouts, visible file status, better filters/search.
- Security testing, performance baselining, availability monitoring and alerting.
- Improved data quality checks (NA/blank normalization; dedupe protections).
- Role capability: allow Line Managers to complete full workflow when designated.

Out-of-Scope (Phase 3/Future)
- Integration with SAP/Coupa (vendor master, PO data).
- Supplier ingredient/COA updates via TraceGains or similar.
- Predictive analytics for formulation outcomes.
- Automated license provisioning workflows beyond basic request/status.

8. Conflict Identification & Open Items

Conflicts/Technical Disagreements
- Table UI feasibility in Power Apps:
  - Vendor claims table format for managing 700 questions/500 attributes is impractical and will be slow; stakeholders require table-based admin with filters and bulk operations.
- Transformation Engine “learning”:
  - Vendor originally indicated matching rate would improve via supervised training; stakeholders observe no improvement over time, matching sometimes ~65%. Vendor now states model is static.
- UX constraints:
  - Vendor asserted Power Apps layout limitations justify horizontal/vertical scrolling; stakeholders require reduced scrolling and improved navigation.
- Post-completion edits:
  - Current design blocks edits propagating to Sensory schema; stakeholders require post-completion edit capability with downstream reflection.

Open Items/Decisions Needed
- Define exact transformation score thresholds (Exact_Threshold, Review_Low, Review_High, Poor_Threshold) and default actions.
- Confirm external auth model (remain email-based IDs vs adopt Azure AD B2B) with Security/IT.
- Confirm non-product test workflow: minimal required metadata, downstream transformation path, and reporting behavior.
- Define audit log retention and access (who can view/ export).
- Clarify concurrency/locking model for multi-user editing on the same test (optimistic locking, field-level locks, or check-in/check-out).
- Specify SIF export formats and templates; confirm required columns for Excel export.
- Determine monitoring/alerting tooling and ownership (who is paged, thresholds, SLAs).
- Establish performance test plan (concurrency targets, scenarios).
- Confirm Line Manager expanded permissions and any governance constraints.
- Confirm One-Pager and Report PPT templates and field-to-slide mappings.

Detailed Functional Additions (Phase 2 Backlog Items Mapped to Transcript)
- Pre-Approval One-Pager before RFP; vendor re-ack on scope changes.
- Data Admin post-completion edit capability with propagation to Sensory schema.
- Transformation Engine:
  - Mapping UI with statuses (Exact/Check/Poor), score display, bulk resolve; enforce admin decisions (“remove”, “mismatch + ID”, “new + definition”).
  - Category-to-attribute mapping management UI.
- Non-Product Tests: SIF-optional path without breaking workflow.
- Multi-Editor: Allow multiple Sensory team members to work on active tests.
- Bulk SIF copy/paste from Excel; SIF export to Excel/PDF.
- File upload visibility: inline “Uploaded/Missing” icons; file names and timestamps.
- Dropdown filtering corrections for packaging types.
- Improved completed test search/filtering.
- One-Pager PPT export; auto-generate report PPT from standardized fields.
- UX remediation: reduce horizontal scrolling, improve layout and navigation.
- Data quality: normalize NA/blank, prevent duplicate domain entries, standard validations before saving to SQL.
- Role enhancement: permit Line Managers to complete full test workflows.
- Admin dropdown/category maintenance via table UI with filters and bulk edit.

Appendix: Current System Facts from Transcript (Traceability)
- Architecture: Stakeholder Portal, Vendor Portal, Transformation Module.
- Roles and access delineated; vendors limited; internal users see own tests and peers’ completed tests; admins see all.
- Notifications: Emails when vendors submit; approval cycles for One-Pager and reports.
- SIF: Product info, cooking instructions, holding/delivery protocols; vendor enters codes; equipment lists extendable by vendor; micro clearance by R&D lead.
- Data flow: App writes to RND (holding) tables during workflow; only on completion push to Sensory schema; Power BI reads Sensory schema.
- Data size: 35 total tables; 19 original sensory; additional app tables; 700+ questions, 500+ attributes to manage.
- Issues: UX basic with extensive scrolling; invisible link statuses; no bulk SIF paste; no SIF export; non-product tests not supported; only one user can edit an active test; post-completion edits don’t flow to reporting tables; transformation matching not improving; manual vendor and user provisioning via emails; reactive incident support (≈45 tracked incidents since go-live).
- Go-Live: March 2025 (effective); 3 months in production at time of meeting; users are global; expected 50–100 users in Year 1.

This document removes conversational filler and translates stakeholder pain points into explicit, testable requirements and rules to guide Phase 2 delivery and governance.