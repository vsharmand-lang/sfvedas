import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-022', 'index.html')

SUMMARY_BULLETS = """
            <li>The significant operational and technical risks of executing unstructured data migrations into Salesforce.</li>
            <li>How to construct a comprehensive Data Migration Schema and Relational Mapping Matrix.</li>
            <li>A tactical, step-by-step sequential migration order of operations for standard and custom Salesforce objects.</li>
            <li>The critical business value of mock loads, dry runs, and sandbox migration rehearsals.</li>
            <li>Practical strategies for data cleansing, duplicate prevention, and volume management before go-live.</li>
            <li>A comprehensive go-live cutover checklist and post-load reconciliation auditing framework.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">The Hidden Costs of Poor Salesforce Data Preparation</a></li>
            <li><a href="#s2">Constructing the Data Migration Mapping Matrix</a></li>
            <li><a href="#s3">Designing a Zero-Loss Relational Migration Sequence</a></li>
            <li><a href="#s4">The Critical Role of Mock Loads and Dry Runs</a></li>
            <li><a href="#s5">Go-Live Cutover and Post-Load Reconciliation</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">The Hidden Costs of Poor Salesforce Data Preparation</h2>
        <p>In enterprise Salesforce delivery, data migration is frequently treated as a minor, downstream technical task. Delivery leaders and project managers allocate substantial budget to custom LWC development, automated flow configurations, and system integrations, while assuming that loading legacy data into the new org is a simple matter of mapping columns in a CSV file and executing a data loader job. This naive assumption is one of the primary drivers of go-live delays, budget overruns, and severe post-launch user adoption failures. When you migrate poor-quality, unstructured, or duplicate data into a pristine Salesforce environment, you immediately compromise the platform's architectural integrity and destroy business trust.</p>

        <p>The first major cost of poor data preparation is **immediate user rejection**. Salesforce is built to act as the single source of truth for customer and operational data. If users log in on go-live day and are confronted with hundreds of duplicate accounts, incomplete contact records with missing email addresses, and active opportunities that actually closed years ago, they will lose faith in the system. They will abandon the platform in favour of legacy spreadsheets and offline databases, completely undermining the business case for the platform. A pristine, highly optimised Lightning console is worthless if the data driving it is corrupt and unreliable.</p>

        <p>The second cost is **technical and customisation debt**. When data migration is poorly planned, developers are often forced to write complex "data remediation" code, construct custom validation rules, or build custom fields to accommodate legacy anomalies. For instance, instead of cleansing incomplete legacy addresses, the team might create custom fields to house "Legacy Address 1" and "Legacy Address 2," bypass standard state and country picklist validations, and write messy Apex triggers to handle the resulting inconsistencies. This compromises the platform's standard data model, creating long-term maintenance overhead and introducing severe friction for future integrations and analytics packages.</p>

        <p>Finally, migrating dirty data is a significant source of **operational risk and regulatory liability**. Under modern privacy frameworks like GDPR and CCPA, organisations are legally obligated to maintain accurate customer records, respect data retention policies, and enforce customer consent preferences. Migrating unverified, expired, or non-compliant legacy records directly into a production environment can trigger severe compliance violations, resulting in massive financial penalties and reputational damage. To protect your programme and your platform, data preparation must be treated as a critical, high-priority workstream that runs parallel to development from day one.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Garbage Paradox</strong>
            <p>Loading dirty legacy data into a clean, newly designed Salesforce org is like putting cheap, contaminated fuel into a high-performance sports car. The engine will fail, and the system will break. No amount of custom LWC code or automated process flows can compensate for a corrupt database foundation. Clean your data before you load it, not after.</p>
          </div>
        </div>

        <h2 id="s2">Constructing the Data Migration Mapping Matrix</h2>
        <p>To execute a secure, structured Salesforce data migration, the architecture team must construct a comprehensive **Data Migration Mapping Matrix (DMMM)**. The DMMM is a living technical specification that maps every single legacy database table and attribute directly to its corresponding target Salesforce standard or custom object and field. Constructing this matrix is a rigorous process that requires deep collaboration between legacy database administrators, Salesforce solution architects, and business data stewards.</p>

        <p>For every target Salesforce field, the DMMM must document four critical technical attributes. The first is **Data Type Alignment**. The matrix must map the legacy field type (e.g. `VARCHAR(255)`) to the precise Salesforce field type (e.g. `Text(255)`, `Phone`, `Email`, `Picklist`). If a legacy attribute is mapped to a Salesforce Picklist, the DMMM must include a detailed **value translation table**, mapping every single legacy value directly to a valid Salesforce picklist API value. For instance, legacy values like "NY," "New York," and "N.Y." must be translated to the standard "New York" value to ensure consistency and prevent picklist value contamination.</p>

        <p>The second attribute is **Validation Rule Compatibility**. The Salesforce org's active validation rules, required fields, and duplicate management rules must be documented within the mapping matrix. If a legacy record lacks a required field, such as a billing country or email address, the data loading script will fail. The DMMM must define the business rules for handling these incomplete records, specifying whether to enrich the records at the source, apply a standardized fallback value (e.g. "Unknown" or "Not Provided"), or quarantine the records in a cleansing table for manual business remediation before load.</p>

        <p>The third attribute is **Target ID Generation and External IDs**. To migrate relational data safely, you must maintain the relationships between records. To achieve this in Salesforce, every custom or standard object involved in the migration must contain a dedicated, indexed **External ID** field (configured as unique and external ID). This field is populated with the legacy database primary key. When migrating child records, the data loading script uses the parent's External ID to dynamically associate the records during the load, eliminating the need to execute manual VLOOKUPs in Excel or perform complex ID mapping queries. This ensures relational integrity across millions of records.</p>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The External ID Index</strong>
            <p>Always mark your External ID fields as unique and indexed in Salesforce. This not only prevents duplicate legacy records from being loaded twice, but also significantly accelerates the performance of your data load operations, as the platform's database engine can rapidly resolve relations without scanning the entire table.</p>
          </div>
        </div>

        <h2 id="s3">Designing a Zero-Loss Relational Migration Sequence</h2>
        <p>Salesforce enforces rigid relational integrity constraints across its database schema. You cannot load a child record (such as a Contact or an Opportunity) before its corresponding parent record (the Account) exists in the system. Attempting to load data in a random or uncoordinated sequence will result in thousands of relational lookup failures. To ensure a zero-loss relational migration, the delivery team must design and execute a highly structured, sequential **Object Migration Order of Operations**.</p>

        <p>The sequential order of operations begins with **Independent Foundation Data**. This includes objects that do not depend on other transactional records, such as Salesforce Users, standard and custom Price Books, and Products. These records must be fully loaded, validated, and locked down first. Crucially, the User migration must be executed early, as every subsequently loaded record must be assigned to an active Salesforce owner. If the legacy owner does not exist in the new org, the records will fallback to a generic integration owner, obscuring data lineage and sharing security.</p>

        <p>The second step is the **Core Customer Accounts**. This includes standard Business Accounts, Person Accounts, and Partner Accounts. Because Accounts act as the absolute root parent for almost all Salesforce data models, they must be loaded and reconciled before any other transactional or child records are touched. Ensure that during the Account load, standard duplicate rules are temporarily deactivated or configured to "report" rather than "block," allowing the migration script to handle cleansing and deduplication via its pre-cleansed mapping datasets.</p>

        <p>The third step is **Primary Customer Relations**. This encompasses standard Contacts (which represent the physical people associated with business accounts) and Account Team Members. Once Contacts are fully loaded, the team can proceed to the fourth step: **Sales and Operational Transactions**. This includes Opportunities, Opportunity Line Items, Contracts, Cases, and custom operational objects. Finally, the migration concludes with **Activity History and Attachments**, loading Tasks, Events, Email Messages, and Content Notes. This sequential approach guarantees that every lookup relationship resolves correctly, ensuring a complete, zero-loss relational structure.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>The Sequential Hierarchy</strong>
            <p>Enforce the sequential hierarchy of Salesforce data loading: 1. Users &amp; Products -> 2. Accounts -> 3. Contacts -> 4. Opportunities &amp; Cases -> 5. Tasks, Events &amp; Files. Deviation from this sequence will trigger massive relational lookup errors, delaying your cutover and corrupting data relationships.</p>
          </div>
        </div>

        <h2 id="s4">The Critical Role of Mock Loads and Dry Runs</h2>
        <p>A delivery manager who executes a data migration for the first time in the production environment during go-live weekend is planning for project failure. A data migration is not a one-off technical event; it is a complex process that must be rehearsed multiple times in dedicated sandbox environments. The delivery team must execute at least three complete **Migration Mock Loads (Dry Runs)** before the actual go-live cutover begins.</p>

        <p>Each mock load must be executed in a pristine, full-copy sandbox that mirrors the exact configuration and metadata structure of the target production environment. The primary goal of **Mock 1** is to test the technical feasibility of the migration scripts, validate the Data Migration Mapping Matrix, and expose basic data anomalies. This mock load will almost certainly trigger thousands of failures due to unexpected null values, validation rule mismatches, and picklist discrepancies, providing the technical team with the raw data needed to refine the cleansing and mapping scripts.</p>

        <p>The goal of **Mock 2** is to execute a complete, end-to-end relational load of the entire legacy dataset, focusing on validation rule remediation, sharing calculations, and integration performance. Crucially, Mock 2 is used to **measure load velocity and timing**. The technical team must log the exact start and end times for every step of the migration sequence (e.g. Account extraction, cleansing, transformation, and Salesforce loading). These duration metrics are vital for constructing the final go-live cutover schedule, ensuring that the business downtime can be accurately planned and managed.</p>

        <p>The final rehearsal, **Mock 3**, is a complete dress rehearsal of the go-live weekend. The technical team executes the migration scripts against the latest production data snapshot, utilizing the exact user profiles, API thresholds, and DevOps deployment sequences planned for go-live. Mock 3 is immediately followed by a formal **business UAT validation audit**, where lead business users and data stewards log in to the sandbox to verify the completeness, relational accuracy, and usability of the migrated data. Only when the business signs off on the Mock 3 data audit should the program be authorized to proceed to production cutover.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>Do not allow your technical team to skip mock load cycles because of timeline pressure. Rehearsing your data migration is the single most effective risk mitigation strategy for go-live. Each mock load reveals hidden platform limits, script errors, and validation clashes that would otherwise crash your live production cutover.</p>
          </div>
        </div>

        <h2 id="s5">Go-Live Cutover and Post-Load Reconciliation</h2>
        <p>Go-live weekend represents the absolute climax of the Salesforce data migration workstream. To execute the final load safely, the delivery team must operate under a highly detailed, minute-by-minute **Cutover Runbook**. The runbook documents every technical and operational task, the exact person responsible, the start and end times, the dependencies between tasks, and the formal sign-off checkpoints required before moving to subsequent phases.</p>

        <p>A critical phase of the runbook is the **pre-load system optimization**. Before loading millions of legacy records into the live production environment, the team must optimize the platform for high-velocity data loading. This includes **deactivating active automation metadata**, such as Salesforce Flows, Process Builders, validation rules, sharing rules, and custom Apex triggers. If these automations are left active, they will trigger for every single loaded record, dragging down load speeds, hitting CPU governor limits, and sending thousands of automated email alerts to customers. Once the data load is complete, these automations are reactivated, and sharing rules are recalculated.</p>

        <p>Once the load operations conclude, the technical and business teams must execute a formal **Post-Load Reconciliation audit**. The technical team runs automated database queries to compare the source records count with the target Salesforce record counts, verifying that 100% of the records have loaded. For every single object, the team must generate a **reconciliation balance sheet**, documenting: Source Records Count = Success Loads + Failures. Any failures must be logged in a detailed error CSV file, showing the exact Salesforce field, record ID, and platform error message (e.g. `FIELD_CUSTOM_VALIDATION_EXCEPTION`).</p>

        <p>The business validation team then executes the **operational spot-check protocol**. Using a pre-defined list of high-value, complex customer accounts, business users log in to the production org to manually verify that the entire account history, contact relationships, active opportunities, and historical cases have migrated correctly. Once the reconciliation balance sheet is balanced, the error logs are analyzed, and the business signs off on the spot-check validation, the migration is officially declared a success. The production org is opened, and the business transitions to live operations with complete database integrity.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>Cutover Phase</th>
                <th>Core Technical Activities</th>
                <th>Required Deactivations</th>
                <th>Validation Gate</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Pre-Load Preparation</strong></td>
                <td>Run production backup; seed system foundation records (Users, Products)</td>
                <td>None; monitor user access</td>
                <td>100% User records active in Production</td>
              </tr>
              <tr>
                <td><strong>Platform Optimisation</strong></td>
                <td>Deactivate Flows, validation rules, Apex triggers; suspend active integrations</td>
                <td>Flows, Process Builders, Validation Rules, Sharing Rules, Apex Triggers</td>
                <td>System administration approval; metadata backup confirmed</td>
              </tr>
              <tr>
                <td><strong>Sequential Loading</strong></td>
                <td>Execute data loads in sequential order: Accounts -> Contacts -> Opportunities -> Cases</td>
                <td>Maintain full automation deactivation during active loading</td>
                <td>Review success/failure logs; 100% relational lookups resolved</td>
              </tr>
              <tr>
                <td><strong>Post-Load Audit</strong></td>
                <td>Reactivate platform automations; run full sharing rules recalculation</td>
                <td>None; reactivate all metadata</td>
                <td>Record counts balance sheet signed; business spot-checks completed</td>
              </tr>
            </tbody>
          </table>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Data migration is a critical technical workstream that must run in parallel with development from day one, not as an afterthought.</li>
            <li>Poor data preparation drives immediate user rejection, creates technical and customisation debt, and exposes the organisation to regulatory liability.</li>
            <li>A comprehensive Data Migration Mapping Matrix (DMMM) must document field data types, picklist translations, validations, and External IDs.</li>
            <li>Implement unique, indexed External ID fields in Salesforce to maintain legacy data relationships without manual Excel lookups.</li>
            <li>Enforce a strict Object Migration Order of Operations to satisfy Salesforce's relational integrity and lookup dependencies.</li>
            <li>Rehearse the migration through at least three complete Sandbox Mock Loads to accurately measure load velocity and identify metadata clashes.</li>
            <li>Optimize production load performance by deactivating Flows, validation rules, and Apex triggers before loading, reactivating them post-migration.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-section" id="quiz">
            <h2>Checkpoint: Test Your Understanding</h2>

            <div class="quiz-question" id="q1">
              <p>1. Why is the implementation of unique, indexed External ID fields critical for enterprise Salesforce data migrations?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. They allow business users to search for records using standard global search.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. They bypass Salesforce validation rules and sharing calculations during high-velocity data loads.</div>
                <div class="quiz-option" onclick="answer(this,'q1','right')">C. They enable the data loading tool to dynamically resolve child-to-parent lookup relationships using legacy primary keys, preventing relational failures.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. They automatically convert legacy character strings into standard picklist values.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. What is the correct sequence of operations when migrating core customer and transactional data into Salesforce?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. 1. Tasks/Events -> 2. Opportunities -> 3. Contacts -> 4. Accounts -> 5. Users.</div>
                <div class="quiz-option" onclick="answer(this,'q2','right')">B. 1. Users/Products -> 2. Accounts -> 3. Contacts -> 4. Opportunities/Cases -> 5. Tasks/Events.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. 1. Accounts -> 2. Opportunities -> 3. Users -> 4. Contacts -> 5. Tasks/Events.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. 1. Contacts -> 2. Accounts -> 3. Products -> 4. Cases -> 5. Users.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. Why must active Flows, validation rules, and Apex triggers be deactivated in the production environment before executing go-live data loads?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. Active metadata consumes additional storage space, hitting platform limits immediately.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. Deactivating metadata allows the technical team to bypass user profile license limits.</div>
                <div class="quiz-option" onclick="answer(this,'q3','right')">C. To accelerate loading speeds, prevent transactional locks, avoid hitting CPU governor limits, and stop the system from sending automated emails.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. Active rules block standard External ID fields from indexing properly during insertion.</div>
              </div>
            </div>
          </div>
"""

def main():
    if not os.path.exists(FILEPATH):
        print(f"Error: {FILEPATH} not found.")
        return

    with open(FILEPATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean literal \n sequences in related grid
    content = content.replace('\\n', '\n')

    # Replace placeholders
    content = content.replace('<!-- [[SUMMARY_BULLETS]] -->', SUMMARY_BULLETS.strip())
    content = content.replace('<!-- [[TOC_LINKS]] -->', TOC_LINKS.strip())
    content = content.replace('<!-- [[BODY_SECTIONS]] -->', BODY_SECTIONS.strip())
    content = content.replace('<!-- [[TAKEAWAY_BULLETS]] -->', KEY_TAKEAWAYS.strip())
    content = content.replace('<!-- [[QUIZ_QUESTIONS]] -->', QUIZ_QUESTIONS.strip())

    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully drafted DEL-022 content!")

if __name__ == '__main__':
    main()
