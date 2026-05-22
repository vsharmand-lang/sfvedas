import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-024', 'index.html')

SUMMARY_BULLETS = """
            <li>The fundamental reasons why traditional project status steering committees fail to drive Salesforce programme success.</li>
            <li>How to design a formal Salesforce Steering Committee Charter with explicit decision-making authority.</li>
            <li>Best practices for structuring a steering committee agenda focused entirely on actions and decisions rather than progress updates.</li>
            <li>Practical strategies for escalating programme risks, managing budget requests, and resolving stakeholder conflicts.</li>
            <li>How to maintain active executive sponsorship and alignment across conflicting business departments.</li>
            <li>Key operational and financial metrics senior leaders must monitor to evaluate overall platform ROI.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">The Anatomy of an Ineffective Steering Committee</a></li>
            <li><a href="#s2">Designing the Executive Salesforce SteerCo Charter</a></li>
            <li><a href="#s3">Structuring the SteerCo Agenda for Decisions, Not Status</a></li>
            <li><a href="#s4">Resolving Escalated Risks and Managing Budget Requests</a></li>
            <li><a href="#s5">Maintaining Executive Sponsorship and Strategic Alignment</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">The Anatomy of an Ineffective Steering Committee</h2>
        <p>In enterprise Salesforce delivery, the steering committee (SteerCo) is theoretically the highest governing body of the programme. It is comprised of executive sponsors, department heads, technology leaders, and delivery partners who gather regularly to oversee progress, resolve major escalations, and protect the programme's budget and strategic alignment. However, in reality, a shocking number of Salesforce steering committees are highly ineffective, operating as expensive, slow-moving status meetings where executives silently review color-coded slides and listen to generic updates without making a single meaningful decision.</p>

        <p>The primary driver of steering committee failure is **status update fixation**. Traditional committees spend 90% of their meeting time walking through historical progress decks, detailing developer velocity metrics, reviewing past task completions, and explaining minor schedule variances. By the time the technical team finishes presenting these details, the meeting is almost over, leaving only a few rushed minutes to address critical program risks or architectural escalations. Executives leave the meeting feeling under-utilized, while the delivery team leaves without the critical strategic decisions and approvals needed to maintain momentum.</p>

        <p>The second driver is the **lack of explicit decision-making authority**. Many committees are established without a clear operational charter defining who owns the final vote, what constitutes a quorum, and what financial or scope boundaries the committee can approve. When a major escalation occurs—such as a budget overrun on middleware licensing or a resource conflict between sales and service workstreams—the committee descends into endless debate. Instead of making an active decision, they defer the choice to subsequent sub-committees or request further analysis, stalling the program and accumulating technical and operational debt.</p>

        <p>Finally, steering committees frequently suffer from **executive disconnect**. Senior business sponsors are often time-poor and unfamiliar with the Salesforce platform. If the delivery team presents escalations using highly technical, platform-specific terminology (such as discussing trigger recursion, governor limits, or metadata merge conflicts), the executives will check out. They cannot evaluate the business impact of these technical risks, leading them to either rubber-stamp poor architectural choices or block critical DevOps investments. To secure true program velocity, we must restructure our steering committees, transforming them from passive status forums into high-performance decision-making machines.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The Status Trap</strong>
            <p>If your steering committee meetings rely on walking through a slide deck detailing completed tasks and sprint burn-downs, you are wasting your executives' time. A status update can be read in a five-minute email. The steering committee exists to steer, which means making hard, binary choices about budget, scope, resources, and risk.</p>
          </div>
        </div>

        <h2 id="s2">Designing the Executive Salesforce SteerCo Charter</h2>
        <p>To rescue a steering committee from passive status fixation, delivery leaders must implement a formal, signed **Salesforce Steering Committee Charter**. The charter is a foundational governance document that establishes the committee's purpose, membership, voting rules, and explicit boundaries of authority, ensuring that every participant understands their operational responsibilities and accountability from day one.</p>

        <p>The core of the charter is the **Explicit Authority matrix**. The charter must define exactly what decisions the committee can authorize without escalating to the board or executive committee. This includes setting clear financial approval thresholds (e.g. approving contract variations up to £250,000 or license purchases up to a specific limit), authorizing major milestone schedule shifts (up to a set number of weeks), and resolving cross-workstream design disputes. By establishing these predefined boundaries, the committee can act decisively, eliminating the need to request external approvals for standard programme remediation.</p>

        <p>The charter must also define the **Membership and Voting structure**. Membership must be restricted to individuals who hold absolute accountability for their department's budget and operations, including the Chief Technology Officer, the heads of the business units adopting Salesforce (such as the VP of Sales or Customer Success), and the Program Director. The charter should enforce a strict **no-proxy rule**: if an executive sponsor cannot attend, they cannot delegate their voting authority to a junior staff member who lacks the mandate to make financial or operational commitments. This ensures that the meeting maintains its decision-making capacity.</p>

        <p>Additionally, the charter establishes the **formal quorum and escalation paths**. A meeting is only valid if a quorum of voting sponsors is present. If a critical decision must be made and quorum is not met, the charter defines an immediate, time-boxed escalation procedure to secure written approvals within 24 hours. By codifying these governance rules, you prevent key decisions from stalling due to calendar conflicts, protecting the delivery team's sprint momentum and maintaining platform velocity.</p>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The No-Proxy Mandate</strong>
            <p>Enforcing a strict no-proxy rule in your steering committee charter is a game-changer. When executives know that they cannot delegate their seat and that their physical absence will block critical department decisions, they will prioritize the SteerCo in their calendars, ensuring high-level alignment and rapid sign-offs.</p>
          </div>
        </div>

        <h2 id="s3">Structuring the SteerCo Agenda for Decisions, Not Status</h2>
        <p>Once the charter is signed, the delivery manager must radically restructure the steering committee's meeting format. The absolute standard rule of successful executive governance is the **90/10 Rule**: 90% of the meeting time must be dedicated to discussing key decisions, escalated risks, and strategic alignment; only 10% may be spent reviewing high-level programme health metrics. Status updates are completely removed from the oral agenda, replaced by a pre-distributed dashboard.</p>

        <p>The foundation of this new model is the **Pre-Read Dashboard**. At least 48 hours prior to the meeting, the delivery team distributes a concise, three-page status report. The report utilizes standardized RAG (Red-Amber-Green) indicators to summarize schedule, budget, scope, and technical quality. It includes key milestone tracking, active sprint velocity, and a summary of budget burn rate. Executives are expected to review this document prior to entering the room. The meeting begins with the immediate assumption that the status report has been read, bypassing the need to walk through slides and launching directly into the decision-making agenda.</p>

        <p>The oral meeting agenda must be structured around the **Decision Log**. The agenda is divided into three distinct segments. The first segment is **Decisions Required** (30 minutes). The Program Director presents a maximum of three critical choices, using structured **Decision Briefs**. Each brief maps out the context, the business impact, the options considered, the financial implications, and the lead architect's recommended path. The committee debates the options and records a formal, binary vote. The second segment is **Escalated Risk Remediation** (20 minutes), where the committee approves mitigation plans for active threats. The final segment is **Strategic Alignment Review** (10 minutes).</p>

        <p>By structuring the meeting around active choices, you change the energy of the room. Executives are engaged because they are executing their strategic mandate. They are not being talked at; they are actively steering the program, resolving resource bottlenecks, and removing blockers that would otherwise stall the technical delivery team, ensuring a clean, predictable path to go-live.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>Restructure the Agenda</strong>
            <p>Restructure your SteerCo agenda: 1. Status Dashboard (Take as Read) -> 2. Decision Brief 1 (Vote) -> 3. Decision Brief 2 (Vote) -> 4. Active Risk Remediation -> 5. Strategic Alignment. Keep status updates in writing, and use the meeting exclusively for live, active decisions.</p>
          </div>
        </div>

        <h2 id="s4">Resolving Escalated Risks and Managing Budget Requests</h2>
        <p>One of the primary strategic functions of a steering committee is the resolution of escalated programme risks and the management of budget contingency requests. In complex Salesforce rollouts, risks often cross departmental boundaries—such as an integration delay caused by an external ERP team, or a licensing cost variation driven by an increase in active users. When these risks escalate, the SteerCo must act as a collaborative resolution body, not a combative auditing committee.</p>

        <p>To manage risk escalations effectively, the delivery team must utilize a **Quantitative Risk Register**. Risks cannot be described in vague terms; they must be quantified by probability, operational impact, and cost. For example, instead of stating: "The middleware integration is delayed," the register documents: "Delay in SAP integration API delivery by external vendor. Probability: High. Impact: Postpones end-to-end testing by 3 weeks, costing £45,000 in technical team burn rate." This quantitative formatting immediately frames the risk in language that business sponsors understand, allowing them to evaluate the cost of inaction.</p>

        <p>When a risk requires a **budget contingency request**, the Program Director must present a formal variation request. The variation request must document three elements: the root cause of the variation, the technical and business alternatives considered, and the precise ROI of the requested budget. For instance, if the lead architect recommends purchasing a specialized AppExchange backup tool to secure data compliance, the brief must contrast the software cost with the massive financial risk of manual database restoration and compliance failure. The committee evaluates the request against the remaining programme contingency funds, ensuring that additional investments are routed to high-value, strategic needs.</p>

        <p>Additionally, the steering committee must enforce a strict **remediation accountability loop**. When a risk mitigation plan or budget variation is approved, the committee assigns a specific executive sponsor to own the remediation action. If the risk is a delay in partner API delivery, the Chief Technology Officer is tasked with personally contacting the partner's leadership to resolve the bottleneck. This active executive intervention removes operational roadblocks that the delivery team has no authority to touch, accelerating progress and protecting the project timeline.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>Never bring a risk or budget escalation to your steering committee without presenting three viable, quantified remediation options and a clear recommendation from your technical leadership. Executives are not there to brainstorm technical solutions; they are there to select the best strategic option from a pre-analyzed menu.</p>
          </div>
        </div>

        <h2 id="s5">Maintaining Executive Sponsorship and Strategic Alignment</h2>
        <p>Salesforce is not merely a database or a departmental CRM; in modern enterprises, it is a core business transformation platform that alters how multiple departments interact with customers and each other. Consequently, a Salesforce rollout inevitably triggers **intense departmental conflicts** over business processes, sharing rules, and resource allocation. The steering committee must act as the ultimate arbiter of these conflicts, maintaining long-term strategic alignment and protecting the program's vision.</p>

        <p>The first major alignment challenge is **cross-departmental process ownership**. For example, during a Sales and Service Cloud implementation, sales leaders may demand a highly open sharing model to maximize pipeline visibility, while service leaders demand a restricted model to secure sensitive customer support logs. The delivery team cannot resolve this conflict; attempting to configure a compromised middle ground leads to a messy sharing architecture and security gaps. The steering committee must step in, review the business impacts against the strategic charter, and declare a single, authoritative policy that the entire organization must follow.</p>

        <p>The second challenge is maintaining **long-term executive sponsorship**. As a multi-year Salesforce transformation progresses, initial excitement can decay, especially if business units experience minor go-live friction or operational change fatigue. To combat this, the steering committee must establish a **Continuous Value Realisation workstream**. The committee runs regular audits to track active system usage, user feedback, and financial ROI against the original business case. By communicating these positive outcomes to the board and the wider organization, the committee preserves strategic support, protecting the program from budget cuts and maintaining platform investment.</p>

        <p>Ultimately, a high-performing steering committee transforms Salesforce delivery from a high-risk technical project into a highly successful, strategic business capability. By combining a signed operational charter, a decision-focused agenda, quantitative risk management, and active executive sponsorship, you establish a world-class governance framework that protects your team, secures your budget, and guarantees the long-term strategic success of your platform.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>SteerCo Activity</th>
                <th>Traditional Status Meeting (Failed)</th>
                <th>High-Performance SteerCo (Success)</th>
                <th>Strategic Business Outcome</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Time Allocation</strong></td>
                <td>90% status updates; 10% rushed risk discussion</td>
                <td>10% status review (read pre-read); 90% decision briefs</td>
                <td>Rapid operational decisions; zero timeline bottlenecks</td>
              </tr>
              <tr>
                <td><strong>Meeting Agenda</strong></td>
                <td>Reviewing developer task details and slide decks</td>
                <td>Voting on 2-3 structured Decision Briefs and risk remediation</td>
                <td>Binary choices; clear technical and financial accountability</td>
              </tr>
              <tr>
                <td><strong>Conflict Resolution</strong></td>
                <td>Endless debates deferred to subsequent meetings</td>
                <td>Sponsors vote on aligned options; assign remediation owners</td>
                <td>Elimination of departmental silos and process compromises</td>
              </tr>
              <tr>
                <td><strong>Attendance</strong></td>
                <td>Junior proxies attending; voting delayed</td>
                <td>Active executive sponsors only; strict no-proxy rule</td>
                <td>Instant strategic alignment; direct executive backing</td>
              </tr>
            </tbody>
          </table>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Avoid status-fixated steering committees; they waste executive capacity and fail to provide the critical decisions required for delivery.</li>
            <li>Establish a signed Steering Committee Charter to codify explicit decision-making authority, membership, and strict quorum rules.</li>
            <li>Enforce the 90/10 rule: 90% of meeting time must be dedicated to Decision Briefs, leaving status tracking to a pre-distributed dashboard.</li>
            <li>Implement a strict no-proxy rule to ensure that only sponsors with absolute operational and financial mandates occupy committee seats.</li>
            <li>Quantify escalated risks by probability, impact, and cost to enable executives to evaluate the financial implications of choices.</li>
            <li>Assign active remediation ownership to specific executive sponsors to remove cross-departmental roadblocks and external bottlenecks.</li>
            <li>Audit post-launch feature adoption and financial ROI to maintain strategic executive sponsorship and justify continuous platform investment.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-section" id="quiz">
            <h2>Checkpoint: Test Your Understanding</h2>

            <div class="quiz-question" id="q1">
              <p>1. What is the primary operational flaw of status-fixated Salesforce steering committees?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. They do not invite junior developers or configurators to present.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. They meet too frequently, causing sprint schedules to slip.</div>
                <div class="quiz-option" onclick="answer(this,'q1','right')">C. They spend 90% of meeting time reviewing historical task details rather than voting on critical decisions and resolving escalations.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. They require the technical team to write detailed business requirement specifications.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. How does a signed Steering Committee Charter protect a Salesforce programme's delivery velocity?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. It guarantees that the project will never exceed its original budget or scope limits.</div>
                <div class="quiz-option" onclick="answer(this,'q2','right')">B. It codifies the committee's explicit boundaries of authority, voting quorum, and no-proxy rules, enabling rapid decision-making.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. It allows developers to configure custom Apex code without undergoing security reviews.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. It routes all minor picklist modifications directly to executive board votes.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. Under the 90/10 steering committee format, how should weekly programme progress and status updates be communicated to executives?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. Via an oral presentation led by the lead developer during the first 45 minutes of the meeting.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. By hosting daily stand-up meetings with the executive sponsors in UAT.</div>
                <div class="quiz-option" onclick="answer(this,'q3','right')">C. Via a concise, pre-read dashboard distributed at least 48 hours prior to the meeting, which is taken as read.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. By inviting executives to scrub through the team's Jira backlog dashboard during the meeting.</div>
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

    print("Successfully drafted DEL-024 content!")

if __name__ == '__main__':
    main()
