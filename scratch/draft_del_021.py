import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-021', 'index.html')

SUMMARY_BULLETS = """
            <li>The unique psychological and technical drivers that make Salesforce projects highly susceptible to scope creep.</li>
            <li>How to establish an independent, authoritative Solution Design Authority to audit and filter incoming scope requests.</li>
            <li>Best practices for implementing a rigid, fixed-capacity, managed-scope agile delivery framework.</li>
            <li>The tactical mechanics of applying the MoSCoW prioritisation methodology under severe steering committee pressure.</li>
            <li>Practical frameworks for saying 'no' to low-value customisation requests while protecting stakeholder relationships.</li>
            <li>A comprehensive set of metrics to track and quantify the technical and financial impact of customisations.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">The Psychology and Mechanics of Salesforce Scope Creep</a></li>
            <li><a href="#s2">Establishing a Solution Design Authority Gate</a></li>
            <li><a href="#s3">Implementing Fixed-Capacity Agile Frameworks</a></li>
            <li><a href="#s4">The MoSCoW Prioritisation Process Under Pressure</a></li>
            <li><a href="#s5">Tactical Refusal and Relationship Protection</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">The Psychology and Mechanics of Salesforce Scope Creep</h2>
        <p>Scope creep is the slow, continuous expansion of a project's boundaries beyond the originally agreed-upon commercial and technical limits. While it affects all custom software engineering projects, Salesforce implementations are uniquely vulnerable to this phenomenon. The primary driver of this susceptibility is the **declarative paradox**. Because Salesforce is a low-code/no-code platform, business stakeholders and delivery managers operate under the illusion that configuration is instantaneous and free. When they request a new custom field, a modified page layout, or an automated screen flow, they assume it can be completed in minutes, ignoring the complex metadata dependencies, regression testing requirements, and governance limits that underpin the change.</p>

        <p>The second major driver of scope creep is **requirement abstraction**. During the initial discovery workshops, requirements are often captured at a high level of abstraction (e.g. "We need to manage customer onboarding"). Stakeholders sign off on these broad concepts, but as the project progresses and they see live functional prototypes during sprint demonstrations, they begin to conceptualise the precise operational workflows they actually desire. Each " Show and Tell" session triggers a cascade of reactive requests, such as "Can we automate this email?", "Can we integrate this third-party service?", or "Can we add another approval step?" These requests are rarely framed as scope extensions; instead, stakeholders argue they are merely "clarifying" the original abstract requirement, making it exceptionally difficult for delivery leaders to hold the line.</p>

        <p>Furthermore, Salesforce's extensive **AppExchange ecosystem** and built-in features create a state of constant temptation. Business leaders attend Salesforce marketing events or read product documentation and immediately want to adopt the latest AI, analytics, or collaborative tools. They push the delivery team to incorporate these complex platform capabilities mid-stream, without understanding that a secure enterprise rollout requires detailed security reviews, data architecture planning, and licensing compliance checks. This "shiny object syndrome" distracts the delivery team from core objectives, introducing massive integration risk and destabilising the core release branch.</p>

        <p>Finally, a primary driver of scope creep is the **lack of architectural ownership** within the business. Business sponsors often fail to appoint a strong internal product owner who can act as a single point of contact and filter stakeholder demands. Instead, a multi-headed stakeholder committee bombards the delivery team with conflicting, unprioritised requirements. The delivery team, eager to satisfy their clients or business sponsors, attempts to accommodate every request, leading to customisation bloat and architectural compromise. To protect platform health and maintain delivery momentum, we must implement a structured, authoritative governance gate to evaluate every single incoming change.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Declarative Trap</strong>
            <p>Just because you can create a custom field or automate a process in five clicks using Flow Builder does not mean you should. Every piece of declarative configuration introduces long-term maintenance overhead, validation complexity, and regression risk. Treat declarative additions with the same technical rigour as custom Apex code.</p>
          </div>
        </div>

        <h2 id="s2">Establishing a Solution Design Authority Gate</h2>
        <p>The most effective defence against scope creep is the establishment of an independent, authoritative governance body: the **Solution Design Authority (SDA)**. The SDA is comprised of the lead program architect, lead business analyst, and the client's internal platform owner. This body acts as the ultimate gatekeeper for all functional and technical customisations, ensuring that no change is introduced into the backlog without a formal review of its business value, technical complexity, and alignment with Salesforce best practices.</p>

        <p>The SDA evaluates every proposed change against a rigid **technical evaluation matrix**. The first filter is the **Declarative vs Custom Code test**. If a business requirement can be met using standard, out-of-the-box Salesforce capabilities or standard declarative configuration, the SDA will approve the approach. If the request requires custom programmatic development (such as custom Apex triggers or Lightning Web Components), the requester must present a comprehensive business case justifying why standard capabilities are insufficient. This immediate friction discourages low-value customisation requests, forcing business units to adapt their processes to the platform's standard design rather than bending the platform to match legacy habits.</p>

        <p>The second filter is the **Platform Governance and Limits audit**. The SDA reviews the proposed change's impact on platform governor limits, sharing architectures, integration middleware, and release environments. For instance, if a team proposes adding a complex real-time integration to an Opportunity edit trigger, the SDA will audit the impact on Apex CPU transaction limits and sharing calculation locking behaviour. By identifying these downstream architectural risks early, the SDA prevents high-risk customisations from corrupting the core system, protecting the long-term stability and upgradeability of the platform.</p>

        <p>To ensure operational efficiency, the SDA operates with a clear **delegated authority framework**. Minor declarative modifications (such as updating a picklist value or adjusting a standard list view) are delegated to the business analysis team for immediate approval. Medium and high-complexity requests (such as altering the sharing model, introducing custom objects, or creating custom integrations) require a formal review session where the technical leads debate the design, evaluate the alternatives, and document the final decision in an Architectural Decision Record (ADR). This structured process ensures that major technical choices are made deliberately, transparently, and with full accountability.</p>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The Cost of Customisation</strong>
            <p>Every line of custom code you write on the Salesforce platform is a liability. It represents a piece of technical debt that must be maintained, documented, tested during Salesforce's three annual release cycles, and upgraded when platform capabilities evolve. Enforce a strict standard-first mindset across your entire program backlog.</p>
          </div>
        </div>

        <h2 id="s3">Implementing Fixed-Capacity Agile Frameworks</h2>
        <p>In traditional project management, delivery leaders attempt to manage scope creep using rigid Waterfall change request processes. While this provides commercial protection, it often creates a highly combative, slow-moving program culture where the business feels ignored. To combine commercial guardrails with agility, modern delivery leaders should implement a **Fixed-Capacity, Managed-Scope Agile framework**.</p>

        <p>Under this delivery framework, the program commercial boundaries are locked using a **Fixed-Capacity model**. The delivery vendor commits to providing a stable, cross-functional delivery team (e.g. one architect, three developers, two configurators, two business analysts, and a QA specialist) for a set number of two-week sprints. The total program budget and launch date are completely fixed, providing the predictable boundaries demanded by corporate procurement and financial audits. However, the functional scope within this container remains flexible, managed dynamically sprint-by-sprint.</p>

        <p>The core mechanism of managed scope is the **Scope Exchange agreement**. When business stakeholders identify a new, high-value requirement mid-program, the delivery manager does not immediately refuse the request or initiate a complex change request process. Instead, they present the stakeholder with the current backlog and state: "We can build this new feature in Sprint 8, but to accommodate it within our fixed capacity, we must remove an equivalent volume of existing scope from the launch backlog." This simple exchange immediately shifts the psychological dynamic, converting a combative debate into a collaborative prioritization exercise where the business must directly evaluate the relative value of their requests.</p>

        <p>To support this dynamic, user stories must be estimated using consistent, objective units (such as story points or T-shirt sizes) that represent relative technical complexity and effort. The delivery team's historical velocity (the average number of story points delivered per sprint) acts as the ultimate capacity boundary. If the team's velocity is 40 points, the product owner cannot load 60 points of scope into the sprint backlog. By keeping the capacity locked and enforcing the scope exchange rule, you ensure that the program launch date is never compromised, while giving the business the flexibility to pivot their priorities as they learn.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>The Scope Exchange Rule</strong>
            <p>Never accept a new requirement into your active program backlog without removing an equivalent volume of lower-priority scope. If you allow stakeholders to add features without trading out existing ones, you are actively planning for program delays and budget overruns. Enforce the exchange rule without exception.</p>
          </div>
        </div>

        <h2 id="s4">The MoSCoW Prioritisation Process Under Pressure</h2>
        <p>Managing scope under capacity constraints requires a highly robust prioritization methodology. The industry standard is the **MoSCoW method**, which categorises requirements into **Must have** (critical features without which the system cannot launch), **Should have** (high-value features that are important but have manual workarounds), **Could have** (desirable features that can be easily deferred), and **Won't have** (features agreed to be out-of-scope for the current release). However, during active delivery, stakeholders often suffer from "Must-Have inflation," categorising every single request as a critical, show-stopping requirement.</p>

        <p>To combat Must-Have inflation, the delivery team must enforce a strict **operational definition for Must-Haves**. A requirement is only classified as a Must-Have if the program would be forced to cancel the launch if the feature were missing, or if launching without it would violate legal, regulatory, or compliance mandates. If a business unit can operate for a single day using a manual workaround (such as updating an Excel sheet or sending a manual email), the feature is immediately downgraded to a Should-Have or Could-Have. Applying this objective filter strips out low-value requests, protecting the core delivery timeline.</p>

        <p>Furthermore, establish a firm **mathematical ratio for backlog composition**. The total estimated volume of Must-Have stories in the launch backlog must never exceed 60% of the team's total program capacity. The remaining 40% of capacity must be allocated to Should-Haves (30%) and Could-Haves (10%). This ratio creates a vital buffer that protects the project from unexpected estimation errors, technical hurdles, and genuine late-stage discovery. If the program encounters delays, the delivery manager can simply trade out the Could-Haves and Should-Haves without impacting the core launch validity, guaranteeing on-time delivery.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>MoSCoW Category</th>
                <th>Objective Criteria</th>
                <th>Alternative Workaround</th>
                <th>Target Backlog Ratio</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Must Have</strong></td>
                <td>System cannot launch; legal or regulatory violation if missing</td>
                <td>None; operational shutdown</td>
                <td>Max 60% of capacity</td>
              </tr>
              <tr>
                <td><strong>Should Have</strong></td>
                <td>High-value operational process; impacts efficiency</td>
                <td>Manual spreadsheet tracking; temporary email process</td>
                <td>Target 30% of capacity</td>
              </tr>
              <tr>
                <td><strong>Could Have</strong></td>
                <td>Nice-to-have user experience enhancement or automation</td>
                <td>Existing legacy process; manual data entry</td>
                <td>Target 10% of capacity</td>
              </tr>
              <tr>
                <td><strong>Won't Have</strong></td>
                <td>Low-value customisation; out of current release scope</td>
                <td>Defer to future continuous innovation backlog</td>
                <td>0% of active release capacity</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h2 id="s5">Tactical Refusal and Relationship Protection</h2>
        <p>Holding the line against scope creep ultimately depends on the delivery leader's interpersonal capability and tactical negotiation skills. Simply saying "no" to a senior business sponsor without context or empathy will build resentment, damage trust, and lead stakeholders to bypass program governance to force changes through executive escalation. We must master the art of the **constructive 'no'**, framing scope decisions around technical realities and platform health rather than obstinacy.</p>

        <p>The first tactical approach is to **depersonalise the refusal**. Avoid framing the decision as your personal choice; instead, frame it around the objective capacity limits of the team, the signed Solution Design Authority charter, or the platform's architectural guardrails. Instead of saying: "I won't build this custom object for you," present the program metrics and state: "Our sprint velocity is capped at 40 points, and our Must-Have backlog is currently full. To build this custom object within our timeline, we would need to defer the core billing integration, or we can place it at the top of the Phase 2 backlog. How would you like us to balance these priorities?" This approach repositions the delivery team as partners helping the business manage their limited resources, rather than gatekeepers blocking their progress.</p>

        <p>The second technique is the **Phase 2 Pipeline**. Never tell a stakeholder that their idea is worthless or will never be built, even if it is technically suboptimal. Instead, validate their business challenge and route the request to a visible, structured **Continuous Platform Innovation backlog** (often referred to as Phase 2 or the Enhancement Pipeline). By documenting their request in a visible system (such as Jira or ADO) and categorising it for post-launch enhancement, you show the stakeholder that their voice has been heard and their requirement has been preserved. This defuses immediate tension, allowing the team to maintain sprint focus on the critical launch MVP.</p>

        <p>Finally, implement a **weekly scope audit report** for the executive steering committee. This report must explicitly track the volume of incoming change requests, the status of SDA evaluations, and the quantitative impact of approved scope exchanges on the launch date. By visualising scope creep at the executive level, you empower your senior sponsors to intervene when specific business units are bombarding the team with low-value requests. When executive sponsors see that a minor operational request threatens to delay a multi-million-pound program, they will quickly step in to hold the line, protecting your team and your timeline.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>The most successful delivery managers are not the ones who never say no, but the ones who say 'no' by presenting clear, data-driven alternatives. When you make the trade-offs of a scope change transparent, business leaders will almost always make the right strategic decision, protecting both the project timeline and the platform's long-term health.</p>
          </div>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Salesforce projects are highly vulnerable to scope creep due to the declarative paradox, requirement abstraction, and the tempting platform ecosystem.</li>
            <li>Establishing an authoritative Solution Design Authority (SDA) is the most effective defence, filtering incoming requirements against standard capabilities and architecture limits.</li>
            <li>Enforce a Fixed-Capacity, Managed-Scope agile commercial model to protect the project timeline and budget while allowing sprint-level flexibility.</li>
            <li>Implement the Scope Exchange rule without exception: every new requirement approved must trade out an equivalent volume of existing scope.</li>
            <li>Downgrade Must-Have inflation by applying a strict operational filter: if a manual workaround exists, the requirement is not a Must-Have.</li>
            <li>Master the art of tactical refusal by depersonalising decisions, routing deferred items to a visible Phase 2 enhancement backlog, and reporting scope audits directly to executives.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-section" id="quiz">
            <h2>Checkpoint: Test Your Understanding</h2>

            <div class="quiz-question" id="q1">
              <p>1. What is the 'declarative paradox' and how does it drive scope creep on enterprise Salesforce programmes?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. Developers prefer writing custom Apex code over using standard declarative Flow features.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. Declarative configurations do not support the creation of custom objects or sharing rules.</div>
                <div class="quiz-option" onclick="answer(this,'q1','right')">C. Stakeholders assume that because Salesforce is a low-code platform, configuration changes are instant and free, ignoring downstream regression testing and maintenance costs.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. Validation rules block users from entering data, driving support tickets immediately after go-live.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. How should a delivery manager apply the 'Scope Exchange' rule when stakeholders request a new, high-value feature mid-project?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. Request additional budget from the steering committee to hire more developers for the active sprint.</div>
                <div class="quiz-option" onclick="answer(this,'q2','right')">B. Accept the new feature only if the business stakeholders agree to defer an equivalent volume of existing backlog scope to protect team capacity.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. Reject the request immediately to ensure that developers are not distracted from their current sprint velocity targets.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. Configure the new feature in a developer sandbox without running regression testing or architectural audits.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. What is the target ratio of Must-Have requirements relative to the total team program capacity in a healthy hybrid Salesforce project?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. 100% of capacity must be allocated to Must-Haves to ensure that all business requirements are met.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. Exactly 20% of capacity should be allocated to Must-Haves, with the remainder reserved for technical debt remediation.</div>
                <div class="quiz-option" onclick="answer(this,'q3','right')">C. Must-Haves should never exceed 60% of total team capacity, leaving the remaining 40% for Should-Haves, Could-Haves, and unexpected delays.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. backlogs should contain 10% Must-Haves, 10% Should-Haves, and 80% Could-Haves to maximise agile flexibility.</div>
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

    print("Successfully drafted DEL-021 content!")

if __name__ == '__main__':
    main()
