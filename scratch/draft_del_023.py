import os
import re

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FILEPATH = os.path.join(WORKSPACE_DIR, 'tutorials', 'del-023', 'index.html')

SUMMARY_BULLETS = """
            <li>How to decouple Salesforce testing into three distinct layers: unit, integration, and regression.</li>
            <li>Best practices for optimizing Apex unit testing to exceed coverage requirements while avoiding governor limits.</li>
            <li>Strategies for designing end-to-end integration and API automated test scripts using modern testing suites.</li>
            <li>How to enforce automated regression testing gates within your version-controlled DevOps deployment pipeline.</li>
            <li>Practical frameworks for structuring User Acceptance Testing (UAT) around operational business scenarios.</li>
            <li>Key quality metrics every delivery leader must track to quantify platform stability and release readiness.</li>
"""

TOC_LINKS = """
            <li><a href="#s1">Decoupling Salesforce Testing: Units, Integration, and Regression</a></li>
            <li><a href="#s2">Optimising Apex Unit Testing and Governor Limit Security</a></li>
            <li><a href="#s3">Designing End-to-End Integration and API Test Automation</a></li>
            <li><a href="#s4">Enforcing Regression Testing Gates in the DevOps Pipeline</a></li>
            <li><a href="#s5">Structuring User Acceptance Testing for Real-World Operations</a></li>
"""

BODY_SECTIONS = """
        <h2 id="s1">Decoupling Salesforce Testing: Units, Integration, and Regression</h2>
        <p>In enterprise Salesforce delivery, testing is frequently treated as a single, homogenous activity executed late in the development cycle. Delivery leaders and project teams often conflate different testing methodologies, leading to a state of operational confusion where developers run manual click-tests in developer sandboxes, business users perform ad-hoc testing during UAT, and the QA team struggles to automate a moving target. This lack of structure is a primary driver of post-launch regression bugs, platform instability, and delayed release cycles. To establish a robust, reliable release gate, we must decouple Salesforce testing into three highly distinct, independent layers: **unit testing**, **integration testing**, and **regression testing**.</p>

        <p>The first layer is **unit testing**. Unit testing is a highly technical, developer-driven activity executed at the absolute lowest level of the platform's codebase. It focuses on isolating and validating the behavior of a single, independent logical component—such as an Apex helper class, a custom trigger handler, a Lightning Web Component controller, or a specific Salesforce Flow path. Crucially, a unit test must run in complete isolation from external dependencies, system integrations, or complex database states. Unit testing is not designed to validate business processes; rather, it is designed to guarantee that the code behaves exactly as intended under every conceivable inputs, boundaries, and error condition.</p>

        <p>The second layer is **integration testing**. Unlike unit testing, integration testing focuses on the interaction and communication boundaries between separate platform components and external systems. This includes validating API endpoints, middleware transformations, external callouts, and multi-system data flows. An integration test verifies that when Salesforce triggers an outbound API call, the middleware receives the payload, maps the attributes correctly, routes the data to the target legacy system, and successfully handles the return confirmation. Integration testing is critical for exposing communication failures, data contract mismatches, and network latency issues that unit tests cannot capture.</p>

        <p>The third layer is **regression testing**. Regression testing is a high-level, automated validation suite executed before every major release to verify that new code additions or declarative customisations have not inadvertently broken existing, functional platform capabilities. As a Salesforce org scales, its metadata structure becomes exceptionally complex. A change to a single shared validation rule or a core Apex trigger can trigger unpredictable regression issues across ten different business processes. An automated regression suite acts as the ultimate safety net, scanning the entire platform to guarantee that the system remains stable, secure, and fully operational prior to production deployment.</p>

        <div class="callout callout--warning">
          <div class="callout-icon">⚠️</div>
          <div class="callout-body">
            <strong>The QA Conflation</strong>
            <p>Do not allow your QA team or business analysts to execute manual regression testing. Salesforce metadata is too tightly coupled, and manual scanning of hundreds of end-to-end scenarios is slow, expensive, and highly prone to human error. Automate your regression suite to protect your timeline and your platform.</p>
          </div>
        </div>

        <h2 id="s2">Optimising Apex Unit Testing and Governor Limit Security</h2>
        <p>Salesforce enforces a strict platform requirement: any custom Apex code deployed to a production environment must have at least 75% unit test coverage. While many development teams view this rule as an annoying administrative hurdle, senior delivery leaders recognize that a well-architected unit testing framework is the foundation of platform stability. However, as the volume of custom Apex scales, running the complete test suite can become extremely slow, hitting governor limits and blocking DevOps pipelines.</p>

        <p>To optimize Apex unit testing, developers must adopt the **Enterprise Test Data Factory pattern**. A common anti-pattern is for every individual test class to manually construct its own mock records (Accounts, Contacts, Opportunities) within the test setup. This leads to massive code duplication and extremely slow test runs, as the database must execute the same insertion queries repeatedly. By establishing a centralized, optimized Test Data Factory class, you standardize record creation, enforce required fields automatically, and drastically reduce execution times. Utilize **Test.startTest()** and **Test.stopTest()** to isolate trigger execution and reset transactional governor limits during your unit runs, ensuring that your test code does not trigger false limit violations.</p>

        <p>Furthermore, developers must implement **strict mocking frameworks** for external callouts and complex database states. You cannot execute live HTTP callouts within an Apex test run; the platform explicitly blocks network access. Instead, developers must write mock classes that implement the standard `HttpCalloutMock` interface, returning pre-defined, realistic mock HTTP responses. Similarly, utilize mocking frameworks (such as Apex Enterprise Patterns and the Selector/Service layers) to mock database queries. By simulating database results in memory rather than physically inserting records, you accelerate unit test execution speeds by up to 90%, enabling continuous integration loops.</p>

        <p>Finally, treat **Apex test coverage as a dynamic, quality gate** rather than a static 75% target. Enforce a local team policy requiring all new custom development to achieve at least 85% coverage, with 100% coverage on critical business calculations (such as pricing engines or tax integrations). Additionally, ensure that your unit tests include comprehensive **negative testing**. Do not just test the happy path; write tests that deliberately input corrupt data, trigger validation rules, and inject null values to verify that your error-handling and exception logging structures behave robustly under stress.</p>

        <pre><code class="language-java">@IsTest
public class OpportunityPricingServiceTest {
    @TestSetup
    static void setupTestData() {
        // Centralised Test Data Factory usage
        Account acc = TestDataFactory.createCustomerAccount('Enterprise Client Ltd');
        Opportunity opp = TestDataFactory.createOpportunity(acc.Id, 'Qualification');
    }

    @IsTest
    static void testCalculateStandardPricing_Positive() {
        Opportunity opp = [SELECT Id FROM Opportunity LIMIT 1];
        
        Test.startTest();
        OpportunityPricingService.calculatePricing(opp.Id);
        Test.stopTest();
        
        Opportunity updatedOpp = [SELECT Amount FROM Opportunity WHERE Id = :opp.Id];
        System.assertEquals(15000.00, updatedOpp.Amount, 'Pricing calculation mismatch.');
    }
}</code></pre>

        <div class="callout callout--insight">
          <div class="callout-icon">💡</div>
          <div class="callout-body">
            <strong>The Mocking Benefit</strong>
            <p>Mocking database queries and external service callouts in your Apex tests is the ultimate performance unlock. It allows you to run a suite of 2,000 unit tests in under five minutes, enabling developers to get immediate feedback on their code changes without waiting hours for a deployment pipeline to run.</p>
          </div>
        </div>

        <h2 id="s3">Designing End-to-End Integration and API Test Automation</h2>
        <p>In a mature enterprise architecture, Salesforce rarely operates in isolation. It is typically integrated with a complex ecosystem of ERP systems, payment gateways, marketing databases, and custom microservices. While unit tests validate local Apex code, they cannot verify that these external communication boundaries are functional. To protect these critical touchpoints, the QA team must design and maintain a comprehensive **automated integration testing suite**.</p>

        <p>The foundation of integration testing is the **API Contract validation**. Utilize automated testing tools (such as Postman, SoapUI, or custom Python testing scripts) to run regular, scheduled integration audits against your sandbox API boundaries. These scripts send structured REST or SOAP payloads to Salesforce endpoints, verifying that the system parses the metadata, processes the business logic, and returns the expected JSON/XML response. By automating this contract validation, you immediately catch middleware configuration changes, API version deprecations, and network routing errors before they impact active business operations.</p>

        <p>Furthermore, implement **end-to-end system validation** using automated browser and interface testing tools (such as Selenium, Playwright, or Provar). A typical end-to-end scenario is: "An account manager updates an opportunity stage to Closed-Won in Salesforce, which triggers an outbound message to middleware, creating an invoice in the SAP ERP system, which then returns an invoice number to Salesforce, updating the record page layout." An automated interface test simulates a user clicking the Closed-Won button in a browser, then utilizes API queries to verify that the invoice was generated in SAP and the corresponding record was updated in Salesforce, ensuring seamless transactional alignment.</p>

        <p>To manage integration testing safely, you must establish **robust, dedicated mock endpoints** for external systems during the development phase. If the external ERP system sandbox is slow or unstable, it will block your integration tests, causing false failures and delaying your release cycles. By utilizing API virtualization tools to mock external systems, you decouple your testing schedule from external environment stability. This allows your team to validate Salesforce's outbound callout behavior and error-handling capabilities reliably under simulated network dropouts, timeout exceptions, and server-side errors.</p>

        <div class="callout callout--key">
          <div class="callout-icon">🔑</div>
          <div class="callout-body">
            <strong>API Sandbox Isolation</strong>
            <p>Never connect a Salesforce development sandbox directly to a live, production external database or API. Always route all sandbox integrations through dedicated staging middleware endpoints or mocked systems. This protects your production data integrity and ensures a predictable testing database.</p>
          </div>
        </div>

        <h2 id="s4">Enforcing Regression Testing Gates in the DevOps Pipeline</h2>
        <p>As a Salesforce programme transitions from a greenfield project to a continuous platform innovation model, the risk of regression increases exponentially. With multiple workstreams making rapid, concurrent metadata changes across sandboxes, manual regression checks become a massive bottleneck. To scale delivery safely, delivery leaders must implement **automated regression testing gates** directly within their version-controlled DevOps deployment pipeline.</p>

        <p>The regression gate is enforced using a **CI/CD orchestration tool** (such as GitHub Actions, GitLab CI, or specialized platforms like Copado or Gearset). When a developer commits code or merges a branch into the shared Integration or UAT environment, the pipeline dynamically initiates three automated validation steps. The first is a **static code analysis scan** (utilising PMD or Salesforce Scanner) to check for security vulnerabilities, naming conventions, and best practices. If the code contains security flaws or poor formatting, the pipeline immediately blocks the merge, preventing technical debt from entering the branch.</p>

        <p>The second step is the **automated execution of all local Apex unit tests**. The pipeline runs the complete Apex test suite with code coverage analysis. If any test fails, or if the cumulative coverage falls below the established 85% quality gate, the deployment fails, the branch is locked, and the developers are notified via Slack or email. This immediate feedback loop ensures that broken metadata or trigger regressions are caught and resolved within minutes of being committed, rather than surfacing weeks later during downstream release deployment preparation.</p>

        <p>The final, most advanced step is the **execution of the automated UI regression suite**. Once the metadata is deployed to the Integration sandbox, the pipeline triggers headless browser automation scripts (e.g. running Playwright or Provar containers) to validate the core business paths. The suite scans critical UI elements, page layouts, sharing access controls, and validation rules. If a Lightning Web Component button is missing or a Flow fails to execute, the test suite captures a screenshot, logs the error stack trace, and fails the build. By automating these gates, you convert your release pipeline into an impenetrable shield that guarantees the platform's stability.</p>

        <div class="callout callout--tip">
          <div class="callout-icon">✅</div>
          <div class="callout-body">
            <strong>Leader Perspective</strong>
            <p>Automated pipeline gates are the absolute secret to high-velocity Salesforce delivery. By automating the static analysis, Apex unit tests, and UI regression checks, you remove human subjectivity from the release process. A release either passes the automated gates and deploys, or it fails and is blocked. This guarantees quality and accelerates velocity.</p>
          </div>
        </div>

        <h2 id="s5">Structuring User Acceptance Testing for Real-World Operations</h2>
        <p>The ultimate release gate is not a technical test, but the formal **User Acceptance Testing (UAT)** sign-off. UAT is the phase where representative business users log in to the system to verify that the platform supports their daily operational routines. However, UAT frequently fails because teams structure it around simple, isolated feature verification checklists (e.g. "Verify you can click the save button"). This approach does not represent real-world operations, leading to massive process gaps and usability issues post-launch.</p>

        <p>To run a highly effective UAT, the business analysis team must structure the phase around **operational day-in-the-life scenarios**. A scenario is a complex, multi-user business flow that runs chronologically across different profiles and departments. For example, a customer onboarding scenario is structured as: "1. A sales representative closes an opportunity -> 2. The system generates an onboarding case -> 3. The onboarding specialist validates the customer documents and triggers credit checking -> 4. The credit controller approves the terms -> 5. The system creates the billing record in Salesforce." Users from each of these roles execute their specific steps in sequence, ensuring that the handoffs, notifications, and security profiles align with real-world operational boundaries.</p>

        <p>To support this structured UAT, establish a formal **Defect Management Framework**. Business users must log defects in a centralized tracking tool, categorizing every ticket by severity and root cause. The lead business analyst and delivery manager triage these tickets daily. Crucially, enforce a strict definition for what constitutes a UAT blocking defect. A defect only blocks release if it represents a critical system crash, a security violation, or a complete operational blocker with no workaround. Minor cosmetic adjustments, picklist additions, and nice-to-have UI changes are routed to the post-launch continuous innovation backlog, preventing UAT from stalling the release timeline.</p>

        <p>UAT concludes with a formal **Go/No-Go Decision Gate**. The steering committee gathers to review the UAT metrics, including total test scenario completion rates, open high-severity defects, and technical regression status. The business sponsors, program director, and lead architect must provide formal, written sign-offs. Only when all critical test scenarios are passed, high-severity defects are closed, and automated pipeline gates are green is the release authorized to deploy to the production environment, ensuring absolute strategic alignment and operational confidence.</p>

        <div class="comparison-table">
          <table>
            <thead>
              <tr>
                <th>Testing Phase</th>
                <th>Primary Ownership</th>
                <th>Automation Level</th>
                <th>Environment</th>
                <th>Exit Criteria</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Unit Testing</strong></td>
                <td>Development Team</td>
                <td>100% Automated (Apex / LWC Jest)</td>
                <td>Developer Sandbox / Scratch Org</td>
                <td>&gt; 85% Apex coverage; 100% tests passing</td>
              </tr>
              <tr>
                <td><strong>Integration Testing</strong></td>
                <td>QA Team / Middleware Leads</td>
                <td>Highly Automated (API suites)</td>
                <td>Integration (INT) Sandbox</td>
                <td>100% API contracts valid; all integration endpoints green</td>
              </tr>
              <tr>
                <td><strong>Regression Testing</strong></td>
                <td>DevOps Team / QA Leads</td>
                <td>100% Automated (CI/CD Gates)</td>
                <td>Staging / UAT Sandbox</td>
                <td>Zero failures in regression suite; static analysis passed</td>
              </tr>
              <tr>
                <td><strong>User Acceptance (UAT)</strong></td>
                <td>Business Product Owners / End-Users</td>
                <td>Manual (Facilitated Scenario labs)</td>
                <td>UAT Sandbox</td>
                <td>100% high-priority operational scenarios passed; sign-off received</td>
              </tr>
            </tbody>
          </table>
        </div>
"""

KEY_TAKEAWAYS = """
            <li>Decouple Salesforce testing into unit, integration, and regression layers to establish clear release gates and maintain platform stability.</li>
            <li>Optimise Apex unit testing by utilising centralized Test Data Factories and mocking query/callout layers to accelerate execution.</li>
            <li>Design automated integration test suites to validate API contracts and end-to-end multi-system data flows.</li>
            <li>Enforce automated regression gates in your DevOps pipeline to scan static code, run Apex units, and execute UI tests on every merge.</li>
            <li>Structure User Acceptance Testing (UAT) around sequential, day-in-the-life operational scenarios rather than feature checklists.</li>
            <li>Implement a strict Defect Management Framework to triage UAT tickets, routing non-critical adjustments to the post-launch backlog.</li>
            <li>Secure formal, multi-disciplinary Go/No-Go sign-offs before launching UAT-cleared releases to the production environment.</li>
"""

QUIZ_QUESTIONS = """
          <div class="quiz-section" id="quiz">
            <h2>Checkpoint: Test Your Understanding</h2>

            <div class="quiz-question" id="q1">
              <p>1. What is the primary technical benefit of utilizing mocking frameworks for database queries and HTTP callouts in Apex unit tests?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">A. They automatically update the production database with mock records during the test run.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">B. They bypass Salesforce's 75% Apex code coverage requirement.</div>
                <div class="quiz-option" onclick="answer(this,'q1','right')">C. They run tests in memory in complete isolation, accelerating execution speeds and avoiding database limits.</div>
                <div class="quiz-option" onclick="answer(this,'q1','wrong')">D. They eliminate the need for writing validation rules and custom exceptions.</div>
              </div>
            </div>

            <div class="quiz-question" id="q2">
              <p>2. In a mature version-controlled Salesforce DevOps pipeline, what occurs immediately if a developer merges a branch that fails the automated Apex unit test coverage gate?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">A. The pipeline automatically deletes the developer's scratch org.</div>
                <div class="quiz-option" onclick="answer(this,'q2','right')">B. The pipeline deployment fails, the branch is locked, and the developers are notified, preventing broken metadata from entering UAT.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">C. The pipeline deactivates all active sharing rules and validation rules in UAT.</div>
                <div class="quiz-option" onclick="answer(this,'q2','wrong')">D. The system administrators are prompted to manually review the trigger code.</div>
              </div>
            </div>

            <div class="quiz-question" id="q3">
              <p>3. How should User Acceptance Testing (UAT) be structured to accurately validate Salesforce platform readiness for live business operations?</p>
              <div class="quiz-options">
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">A. Around generic, one-off click-testing checklists for individual fields and buttons.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">B. By allowing developers to execute unit tests inside the production sandbox.</div>
                <div class="quiz-option" onclick="answer(this,'q3','right')">C. Around sequential, day-in-the-life operational scenarios that trace multi-user, multi-department business flows.</div>
                <div class="quiz-option" onclick="answer(this,'q3','wrong')">D. By letting users explore the system without guidance or pre-seeded data.</div>
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

    print("Successfully drafted DEL-023 content!")

if __name__ == '__main__':
    main()
