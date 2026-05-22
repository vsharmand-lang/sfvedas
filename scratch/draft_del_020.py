import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-020', 'index.html')

SUMMARY_BULLETS = """
            <li>The fundamental structural reasons why generic classroom training fails to drive user adoption in complex Salesforce orgs.</li>
            <li>How to design role-based training labs in sandboxes to simulate real-world day-in-the-life operational scenarios.</li>
            <li>Strategies for establishing on-demand video channels and micro-learning content to support continuous learning.</li>
            <li>Best practices for constructing context-sensitive, interactive in-app guidance paths using standard Salesforce capabilities.</li>
            <li>A comprehensive checklist for identifying and training platform champions within business units before go-live.</li>
            <li>Tactical methods for measuring training effectiveness and platform adoption using objective system log data.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">The Failure of Generic Classroom Instruction</a></li>
            <li><a href="#s2">Designing Role-Based Sandbox Training Labs</a></li>
            <li><a href="#s3">Operationalising On-Demand Micro-Learning</a></li>
            <li><a href="#s4">Constructing Contextual In-App Guidance Paths</a></li>
            <li><a href="#s5">Measuring Training Effectiveness Post-Go-Live</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">The Failure of Generic Classroom Instruction</h2>
        <p>For decades, the standard playbook for enterprise software rollouts has relied heavily on generic classroom instruction. Under this traditional model, hundreds of business users are gathered in physical or virtual training rooms, where an external trainer clicks through a pre-configured slide deck and walks through a vanilla, non-customised Salesforce environment. Stakeholders and delivery managers check the "training complete" box, assuming that because users sat through a two-hour session, they have acquired the necessary proficiency to execute their daily tasks. In reality, this model is a fundamental failure of design that actively sabotages user adoption from day one.</p>

        <p>The primary reason generic classroom instruction fails is the <strong>contextual disconnect</strong>. Salesforce is highly customisable, and in any mature enterprise implementation, the platform is heavily tailored to reflect the organisation's specific business processes, validation rules, automated flows, and page layouts. When users are trained on a generic Sales or Service Cloud interface, they are forced to translate vanilla terminology and simplified workflows into their highly specific, complex daily routines. When they log in to the production org on go-live day, they find a completely different environment filled with custom objects, complex fields, and rigid validation rules that they have never seen before, triggering immediate frustration and operational paralysis.</p>

        <p>Furthermore, human cognitive processing is highly susceptible to <strong>information overload</strong>. Presenting dozens of complex fields, stage transitions, and data entry guidelines in a single, continuous lecture exceeds the brain's working memory capacity. Users retain only a fraction of the information presented, typically remembering only the initial and final steps of a workflow. Without hands-on reinforcement and immediate application of the learned material within their specific context, the knowledge decays rapidly. By the time go-live arrives several weeks later, the retention curve has bottomed out, leaving the support team overwhelmed with basic usability questions that training was supposed to eliminate.</p>

        <p>Additionally, classroom training treats all users as a single homogeneous group, ignoring the diverse roles, experience levels, and operational responsibilities across the organisation. A high-performing field sales representative, a high-volume call centre agent, and a senior operations executive require entirely different interfaces and data entry habits. Forcing them into the same standard curriculum is an inefficient use of business capacity. The sales representative becomes bored by call routing configuration details, while the support agent is overwhelmed by complex pipeline forecasting methodologies. To secure true platform adoption, we must abandon generic instruction and transition to role-based, active learning models.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Presentation Trap</strong>
            <p>Demonstrating active Salesforce features on a screen is not training; it is a product demo. True user enablement requires active cognitive engagement, hands-on error resolution, and role-specific workflows. If your training strategy relies on users silently watching a trainer click through screens, your adoption rates will suffer on go-live day.</p>
          </div>
        </div>

        <h2 id="s2">Designing Role-Based Sandbox Training Labs</h2>
        <p>To replace passive listening with active learning, delivery leaders must construct role-based training labs housed within dedicated, high-fidelity sandbox environments. Rather than presenting abstract platform capabilities, these labs are structured around comprehensive "day-in-the-life" operational scenarios. Users log in to a training sandbox that mirrors the exact production metadata and security structure, where they are tasked with executing a complete end-to-end business transaction from start to finish under the guidance of a training facilitator.</p>

        <p>Creating these high-fidelity environments requires a structured <strong>data seeding strategy</strong>. A training sandbox cannot be empty; it must contain realistic, pre-populated mock data that matches the operational context of the users. For instance, a sales representative lab should open with a set of pre-assigned Leads and Opportunities that reflect realistic customer segments, product lines, and value ranges. This data should be seeded using automated scripting tools or sandbox templates to ensure that the environment can be rapidly refreshed and reset between training cohorts, preventing data pollution and maintaining laboratory consistency.</p>

        <p>Each training lab is structured around a sequence of practical <strong>scenario checklists</strong>. For example, instead of instructing a user to "create a contact," the scenario guide instructs them: "Receive a phone call from an existing client requesting an urgent billing address change, locate their Account record, update the primary Contact, initiate the address validation process, and verify that the automated confirmation email was sent." This approach forces the user to navigate the interface, interact with validation rules, resolve common data quality warnings, and experience the actual downstream automations that occur in the production system.</p>

        <p>By forcing users to complete these actions hands-on, the training labs intentionally expose them to the platform's guardrails, including validation errors, required lookup fields, and duplicate alert rules. Experiencing these system behaviours in a safe sandbox environment is a critical part of the learning process. It allows users to make mistakes, understand why the system blocked an action, and learn how to correct the issue without risking production data integrity or disrupting real-world customer relationships. This builds operational confidence and reduces go-live anxiety.</p>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The Sandbox Refresh Cycle</strong>
            <p>Establish a regular, automated sandbox refresh cycle for your training environments. Ensure that the training database is completely reset and re-seeded every weekend. This guarantees that each new training cohort begins their labs with a clean, predictable dataset, free from the data anomalies introduced by previous participants.</p>
          </div>
        </div>

        <h2 id="s3">Operationalising On-Demand Micro-Learning</h2>
        <p>While structured training labs are highly effective for establishing initial competency, they do not address the long-term challenge of continuous learning and user reinforcement. In any dynamic enterprise, business processes evolve, new platform features are deployed, and new employees join the organisation. To support this continuous learning curve, delivery managers must operationalise an on-demand micro-learning strategy, converting dense reference manuals into short, highly targeted digital content blocks.</p>

        <p>The foundation of micro-learning is the <strong>two-minute video capsule</strong>. Traditional one-hour recorded webinars are rarely watched because users do not have the time to scrub through sixty minutes of footage to locate a specific three-step procedure. Instead, construct a centralised library of short, single-topic screen recordings. Each video capsule must address exactly one tactical question, such as "How to log a phone call on a mobile device" or "How to request a discount approval." By keeping these videos under two minutes, you provide immediate, frictionless answers at the point of need.</p>

        <p>To support these video capsules, implement a search-optimised <strong>interactive knowledge base</strong> within the organisation's intranet or Salesforce Community. Every article must follow a standardised structure: a clear problem statement, a three-step action checklist, a visual GIF demonstrating the user interface action, and a link to the corresponding video capsule. Avoid writing long, text-heavy paragraphs; instead, use bold, numbered steps and highlighted UI annotations (such as red boxes highlighting the specific buttons to click) to ensure maximum scannability.</p>

        <p>Furthermore, integrate this micro-learning content directly with the organisation's onboarding and performance management systems. When a new user is provisioned, their initial Salesforce training is not a massive one-off event; instead, it is structured as a series of bite-sized, gamified learning paths (utilising custom Trailhead modules or Enablement Sites). By tracking completion rates and quiz scores, the delivery team and department managers can objectively monitor the onboarding velocity and verify that new hires have achieved the baseline technical proficiency required for their roles.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>Do not waste budget on creating expensive, professionally produced training videos. High-fidelity, informal screen recordings created by your internal business analysts or platform champions are far more effective. They feel authentic, can be updated in minutes when the UI changes, and cost almost nothing to produce.</p>
          </div>
        </div>

        <h2 id="s4">Constructing Contextual In-App Guidance Paths</h2>
        <p>The absolute gold standard of user training is the complete elimination of the need for external learning materials. The system itself should guide the user through complex workflows in real-time. Modern Salesforce capabilities allow delivery teams to build contextual, interactive in-app guidance paths that overlay the standard user interface, providing tactical support exactly when and where the user is executing a business process.</p>

        <p>The first tier of in-app enablement is the **Single-Prompt Target**. These are small, non-intrusive pop-up cards anchored to specific fields or buttons on a Lightning page layout. Use them to highlight critical process changes or platform optimisations. For example, if a new fields layout is deployed to track customer sentiment on an Opportunity, place a targeted prompt next to the field explaining its purpose and data entry criteria. This eliminates the need to send mass emails or host update meetings, as the system communicates the change directly to the user during their natural workflow.</p>

        <p>The second tier is the **Multi-Step Walkthrough**. This is an interactive guided path that leads a user through a sequence of steps across multiple records and pages. Walkthroughs are exceptionally valuable for onboarding new users or steering existing users through high-risk, low-frequency processes, such as completing a complex customer onboarding checklist or closing out a fiscal year pipeline. The walkthrough dynamically prompts the user to enter data in step one, guides them to click the next button in step two, and directs them to verify the approval status in step three, ensuring compliance without prior memorisation.</p>

        <p>To ensure in-app guidance does not become a source of user frustration, enforce strict **frequency capping and targeting rules**. Showing too many prompts will lead to user fatigue, causing them to dismiss alerts without reading the content. Target prompts to specific profiles or permission sets, ensuring that users see only the guidance relevant to their responsibilities. Additionally, configure the system to display walkthroughs only when a user accesses a feature for the first time, or after a major platform release, allowing experienced users to operate without unnecessary distractions.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>Contextual Enablement</strong>
            <p>In-app guidance represents a fundamental shift in user enablement: moving from "know-it-all" training (where users must memorise processes weeks in advance) to "just-in-time" support (where the system guides them through the work in real-time). This significantly reduces training costs and virtually eliminates data entry errors.</p>
          </div>
        </div>

        <h2 id="s5">Measuring Training Effectiveness Post-Go-Live</h2>
        <p>A delivery leader's job is not complete when the training sessions conclude; the ultimate measure of success is the objective adoption and competency of the users post-go-live. Relying on subjective feedback surveys or attendance rosters is insufficient. We must establish quantitative, data-driven metrics to track how users are actually interacting with Salesforce, identifying training gaps and platform friction points in real-time.</p>

        <p>The first critical metric category is **Operational Data Completeness**. Run regular quality audits to check the completeness and accuracy of key fields across high-priority records. For instance, if a training goal was to ensure all sales representatives accurately categorised their pipeline using the "Loss Reason" picklist, track the percentage of closed-lost Opportunities where this field is left blank or set to "Other." High rates of incomplete data represent a clear training failure, highlighting specific business units or user cohorts that require targeted coaching.</p>

        <p>The second category is **Workflow Velocity and Friction**. Utilise Salesforce event monitoring logs to track the time users spend navigating through specific screen flows, page transitions, and approval processes. If a user spends ten minutes completing an automated case closure flow that should take two minutes, they are experiencing significant cognitive friction. This metric allows the delivery team to identify whether the issue is a training gap (the user does not understand the workflow) or an architectural defect (the page layout is too complex or slow), allowing for targeted system optimisation.</p>

        <p>Finally, track **Support Ticket Volume and Categorisation**. Monitor the volume, severity, and root cause of incoming help desk requests during the immediate weeks following go-live. Categorise tickets into "How-To" queries (usability questions that training should have covered) and "System Bugs" (actual platform defects). A high volume of how-to tickets indicates that the training labs or in-app guidance failed to prepare users for operational realities. By analyzing these tickets, the support and training teams can immediately adjust the micro-learning library and deploy new contextual walkthroughs to address the most common user struggles.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>Adoption Metric</th>
                <th>Measurement Method</th>
                <th>Target Threshold</th>
                <th>Remediation Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Login Frequency</strong></td>
                <td>Active users logging in daily / weekly via System logs</td>
                <td>&gt; 95% of provisioned users</td>
                <td>Manager escalation; profile audit; direct coaching</td>
              </tr>
              <tr>
                <td><strong>Data Quality Index</strong></td>
                <td>Completeness of mandatory and key business fields</td>
                <td>&gt; 98% record completeness</td>
                <td>Deploy validation rules; update targeted guidance prompts</td>
              </tr>
              <tr>
                <td><strong>Support Ticket Volume</strong></td>
                <td>Ratio of "How-To" tickets to overall platform users</td>
                <td>&lt; 5% in first fortnight</td>
                <td>Record new micro-learning videos; deploy walkthroughs</td>
              </tr>
              <tr>
                <td><strong>Feature Utilization</strong></td>
                <td>Event monitoring data for specific custom buttons/tabs</td>
                <td>&gt; 80% target cohort usage</td>
                <td>Run targeted feedback focus groups; simplify UI layouts</td>
              </tr>
            </tbody>
          </table>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Generic classroom training is fundamentally flawed because it lacks operational context, causes cognitive overload, and fails to account for role-based responsibilities.</li>
            <li>Role-based sandbox labs built around realistic 'day-in-the-life' scenarios allow users to practice processes hands-on, resolving errors in a safe environment.</li>
            <li>High-fidelity training sandboxes require a structured, automated data seeding strategy to ensure realistic datasets and rapid refresh cycles.</li>
            <li>On-demand micro-learning replaces dense reference manuals with search-optimised knowledge articles and targeted two-minute video capsules.</li>
            <li>Contextual in-app guidance using targeted prompts and multi-step walkthroughs guides users through complex flows in real-time, eliminating memorisation requirements.</li>
            <li>Post-go-live training effectiveness must be quantitatively measured using data completeness audits, support ticket analysis, and workflow event logs.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-question" id="q1">
            <p>1. Why is generic classroom instruction highly ineffective for driving user adoption in enterprise Salesforce rollouts?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. It takes too long to schedule across global business units.</div>
              <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. It does not provide users with printed reference manuals that they can study after hours.</div>
              <div class="quiz-option" onclick="answer(this,'q1','right')">C. It creates a contextual disconnect by presenting vanilla features rather than the custom fields, rules, and layouts specific to the user's daily operations.</div>
              <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. Most trainers are unfamiliar with the standard Salesforce platform features.</div>
            </div>
          </div>

          <div class="quiz-question" id="q2">
            <p>2. What is a critical operational requirement when constructing role-based sandbox training laboratories?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. Standardising page layouts across all business profiles.</div>
              <div class="quiz-option" onclick="answer(this,'q2','right')">B. Implementing a structured data seeding strategy to populate sandboxes with realistic, mock customer data that is regularly refreshed.</div>
              <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. Disabling all validation rules to prevent users from encountering errors during training.</div>
              <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. Limiting training sandbox access to only the IT and support departments.</div>
            </div>
          </div>

          <div class="quiz-question" id="q3">
            <p>3. How should a delivery leader quantitatively measure training effectiveness and platform adoption after a Salesforce go-live?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. Reviewing the overall project budget and actual development velocity.</div>
              <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. Conducting subjective satisfaction surveys during the post-project retrospective meeting.</div>
              <div class="quiz-option" onclick="answer(this,'q3','wrong')">C. Counting the total number of user seats provisioned in the production environment.</div>
              <div class="quiz-option" onclick="answer(this,'q3','right')">D. Analysing quantitative metrics such as data completeness audits, support ticket categorisation, and system logs tracking navigation velocity.</div>
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

    print("Successfully drafted DEL-020 content!")

if __name__ == '__main__':
    main()
