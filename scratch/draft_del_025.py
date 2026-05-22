import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-025', 'index.html')

SUMMARY_BULLETS = """
            <li>How to manage the high-risk operational transition from project delivery to platform support.</li>
            <li>An objective operational comparison of in-house, outsourced, and hybrid Salesforce support models.</li>
            <li>How to design and establish a high-performing internal Salesforce Center of Excellence (CoE).</li>
            <li>Best practices for establishing Service Level Agreements (SLAs) tailored to Salesforce's unique architecture.</li>
            <li>How to balance continuous platform customisation with technical debt management and upgrade readiness.</li>
            <li>Practical strategies for recruiting, training, and retaining top-tier internal Salesforce talent.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">The Critical Transition: From Project to Platform Support</a></li>
            <li><a href="#s2">Operational Comparison: In-House vs Outsourced Salesforce Support</a></li>
            <li><a href="#s3">Designing the Hybrid Support Model and Center of Excellence</a></li>
            <li><a href="#s4">Establishing Service Level Agreements (SLAs) for Salesforce</a></li>
            <li><a href="#s5">Managing Continuous Platform Innovation and Technical Debt</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">The Critical Transition: From Project to Platform Support</h2>
        <p>In enterprise Salesforce delivery, go-live is often celebrated as the absolute end of the programme. The delivery team packages the metadata, executes the final data load, completes the cutover checklist, and hosts a celebratory launch event. However, for the business, go-live is not the end; it is merely the beginning of the platform's operational lifecycle. A common, high-risk mistake is failing to plan for the post-go-live transition phase, assuming that because the software is deployed, it will support itself. This lack of operational preparation leads to severe **hypercare instability**, high volumes of unresolved support tickets, and immediate user frustration.</p>

        <p>The primary driver of transition failure is the **operational gap** between the project delivery team and the business-as-usual (BAU) support team. During the development phase, the project team operates with deep, context-specific knowledge of the customisations, integrations, and business processes they have configured. The BAU support team, often a generic enterprise IT help desk, is typically excluded from the design workshops. When the project team rolls off, the support team is suddenly bombarded with complex, platform-specific queries that they have no training to resolve. Tickets pile up, business operations slow down, and users begin to reject the platform.</p>

        <p>To bridge this operational gap, delivery leaders must execute a formal, structured **Service Transition Plan**. The transition process begins at least four weeks prior to go-live with **joint hypercare collaboration**. The lead support analysts are embedded directly within the project QA and business analysis teams. They participate in UAT triaging sessions, shadow developers during deployment preparation, and review the Architectural Decision Records (ADRs). This hands-on exposure ensures that the support team acquires the contextual technical knowledge needed to handle real-world user struggles before they take absolute ownership of the live org.</p>

        <p>Furthermore, the Service Transition Plan must define a strict **hypercare exit criteria**. The project delivery team does not roll off immediately on go-live day; instead, they remain active in a hybrid support capacity for a set period (typically two to four weeks). During this hypercare window, the project team handles complex level-3 escalations while actively training the BAU support analysts. The transition is only complete, and the project team is only released, when the platform meets predefined stability thresholds, including: 100% of high-priority UAT bugs resolved, help desk ticket queue volume within normal bounds, and all operational runbooks fully signed and delivered.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Rolloff Danger</strong>
            <p>Do not allow your development partners or implementation team to roll off immediately after go-live. A platform support team requires a structured, multi-week knowledge transfer window to absorb the technical context of custom code and complex integrations. If you roll off your team without a transition plan, your post-launch stability is at risk.</p>
          </div>
        </div>

        <h2 id="s2">Operational Comparison: In-House vs Outsourced Salesforce Support</h2>
        <p>Once the initial hypercare phase concludes, delivery leaders and technology executives must establish the long-term operational support model for the Salesforce platform. This decision represents a critical strategic choice, requiring an objective evaluation of the financial and operational trade-offs between three distinct support structures: **in-house support**, **outsourced managed services**, and the **hybrid model**.</p>

        <p>The first option is the **100% In-House Support Model**. This involves recruiting, training, and retaining a dedicated internal team of Salesforce administrators, business analysts, and developers who reside within the organization's IT department. The primary advantage of this model is **deep business context**. Internal employees develop an intimate understanding of the company's culture, daily operations, and long-term strategic goals. They collaborate closely with business units, providing rapid, highly customized support and driving organic platform innovation. However, the in-house model is expensive, difficult to scale, and exposes the organization to significant talent retention risk in a highly competitive market.</p>

        <p>The second option is the **100% Outsourced Managed Services Model**. Under this structure, the organization retains an external Salesforce partner or specialist systems integrator to handle all platform support, maintenance, and enhancement requests. This model provides **exceptional scalability and deep technical expertise**. The organization can scale support capacity up or down based on business demand, and has immediate access to highly specialized skills (such as senior architects, integration specialists, or CPQ developers) that would be too expensive to retain full-time. However, outsourced partners often lack deep business context, leading to transactional relationships focused strictly on ticket closure rather than strategic value creation.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>Operational Attribute</th>
                <th>In-House Support Team</th>
                <th>Outsourced Managed Services</th>
                <th>Hybrid Model &amp; CoE</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Contextual Knowledge</strong></td>
                <td>Exceptional; deep operational and cultural context</td>
                <td>Limited; transactional understanding of processes</td>
                <td>High; internal leads guide external experts</td>
              </tr>
              <tr>
                <td><strong>Technical Depth</strong></td>
                <td>Variable; limited by internal staff skillsets</td>
                <td>Exceptional; access to specialized partner pools</td>
                <td>High; internal leads coordinate partner experts</td>
              </tr>
              <tr>
                <td><strong>Scale &amp; Flexibility</strong></td>
                <td>Rigid; capacity capped by full-time headcount</td>
                <td>Highly flexible; capacity scales with demand</td>
                <td>Optimal; stable core with flexible partner extensions</td>
              </tr>
              <tr>
                <td><strong>Strategic Focus</strong></td>
                <td>High; focused on long-term business innovation</td>
                <td>Low; focused strictly on SLA ticket closure</td>
                <td>Balanced; internal team leads strategy; partner executes build</td>
              </tr>
              <tr>
                <td><strong>Operational Cost</strong></td>
                <td>High fixed cost; recruitment overhead</td>
                <td>Variable cost; monthly retainer model</td>
                <td>Optimised; efficient core with variable extensions</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The Talent Bottleneck</strong>
            <p>Retaining high-performing Salesforce talent internally is exceptionally difficult. If your support model relies entirely on a single in-house administrator, their sudden resignation will leave your organization highly vulnerable. Always maintain a backup talent plan or a partner relationship to secure operational continuity.</p>
          </div>
        </div>

        <h2 id="s3">Designing the Hybrid Support Model and Center of Excellence</h2>
        <p>The absolute industry gold standard for enterprise Salesforce operations is the **Hybrid Support Model**, governed by an internal **Center of Excellence (CoE)**. This model combines the strategic alignment and business context of an in-house core team with the scalability, deep technical expertise, and resource flexibility of an external managed services partner, delivering the absolute highest return on investment.</p>

        <p>The **internal core team** is structured around key business-facing roles. This includes the Salesforce Platform Director, senior business analysts, and solution architects. These internal leaders own the strategic platform roadmap, manage the relationships with executive business sponsors, and enforce the Solution Design Authority governance rules. They ensure that all platform enhancements directly align with corporate strategic goals, protecting the platform from ad-hoc, low-value customisation requests. They act as the "brains" of the platform, directing the delivery of value.</p>

        <p>The **managed services partner** acts as the highly scalable "delivery engine." When the core team approves a major set of enhancements or a complex release cycle, they task the partner's developers, configurators, and QA specialists with the execution. The partner operates under a structured monthly retainer or capacity contract, allowing the organization to scale resource capacity up or down based on active program demands. This eliminates the overhead of recruiting and maintaining a massive internal development team, while securing immediate access to specialized technical talent when needed.</p>

        <p>The hybrid model is governed by the **Center of Excellence (CoE)**. The CoE is a cross-functional governing body that establishes platform standards, defines the environment and DevOps pipelines, manages licensing commercial structures, and facilitates knowledge sharing across business units. By centralizing governance, the CoE prevents disparate departments from building siloed solutions in the same org, ensuring that Salesforce scales as a unified, cohesive enterprise platform that drives strategic corporate value.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>The Hybrid Partition</strong>
            <p>The secret to hybrid success is clear partitioning of responsibilities: keep business context, architectural roadmaps, and platform governance strictly in-house; outsource development execution, testing, and ticket management to your managed services partner. This protects your strategic direction while maximizing operational efficiency.</p>
          </div>
        </div>

        <h2 id="s4">Establishing Service Level Agreements (SLAs) for Salesforce</h2>
        <p>To manage a hybrid or outsourced support model successfully, technology leaders must establish clear, robust **Service Level Agreements (SLAs)**. An SLA is a formal contract that defines the expected responsiveness, resolution quality, and operational availability of the support services. However, a common mistake is adopting generic IT help desk SLAs that do not reflect the unique, metadata-driven architecture of the Salesforce platform.</p>

        <p>Salesforce SLAs must be explicitly structured around **operational business severity**, rather than simple technical ticket queues. We define four distinct severity tiers. **Severity 1 (Critical)** represents a complete platform outage or a total business blocker with no workaround (e.g. the checkout flow fails for all customers, or the integration with the primary ERP drops). The SLA must mandate an immediate **response within 15 minutes** and a **resolution target of under 4 hours**, with the support team operating continuously until the service is restored.</p>

        <p>**Severity 2 (High)** represents a major process impairment affecting an entire department or high-value customer group (e.g. sales representatives cannot generate PDF quotes, or support agents cannot view historical cases). The target resolution is under **8 business hours**. **Severity 3 (Medium)** represents a minor operational issue affecting a small group of users with a viable workaround (e.g. a specific dashboard fails to refresh, or a validation rule throws an incorrect error). The target resolution is under **3 business days**. Finally, **Severity 4 (Low)** covers standard administrative requests, list views, and password resets, with a target resolution of **5 business days**.</p>

        <p>To enforce these SLAs, implement a robust **ticketing system integration** (such as ServiceNow or Salesforce Service Cloud) to track ticket metrics automatically. Monitor four core support KPIs: **First Response Time** (the speed of initial triage), **Mean Time to Resolution** (MTTR), **SLA Compliance Rate** (the percentage of tickets resolved within target thresholds), and **First Contact Resolution Rate** (the percentage of tickets resolved without multi-agent handoffs). Review these KPIs weekly with your support leads and monthly with your managed service partner's leadership, linking SLA compliance directly to financial retainers and performance penalties to guarantee operational excellence.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>Do not allow your support partner to inflate their SLA compliance rates by closing tickets before a permanent fix is deployed. Enforce a strict ticket re-open policy: if a user's issue recurs within 48 hours of ticket closure, the ticket must be re-opened and the SLA timer must retroactively calculate from the original submission date. This ensures genuine resolution quality.</p>
          </div>
        </div>

        <h2 id="s5">Managing Continuous Platform Innovation and Technical Debt</h2>
        <p>The final pillar of post-go-live success is managing the delicate balance between **continuous platform innovation** and **technical debt accumulation**. Salesforce is not a static software installation; the business will constantly request new features, layout changes, and process automations to adapt to market shifts. However, if the support team executes these requests reactively without strict architectural control, the org will rapidly accumulate technical debt, leading to platform instability and upgrading friction.</p>

        <p>To manage this balance, enforce a strict **Release Cadence framework**. Support and enhancement requests must be categorized into three release streams. **Hotfixes (Severity 1 and 2)** are deployed immediately through isolated DevOps pipelines to resolve active production emergencies. **Minor Enhancements (declarative modifications)** are packaged and deployed on a weekly or bi-weekly cycle. **Major Enhancements (custom code, new integrations, or major object modifications)** are managed as mini-projects, developed in sandboxes, and deployed on a structured monthly or quarterly release cadence.</p>

        <p>Furthermore, the Platform Director must dedicate a fixed percentage of every release cycle's capacity (typically **20% of team capacity**) exclusively to **technical debt remediation and platform health**. This capacity is used to refactor complex legacy Flows, clean up unused custom fields, optimize Apex trigger performance, update API versions, and ensure compliance with Salesforce's three annual release upgrades (Spring, Summer, and Winter). By proactively managing platform health, you prevent the org from becoming an unmaintainable "spaghetti org," ensuring that Salesforce remains agile, secure, and ready to adopt future platform innovations.</p>

        <p>Ultimately, a high-performing post-go-live support model transforms Salesforce from a simple CRM into a highly responsive, strategic business asset. By establishing a robust hybrid support model, defining clear, severity-based SLAs, governing through a Center of Excellence, and dedicating consistent capacity to platform health, you protect your technical investment and empower your business to innovate continuously with absolute operational confidence.</p>
"""

KEY_TAKEAWAYS = """
            <li>Go-live is not the end of the Salesforce lifecycle; it represents the high-risk operational transition to platform support that requires structured planning.</li>
            <li>In-house support offers deep business context but is expensive and carries talent retention risks, while outsourced managed services provide scale but lack context.</li>
            <li>The hybrid support model is the industry standard: keep strategic governance and business analysis in-house, and outsource execution to a managed service partner.</li>
            <li>Establish a Center of Excellence (CoE) to centralize governance, define DevOps standards, manage licensing, and prevent departmental silos.</li>
            <li>Define Service Level Agreements (SLAs) tailored to Salesforce, structured explicitly around business severity and operational RAG KPIs.</li>
            <li>Enforce a strict Release Cadence framework, separating hotfixes, minor enhancements, and major releases to maintain system stability.</li>
            <li>Dedicate at least 20% of support team capacity to technical debt remediation, Apex refactoring, and Salesforce upgrade compliance.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-section" id="quiz">
            <h2>Checkpoint: Test Your Understanding</h2>

            <div class="quiz-question" id="q1">
              <p>1. What is the primary operational advantage of implementing a Hybrid Support Model for enterprise Salesforce platforms?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. It completely eliminates the need for internal solution architects or platform directors.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. It allows business users to configure and deploy Apex code directly to the production environment.</div>
                <div class="quiz-option" onclick="answer(this,'q1','right')">C. It pairs the strategic business context of a small, core in-house team with the scalable technical capacity of an external managed services partner.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. It guarantees that the monthly licensing costs will remain fixed regardless of user volume.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. How should a technology leader structure SLAs for a Salesforce support contract to ensure genuine business alignment?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. Around the total number of developer story points completed during each active sprint.</div>
                <div class="quiz-option" onclick="answer(this,'q2','right')">B. Around clear operational business severity tiers (Severity 1 to 4) with explicit, quantitative response and resolution targets.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. Around the number of custom fields and validation rules created by the support team.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. By requiring the support team to respond to all emails within exactly 5 minutes.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. Why must a platform director dedicate a fixed percentage (typically 20%) of the support team's capacity to technical debt remediation?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. To comply with standard Salesforce developer certification renewal requirements.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. To ensure that the QA team has sufficient capacity to execute manual UAT scenarios.</div>
                <div class="quiz-option" onclick="answer(this,'q3','right')">C. To refactor complex legacy metadata, clean up unused customisations, and ensure compatibility with Salesforce's three annual upgrade releases.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. To justify the purchase of additional Salesforce sandboxes and pipeline deployment tools.</div>
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

    print("Successfully drafted DEL-025 content!")

if __name__ == '__main__':
    main()
