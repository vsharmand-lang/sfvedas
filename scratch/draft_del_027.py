import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-027', 'index.html')

SUMMARY_BULLETS = """
            <li>Why independent technical reviews are critical for auditing vendor quality and avoiding architectural drift.</li>
            <li>The step-by-step methodology for structuring a comprehensive Salesforce architecture audit.</li>
            <li>How to identify critical performance bottlenecks, trigger recursion, and governor limit vulnerabilities.</li>
            <li>Strategies for auditing sharing models, system security, and compliance guardrails.</li>
            <li>Practical frameworks for prioritizing, managing, and operationalising the post-review remediation backlog.</li>
            <li>Contractual and governance techniques for holding implementation partners accountable for code quality.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">Why Delivery Leaders Need Independent Technical Reviews</a></li>
            <li><a href="#s2">Structuring the Salesforce Code and Architecture Audit</a></li>
            <li><a href="#s3">Identifying Critical Platform Quality and Performance Gaps</a></li>
            <li><a href="#s4">Reviewing Sharing, Security, and Compliance Guardrails</a></li>
            <li><a href="#s5">Operationalising the Remediation Plan Post-Review</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">Why Delivery Leaders Need Independent Technical Reviews</h2>
        <p>In large-scale enterprise Salesforce programmes, delivery leaders face intense pressure to meet launch dates, stay within budgets, and satisfy demanding business stakeholders. In this high-stakes environment, the technical quality of the implementation is frequently compromised. Implementation partners, driven by tight milestones and resource constraints, may cut corners, rely on sub-optimal custom development where standard features would suffice, or neglect long-term platform health. Internal code reviews are often insufficient; developers within the delivery team are too close to the project, under too much pressure to release, and may suffer from groupthink. To safeguard the investment and secure the platform's future, organisations must implement independent, external technical reviews.</p>

        <p>An independent technical review serves as an objective, unbiased audit of your Salesforce org's architecture, configuration, customisation, and security posture. It is conducted by an architect who has no personal stake in the delivery timeline, vendor relationship, or past design decisions. This independence ensures complete objectivity. The primary goal is to identify hidden technical debt, compliance violations, security vulnerabilities, and scalability bottlenecks before they manifest as critical production outages, performance degradation, or data breaches. By catching these issues early, delivery leaders can take corrective action, hold vendors accountable, and prevent costly remediation efforts after go-live.</p>

        <p>Without an independent review, delivery leaders are effectively operating in the dark. They are forced to rely on the self-reporting of the implementation vendor, which naturally tends to minimise architectural risks to protect their commercial interests. A platform that appears functional during user acceptance testing (UAT) may collapse under the volume, concurrency, and complexity of a live production environment. Issues like trigger recursion, CPU timeouts, and record locking only become visible when thousands of users interact with the system simultaneously. An independent review simulates these conditions through static code analysis, data volume modelling, and architectural pattern analysis, providing a realistic assessment of the platform's readiness.</p>

        <p>Furthermore, an independent review acts as a vital tool for stakeholder management and alignment. When a programme is facing delays or escalating costs, disputes often arise between the client and the implementation vendor regarding the root causes. A vendor may blame legacy data quality or shifting client requirements, while the client may suspect poor engineering. An objective, data-backed technical review report provides a single source of truth, removing emotion from the discussion. It translates complex technical risks into clear business impacts, enabling steering committees, CIOs, and business sponsors to make informed, rational decisions regarding remediation, budgeting, and go-live schedules.</p>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The Independence Factor</strong>
            <p>True architectural governance requires a separation of duties. Never allow the same vendor responsible for building the solution to be the sole validator of its quality. An external review provides the objectivity required to protect your multi-million-pound CRM investment from technical drift and vendor lock-in.</p>
          </div>
        </div>

        <h2 id="s2">Structuring the Salesforce Code and Architecture Audit</h2>
        <p>To deliver maximum value, an independent Salesforce technical review must be structured, methodical, and comprehensive. It is not merely a cursory glance at a few Apex classes or a run of a static code analyser. It is a deep, multi-dimensional investigation that covers five core pillars: declarative configuration, custom programmatic development, data architecture, security/sharing model, and release management. A successful audit requires a structured timeline—typically spanning two to four weeks—comprising four distinct phases: scope definition, data gathering and scanning, stakeholder interviews, and synthesis/reporting.</p>

        <p>The first phase is **Scope Definition**. Here, the lead auditor aligns with client stakeholders to define the boundaries of the review. While a holistic audit is ideal, specific areas may receive greater focus based on the programme's pain points. For instance, if the client has security concerns, the sharing model and API integrations will be scrutinised. If the system is experiencing performance lag, the Apex triggers, Flows, and data skew will be prioritized. The auditor defines the success criteria, establishes access protocols to the target environments (usually a full copy sandbox), and secures the necessary documentation, including functional specifications, solution design documents, and integration architecture diagrams.</p>

        <p>The second phase is **Data Gathering and Scanning**. The auditor utilises automated tools to conduct an initial sweep of the Salesforce org. This includes running static code analysis (using tools like PMD or Salesforce Code Analyzer) on the custom Apex codebase, scanning declarative automations (using Flow analyzers), and utilising platform utilities like Optimizer to identify obsolete metadata, empty fields, and profile limits. Concurrently, the auditor manually reviews critical architectural components. They analyse the Apex trigger architecture, examining whether the team has implemented a single-trigger framework or allowed uncoordinated triggers to execute on the same object, which causes unpredictable order-of-execution issues and trigger recursion.</p>

        <p>The third phase is **Stakeholder Interviews**. Automated scans and document reviews only tell part of the story. To understand the "why" behind the technical patterns, the auditor conducts interviews with key personas, including the implementation partner's lead architect, developer leads, internal business analysts, and security officers. These interviews reveal the operational constraints, legacy integrations, and shifting business requirements that influenced the design. They also assess the technical maturity of the delivery team, identifying gaps in their understanding of Salesforce best practices, such as bulkification, custom metadata usage, or error logging frameworks. This qualitative context is essential for shaping realistic, actionable remediation recommendations.</p>

        <p>The fourth phase is **Synthesis and Reporting**. The auditor aggregates the quantitative scan results and qualitative interview insights into a comprehensive, high-impact technical audit report. The report is structured to address both executive and technical audiences. It begins with an executive summary, mapping technical findings to business risks (such as system instability, security exposure, or high maintenance costs) using a clear traffic-light system (Red, Amber, Green). For the technical team, the report provides a detailed, categorised breakdown of every finding, complete with specific metadata references, code snippets, root-cause analyses, and concrete remediation instructions.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Metadata Trap</strong>
            <p>Salesforce orgs can accumulate thousands of obsolete custom fields, deactivated validation rules, and orphaned Flows. If your audit focuses solely on custom code, you will miss the declarative bloat that degrades admin productivity and slows down metadata deployments. Ensure your audit covers the entire metadata footprint.</p>
          </div>
        </div>

        <h2 id="s3">Identifying Critical Platform Quality and Performance Gaps</h2>
        <p>The core of any technical review is the identification of platform quality and performance gaps that threaten system stability and scalability. Because Salesforce operates in a multi-tenant environment, the platform strictly enforces governor limits to prevent any single customer from monopolising shared resources. A poorly engineered solution will inevitably breach these limits, resulting in unhandled exceptions, transactional rollbacks, and a highly frustrating user experience. Delivery leaders must understand the most common and damaging performance vulnerabilities to monitor their remediation effectively.</p>

        <p>The first major vulnerability is **Trigger and Flow Recursion**. Trigger recursion occurs when a database operation (such as an insert or update) fires a trigger, which performs a sub-operation that fires the same trigger again, creating an infinite loop. This rapidly exhausts the Apex CPU timeout limit (10 seconds for synchronous transactions) or the DML statement limit (150 statements). Similarly, nested Loops and un-bulkified elements within Salesforce Flows are a massive performance bottleneck. If a Flow executes a SOQL query or a DML statement inside a loop, it will breach the governor limit (100 SOQL queries per transaction) when processing more than a handful of records. The audit must ensure that all Flows are structured to bulkify data processing and that Apex triggers utilise a robust, single-trigger framework that incorporates static variables to prevent recursive execution.</p>

        <p>The second critical area is **Data Skew and Ownership Skew**. These database-level design flaws cause severe performance degradation and record locking errors in high-volume environments. **Parent-Child Skew** occurs when a single parent record has more than 10,000 child records (for example, associating 50,000 contacts with a single generic 'Placeholder Account'). When a user updates a child record, Salesforce locks the parent record to maintain data integrity. If multiple users attempt to update different child records associated with the same parent concurrently, their transactions will block each other, leading to "UNABLE_TO_LOCK_ROW" exceptions. **Ownership Skew** occurs when a single user or queue owns more than 10,000 records of a specific object. This causes massive sharing recalculation overhead when that owner's role or group membership changes, stalling the entire org's sharing engine. The review audits the data model to ensure child records are distributed and that ownership is balanced across active users.</p>

        <p>The third performance gap is the **Lack of a Centralised Logging and Error Handling Framework**. Many Salesforce implementations rely on scattered, inconsistent try-catch blocks in Apex, or worse, have no error logging at all, allowing silent failures in background asynchronous processes (like Batch Apex or Queueable jobs). When errors occur, administrators have no way of knowing what failed, why, or which records were affected. An independent audit checks for the implementation of a robust, centralized logging framework (such as the open-source Nebula Logger or a custom platform-event-driven utility). This framework should capture full execution contexts, stack traces, and record IDs, and save them in a secure, queryable custom object. This enables rapid debugging, reduces downtime, and ensures that data integrity issues are caught and resolved proactively before users even notice them.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>CPU Timeouts</strong>
            <p>Apex CPU timeout issues are incredibly difficult to debug because they are highly transient, depending on concurrent transaction volume and Salesforce server load. Enforce proactive performance testing on your codebase, and replace heavy custom programmatic logic with standard features or asynchronous processes to keep your CPU time low.</p>
          </div>
        </div>

        <h2 id="s4">Reviewing Sharing, Security, and Compliance Guardrails</h2>
        <p>Because Salesforce houses highly sensitive customer records, financial transactions, and proprietary business intellectual property, its security configuration must be absolutely ironclad. Security in Salesforce is dynamic, governed by a complex interplay of Org-Wide Defaults (OWDs), role hierarchies, sharing rules, permission sets, and programmatic security enforcement. A technical audit must meticulously examine these security layers to ensure compliance with corporate data protection policies, external regulations (such as GDPR or HIPAA), and the principle of least privilege.</p>

        <p>The first security audit target is the **Data Sharing Model and OWDs**. Org-Wide Defaults define the baseline access level that users have to records they do not own. A major anti-pattern in rushed implementations is setting OWDs to "Public Read/Write" for core objects (like Account, Contact, or custom financial objects) simply because the implementation partner found it easier than configuring a structured sharing model. This exposes sensitive data to unauthorized internal users and increases the risk of data exfiltration. The auditor reviews OWD settings, ensuring they are set to "Private" or "Public Read Only" where business confidentiality is required, and that access is opened up systematically using role hierarchies, criteria-based sharing rules, or restricted sharing groups.</p>

        <p>The second critical area is **Programmatic Security Enforcement in Custom Apex**. When developers write custom Apex controllers, APIs, or trigger handlers, the code executes by default in a privileged system context, bypassing the user's object-level security (CRUD), field-level security (FLS), and sharing rules. If a developer fails to explicitly enforce security, a user could view or modify fields they have no permission to access. The audit scans the codebase to ensure that Apex classes enforce sharing rules by utilizing the `with sharing` keyword. Furthermore, the auditor verifies that all custom SOQL queries and DML statements utilise standard security enforcement keywords, such as `WITH USER_MODE`, or enforce field-level security checks using `Security.stripInaccessible()`. Any instance of `without sharing` is heavily scrutinized and must be justified by an approved Architectural Decision Record (ADR).</p>

        <p>The third security concern is the **Exposure of Credentials and Insecure Integrations**. Modern enterprise Salesforce orgs are connected to multiple third-party systems via REST or SOAP APIs. A common and severe vulnerability is hardcoding API endpoints, client secrets, and passwords directly within Apex classes, or storing them in custom metadata without encryption. This exposes credentials to any developer or administrator with access to the sandbox codebase. The review verifies that all external integrations utilize **Named Credentials** or **External Credentials**. These standard platform features securely store authentication details, support OAuth flows, and abstract endpoints away from custom code, ensuring that credentials are never exposed in plaintext and are securely managed by the Salesforce platform.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>The Least Privilege Rule</strong>
            <p>Deactivate generic profiles and migrate your user permissions entirely to Permission Sets and Permission Set Groups. This standard Salesforce pattern prevents permission creep, simplifies user onboarding, and allows your security officer to audit and adjust specific user privileges without altering core profiles.</p>
          </div>
        </div>

        <h2 id="s5">Operationalising the Remediation Plan Post-Review</h2>
        <p>An independent technical review is only as valuable as the action it inspires. A common failure in delivery programmes is treating the audit report as a passive document—a tick-box exercise that is filed away while the delivery team continues using the same high-risk patterns. To prevent this waste, delivery leaders must proactively operationalise the audit findings, translating them into an actionable, prioritised backlog and establishing a governance structure to monitor remediation progress.</p>

        <p>The first step in operationalisation is **Triage and Prioritisation**. The audit report will inevitably contain dozens, if not hundreds, of findings ranging from minor formatting guidelines to critical security breaches. Attempting to fix everything at once is a recipe for delivery paralysis. The delivery leader must collaborate with the lead auditor, the internal product owner, and the vendor's technical lead to triage the findings using a **Risk-Impact Prioritisation Matrix**. Findings are categorised into four distinct tiers: Critical (system-stalling or severe security risks that must be fixed immediately), High (must be resolved before go-live to ensure launch stability), Medium (technical debt that can be deferred to post-launch hypercare or early sprints), and Low (best-practice improvements to be addressed during continuous maintenance).</p>

        <p>The second step is **Backlog Integration and Vendor Accountability**. Every accepted audit finding must be converted into a structured user story or bug ticket within the programme's tracking tool (such as Jira). These tickets must clearly describe the issue, reference the specific metadata component, specify the remediation steps, and define clear acceptance criteria based on the audit's success gates. More importantly, delivery leaders must hold the implementation partner contractually accountable for the quality of their work. If the review identifies that the vendor has breached agreed-upon coding standards (such as failing to bulkify triggers, leaving hardcoded IDs, or failing to write unit tests), the remediation of these issues must be executed by the vendor at their own expense, with milestone payments bound to the successful passing of the audit's remediation gates.</p>

        <p>Finally, establish **Continuous Automated Quality Gates** to prevent the reintroduction of technical debt. It is not enough to clean the org once; you must ensure it stays clean. Integrate static code analysis tools (PMD, EsLint) directly into your CI/CD deployment pipeline. Configure the pipeline to block any deployment package that fails to meet quality standards, such as falling below 80% Apex unit test coverage, violating security rules, or introducing un-bulkified patterns. By establishing these automated quality gates, you embed the learnings from your independent review directly into the developer workflow, securing the long-term health, stability, and scalability of your Salesforce enterprise platform.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>Remediation Priority</th>
                <th>Typical Technical Findings</th>
                <th>Operational &amp; Business Impact</th>
                <th>Responsibility</th>
                <th>Remediation Timeline Gate</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Critical</strong></td>
                <td>Unsecured Apex sharing, plaintext API credentials, trigger recursion loops</td>
                <td>Data breach risk, complete transaction failure, platform lockout</td>
                <td>Implementation Partner (At Vendor Cost)</td>
                <td>Immediate; must resolve before next sandbox environment refresh</td>
              </tr>
              <tr>
                <td><strong>High</strong></td>
                <td>Un-bulkified Flow loops, parent-child data skew, missing integration retry logic</td>
                <td>Breaching governor limits under high UAT volumes, row lock errors</td>
                <td>Implementation Partner (At Vendor Cost)</td>
                <td>Must-win gate; must resolve and pass regression tests before Go-Live</td>
              </tr>
              <tr>
                <td><strong>Medium</strong></td>
                <td>Obsolete custom fields, duplicate Validation rules, missing error logging framework</td>
                <td>Degraded admin efficiency, delayed bug diagnostics, customisation bloat</td>
                <td>Joint Delivery Team (Shared Backlog)</td>
                <td> hypercare phase or first 3 post-launch operational sprints</td>
              </tr>
              <tr>
                <td><strong>Low</strong></td>
                <td>Inconsistent naming conventions, lack of description fields on metadata</td>
                <td>Slight increase in maintenance overhead, minor technical documentation drift</td>
                <td>Internal Salesforce Centre of Excellence</td>
                <td>Continuous optimisation backlog; prioritised when capacity allows</td>
              </tr>
            </tbody>
          </table>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Independent technical reviews provide an unbiased, data-backed assessment of your Salesforce org's long-term health and stability.</li>
            <li>Structure audits across declarative, custom code, data, security, and deployment release pillars over a 2-to-4-week timeline.</li>
            <li>Enforce trigger handler frameworks and strict Flow bulkification to prevent governor limit breaches and CPU timeouts.</li>
            <li>Identify and remediate parent-child data skew and ownership skew to eliminate Row Lock errors in high-volume environments.</li>
            <li>Enforce security by utilising Named Credentials for integrations, Public Private sharing models, and USER_MODE custom queries.</li>
            <li>Triage review findings into a prioritised backlog, holding the implementation partner contractually accountable for quality deviations.</li>
            <li>Establish automated static code analysis gates in your CI/CD pipeline to continuously prevent new technical debt.</li>
"""

QUIZ_QUESTIONS = """
            <div class="quiz-question" id="q1">
              <p>1. Why is an independent, external technical review preferred over an internal review by the active delivery team?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Internal reviews are technically superior as the team already understands the business processes.</div>
                <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. External reviews are faster and can be completed in a few hours without sandbox access.</div>
                <div class="quiz-option" onclick="answer(this, 'q1', 'right')">C. External reviews provide unbiased objectivity, free from delivery timeline pressures and vendor self-reporting bias.</div>
                <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Internal teams are not permitted by Salesforce licensing agreements to perform code reviews.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. What database-level design flaw is a major source of row-locking errors (UNABLE_TO_LOCK_ROW) in high-volume Salesforce orgs?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. Setting custom field indexes on text fields.</div>
                <div class="quiz-option" onclick="answer(this, 'q2', 'right')">B. Parent-Child data skew, where a single parent record is associated with more than 10,000 child records.</div>
                <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. Storing external integration endpoints inside standard Named Credentials.</div>
                <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. Utilising version-controlled DevOps release pipelines for deployment package merges.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. How should delivery leaders handle structural coding defects identified during an independent technical review that violate agreed-upon standards?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. Accept them as inevitable technical debt and let internal administrators fix them post-go-live.</div>
                <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. Immediately pause the entire Salesforce programme and redesign the data schema from scratch.</div>
                <div class="quiz-option" onclick="answer(this, 'q3', 'right')">C. Triage them into the backlog and hold the implementation partner contractually and financially accountable for remediation.</div>
                <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Deactivate all Apex triggers and validation rules in the production environment to bypass performance issues.</div>
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

    print("Successfully drafted DEL-027 content!")

if __name__ == '__main__':
    main()
