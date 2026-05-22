# -*- coding: utf-8 -*-
import os
import re
import sys

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIALS_DIR = os.path.join(WORKSPACE_DIR, 'tutorials')

def update_file(slug, data):
    filepath = os.path.join(TUTORIALS_DIR, slug, 'index.html')
    if not os.path.exists(filepath):
        print(f"Error: File not found {filepath}")
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Summary Bullets
    summary_bullets_html = ""
    for bullet in data['summary_bullets']:
        summary_bullets_html += f"            <li>{bullet}</li>\n"
    content = content.replace('<!-- [[SUMMARY_BULLETS]] -->', summary_bullets_html.strip())

    # 2. Body Sections
    body_sections_html = ""
    for sec_id, sec_title, sec_content in data['body_sections']:
        body_sections_html += f'        <h2 id="{sec_id}">{sec_title}</h2>\n'
        body_sections_html += f'        {sec_content}\n\n'
    content = content.replace('<!-- [[BODY_SECTIONS]] -->', body_sections_html.strip())

    # 3. Key Takeaways
    takeaway_bullets_html = ""
    for bullet in data['takeaway_bullets']:
        takeaway_bullets_html += f"            <li>{bullet}</li>\n"
    content = content.replace('<!-- [[TAKEAWAY_BULLETS]] -->', takeaway_bullets_html.strip())

    # 4. Quiz Questions
    quiz_html = ""
    for q_idx, q in enumerate(data['quiz_questions'], start=1):
        q_id = f"q{q_idx}"
        quiz_html += f'          <div class="quiz-question" id="{q_id}">\n'
        quiz_html += f'            <p class="quiz-q-text">{q["question"]}</p>\n'
        for opt_idx, opt in enumerate(q['options']):
            letter = chr(65 + opt_idx)
            is_correct = 'right' if opt_idx == q['correct_index'] else 'wrong'
            quiz_html += f'            <div class="quiz-option" onclick="answer(this, \'{q_id}\', \'{is_correct}\')">{letter}. {opt}</div>\n'
        quiz_html += f'          </div>\n'
    content = content.replace('<!-- [[QUIZ_QUESTIONS]] -->', quiz_html.strip())

    # 5. TOC Links
    toc_links_html = ""
    for sec_id, sec_title, _ in data['body_sections']:
        # Strip numbering or tags if any in toc title
        clean_title = re.sub(r'^\d+\.\s*', '', sec_title)
        toc_links_html += f'            <li><a href="#{sec_id}">{clean_title}</a></li>\n'
    content = content.replace('<!-- [[TOC_LINKS]] -->', toc_links_html.strip())

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully updated {slug}")
    return True

# ----------------- DATA PREPARATION FOR SEC-012 -----------------
sec012_data = {
    'summary_bullets': [
        "Demystify the end-to-end AppExchange Security Review workflow, timeline, and core testing philosophies.",
        "Learn how to run and configure Salesforce Code Analyzer (SFCA) and PMD to identify potential compliance violations.",
        "Detail the exact manual penetration testing techniques employed by the Salesforce review team on external endpoints.",
        "Review and mitigate injection vulnerabilities including SOQL Injection, Stored/Reflected XSS, and Cross-Site Request Forgery (CSRF).",
        "Enforce strict CRUD and FLS (Field-Level Security) checks using Apex modern practices, including WITH USER_MODE and the Security.stripInaccessible API.",
        "Secure external integrations using Named Credentials, Content Security Policies (CSP), and Cross-Origin Resource Sharing (CORS)."
    ],
    'body_sections': [
        (
            "s1",
            "1. The AppExchange Gatekeeper: Understanding the Security Review Architecture",
            """<p>The AppExchange is the cornerstone of the enterprise cloud software ecosystem, but its immense success relies on a single, non-negotiable principle: absolute trust. To protect client organisations from malicious actors, data leakages, and unstable code, Salesforce enforces the AppExchange Security Review. This process is not a cursory checklist exercise or a simple automated pass; it is an exhaustive architectural and security assessment. It applies to managed packages, external connected applications, browser extensions, and mobile clients that interact with the Salesforce API.</p>
            <p>For ISV partners, understanding the architecture of the review is vital. The process evaluates the entire threat model of your offering. If your managed package communicates with an external Heroku application, the Heroku application, its APIs, its database, and its hosting infrastructure are all in scope. Salesforce treats your solution as a unified system, meaning a vulnerability in your external Node.js backend will fail your entire Salesforce listing. The review aims to verify three core pillars: data isolation, platform integrity, and secure transport. By standardising on robust security practices from day one, organisations can avoid the common cycle of failure, redesign, and resubmission.</p>
            <p>The lifecycle of the security review typically involves several key stages. First is the preparatory stage where developers run local scanners and document the architecture. Next is the submission phase where the managed package and all required documentation (including automated scan reports and architecture diagrams) are uploaded. This is followed by the automated scanning queue and finally the manual penetration testing phase. If issues are discovered, the review team issues a detailed report listing the failures, which the partner must remediate before resubmitting. Understanding this operational sequence allows product teams to align their development schedules with realistic certification timelines.</p>"""
        ),
        (
            "s2",
            "2. Automated Static Analysis: Mastering Salesforce Code Analyzer and PMD",
            """<p>Before your package is submitted, you must run automated static application security testing (SAST). The standard tool for this is the Salesforce Code Analyzer (SFCA), which bundles PMD, ESLint, Retire.js, and Salesforce's proprietary Graph Engine. These tools inspect code without executing it, searching for patterns that indicate security vulnerabilities or poor coding practices.</p>
            <p>PMD scans Apex source code for common violations, such as missing CRUD/FLS checks, hardcoded sharing keywords, or SOQL inside loops. The Graph Engine takes static analysis further by performing path-sensitive dataflow analysis. It tracks user-controlled inputs (sources) to dangerous execution points (sinks) across multiple classes and methods. This helps to detect complex vulnerabilities like nested sharing bypasses and indirect injections that standard AST scanners miss.</p>
            <p>To pass automated scanning, developers must address all high-severity violations. When false positives occur, they must be documented in a detailed security web-scan explanation spreadsheet, justifying why a specific pattern is secure (e.g., using a custom sanitisation method). Standardising on this sanitisation and documenting it clearly is the only path to gaining approval for unconventional architectural designs. Let us look at a typical PMD scan violation: using dynamic SOQL queries with string concatenation. The scanner flags this as a potential SOQL injection. The remedy is to standardise on static queries or leverage dynamic bind variables.</p>"""
        ),
        (
            "s3",
            "3. Manual Penetration Testing: What the Security Team Probes",
            """<p>Automated scans are only the first gate. Once they pass, your application is handed to the Salesforce Security Review team for manual penetration testing. This team acts as ethical hackers, probing your implementation for flaws that static scanners cannot detect. They look for logical vulnerabilities, privilege escalation bypasses, and access control issues.</p>
            <p>Common manual attack vectors include privilege escalation, broken object-level authorisation, and session handling flaws. The review team will install your package in a test environment with multiple user profiles: a System Administrator, a Standard User, and a low-privilege Community User. They will attempt to bypass your UI controls by making direct API calls, manipulating network payloads, and modifying cookie parameters. They want to ensure that a user with restricted access cannot view, modify, or delete records they do not own or have not been explicitly granted access to.</p>
            <p>If a low-privilege user can access clinical data by altering an ID parameter in a URL (Insecure Direct Object Reference, or IDOR), the review fails immediately. The testers also evaluate the security of your connected apps, looking for weak OAuth flows, token storage vulnerabilities, and improper scope requests. If your app integrates with an external service, they will probe the external API endpoints using tools like OWASP ZAP and Burp Suite to test for SQL injection, CSRF, and session hijacking vulnerabilities. Understanding that the manual testers leave no stone unturned is essential for building a bulletproof application.</p>"""
        ),
        (
            "s4",
            "4. Defending Against Injection and Client-Side Vulnerabilities",
            """<p>Injection attacks remain a primary reason for security review failures. In Apex, SOQL injection occurs when user input is concatenated directly into a dynamic SOQL query. To prevent this, dynamic queries must use bind variables or the input must be explicitly typed or sanitised using <code>String.escapeSingleQuotes()</code>.</p>
            <p>In client-side components (Lightning Web Components or Visualforce), Cross-Site Scripting (XSS) is a major concern. Salesforce's Lightning Locker and Lightning Web Security (LWS) provide sandboxing, but developers can still introduce vulnerabilities by using <code>lwc:dom="manual"</code> or rendering raw HTML with <code>v-html</code> equivalents. Let us examine how to secure an Apex controller against SOQL injection:</p>
            <pre><code class="language-java">// VULNERABLE APEX CODE
public with sharing class VulnerableController {
    public List<Account> searchAccounts(String userInput) {
        // Vulnerable to SOQL Injection via user input manipulation
        String query = 'SELECT Id, Name FROM Account WHERE Name LIKE \\'%' + userInput + '%\\'';
        return Database.query(query);
    }
}

// SECURED APEX CODE
public class SecuredController {
    public List<Account> searchAccounts(String userInput) {
        // Secured using dynamic bind variables and explicit USER_MODE enforcement
        String query = 'SELECT Id, Name FROM Account WHERE Name LIKE :userInput';
        return Database.query(query, AccessLevel.USER_MODE);
    }
}</code></pre>
            <p>In Visualforce, output components automatically encode variables, but functions like <code>&lt;apex:outputText escape="false"&gt;</code> bypass this protection. Unless absolutely necessary, always let the platform escape output, or use programmatic sanitisation methods. When writing Lightning Web Components, adhere to the strict separation of concerns and avoid bypassing standard security boundaries. By customising and validating every user input before it reaches a DML or dynamic query sink, developers ensure their package meets the highest standard of security.</p>
            <p>Cross-Site Request Forgery (CSRF) is another critical attack vector evaluated during the review. CSRF occurs when a malicious website causes a user's web browser to perform an unwanted action on a trusted site where the user is currently authenticated. In Salesforce, built-in anti-CSRF tokens protect standard actions, but developers must ensure that custom integration endpoints and external pages also enforce state-verification tokens or utilise HTTP POST methods with strict body validation. Never perform DML actions or state changes in page-load initialization methods (such as Visualforce action methods) as these are highly vulnerable to CSRF manipulation.</p>"""
        ),
        (
            "s5",
            "5. Enforcing CRUD and FLS: Programmatic and Declarative Shielding",
            """<p>Unlike standard enterprise customisation where developers occasionally bypass security for system processes, AppExchange packages must strictly enforce Object-Level Security (CRUD) and Field-Level Security (FLS). If your package displays or modifies fields without verifying that the current user has permission to do so, it will fail the security review. This requirement is absolute and applies to all components of your package, including controllers, triggers, and APIs.</p>
            <p>Historically, developers had to write verbose checks using <code>Schema.DescribeSObjectResult</code> and <code>Schema.DescribeFieldResult</code>. While this is still acceptable, modern Apex provides elegant ways to enforce security:
            1. <code>WITH USER_MODE</code>: Appending <code>WITH USER_MODE</code> to SOQL queries or running DML operations in <code>USER_MODE</code> forces the platform to enforce CRUD, FLS, and sharing rules.
            2. <code>Security.stripInaccessible()</code>: This method filters out fields and objects that the user does not have permission to access, raising no exceptions but sanitising the data before it is rendered or updated.</p>
            <p>Let us see an example of modern CRUD/FLS enforcement using these modern paradigms:</p>
            <pre><code class="language-java">public class SecureDataService {
    // Enforcing security directly in the SOQL query using USER_MODE
    public List<Opportunity> getOpportunitiesInUserMode() {
        return [SELECT Id, Name, Amount, StageName 
                FROM Opportunity 
                WITH USER_MODE];
    }
    
    // Filtering inaccessible fields during DML operations
    public void updateOpportunityAmount(List<Opportunity> records) {
        SObjectAccessDecision decision = Security.stripInaccessible(
            AccessType.UPDATABLE, 
            records
        );
        
        // Update the sanitised records
        update decision.getRecords();
    }
}</code></pre>
            <p>By adopting <code>USER_MODE</code> and <code>Security.stripInaccessible</code>, you dramatically reduce the surface area for security review findings and ensure your application respects the customer's security settings. Remember, the review tests not only your code but also your behaviour in handling data access. Ensure that your testing processes validate these access controls across different user profiles to identify and resolve privilege escalation risks before submission. Optimising your security design in this manner guarantees a faster, smoother path through the AppExchange certification gates.</p>"""
        )
    ],
    'takeaway_bullets': [
        "The AppExchange Security Review evaluates the entire threat model of your offering, including external endpoints, APIs, and connected applications.",
        "Running the Salesforce Code Analyzer (SFCA) and resolving all high-severity violations is a mandatory pre-requisite for submission.",
        "Manual penetration testing by the Salesforce security team probes for logical flaws like IDOR, privilege escalation, and weak session handling.",
        "Injection vulnerabilities (SOQL Injection and XSS) must be eradicated by utilising dynamic bind variables, escaping single quotes, and avoiding escaping HTML output.",
        "AppExchange packages must strictly enforce CRUD and FLS using modern Apex features like USER_MODE and Security.stripInaccessible().",
        "External integrations must be secured through Named Credentials, strict Content Security Policies (CSP), and correct Cross-Origin Resource Sharing (CORS) configurations."
    ],
    'quiz_questions': [
        {
            'question': "Which automated analysis tool executes path-sensitive dataflow analysis to track user-controlled inputs to dangerous execution points?",
            'options': [
                "PMD Static Ruleset Engine",
                "Salesforce Code Analyzer Graph Engine",
                "Retire.js Dependency Scanner",
                "ESLint Syntax Validation Parser"
            ],
            'correct_index': 1
        },
        {
            'question': "What is the recommended modern approach to automatically enforce CRUD and FLS in an Apex SOQL query?",
            'options': [
                "Utilising 'with sharing' in the class definition header",
                "Looping through Schema.SObjectField describe results manual checks",
                "Appending 'WITH USER_MODE' to the end of the SOQL query statement",
                "Calling Database.setQueryLevel(QueryLevel.ENFORCE_ALL)"
            ],
            'correct_index': 2
        },
        {
            'question': "During manual penetration testing, how does the security review team evaluate data isolation boundaries?",
            'options': [
                "By reviewing the package's XML metadata configuration files statically",
                "By logging in as different profiles to attempt to access unauthorised record IDs",
                "By checking if the package utilises a custom namespace prefix",
                "By testing if the application supports standard Salesforce Single Sign-On"
            ],
            'correct_index': 1
        }
    ]
}

# ----------------- DATA PREPARATION FOR SEC-013 -----------------
sec013_data = {
    'summary_bullets': [
        "Demystify the legal frameworks of HIPAA and the HITECH Act within a multi-tenant cloud context.",
        "Define the limits and mutual obligations established by the Salesforce Business Associate Agreement (BAA).",
        "Implement Shield Platform Encryption using deterministic and probabilistic cryptographic strategies for PHI.",
        "Build Real-Time Event Monitoring transaction policies to detect and block unauthorised clinical data exports.",
        "Configure Field Audit Trail (FAT) to establish a compliant, immutable forensic change log for up to ten years.",
        "Harden external-facing Experience Cloud patient portals against access-control and data-exposure vulnerabilities."
    ],
    'body_sections': [
        (
            "s1",
            "1. HIPAA and HITECH on Salesforce: Regulatory Foundations and BAA Boundaries",
            """<p>For healthcare organisations operating in the United States, compliance with the Health Insurance Portability and Accountability Act (HIPAA) and the Health Information Technology for Economic and Clinical Health (HITECH) Act is a legal imperative. These regulations dictate how Protected Health Information (PHI) must be stored, processed, and transmitted. Failure to comply can result in severe financial penalties, reputational damage, and loss of clinical trust.</p>
            <p>Salesforce is fully capable of hosting HIPAA-compliant applications, but doing so requires strict adherence to administrative, physical, and technical safeguards. The foundational step for any healthcare organisation deploying Salesforce is signing a Business Associate Agreement (BAA) with Salesforce. This agreement establishes a legally binding contract that defines each party's regulatory obligations regarding the protection of sensitive medical data.</p>
            <p>The BAA is a legal contract that establishes Salesforce as a \"business associate\" of your healthcare organisation (the \"covered entity\"). By signing the BAA, Salesforce guarantees that its infrastructure meets the physical security and data integrity requirements of HIPAA. However, signing the BAA does not make your Salesforce implementation instantly compliant. It merely creates the legal framework under which you must configure the platform's security controls to protect PHI. Healthcare leaders must understand that compliance is an active, ongoing operational configuration process rather than a static procurement checkbox.</p>"""
        ),
        (
            "s2",
            "2. The Salesforce Shared Responsibility Model for Protected Health Information (PHI)",
            """<p>The cornerstone of cloud compliance is the Shared Responsibility Model. Under this framework, Salesforce guarantees the physical security of the data centres, hypervisor isolation, and the core platform infrastructure. Your organisation is responsible for how the platform is configured, who is granted access to the data, and how clinical processes are operationalised. This division of duties ensures that both the platform provider and the customer collaborate to maintain compliance.</p>
            <p>For instance, if a system administrator accidentally opens up sharing settings on the Patient object so that all external guest users can read patient medical records, this is a breach of HIPAA caused by the customer's configuration, not Salesforce's infrastructure. To maintain compliance, healthcare organisations must map their business processes to the technical controls provided by Salesforce. This involves classifying fields containing PHI, configuring restrictive role hierarchies, enforcing multi-factor authentication (MFA), and regularly auditing access logs.</p>
            <p>Establishing a comprehensive data classification scheme is a vital first step. Within Salesforce, fields should be tagged with metadata indicating their sensitivity (e.g., classifying a Field Usage as 'Active' and Data Sensitivity as 'Confidential' or 'PHI'). This structured labelling allows architects to apply targeted access controls, encryption, and monitoring rules to fields containing social security numbers, medical histories, or treatment plans. Regular reviews of this data mapping ensure that new custom fields are automatically captured within the organisation's security posture.</p>"""
        ),
        (
            "s3",
            "3. Architecting Shield Platform Encryption for Healthcare Data",
            """<p>Under HIPAA, data must be encrypted both in transit and at rest. Salesforce encrypts all data in transit using TLS 1.2 or higher. To encrypt data at rest, healthcare organisations must utilise Salesforce Shield Platform Encryption. This advanced security feature allows customers to encrypt sensitive fields, files, and attachments at the database level while preserving core platform functionalities like search, reports, and workflows.</p>
            <p>Unlike standard classic encryption, which only masks fields on the user interface, Shield Platform Encryption encrypts the data at the database level. When architecting Shield Platform Encryption, architects must select between two primary encryption strategies:
            1. <strong>Probabilistic Encryption</strong>: This method uses a unique initialisation vector for every record, meaning the same text will encrypt to different ciphertext each time. While highly secure, it blocks indexing, searching, and filtering on the encrypted fields.
            2. <strong>Deterministic Encryption</strong>: This method generates static ciphertext for a given plaintext, allowing developers to run SOQL queries, execute search indexes, and use the fields in reports.</p>
            <p>For PHI, deterministic encryption is widely preferred for key identifiers (like Medical Record Numbers or National Insurance Numbers) because it allows clinical coordinators to search for patients without exposing the data to unauthorised users. Let us see an Apex pattern that handles encrypted fields dynamically and securely:</p>
            <pre><code class="language-java">public class PatientDataService {
    public Patient__c findPatientByMRN(String mrn) {
        // Enforcing deterministic search query on encrypted field in user mode
        List<Patient__c> patients = [
            SELECT Id, First_Name__c, Last_Name__c, Medical_Record_Number__c, Medical_History__c 
            FROM Patient__c 
            WHERE Medical_Record_Number__c = :mrn
            WITH USER_MODE
        ];
        return patients.isEmpty() ? null : patients[0];
    }
}</code></pre>
            <p>Key Lifecycle Management is another critical aspect. Healthcare leaders must define policies for generating, rotating, and destroying tenant encryption keys. Under HIPAA, keys should be rotated at least annually, and older keys must be archived securely to allow decryption of legacy backups. Standardising these cryptographic procedures ensures that the organisation is prepared for compliance audits and can rapidly respond to potential key compromise scenarios.</p>"""
        ),
        (
            "s4",
            "4. Forensic Auditing with Field Audit Trail and Real-Time Event Monitoring",
            """<p>HIPAA requires covered entities to maintain detailed logs of who accessed clinical records and what modifications were made. The standard Salesforce history tracking only retains field changes for 18 months. To meet the rigorous auditing requirements of HIPAA (which often require up to 6 or even 10 years of audit history), organisations must implement Shield Field Audit Trail (FAT).</p>
            <p>FAT allows you to define custom metadata policies to retain history data for up to 10 years, archiving it to cold storage while keeping it queryable via the API. This provides a reliable, immutable forensic audit trail of all changes made to patient data. Healthcare organisations can use this historical record to demonstrate compliance during regulatory audits or internal investigations.</p>
            <p>In addition to tracking changes, healthcare organisations must monitor read access. If a user exports a report containing 10,000 patient records, this represents a massive security risk. Real-Time Event Monitoring allows you to construct transaction security policies that evaluate user behaviour in real time. If a user attempts to export data outside of normal working hours, or exceeds a specific record threshold, the policy can block the export, send an alert to the security team, or force a multi-factor challenge. Here is a conceptual Apex Transaction Security policy that checks for suspicious clinical data access:</p>
            <pre><code class="language-java">global class PatientDataExportControl implements TxnSecurity.EventCondition {
    public boolean evaluate(SObject event) {
        switch on event {
            when ReportEvent reportEvt {
                // If user attempts to export more than 200 patient records, trigger block
                if (reportEvt.Operation == 'Export' && reportEvt.RowsProcessed > 200) {
                    return true; // Block or challenge user
                }
            }
        }
        return false;
    }
}</code></pre>
            <p>Optimising these policies is critical to avoid disrupting clinical workflows. By customising parameters based on roles, locations, and time-windows, organisations can establish a secure environment that protects PHI without hindering the delivery of patient care.</p>"""
        ),
        (
            "s5",
            "5. Access Control and Hardening Portal Architectures for Patients",
            """<p>Modern healthcare organisations leverage Experience Cloud (formerly Communities) to build portals where patients can view medical records, message doctors, and schedule appointments. Portals represent a significant compliance risk because they expose your Salesforce org to external networks, making them a prime target for malicious actors.</p>
            <p>Architects must enforce strict data segregation in these portals. The primary rule is that guest users (unauthenticated visitors) must never have read or write access to PHI. Guest user sharing rules must be checked and locked down. For authenticated patients, access must be governed using User-Share mappings. High-Volume Customer Portal licences or Customer Community Plus licences should be configured with sharing sets or sharing groups that dynamically grant access only to records linked directly to the patient's Contact record.</p>
            <p>Furthermore, any APEX controllers backing these portals must enforce strict object-level and field-level security checks using <code>WITH USER_MODE</code> or programmatic schema validation to prevent privilege escalation or IDOR vulnerabilities. Regular penetration testing and vulnerability assessments of the portal interface should be conducted to ensure that external access vectors remain secure. Customising error messages to avoid disclosing system architecture and limiting API request rates are additional best practices for hardening patient portals against cyber threats.</p>"""
        )
    ],
    'takeaway_bullets': [
        "HIPAA compliance on Salesforce is a shared responsibility; the BAA covers infrastructure security, while you must secure your custom configuration.",
        "Shield Platform Encryption encrypts PHI at rest, and deterministic encryption should be utilised on fields requiring search, reports, or indexing.",
        "Key lifecycle management policies must be defined, including annual rotation of tenant encryption keys and secure archiving of legacy keys.",
        "Shield Field Audit Trail must be configured to retain history tracking data for up to ten years to comply with healthcare auditing regulations.",
        "Real-Time Event Monitoring transaction security policies should be deployed to detect, block, or challenge suspicious patient report exports.",
        "Experience Cloud patient portals must be hardened by enforcing strict sharing sets, disabling guest user PHI access, and validating all Apex inputs."
    ],
    'quiz_questions': [
        {
            'question': "What does signing a Business Associate Agreement (BAA) with Salesforce guarantee?",
            'options': [
                "That the customer's custom apex code is automatically secured and compliant",
                "That the physical and infrastructure layer of Salesforce meets HIPAA security standards",
                "That patient medical record fields are automatically encrypted with Shield Platform Encryption",
                "That Salesforce assumes all legal liability for any data breach or configuration exploit"
            ],
            'correct_index': 1
        },
        {
            'question': "Which encryption type should be used under Shield Platform Encryption for a Field like a Patient ID that users need to search for?",
            'options': [
                "Probabilistic Encryption",
                "Classic Masked Encryption",
                "Deterministic Encryption",
                "Standard Transport Layer Security"
            ],
            'correct_index': 2
        },
        {
            'question': "How can an architect prevent a standard call-centre agent from exporting massive volumes of patient data using event logs?",
            'options': [
                "By disabling the API access checkbox on all standard user profiles",
                "By writing a Real-Time Event Monitoring transaction security policy that evaluates ReportEvent parameters",
                "By customising the Role Hierarchy to place agents at the absolute bottom of the organization tree",
                "By configuring classic field history tracking to log data exports"
            ],
            'correct_index': 1
        }
    ]
}

# ----------------- DATA PREPARATION FOR SEC-014 -----------------
sec014_data = {
    'summary_bullets': [
        "Demystify SOC 2 Type I and Type II audits and their applications to custom Salesforce configurations.",
        "Map the AICPA Trust Services Criteria (Security, Confidentiality, Processing Integrity) directly to Salesforce settings.",
        "Enforce strict identity governance utilising Single Sign-On (SSO), Multi-Factor Authentication (MFA), and automated reviews.",
        "Establish secure Sandbox pipelines and auditable deployment workflows to satisfy change management requirements.",
        "Implement continuous monitoring and proactive logging using Setup Audit Trail and Event Monitoring.",
        "Vet and manage third-party AppExchange packages using secure lifecycle assessment frameworks."
    ],
    'body_sections': [
        (
            "s1",
            "1. Demystifying SOC 2 Audits for Salesforce Enterprise Implementations",
            """<p>Service Organisation Control (SOC) 2 is a voluntary compliance standard developed by the American Institute of CPAs (AICPA). It evaluates how technology companies manage customer data based on five Trust Services Criteria (TSC): Security, Availability, Processing Integrity, Confidentiality, and Privacy. For modern enterprise organisations, passing a SOC 2 audit is crucial for demonstrating operational credibility and secure data handling practices.</p>
            <p>While Salesforce itself maintains a robust SOC 2 Type II report for its physical infrastructure and managed services, this does not mean your custom Salesforce implementation is SOC 2 compliant. An auditor evaluating your organisation's compliance will review how you have configured, managed, and monitored Salesforce. The onus is on the customer to prove that their custom configurations do not introduce security loopholes.</p>
            <p>A SOC 2 Type I audit evaluates the design of your security controls at a single point in time, verifying that the appropriate policies are in place. A SOC 2 Type II audit, which is far more rigorous, evaluates the operational effectiveness of those controls over an extended period (typically six to twelve months). For enterprise architects, this means every policy, user access review, and metadata deployment must be consistently executed and meticulously documented. Developing a repeatable, automated compliance programme is the key to passing these audits with minimal friction.</p>"""
        ),
        (
            "s2",
            "2. Mapping Trust Services Criteria to Concrete Platform Configurations",
            """<p>To successfully pass a SOC 2 audit, architects must map the general Trust Services Criteria to specific Salesforce configurations. This mapping acts as the translation layer between high-level compliance goals and technical platform settings, making the audit process highly objective and transparent.</p>
            <p>Here is how the key Trust Services Criteria align with concrete Salesforce features:
            - <strong>Security</strong>: Hardening the perimeter. This includes enforcing Multi-Factor Authentication (MFA), setting restrictive login IP ranges, and configuring session timeouts to prevent unauthorised access.
            - <strong>Confidentiality</strong>: Ensuring sensitive data is restricted to authorised personnel. This is governed by Organization-Wide Defaults (OWD), Role Hierarchies, sharing rules, and Field-Level Security (FLS).
            - <strong>Processing Integrity</strong>: Ensuring system inputs produce accurate, reliable outputs. In Salesforce, this is controlled by validation rules, Apex triggers, automated regression testing, and robust error-handling mechanisms.</p>
            <p>By aligning your Salesforce configuration backlog with these criteria, you build a compliance-first architecture that naturally generates the evidence your auditors require. For example, setting up standard data validation rules and automated trigger tests proves to auditors that your system is designed to prevent data corruption. Regularly auditing these configurations ensuring they remain active and correctly tuned is a core responsibility of the architecture team.</p>"""
        ),
        (
            "s3",
            "3. User Access Governance: Hardening Authentication and Permission Set Hygiene",
            """<p>Identity and Access Management (IAM) is the first area auditors will scrutinise during a SOC 2 assessment. They will ask for evidence that you enforce the principle of least privilege, audit user access regularly, and securely manage high-privilege credentials.</p>
            <p>First, standardise on Single Sign-On (SSO) backed by an enterprise identity provider (like Okta or Azure AD). This allows you to centralise access termination. If an employee leaves the company, disabling their account in your identity provider must instantly revoke their Salesforce access. Second, enforce Multi-Factor Authentication (MFA). Salesforce mandates MFA, but your SSO configuration must also be verified to ensure MFA is required at the identity provider level.</p>
            <p>Third, eliminate the \"Admin Creep\" phenomenon. Having too many System Administrators is a major security risk. Restrict the System Administrator profile only to core platform owners. For everyone else, assign the standard \"Minimum Access - Salesforce\" profile and grant permissions incrementally using Permission Sets and Permission Set Groups. Let us see an administrative best practice: rather than granting the broad \"Modify All Data\" permission, write modular Apex or flow designs that execute system processes in system mode, keeping user permissions strictly defined:</p>
            <pre><code class="language-java">// SECURE PATTERN: Enforce least privilege by restricting user DML capabilities 
// and executing system-level actions strictly within controlled service classes
public class OrderProcessingService {
    public void processOrder(Id orderId) {
        // Step 1: Verify the current user has permission to read the Order
        List<Order> orders = [SELECT Id, Status FROM Order WHERE Id = :orderId WITH USER_MODE];
        if (orders.isEmpty()) {
            throw new SecurityException('Unauthorised access or invalid Order ID.');
        }
        
        // Step 2: Perform the privileged update in a system-controlled manner
        // without granting 'Modify All Data' to the user
        SystemOrderProcessor.markAsProcessed(orderId);
    }
    
    private without sharing class SystemOrderProcessor {
        private static void markAsProcessed(Id orderId) {
            Order o = new Order(Id = orderId, Status = 'Processed');
            update o;
        }
    }
}</code></pre>
            <p>Enforcing this separation of duties programmatic pattern ensures that standard users can perform necessary operations without requiring elevated platform permissions. Regularly review permission assignments and de-provision inactive users to maintain a clean security posture.</p>"""
        ),
        (
            "s4",
            "4. Secure Change Management: Sandboxes, Pipelines, and Auditable Deployments",
            """<p>Change management is the engine of SOC 2 compliance. Auditors want to verify that no developer can write code in a sandbox and push it directly to production without oversight. They seek to prevent unauthorised, untested, or malicious changes from entering your production environment.</p>
            <p>To satisfy this criterion, your organisation must implement a structured, auditable DevOps pipeline. The standard workflow dictates:
            1. <strong>Isolation</strong>: Development occurs in Developer or Developer Pro Sandboxes. No development is ever performed directly in Production.
            2. <strong>Testing</strong>: Code is merged into a Full or Partial Copy Sandbox (UAT/Staging) where business users perform user acceptance testing.
            3. <strong>Peer Review</strong>: Metadata changes are stored in a Git-based version control system. All merges into major branches must require peer review via Pull Requests.
            4. <strong>Automated Testing</strong>: CI/CD pipelines must execute all Apex tests and run static analysis tools (like PMD and ESLint) before deployment.
            5. <strong>Separation of Duties</strong>: The person who wrote the code must not be the person who authorises and executes the deployment to Production.</p>
            <p>Every deployment must be logged, showing a direct link between a business ticket (e.g., Jira), the pull request, and the deployment log. This end-to-end traceability proves to auditors that your production environment is strictly controlled. Avoid manual hotfixes in production at all costs; they bypass change management controls and represent a severe SOC 2 violation that is difficult to justify during an audit.</p>"""
        ),
        (
            "s5",
            "5. Continuous Monitoring, Incident Response, and Setup Audit Trail Forensics",
            """<p>A key aspect of SOC 2 Type II is continuous monitoring. You must be able to detect security incidents, policy violations, and administrative changes in real time, and demonstrate that your team responds to alerts swiftly and effectively.</p>
            <p>The <strong>Setup Audit Trail</strong> tracks administrative changes made in your Salesforce org. Auditors will routinely ask for logs from this trail to verify that no unauthorised metadata changes were made directly in Production. By regularly querying and reviewing these logs, you ensure the integrity of your system configuration. Let us look at how to monitor critical administrative changes using SOQL queries against the SetupAuditTrail object:</p>
            <pre><code class="language-java">public class SetupAuditMonitor {
    public List<SetupAuditTrail> getRecentCriticalChanges() {
        // Query Setup Audit Trail to log critical administrative actions
        return [
            SELECT Id, Action, Section, CreatedBy.Username, CreatedDate, Display 
            FROM SetupAuditTrail 
            WHERE Action IN ('manageIpRanges', 'passwordPolicyUpdated', 'securitySettingsUpdated')
            ORDER BY CreatedDate DESC 
            LIMIT 50
        ];
    }
}</code></pre>
            <p>Additionally, you should implement <strong>Event Monitoring</strong> to capture system-level logs, such as API usage, login history, and report exports. These logs should be streamed to an enterprise Security Information and Event Management (SIEM) system (like Splunk or Datadog) where they can be correlated with other enterprise logs. If an incident occurs (such as an administrative account being compromised), your Incident Response Plan must detail the exact steps to isolate the org, rotate integration secrets, terminate active sessions, and restore data integrity. Documenting this incident response loop is essential for demonstrating operational resilience to your SOC 2 auditors.</p>"""
        )
    ],
    'takeaway_bullets': [
        "Salesforce's infrastructure SOC 2 report does not cover your custom implementation; you must prove your configurations and processes are compliant.",
        "The Trust Services Criteria (Security, Confidentiality, Processing Integrity) must be mapped to native Salesforce settings like OWDs, MFA, and Validation Rules.",
        "Enforce strict least privilege by using SSO, MFA, de-provisioning inactive users, and replacing administrative profile access with Permission Sets.",
        "Change management audits require a strict, sandbox-isolated DevOps pipeline with peer reviews, automated CI/CD testing, and separation of duties.",
        "Setup Audit Trail and Event Monitoring must be utilised to continuously log administrative changes and track potential data exfiltration vectors.",
        "Production hotfixes should be strictly forbidden, ensuring all metadata alterations go through the approved, auditable deployment pipeline."
    ],
    'quiz_questions': [
        {
            'question': "What is the difference between a SOC 2 Type I and a SOC 2 Type II audit?",
            'options': [
                "Type I evaluates security at a single point in time, while Type II evaluates operational effectiveness over a period of months",
                "Type I evaluates physical infrastructure, while Type II evaluates application software configuration security",
                "Type I is mandatory for cloud software providers, while Type II is completely optional and self-assessed",
                "Type I is performed by internal security staff, while Type II must be performed by the AICPA Board of CPAs"
            ],
            'correct_index': 0
        },
        {
            'question': "To enforce the SOC 2 principle of least privilege, what is the best practice for granting elevated user permissions?",
            'options': [
                "Creating multiple custom administrator profiles and assigning them to different departments",
                "Utilising the Minimum Access profile and assigning modular Permission Sets dynamically",
                "Enabling 'Modify All Data' on standard profiles to simplify workflow processes",
                "Allowing developers to temporarily use production login access to execute system changes"
            ],
            'correct_index': 1
        },
        {
            'question': "How can an architect prove to a SOC 2 auditor that only authorised changes have been deployed to production?",
            'options': [
                "By showing that all developers have access to the production system settings",
                "By providing a verbal confirmation that the team follows agile scrum principles",
                "By presenting a Git change-log showing code reviews, CI/CD runs, and linked business tracking tickets",
                "By running a monthly backup of the production database metadata"
            ],
            'correct_index': 2
        }
    ]
}

# ----------------- DATA PREPARATION FOR SEC-015 -----------------
sec015_data = {
    'summary_bullets': [
        "Analyse the dual mechanics of the Role Hierarchy: security enforcement versus data aggregation.",
        "Delineate how role updates trigger extensive background sharing recalculations and lock sharing tables.",
        "Address large data volume (LDV) risks including ownership skew and locking bottlenecks.",
        "Implement architectural design rules to reduce role counts and isolate partner portal users.",
        "Evaluate alternative sharing mechanisms including Public Groups, Territory Management, and Team Sharing.",
        "Configure collaborative forecasting and reporting boundaries without expanding the role structure."
    ],
    'body_sections': [
        (
            "s1",
            "1. The Dual Imperatives of Role Hierarchy: Security versus Analytics",
            """<p>The Salesforce Role Hierarchy is one of the most powerful declarative security features on the platform. It automatically escalates record access to users who sit above record owners in the hierarchy. For example, if a sales representative owns a lead, their manager automatically inherits read/write access to that lead, assuming standard Grant Access Using Hierarchies is enabled on that sObject.</p>
            <p>However, organisations frequently fall into the trap of using the Role Hierarchy for two incompatible purposes: strict data security enforcement and analytical reporting or management reporting. Business leaders often assume that because a manager needs to view a report on a team's activity, that manager's team must sit directly below them in the security hierarchy. This is a critical misconception.</p>
            <p>An organisation chart is rarely a good model for a role hierarchy. Business management maps reporting structures, while security architects map data visibility. If you design your role hierarchy to mirror your entire organisational chart, you will end up with a highly complex, deep, and fragile tree that degrades system performance and creates administrative nightmares. By customising the hierarchy to focus solely on data visibility boundaries, architects can maintain a clean, high-performing platform that supports both security and analytics.</p>"""
        ),
        (
            "s2",
            "2. Behind the Scenes: How Role Modifications Trigger Sharing Recalculations",
            """<p>To understand why complex role hierarchies degrade performance, we must look at Salesforce's underlying database mechanics. The platform operates on a multi-tenant architecture where data must be isolated and partitioned efficiently at scale. When security rules are modified, the system performs extensive database recalculations in the background.</p>
            <p>Salesforce stores record visibility in a hidden table called the <strong>Object Sharing Table</strong> (e.g., <code>AccountShare</code> or <code>OpportunityShare</code>). When a user owns a record or is granted access via sharing rules, Salesforce writes rows to this table. The system also maintains a <strong>Group Membership Table</strong>, which records who belongs to what public groups, roles, and territories.</p>
            <p>When you modify the role hierarchy (e.g., moving a role from one branch to another, or changing a user's role), Salesforce must recalculate the entire sharing tree. If your hierarchy is deep and contains hundreds of roles and millions of records, a single role change can trigger an extensive background sharing recalculation. This recalculates group memberships, updates sharing rows, and locks the sharing tables. This locking behaviour can cause UI freezes, API timeouts, and failed integrations, highlighting the need for flat, streamlined role structures.</p>"""
        ),
        (
            "s3",
            "3. Ownership Skew and Large Data Volumes: Avoiding Architectural Pitfalls",
            """<p>In large-scale implementations containing Large Data Volumes (LDV), improper role assignment can lead to critical performance bottlenecks known as <strong>Ownership Skew</strong>. This is one of the most severe performance bottlenecks in enterprise Salesforce deployments.</p>
            <p>Ownership Skew occurs when a single user (or a small group of users) owns more than 10,000 records of a specific sObject type. If that owner is placed in a role that sits high in the role hierarchy, or is shifted within the hierarchy, Salesforce must recalculate sharing for all those records. This recalculation can take hours and lock system tables, preventing other users from creating or modifying records. Let us see an Apex pattern that highlights how programmatic inserts can dynamically route record ownership to avoid skew:</p>
            <pre><code class="language-java">public class RecordOwnerAssignment {
    // Dynamically assign record owner to a system user with a flat role to prevent ownership skew
    public void assignSafeOwner(List<Account> accounts, Id safeSystemUserId) {
        for (Account acc : accounts) {
            acc.OwnerId = safeSystemUserId;
        }
        // Save records using modern DML enforcement and explicit user mode
        Database.insert(accounts, AccessLevel.USER_MODE);
    }
}</code></pre>
            <p>To prevent ownership skew, organisations must implement the following design rules:
            1. <strong>Assign Skewed Owners to Roles at the Bottom</strong>: If a system user or integration user must own a massive volume of records, do not assign them a role, or place them in a role at the absolute bottom of the hierarchy that has no children.
            2. <strong>Avoid High-Level Ownership</strong>: Ensure high-level executives or managers do not directly own data; let the data be owned by operations staff or integration accounts, and escalated via sharing rules. This keeps the top of your hierarchy extremely light and agile.</p>"""
        ),
        (
            "s4",
            "4. Architectural Strategy: Minimising Roles and Separating Portals",
            """<p>The golden rule of Role Hierarchy design is: <strong>Keep it as flat and simple as possible</strong>. Architects should challenge the creation of any new role, ensuring that alternate security controls are exhausted before adding complexity to the tree.</p>
            <p>Architects should challenge the creation of any new role. Instead of creating distinct roles for every department and team (e.g., \"North London Junior Account Executive\"), standardise on broader roles (e.g., \"UK Sales Rep\") and differentiate access using Permission Sets and public groups. This reduces the number of nodes in the sharing tree and dramatically optimises recalculation speeds.</p>
            <p>Additionally, you must separate internal employee hierarchies from external portal or partner hierarchies. External portal users (Experience Cloud) can generate thousands of roles if Partner Super User or Account Role options are not carefully managed. To prevent portal roles from clogging your internal sharing engine, implement <strong>User Role Limitation</strong> settings and utilise <strong>Sharing Sets</strong> or <strong>Share Groups</strong>. Sharing Sets completely bypass the role hierarchy for high-volume customer community licences, routing access through efficient lookup relations instead of database sharing tables.</p>"""
        ),
        (
            "s5",
            "5. Alternative Access Controls: Enforcing Reporting and Forecasting Segregation",
            """<p>If we cannot use the Role Hierarchy to structure our analytical reporting, how do we support managers who need to view reports and forecasts for their teams? Salesforce provides several robust, native features designed to solve this exact problem without adding burden to the sharing calculations engine.</p>
            <p>Salesforce provides excellent alternative mechanisms that do not rely on the Role Hierarchy:
            - <strong>Collaborative Forecasting</strong>: This tool uses a separate forecasting hierarchy. You can structure your forecasting tree to match your management chart while keeping the security role hierarchy flat and efficient.
            - <strong>Enterprise Territory Management (ETM)</strong>: ETM allows you to model complex, multi-dimensional sales structures (by region, product, and industry) separate from the role hierarchy. Record access and reporting are determined by territory membership, leaving your role hierarchy streamlined.
            - <strong>Public Groups and Team Sharing</strong>: To grant horizontal visibility across teams, use Account Teams, Opportunity Teams, or manual sharing rules backed by public groups, rather than moving users up and down the role hierarchy.</p>
            <p>By decoupling reporting from visibility, you build a high-performance, compliant, and scalable Salesforce architecture. Standardising on these alternative patterns ensures that your platform can scale smoothly to support millions of records and thousands of users without experiencing sharing calculations bottlenecks. Customise your architecture to prioritise these flat designs, and you will minimise the administrative overhead of managing the system.</p>"""
        )
    ],
    'takeaway_bullets': [
        "The Role Hierarchy should be architected to enforce data visibility boundaries rather than mirroring the corporate org chart.",
        "Role modifications trigger background group membership recalculations that lock sharing tables and can cause system timeouts.",
        "Ownership skew (one user owning >10,000 records) must be avoided, especially for users placed high in the role hierarchy.",
        "Keep the role hierarchy flat by standardising on broad roles and using Permission Sets or Public Groups for granular access.",
        "Separate internal hierarchies from external portal hierarchies, and utilise Sharing Sets to bypass portal role generation completely.",
        "Leverage Collaborative Forecasting and Enterprise Territory Management to satisfy complex reporting needs without expanding roles."
    ],
    'quiz_questions': [
        {
            'question': "What is the primary technical issue triggered by moving a highly-populated role in a deep hierarchy?",
            'options': [
                "Salesforce automatically logs out all active users assigned to that role",
                "Extensive database recalculation locks sharing tables and may cause timeouts",
                "The system automatically deletes all custom validation rules on the affected sObjects",
                "The metadata API rejects any future packages containing that role name"
            ],
            'correct_index': 1
        },
        {
            'question': "To prevent performance locking during sharing recalculations, what is the best practice for integration user roles?",
            'options': [
                "Assigning the integration user to the highest role in the executive hierarchy",
                "Placing the integration user in a role at the absolute bottom of the tree, or assigning no role",
                "Assigning the integration user to a new custom role for every integration service",
                "Enabling 'Grant Access Using Hierarchies' on all integration objects"
            ],
            'correct_index': 1
        },
        {
            'question': "Which Salesforce feature allows you to model complex sales structures for reporting and access separate from the Role Hierarchy?",
            'options': [
                "Enterprise Territory Management (ETM)",
                "Custom Metadata Types and validation logic",
                "Visualforce page action controllers",
                "Object Sharing Rules using public groups"
            ],
            'correct_index': 0
        }
    ]
}

# ----------------- EXECUTE UPDATES -----------------
print("----------------- UPDATING SEC-012 -----------------")
update_file('sec-012', sec012_data)

print("\n----------------- UPDATING SEC-013 -----------------")
update_file('sec-013', sec013_data)

print("\n----------------- UPDATING SEC-014 -----------------")
update_file('sec-014', sec014_data)

print("\n----------------- UPDATING SEC-015 -----------------")
update_file('sec-015', sec015_data)

print("\n----------------- RUNNING VALIDATION INTERNALLY -----------------")
import importlib.util

spec = importlib.util.spec_from_file_location("validate_sec_tutorials", os.path.join(WORKSPACE_DIR, "scratch", "validate_sec_tutorials.py"))
validate_module = importlib.util.module_from_spec(spec)
sys.modules["validate_sec_tutorials"] = validate_module
spec.loader.exec_module(validate_module)

all_ok = True
results_log = []

for slug in ['sec-012', 'sec-013', 'sec-014', 'sec-015']:
    validator = validate_module.TutorialValidator(slug)
    success = validator.validate()
    status = "PASS" if success else "FAIL"
    log_msg = f"[{status}] {slug}"
    print(log_msg)
    results_log.append(log_msg)
    if validator.errors:
        all_ok = False
        for err in validator.errors:
            err_msg = f"   ↳ ERROR: {err}"
            print(err_msg)
            results_log.append(err_msg)
    if validator.warnings:
        for warn in validator.warnings:
            warn_msg = f"   ↳ WARNING: {warn}"
            print(warn_msg)
            results_log.append(warn_msg)

log_path = os.path.join(WORKSPACE_DIR, "scratch", "validation_results.txt")
with open(log_path, 'w', encoding='utf-8') as lf:
    lf.write("\n".join(results_log))

print(f"\nWritten validation logs to: {log_path}")
if all_ok:
    print("SUCCESS: ALL 4 DIRECTORIES ARE STRUCTURALLY PERFECT AND PASS!")
else:
    print("WARNING/FAILURES FOUND, PLEASE CHECK LOG FILE!")
sys.exit(0 if all_ok else 1)
