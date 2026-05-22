import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-026', 'index.html')

SUMMARY_BULLETS = """
            <li>How to establish the Tri-Arch Framework of Salesforce Programme Governance.</li>
            <li>The critical operational role of a Solution Design Authority (SDA) in large projects.</li>
            <li>Best practices for structuring a multi-workstream Business Design Authority (BDA).</li>
            <li>Strategies for managing cross-workstream technical dependencies and DevOps environment branches.</li>
            <li>How to enforce auditability, compliance standards, and risk reporting at the programme level.</li>
            <li>Practical frameworks for resolving solution conflicts between business departments.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">The Tri-Arch Framework of Salesforce Programme Governance</a></li>
            <li><a href="#s2">Establishing a Solution Design Authority (SDA)</a></li>
            <li><a href="#s3">Structuring the Multi-Workstream Business Design Authority</a></li>
            <li><a href="#s4">Managing Cross-Workstream Technical Dependencies and DevOps</a></li>
            <li><a href="#s5">Auditability, Risk Reporting, and Compliance Governance</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">The Tri-Arch Framework of Salesforce Programme Governance</h2>
        <p>Large-scale enterprise Salesforce implementations are exceptionally complex business transformation initiatives. They rarely involve a single, isolated CRM department; instead, they encompass multiple concurrent workstreams, dozens of systems integrations, massive legacy data migrations, and thousands of end-users across diverse geographic business units. Managing this level of complexity requires a robust, structured operational framework. Traditional IT project management methodologies fail because they do not account for the unique, metadata-driven architecture of the Salesforce platform. To secure delivery success, organisations must establish the **Tri-Arch Framework of Salesforce Programme Governance**.</p>

        <p>The Tri-Arch Framework partitions governance into three highly distinct, independent governing bodies that operate in parallel. The first pillar is the **Solution Design Authority (SDA)**. The SDA is a technical governance body that owns the platform's architectural integrity. Led by the Program Lead Architect, it audits all customisations, enforces metadata standards, manages governor limits, and defines the environment strategy. The SDA ensures that Salesforce is built using standard-first, sustainable patterns, protecting the platform's long-term health and upgradeability from ad-hoc customisation requests.</p>

        <p>The second pillar is the **Business Design Authority (BDA)**. While the SDA governs technical design, the BDA governs business processes and functional requirements. Led by the lead business analyst and business owners, the BDA manages the program backlog, resolves process conflicts between business units, and defines operational workflows. The BDA ensures that Salesforce customisations directly support real-world business outcomes, preventing departments from configuring silod, conflicting processes within the same shared org.</p>

        <p>The third pillar is the **PMO &amp; Release Governance Board**. The PMO (Project Management Office) manages the commercial, financial, and timeline guardrails of the programme. It monitors budget burn rates, tracks milestones, manages risk registers, and coordinates the downstream release cycles. By separating PMO governance from technical design, the framework prevents delivery timelines from compromising architectural quality. If a project milestone is at risk, the PMO cannot pressure the technical team to bypass SDA code reviews or skip automated testing pipelines; the architectural gates remain absolute, guaranteeing a stable launch.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Silo Threat</strong>
            <p>If your multi-workstream Salesforce programme operates without a centralized Tri-Arch governance framework, your departments will inevitably configure conflicting solutions in the shared org. One team's picklist change or validation rule will silently break another team's automated flow. Centralize your governance to protect your platform.</p>
          </div>
        </div>

        <h2 id="s2">Establishing a Solution Design Authority (SDA)</h2>
        <p>The Solution Design Authority (SDA) is the ultimate technical gatekeeper of the Salesforce programme. Led by the Program Lead Architect, the SDA is comprised of the technical leads from the implementation partner, the lead Salesforce developers, and the client's internal Enterprise Architect. Its primary mandate is to protect the platform's core architecture and enforce a standard-first design philosophy across all workstreams.</p>

        <p>The SDA enforces governance through a strict **Technical Review Cycle**. Every developer story, epic, and design document must undergo a formal architectural audit before configuration begins. The SDA evaluates designs against standard Salesforce capabilities. If a business unit requests a complex custom programmatic solution (such as building a custom search interface using LWC and custom Apex), the SDA will audit the design. If standard global search or standard list views can achieve 80% of the operational goal, the SDA will block the custom request, forcing the business to adopt standard platform capabilities. This standard-first mandate drastically reduces customisation bloat.</p>

        <p>For custom programmatic development that is approved, the SDA mandates the use of **formal design patterns and frameworks**. This includes enforcing a single trigger framework per object (such as the SObject Trigger Handler pattern) to prevent order-of-execution conflicts, standardizing error handling and exception logging (utilising centralized frameworks like Nebula Logger), and establishing strict code review checklists. By enforcing coding standards, the SDA ensures that all developers write clean, maintainable, and secure code, preventing the accumulation of technical debt.</p>

        <p>The SDA also owns the **Architectural Decision Record (ADR) registry**. Any major technical deviation or design choice must be documented in a structured ADR, capturing the context, options considered, financial implications, and the lead architect's rationale. Once signed by the SDA board, the ADR becomes a binding strategic document. This prevents stakeholders from reopening closed technical debates during later sprints, securing delivery momentum and establishing a clear, auditable technical lineage for the platform.</p>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The SDA Mandate</strong>
            <p>The Solution Design Authority must be empowered by the executive steering committee with absolute veto power over technical designs. If the lead architect identifies an integration or customisation design as high-risk, the BDA and PMO cannot overwrite their veto to meet a timeline. Architectural quality is non-negotiable.</p>
          </div>
        </div>

        <h2 id="s3">Structuring the Multi-Workstream Business Design Authority</h2>
        <p>While the SDA manages technical design, large Salesforce programmes frequently clash on business processes. When deploying a shared Salesforce org to multiple business units (such as regional sales teams or diverse product lines), departments will demand highly customized workflows, page layouts, and validation rules that reflect their legacy operations. To prevent this process fragmentation, organisations must establish the **Business Design Authority (BDA)**.</p>

        <p>The BDA is structured around **Cross-Functional Process Owners**. Instead of having departmental silos, the BDA appoints single process owners for core Salesforce capabilities (e.g. one owner for Lead Management, one for Case Resolution, and one for Billing Integration). These process owners collaborate to define a single, global standard process layout. If a specific business unit requires a deviation (such as a unique sales stage or custom opportunity validation), they must present their business case to the BDA. The BDA evaluates the request, prioritizing global standardization over local customisation.</p>

        <p>To manage backlog prioritisation under pressure, the BDA implements the **MoSCoW prioritisation methodology**. The BDA triages the master programme backlog weekly, ensuring that the volume of Must-Have stories never exceeds 60% of the team's total sprint capacity. Business owners must defend their Must-Have classifications against strict operational definitions: if a process can be executed using a temporary manual workaround, it is immediately downgraded. This rigorous filtering prevents backlog inflation, ensuring that the delivery team focuses exclusively on the core business capabilities required for a successful launch.</p>

        <p>The BDA also plays a critical role in **Change Management and Training**. As business processes are standardized and simplified, users will experience operational change fatigue. The BDA collaborates closely with the change management workstream to design role-based training sandboxes, draft contextual in-app guidance prompts, and record micro-learning videos. By actively steering user enablement, the BDA ensures that business units are fully prepared for the operational realities of the new system, driving rapid user adoption on go-live day.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>The Global Template</strong>
            <p>Enforce a strict Global Template strategy for multi-region Salesforce rollouts. Build a single standard process and layout that satisfies 80% of all user requirements. Only approve regional customisations when they are driven by legal, regulatory, or compliance mandates, keeping your core schema clean and upgradable.</p>
          </div>
        </div>

        <h2 id="s4">Managing Cross-Workstream Technical Dependencies and DevOps</h2>
        <p>In large Salesforce programmes with multiple concurrent workstreams, technical dependency management is a critical delivery bottleneck. If Workstream A is configuring a new billing flow on the Account object while Workstream B is modifying sharing rules and Workstream C is integrating a middleware API on the same Account trigger, their changes will conflict, leading to metadata overwrites and deployment failures. To prevent this, the program must implement a **strict DevOps environment strategy**.</p>

        <p>The DevOps strategy is built around a **Version-Controlled Git Branching model** (utilising tools like GitHub or GitLab). Developers do not configure in a shared sandbox; instead, every developer operates in an isolated Developer Sandbox or Scratch Org. When a developer begins a user story, they create a feature branch off the main repository branch. When development is complete, they push their changes to the repository, initiating an automated pull request. This version-controlled pipeline tracks every single metadata modification, ensuring absolute change auditability and preventing developer overwrites.</p>

        <p>Furthermore, enforce **automated regression testing gates** within the deployment pipeline. When a pull request is merged into the shared Integration or UAT sandboxes, the CI/CD orchestration tool (such as Copado or Gearset) dynamically executes all local Apex unit tests, runs static code analysis (PMD), and triggers automated UI regression test scripts. If a conflict occurs, or if cumulative Apex test coverage falls below the 85% gate, the pipeline blocks the merge, keeping the target environment stable and ensuring that cross-workstream bugs are caught immediately.</p>

        <p>To manage technical dependencies, the SDA hosts a **weekly cross-workstream design review**. The technical leads map out metadata touchpoints, coordinate release cycles, and plan database modifications. By proactively mapping dependencies, the team schedules releases to avoid overlapping changes on core objects, reducing merge conflicts and ensuring a clean, predictable path to go-live.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>DevOps is not an option for large Salesforce programs; it is a critical operational guardrail. By investing in automated branching, version control, and pipeline testing gates early, you remove human subjectivity and merge friction from your release lifecycle. This guarantees stability and accelerates development speed.</p>
          </div>
        </div>

        <h2 id="s5">Auditability, Risk Reporting, and Compliance Governance</h2>
        <p>The final pillar of large-scale Salesforce programme governance is the enforcement of strict **auditability, compliance standards, and risk reporting**. Because Salesforce houses highly sensitive customer, financial, and operational data, the platform is subject to intense regulatory scrutiny. Delivery leaders must establish a governance framework that satisfies corporate compliance requirements and provides absolute transparency to the executive steering committee.</p>

        <p>First, implement **detailed configuration audit trails**. Every metadata change—whether declarative configuration or custom Apex code—must be mapped directly to a signed user story in your tracking tool (e.g. Jira or Azure DevOps). Utilize version control commit messages to link physical code changes to Jira ticket IDs (e.g., `feat(opp-billing): DEL-123 pricing engine configuration`). This creates an unbroken, auditable link from the initial business requirement to the physical production deployment, satisfying internal compliance audits and facilitating rapid troubleshooting.</p>

        <p>Second, establish a **Quantitative Risk Reporting framework** for the executive steering committee. Risks must be quantified by probability, operational impact, and cost. Instead of reporting: "The Salesforce data load is delayed," report: "Delay in source database extraction by client IT team. Probability: High. Impact: Postpones Mock 3 load by 2 weeks, delaying go-live and costing £30,000 in burn rate." This quantitative formatting immediately frames the risk in executive language, enabling rapid decision-making and resource allocation.</p>

        <p>Finally, enforce **regulatory compliance audits** (such as GDPR, HIPAA, or SOC2) directly within your solution design authority gates. The SDA audits sharing models, field-level security access, data encryption standards, and user profile permissions. Ensure that highly sensitive fields (such as credit card numbers or government IDs) are encrypted at rest using Salesforce Shield Platform Encryption, and that data retention policies are enforced via automated archiving. By prioritizing compliance in your design gates, you protect your organisation from severe security breaches, financial penalties, and reputational damage, ensuring a highly secure and stable platform.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>Governance Dimension</th>
                <th>Traditional Project Management (Failed)</th>
                <th>Tri-Arch Enterprise Governance (Success)</th>
                <th>Strategic Business Outcome</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Technical Authority</strong></td>
                <td>Rushed review; timeline pressure overwrites design quality</td>
                <td>Independent Solution Design Authority with absolute veto power</td>
                <td>Zero customization bloat; high platform upgradability</td>
              </tr>
              <tr>
                <td><strong>Process Alignment</strong></td>
                <td>Siloed business units configure conflicting features</td>
                <td>Business Design Authority enforces a standard Global Template</td>
                <td>Unified corporate processes; clean shared database</td>
              </tr>
              <tr>
                <td><strong>DevOps Strategy</strong></td>
                <td>Developers overwrite changes in shared sandbox sandboxes</td>
                <td>Version-controlled branching with automated pipeline gates</td>
                <td>No merge conflicts; 100% automated regression gates</td>
              </tr>
              <tr>
                <td><strong>Audit &amp; Compliance</strong></td>
                <td>Vague change history; no links to business requirements</td>
                <td>Every metadata change linked to Jira stories via Git commits</td>
                <td>Absolute regulatory compliance; clean internal audit trails</td>
              </tr>
            </tbody>
          </table>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Implement the Tri-Arch Framework of Salesforce Programme Governance, separating technical, business, and PMO authorities.</li>
            <li>Establish an independent Solution Design Authority (SDA) with absolute veto power to enforce a standard-first design philosophy.</li>
            <li>Enforce the Global Template strategy: build a single standard process, restricting local customisations to compliance requirements.</li>
            <li>Deploy a version-controlled DevOps environment strategy to prevent cross-workstream metadata overwriting.</li>
            <li>Link every metadata change to a signed Jira user story via Git commit messages to ensure absolute auditability.</li>
            <li>Quantify programme risks by probability, impact, and cost to enable rapid executive decision-making.</li>
            <li>Incorporate regulatory compliance audits directly into your SDA design gates to protect sensitive enterprise data.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-section" id="quiz">
            <h2>Checkpoint: Test Your Understanding</h2>

            <div class="quiz-question" id="q1">
              <p>1. Under the Tri-Arch Framework of Salesforce Programme Governance, what is the primary operational mandate of the Solution Design Authority (SDA)?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. Managing the financial budget and coordinate sprint timelines.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. Triaging the daily help desk support tickets post-go-live.</div>
                <div class="quiz-option" onclick="answer(this,'q1','right')">C. Protecting the platform's architectural integrity by auditing designs, enforcing standard patterns, and managing limits.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. Drafting the business requirements specifications and global training materials.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. What is the correct DevOps environment strategy to prevent developers from overwriting each other's changes in a multi-workstream Salesforce programme?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. Requiring all developers to configure directly in a single, shared production sandbox.</div>
                <div class="quiz-option" onclick="answer(this,'q2','right')">B. Enforcing an isolated sandbox or scratch org per developer, with all changes merged via a version-controlled Git repository.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. Deactivating all validation rules and automated trigger handlers in the Integration sandbox.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. Restricting metadata deployment access exclusively to the business analysis team.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. Why is a 'Global Template' strategy critical for large-scale Salesforce programmes across multi-region organisations?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. It guarantees that the overall programme budget will remain fixed.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. It allows regional departments to choose their own licensing models.</div>
                <div class="quiz-option" onclick="answer(this,'q3','right')">C. It standardises 80% of all user processes and layouts, keeping the database schema clean and allowing for seamless future upgrades.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. It completely eliminates the need for user acceptance testing or training sandbox mock loads.</div>
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

    print("Successfully drafted DEL-026 content!")

if __name__ == '__main__':
    main()
