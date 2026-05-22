# -*- coding: utf-8 -*-
import os
import re
import sys

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIALS_DIR = os.path.join(WORKSPACE_DIR, 'tutorials')

# SEC-002 Content: GDPR Compliance in Salesforce
sec_002_summary = """
<li>Implementing the Right to be Forgotten (Erasure) and Right to Portability at a database level.</li>
<li>Configuring the Individual object and Consent Management API to capture granular data processing preferences.</li>
<li>Using Apex and Flow to automate data masking, anonymisation, and hard deletion.</li>
<li>Setting up Restricted Processing controls to lock down records during dispute periods.</li>
<li>Constructing automated compliance auditing dashboards and event logs.</li>
"""

sec_002_toc = """
<li><a href="#s1">Consent Management and the Individual Object</a></li>
<li><a href="#s2">Implementing the Right to Erasure (Anonymisation vs Hard Deletion)</a></li>
<li><a href="#s3">Restricting Data Processing and Portability Workflows</a></li>
<li><a href="#s4">Automating GDPR Audits and Compliance Dashboards</a></li>
<li><a href="#s5">Architectural Governance and Data Lifecycle Control</a></li>
"""

sec_002_body = """
<h2 id="s1">Consent Management and the Individual Object</h2>
<p>
Under the General Data Protection Regulation (GDPR), organisations are strictly required to manage data subjects' consent with a high degree of granularity. In Salesforce, treating consent as a simple checkbox on the Contact or Lead record is no longer sufficient or compliant. Standardising on the standard <code>Individual</code> object represents the architectural gold standard for consent management. The <code>Individual</code> object acts as a central repository for privacy preferences, decoupled from the specific communication channels (Lead, Contact, User, or Person Account), thereby enabling a unified and compliant view of data subject desires.
</p>
<p>
The <code>Individual</code> object stores critical consent flags such as <code>SendIndividualRequests</code>, <code>ShouldForget</code>, <code>HasOptedOutSolicit</code>, and <code>HasOptedOutTracking</code>. To establish a robust architecture, you must establish a 1:1 lookup relationship between the Contact/Lead and the <code>Individual</code> record. When a new prospect or customer is created, a trigger or flow should automatically instantiate a corresponding <code>Individual</code> record if one does not already exist. This process ensures that privacy settings are synchronised across all touchpoints, preventing accidental communication that violates the subject's stated preferences.
</p>
<p>
Here is an Apex trigger handler pattern that illustrates how to programmatically enforce this alignment and ensure every Contact has a corresponding <code>Individual</code> record:
</p>
<pre><code class="language-java">
public class ContactIndividualSyncHandler {
    public static void ensureIndividualRecords(List&lt;Contact&gt; contacts) {
        List&lt;Contact&gt; contactsNeedIndividual = new List&lt;Contact&gt;();
        for (Contact c : contacts) {
            if (c.IndividualId == null) {
                contactsNeedIndividual.add(c);
            }
        }
        
        if (contactsNeedIndividual.isEmpty()) {
            return;
        }
        
        List&lt;Individual&gt; individualsToCreate = new List&lt;Individual&gt;();
        for (Contact c : contactsNeedIndividual) {
            individualsToCreate.add(new Individual(
                FirstName = c.FirstName,
                LastName = c.LastName,
                EmailAddress = c.Email,
                SendIndividualRequests = true
            ));
        }
        
        insert individualsToCreate;
        
        for (Integer i = 0; i &lt; contactsNeedIndividual.size(); i++) {
            contactsNeedIndividual[i].IndividualId = individualsToCreate[i].Id;
        }
    }
}
</code></pre>
<p>
By utilising this centralised approach, any privacy preference update made to the <code>Individual</code> record is immediately inherited by the associated Contact, Lead, or User. This architecture mitigates the compliance risk associated with disjointed, siloed consent checkboxes across different functional areas of the Salesforce platform.
</p>

<h2 id="s2">Implementing the Right to Erasure (Anonymisation vs Hard Deletion)</h2>
<p>
GDPR Article 17 defines the "Right to Erasure" (commonly known as the Right to be Forgotten). When an individual exercises this right, organisations must delete or obfuscate their personal data without undue delay. In Salesforce, executing a hard database delete (via the <code>hardDelete()</code> API method or standard Apex <code>delete</code>) presents significant technical and analytical challenges. Hard deletion cascades to child records, orphans historic activity histories, and breaks key relational constraints. Crucially, it completely destroys historical aggregate metrics, leaving the organisation unable to perform accurate revenue attribution or trend analysis.
</p>
<p>
To resolve this, architects must design an anonymisation framework that obfuscates personally identifiable information (PII) while preserving the non-identifiable, transactional record structure for analytical purposes. For example, replacing a Contact's name with "Anonymised Subject", clearing their phone number, and resetting their email address to a dummy domain (such as <code>forgotten@anonymised.sfvedas.com</code>) allows the business to retain the integrity of sales pipelines and historical dashboards.
</p>
<p>
An anonymisation service must run asynchronously to avoid hitting transaction governors and limits, particularly when child records and history tables must also be cleaned. The following <code>Queueable</code> Apex pattern demonstrates how to safely perform mass obfuscation of data subject records:
</p>
<pre><code class="language-java">
public class GDPRAnonymisationService implements Queueable {
    private List&lt;Id&gt; contactIds;
    
    public GDPRAnonymisationService(List&lt;Id&gt; contactIds) {
        this.contactIds = contactIds;
    }
    
    public void execute(QueueableContext context) {
        List&lt;Contact&gt; contactsToAnonymise = [
            SELECT Id, FirstName, LastName, Email, Phone, MobilePhone, MailingStreet, MailingCity, IndividualId 
            FROM Contact 
            WHERE Id IN :contactIds
        ];
        
        List&lt;Individual&gt; individualsToForget = new List&lt;Individual&gt;();
        
        for (Contact c : contactsToAnonymise) {
            c.FirstName = 'Forgotten';
            c.LastName = 'Individual';
            c.Email = 'forgotten-' + c.Id + '@anonymised.sfvedas.com';
            c.Phone = null;
            c.MobilePhone = null;
            c.MailingStreet = null;
            c.MailingCity = null;
            
            if (c.IndividualId != null) {
                individualsToForget.add(new Individual(
                    Id = c.IndividualId,
                    ShouldForget = true,
                    LastName = 'Forgotten'
                ));
            }
        }
        
        update contactsToAnonymise;
        if (!individualsToForget.isEmpty()) {
            update individualsToForget;
        }
    }
}
</code></pre>
<p>
This Queueable pattern represents a safe, scalable method to meet the Right to Erasure. It minimises the footprint of PII while preserving the record's underlying ID structure, ensuring that your reports, financial summaries, and security tracking remain accurate and consistent.
</p>

<h2 id="s3">Restricting Data Processing and Portability Workflows</h2>
<p>
GDPR Article 18 grants data subjects the right to restrict the processing of their personal data under specific circumstances, such as during a dispute over data accuracy. When processing is restricted, the data can only be stored; it cannot be modified, shared with external integrations, or used in marketing campaigns.
</p>
<p>
Architecturally, enforcing this requires a dynamic locking mechanism. A standard practice is to deploy a custom flag on the Contact or <code>Individual</code> object, such as <code>Is_Processing_Restricted__c</code>. This flag must be evaluated by every downstream process, including Apex triggers, Flow builders, integration middleware, and marketing automation connectors (like Marketing Cloud or Pardot).
</p>
<p>
For user-facing interactions, you can enforce this restriction using declarative Salesforce validation rules that prevent any modifications to records under active restriction:
</p>
<pre><code class="language-java">
AND(
    OR(
        ISCHANGED(FirstName),
        ISCHANGED(LastName),
        ISCHANGED(Email),
        ISCHANGED(Phone)
    ),
    Individual.Is_Processing_Restricted__c = TRUE
)
</code></pre>
<p>
Additionally, GDPR Article 20 mandates the Right to Data Portability, requiring organisations to provide data subjects with their personal data in a structured, commonly used, and machine-readable format. The architectural response to this is to construct an API-driven extraction tool that compiles a data subject's record graph into a standardized JSON payload. The following Apex method demonstrates how to query a Contact's graph and return a structured JSON response suitable for direct delivery to the data subject:
</p>
<pre><code class="language-java">
public class GDPRPortabilityExporter {
    public static String exportDataSubjectGraph(Id contactId) {
        Contact contactData = [
            SELECT Id, FirstName, LastName, Email, Phone,
                (SELECT Id, Subject, Status FROM Cases),
                (SELECT Id, ActivityDate, Subject FROM ActivityHistories)
            FROM Contact 
            WHERE Id = :contactId
        ];
        
        Map&lt;String, Object&gt; exportPayload = new Map&lt;String, Object&gt;();
        exportPayload.put('subject_id', contactData.Id);
        exportPayload.put('first_name', contactData.FirstName);
        exportPayload.put('last_name', contactData.LastName);
        exportPayload.put('email', contactData.Email);
        exportPayload.put('phone', contactData.Phone);
        
        List&lt;Map&lt;String, Object&gt;&gt; cases = new List&lt;Map&lt;String, Object&gt;&gt;();
        for (Case c : contactData.Cases) {
            cases.add(new Map&lt;String, Object&gt;{
                'case_id' =&gt; c.Id,
                'subject' =&gt; c.Subject,
                'status' =&gt; c.Status
            });
        }
        exportPayload.put('cases', cases);
        
        return JSON.serializePretty(exportPayload);
    }
}
</code></pre>
<p>
By implementing this automated export capability, your organisation can fulfill portability requests rapidly and programmatically, reducing administrative overhead and eliminating manual database extraction efforts.
</p>

<h2 id="s4">Automating GDPR Audits and Compliance Dashboards</h2>
<p>
Fulfilling GDPR obligations requires absolute transparency. Under Article 30, organisations must maintain a record of processing activities, and they must be prepared to prove compliance to supervisory authorities at any moment. In Salesforce, this audit capability is achieved by combining three distinct native layers: Field History Tracking, Shield Field Audit Trail, and Real-Time Event Monitoring.
</p>
<p>
Field History Tracking captures the "who, when, and what" of field-level modifications. However, standard tracking is limited to 20 fields per object and a retention period of 18 months. For high-volume enterprise architectures, this is insufficient. Implementing Salesforce Shield Field Audit Trail allows you to track up to 60 fields per object and retain that audit history in big objects for up to ten years, meeting the stringent retention requirements of national regulatory bodies.
</p>
<p>
To demonstrate compliance programmatically, you should deploy automated batch classes that sweep audit histories and flag compliance gaps—such as PII fields that are modified without an associated Consent record. The following SOQL pattern demonstrates how to programmatically query audit history tables to identify modifications to sensitive data fields:
</p>
<pre><code class="language-sql">
SELECT ParentId, OldValue, NewValue, Field, CreatedById, CreatedDate 
FROM ContactHistory 
WHERE Field IN ('Email', 'Phone', 'MailingStreet') 
ORDER BY CreatedDate DESC 
LIMIT 500
</code></pre>
<p>
These raw histories can then be aggregated into central compliance dashboards. DPOs (Data Protection Officers) can monitor key risk indicators, such as the volume of anonymisation requests processed, the percentage of restricted records, and any unauthorised changes to opt-out statuses.
</p>

<h2 id="s5">Architectural Governance and Data Lifecycle Control</h2>
<p>
The final pillar of a GDPR-compliant Salesforce ecosystem is robust data lifecycle governance. Compliance is not merely a production database concern; it must extend to your entire sandbox development pipeline. When copy paste operations or refresh tasks copy production data into Dev or Full Copy sandboxes, sensitive PII is exposed to developers, QA testers, and third-party contractors. This represents a critical compliance violation.
</p>
<p>
To mitigate this risk, you must deploy <code>Salesforce Data Mask</code> as a standard component of your sandbox creation process. Data Mask automatically obfuscates, anonymises, or deletes PII in sandboxes, ensuring that testing and development are performed using realistic but synthetically generated data.
</p>
<p>
Furthermore, standardise your data retention policies using automated data deletion pipelines. Establish hard limits on how long inactive Leads or closed Cases are stored. By purging stale data programmatically, you minimise your data footprint and limit the impact of any potential security breach. In summary, GDPR compliance requires a proactive, secure-by-design approach. By implementing centralised consent management, scalable asynchronous anonymisation, strict record locking, automated JSON portability exports, and comprehensive sandbox masking, your organisation can confidently satisfy European regulations while maintaining high-performing CRM systems.
</p>
"""

sec_002_takeaways = """
<li>Leverage the standard Individual object as the central, single source of truth for user consent across all objects.</li>
<li>Avoid database integrity and analytical reporting breaks by choosing data anonymisation over hard record deletions.</li>
<li>Use asynchronous Queueable Apex for anonymisation to prevent governor limit issues when processing large volumes.</li>
<li>Implement dynamic validation rules and trigger logic tied to an Is_Processing_Restricted__c flag to restrict data processing.</li>
<li>Create structured JSON payloads programmatically to support the Right to Data Portability under Article 20.</li>
<li>Obfuscate PII in sandboxes using Salesforce Data Mask to maintain regulatory compliance throughout the development lifecycle.</li>
"""

sec_002_quiz = """
<div class="quiz-question" id="q1">
  <p><strong>Question 1:</strong> What is the primary benefit of record anonymisation over hard deletion under GDPR in Salesforce?</p>
  <div class="quiz-option" onclick="answer(this, 'q1', 'right')">A. Preserving relational integrity and historical aggregate reporting metrics.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. Decreasing the overall storage space immediately inside the org.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">C. Automatically updating third-party integrations via Outbound Messages.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Bypassing the need to notify the Data Protection Officer.</div>
</div>

<div class="quiz-question" id="q2">
  <p><strong>Question 2:</strong> Which standard object is designed specifically to store consent preferences and link to Leads, Contacts, and Users?</p>
  <div class="quiz-option" onclick="answer(this, 'q2', 'right')">A. Individual</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">B. Account</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. ConsentHeader</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. PrivacySetting</div>
</div>

<div class="quiz-question" id="q3">
  <p><strong>Question 3:</strong> How should Article 18 (Restriction of Processing) be technically implemented for a Contact record in Salesforce?</p>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. By deleting the record immediately from the active database.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'right')">B. Implementing a flag like Is_Restricted__c and enforcing it via Validation Rules, Apex triggers, and Sharing Rules.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. Revoking the Salesforce licence of the user who owns the record.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Moving the Contact to a custom big object archive table.</div>
</div>
"""

# SEC-003 Content: Salesforce Shield
sec_003_summary = """
<li>Designing a robust encryption strategy using Shield Platform Encryption (Deterministic vs Probabilistic).</li>
<li>Structuring Tenant Secret management, rotation cycles, and key derivation processes.</li>
<li>Capturing, analysing, and acting upon real-time security events using Real-Time Event Monitoring.</li>
<li>Implementing Field Audit Trail (FAT) to enforce a 10-year audit history retention policy.</li>
<li>Overcoming technical limitations, indexing challenges, and performance impacts of Shield.</li>
"""

sec_003_toc = """
<li><a href="#s1">Shield Platform Encryption Architecture (Probabilistic vs Deterministic)</a></li>
<li><a href="#s2">Secret Management, Rotation, and Key Derivation</a></li>
<li><a href="#s3">Real-Time Event Monitoring and Threat Detection</a></li>
<li><a href="#s4">Field Audit Trail (FAT) and Historical Data Archival</a></li>
<li><a href="#s5">Performance Optimisation and Technical Limitations of Shield</a></li>
"""

sec_003_body = """
<h2 id="s1">Shield Platform Encryption Architecture (Probabilistic vs Deterministic)</h2>
<p>
Salesforce Shield Platform Encryption provides enterprise-grade data encryption at rest while maintaining critical CRM functionalities. The foundation of this system relies on a two-tier key architecture consisting of a Master Secret managed by Salesforce and a Tenant Secret managed by the customer. When these secrets are combined, the application server generates a unique Data Encryption Key (DEK) locally to encrypt and decrypt fields on the fly using standard AES-256 encryption.
</p>
<p>
Architects must choose between two encryption schemes: Probabilistic and Deterministic. Probabilistic encryption is the most secure option. It generates completely different, random ciphertext every single time the same plaintext is encrypted. For instance, if you encrypt the word "Vedas" twice, the resulting ciphertexts will not match. While highly secure, this method prevents users from filtering, searching, or grouping by this field in SOQL queries, since the database cannot perform match operations on dynamic ciphertext.
</p>
<p>
To support standard search and filtering requirements, Salesforce introduced Deterministic encryption. With Deterministic encryption, the same plaintext always yields the identical ciphertext (e.g. "Vedas" always encrypts to "Xy78z"). This allows exact match filtering in WHERE clauses, index structures, and report filters. Within Deterministic encryption, you must choose between <code>Case-Sensitive</code> (requires precise case matching) and <code>Case-Insensitive</code> (converts text to lowercase prior to encryption) schemes.
</p>
<p>
When designing schemas, probabilistic encryption should be utilised for highly sensitive fields that do not require search filtering (such as Credit Card Numbers or Social Security Numbers). Conversely, deterministic encryption is suited for fields like Email Address or Account Name that are regularly queried.
</p>

<h2 id="s2">Secret Management, Rotation, and Key Derivation</h2>
<p>
Securing and managing encryption keys is a critical governance requirement. Salesforce Shield employs a secure, hardware-based key derivation process. The tenant secret is generated using a secure Hardware Security Module (HSM) on demand. Architects can choose to have Salesforce generate this secret, or they can opt for a "Bring Your Own Key" (BYOK) architecture, where the tenant secret is generated in their own external cloud key manager (such as AWS KMS) and uploaded securely to Salesforce.
</p>
<p>
To maintain standard compliance, organizations must establish a routine rotation cycle for tenant secrets. Rotating a secret changes the active key used for encrypting new data. Crucially, legacy archived data remains encrypted with the old archived secrets. If you rotate your tenant secret, historical data is not automatically re-encrypted. The legacy keys must remain stored in an archived state within the org to allow decryption on the fly, unless you trigger a full data sync to rewrite and re-encrypt historical records.
</p>
<p>
Managing tenant secrets programmatically can be achieved via the Tooling API. The following metadata pattern outlines the logical structure of a TenantSecret representation in Salesforce:
</p>
<pre><code class="language-java">
// Conceptual representation of querying Tenant Secret metadata for compliance auditing
public class TenantKeyAuditService {
    public static void logActiveSecrets() {
        // Querying the active tenant secret metadata via Tooling API mock/query structure
        List&lt;TenantSecretInfo&gt; secrets = new List&lt;TenantSecretInfo&gt;();
        // Standard compliance mandates that we check for active, archived, and destroyed key states
        for (TenantSecretInfo secret : secrets) {
            System.debug('Secret Id: ' + secret.Id + ' Status: ' + secret.Status + ' Type: ' + secret.Type);
        }
    }
    
    private class TenantSecretInfo {
        public String Id;
        public String Status; // Active, Archived, Destroyed
        public String Type;   // DataTemplate, SearchIndex, Analytics
    }
}
</code></pre>
<p>
Archiving a key makes it read-only, which is necessary for historical decryption. Under no circumstances should you destroy an archived tenant secret unless you are absolutely certain that no data in the database remains encrypted with that specific key. Destroying an archived secret without re-encrypting the associated data will lead to permanent, unrecoverable data loss.
</p>

<h2 id="s3">Real-Time Event Monitoring and Threat Detection</h2>
<p>
Salesforce Shield Event Monitoring exposes deep behavioural analytics by tracking user activity across more than 50 different event types, including logins, report exports, API queries, and page views. While legacy Event Monitoring relies on daily log files stored in the <code>EventLogFile</code> object, Real-Time Event Monitoring leverages the Salesforce Event Bus to broadcast events as they occur, enabling instant threat mitigation.
</p>
<p>
Using Transaction Security Policies (built on the enhanced policy framework), architects can write Apex classes that continuously evaluate user behaviour against risk thresholds. If a user attempts to export more than a specific limit of Contact records, the system can dynamically block the transaction, log the threat, and prompt the user to complete Multi-Factor Authentication (MFA).
</p>
<p>
The following Apex pattern illustrates how to construct an enhanced Transaction Security policy to intercept and block high-volume report exports:
</p>
<pre><code class="language-java">
global class HighVolumeExportBlocker implements TxnSecurity.EventCondition {
    public boolean evaluate(SObject event) {
        if (event instanceof ReportEvent) {
            ReportEvent repEvent = (ReportEvent) event;
            // Intercept report exports where the row count exceeds 1000 records
            if (repEvent.Operation == 'Export' && repEvent.RowsProcessed > 1000) {
                return true; // Trigger policy action (e.g. block or enforce MFA)
            }
        }
        return false;
    }
}
</code></pre>
<p>
Deploying this automated defensive logic directly onto the Salesforce Event Bus secures the perimeter of the CRM, ensuring that external threats or malicious insider behaviours are instantly blocked before data leakage can occur.
</p>

<h2 id="s4">Field Audit Trail (FAT) and Historical Data Archival</h2>
<p>
Standard Field History Tracking is limited to 20 fields per object and retains history records for up to 18 months. In highly regulated sectors like banking, healthcare, and insurance, standard compliance rules require changes to be audited for up to a decade. Field Audit Trail (FAT) elevates this limit, allowing organizations to track up to 60 fields per object and store history records for up to 10 years.
</p>
<p>
FAT achieves this long-term storage capacity by offloading history records into high-scale big tables (Big Objects). Managing the retention lifecycle of these histories is configured via the Metadata API using the <code>HistoryRetentionPolicy</code> component. This XML-based policy specifies how long history records remain in standard active storage before being automatically archived into big tables.
</p>
<p>
Below is an example of a <code>HistoryRetentionPolicy</code> metadata configuration for a custom object:
</p>
<pre><code class="language-java">
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;CustomObject xmlns="http://soap.sforce.com/2006/04/metadata"&gt;
    &lt;historyRetentionPolicy&gt;
        &lt;archiveAfterMonths&gt;6&lt;/archiveAfterMonths&gt;
        &lt;archiveRetentionYears&gt;10&lt;/archiveRetentionYears&gt;
        &lt;gracePeriodDays&gt;30&lt;/gracePeriodDays&gt;
    &lt;/historyRetentionPolicy&gt;
&lt;/CustomObject&gt;
</code></pre>
<p>
Once archived into big tables, these histories can be queried using standard SOQL (provided you filter exactly on the primary key fields of the Big Object) or by using Async SOQL for complex reporting. This architecture ensures that historical changes remain queryable for audits without degrading the performance of active CRM databases.
</p>

<h2 id="s5">Performance Optimisation and Technical Limitations of Shield</h2>
<p>
While Shield Platform Encryption is essential for security compliance, it introduces specific technical limitations and performance impacts that must be carefully managed. When encryption is active, the database must decrypt fields on the fly, which can introduce processing latency during high-volume data loads.
</p>
<p>
The most significant impact is on database indexing. Standard custom indexes cannot be built directly on probabilistically encrypted fields because the index cannot match random ciphertexts. Consequently, using a probabilistically encrypted field in a SOQL <code>WHERE</code> clause will trigger a full table scan, degrading query performance and potentially resulting in query timeouts on large tables.
</p>
<p>
To optimise performance and maintain scalability, architects should adhere to the following best practices:
</p>
<ul>
    <li>Prefer Deterministic encryption for fields that must be used in search forms, filters, or SOQL queries.</li>
    <li>Use custom indexes specifically derived for deterministic fields by coordinating with Salesforce Support.</li>
    <li>Avoid encrypting system fields, formula fields, or fields used in active workflow rules and validation rules.</li>
    <li>Optimise search layouts and restrict wildcard searches, as standard searching behaves differently with encrypted strings.</li>
</ul>
<p>
By systematically addressing indexing challenges, managing key lifecycles, and writing precise real-time transaction guards, you can design a secure, compliant Salesforce org that scales effortlessly under extreme workloads.
</p>
"""

sec_003_takeaways = """
<li>Understand that Probabilistic encryption generates random ciphertexts, preventing any SOQL search or filtering.</li>
<li>Deploy Deterministic encryption (Case-Sensitive or Case-Insensitive) when you must search or filter on encrypted fields.</li>
<li>Establish robust tenant secret rotation policies, and never destroy archived secrets to avoid permanent data corruption.</li>
<li>Leverage Real-Time Event Monitoring and Transaction Security Policies to intercept and block unauthorised high-volume exports.</li>
<li>Utilise Field Audit Trail (FAT) to track changes on up to 60 fields per object and retain histories for up to 10 years.</li>
<li>Configure the HistoryRetentionPolicy metadata component to define the transition rules from active storage to big tables.</li>
"""

sec_003_quiz = """
<div class="quiz-question" id="q1">
  <p><strong>Question 1:</strong> What is the main operational difference between Probabilistic and Deterministic encryption in Salesforce Shield?</p>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Probabilistic encryption allows exact match filtering, while Deterministic does not.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'right')">B. Deterministic allows exact match filtering in WHERE clauses, whereas Probabilistic does not support search filtering.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">C. Probabilistic encryption is only available for custom objects.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Deterministic encryption is significantly less secure because it uses standard MD5 hashing.</div>
</div>

<div class="quiz-question" id="q2">
  <p><strong>Question 2:</strong> How is the actual Data Encryption Key (DEK) generated in Salesforce Shield?</p>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. It is generated by the user's browser during authentication.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">B. Stored permanently inside the Salesforce metadata database.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'right')">C. Derived locally on the application server by combining the Salesforce master secret and the customer-managed Tenant Secret.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. Retained inside the external cloud directory server.</div>
</div>

<div class="quiz-question" id="q3">
  <p><strong>Question 3:</strong> Which metadata component is configured to define the archive and retention policy for Field Audit Trail?</p>
  <div class="quiz-option" onclick="answer(this, 'q3', 'right')">A. HistoryRetentionPolicy</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. FieldAuditTrailPolicy</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. ObjectHistoryRetention</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. DataRetentionSchedule</div>
</div>
"""

# SEC-004 Content: Zero-Trust Security in Salesforce
sec_004_summary = """
<li>Shifting from network-centric perimeter security to identity-driven continuous verification.</li>
<li>Implementing Context-Aware Access using IP restriction, device profiles, and MFA.</li>
<li>Designing granular sharing architectures using restriction rules and scoping rules.</li>
<li>Automating threat detection and real-time response using Transaction Security Policies.</li>
<li>Governing API access and securing third-party integrations with mutual TLS and OAuth.</li>
"""

sec_004_toc = """
<li><a href="#s1">The Philosophy of Zero-Trust in CRM Environments</a></li>
<li><a href="#s2">Context-Aware Access Control and Continuous Authentication</a></li>
<li><a href="#s3">Enforcing Least Privilege with Restriction and Scoping Rules</a></li>
<li><a href="#s4">Real-Time Threat Mitigation via Transaction Security</a></li>
<li><a href="#s5">Securing the API Perimeter and External Integrations</a></li>
"""

sec_004_body = """
<h2 id="s1">The Philosophy of Zero-Trust in CRM Environments</h2>
<p>
For decades, enterprise security relied on a network-centric "castle-and-moat" paradigm. Access was determined by whether a user was inside the corporate perimeter—such as a specific office building or logged in via a virtual private network (VPN). However, the rise of cloud-native systems, remote working, and dynamic mobile environments has rendered this network-focused security model obsolete. In the modern enterprise, CRM environments hold highly sensitive customer databases, intellectual property, and financial records. Enforcing perimeter-based security alone leaves organisations vulnerable to lateral movement if an attacker breaches the outer network.
</p>
<p>
The Zero-Trust framework addresses this challenge by operating on three fundamental tenets: "never trust, always verify," "enforce least privilege," and "assume breach." In a Zero-Trust Salesforce architecture, we do not grant access based on a user's location or their corporate network connection. Instead, every single access request is evaluated dynamically. We verify the user's identity, the security state of their device, the time of day, the specific record they are attempting to read, and their recent behaviour before granting access. By removing implicit trust, the organisation dramatically reduces its risk profile.
</p>

<h2 id="s2">Context-Aware Access Control and Continuous Authentication</h2>
<p>
Implementing Zero-Trust starts at the login interface. Salesforce architects must configure Context-Aware Access Control to evaluate the specific risk level of each login request in real time. This requires combining native Salesforce security tools, such as Login IP Ranges, Login Hours, Multi-Factor Authentication (MFA), and Session Security Levels.
</p>
<p>
To implement context-aware verification, define High Assurance sessions. For example, standard passwords grant "Standard" assurance, while completed MFA challenges upgrade the session to "High Assurance". You can enforce a security policy that allows users to browse general pages with standard assurance, but requires high assurance (MFA) when they access sensitive areas, like viewing reports or exporting records.
</p>
<p>
Additionally, you can deploy custom Login Flows. These flows allow you to run Apex checks during the login handshake to verify external parameters, such as checking if the user's device is registered in your enterprise mobile device management (MDM) system before granting access:
</p>
<pre><code class="language-java">
global class MDMDeviceVerifier implements Auth.LoginFlowHandler {
    global PageReference initiate(Map&lt;String, Object&gt; context) {
        Id userId = (Id) context.get('userId');
        String ipAddress = (String) context.get('ipAddress');
        
        // Custom logic to query MDM inventory API to verify device registration
        Boolean isDeviceValid = checkMDMInventory(userId, ipAddress);
        
        if (!isDeviceValid) {
            // Redirect to custom error page or block session instantiation
            return new PageReference('/apex/MDMDeviceValidationError');
        }
        return null; // Proceed with standard authentication flow
    }
    
    private Boolean checkMDMInventory(Id userId, String ipAddress) {
        // Query external MDM database or local registry mapping (Mock representation)
        return true;
    }
}
</code></pre>
<p>
Integrating this continuous context-aware check ensures that authentication is treated as a dynamic, ongoing process rather than a one-time boundary event.
</p>

<h2 id="s3">Enforcing Least Privilege with Restriction and Scoping Rules</h2>
<p>
Enforcing least privilege is a core component of Zero-Trust. In traditional Salesforce sharing architectures, permissions were largely additive. Org-Wide Defaults (OWD) established the base-level access, and Sharing Rules, Role Hierarchies, and Permission Sets granted broader access to records. However, this additive model made it difficult to restrict access for specific compliance scenarios, such as preventing support agents from viewing highly confidential VIP customer records.
</p>
<p>
To address this limitation, Salesforce introduced **Restriction Rules** and **Scoping Rules**. Restriction Rules are subtractive, allowing you to explicitly block record access. If a Restriction Rule is active for a user, Salesforce evaluates their sharing access as usual and then applies the rule's criteria to filter out records, ensuring that only records matching the rule are visible.
</p>
<p>
Below is an example of a <code>RestrictionRule</code> metadata configuration designed to prevent non-executive users from viewing high-value accounts:
</p>
<pre><code class="language-java">
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;RestrictionRule xmlns="http://soap.sforce.com/2006/04/metadata"&gt;
    &lt;active&gt;true&lt;/active&gt;
    &lt;description&gt;Restrict high-value account access to executives only&lt;/description&gt;
    &lt;enforcementType&gt;Restrict&lt;/enforcementType&gt;
    &lt;masterLabel&gt;High_Value_Account_Restriction&lt;/masterLabel&gt;
    &lt;targetEntity&gt;Account&lt;/targetEntity&gt;
    &lt;userCriteria&gt;{!User.UserRole.DeveloperName != 'Executive_Team'}&lt;/userCriteria&gt;
    &lt;recordCriteria&gt;{!Record.AnnualRevenue &lt; 5000000}&lt;/recordCriteria&gt;
&lt;/RestrictionRule&gt;
</code></pre>
<p>
By utilising this metadata configuration, any user outside the "Executive_Team" role will be unable to view Account records where Annual Revenue is 5,000,000 or greater, even if their standard profile or sharing rules would otherwise grant access.
</p>

<h2 id="s4">Real-Time Threat Mitigation via Transaction Security</h2>
<p>
Zero-Trust architectures assume that breaches will occur. Therefore, continuous monitoring of user behaviours is critical. Real-Time Event Monitoring enables transaction security policies to act as an automated firewall inside your Salesforce org, blocking threats as they occur.
</p>
<p>
For example, if a user's credentials are compromised, an attacker might log in and immediately attempt to export a customer contact list. A Transaction Security Policy can intercept this request in real time, evaluate the volume, and block the action.
</p>
<p>
The following Apex pattern illustrates how to programmatically evaluate and intercept suspicious API query behaviour:
</p>
<pre><code class="language-java">
global class SuspiciousQueryBlocker implements TxnSecurity.EventCondition {
    public boolean evaluate(SObject event) {
        if (event instanceof ApiEvent) {
            ApiEvent apiEvt = (ApiEvent) event;
            // Track API queries that pull large amounts of contact data at unusual times
            Integer hour = DateTime.now().hour();
            if (apiEvt.QueriedEntities.contains('Contact') && apiEvt.RowsProcessed > 5000 && (hour < 6 || hour > 20)) {
                return true; // Suspend the API call or trigger security notifications
            }
        }
        return false;
    }
}
</code></pre>
<p>
This transaction check runs automatically within the Salesforce application framework, providing immediate threat detection that secures data assets without requiring manual intervention from security analysts.
</p>

<h2 id="s5">Securing the API Perimeter and External Integrations</h2>
<p>
In modern architectures, the Salesforce API is a highly targeted entry point. Securing the API perimeter is just as important as securing user-facing login portals. Under a Zero-Trust strategy, standard username and password combinations for API integrations must be completely deactivated.
</p>
<p>
Instead, secure all integrations using certificate-based authentication and modern OAuth 2.0 flows, specifically the OAuth 2.0 JWT Bearer Flow for server-to-server communications. The JWT flow requires the calling application to sign a JSON Web Token using a private key, which Salesforce verifies against a certificate uploaded to a custom Connected App.
</p>
<p>
To secure critical APIs, implement Mutual TLS (mTLS). Standard TLS verifies the identity of the Salesforce server to the client. Mutual TLS requires both Salesforce and the calling client to present and verify certificates to establish a secure, encrypted connection.
</p>
<ul>
    <li>Create dedicated integration users with restricted profiles and minimal permissions.</li>
    <li>Deactivate the "API Enabled" permission for users who do not require system integration access.</li>
    <li>Implement IP whitelisting inside Connected Apps to restrict API calls to trusted IP ranges.</li>
    <li>Conduct regular reviews of OAuth tokens and revoke inactive sessions to minimise risk.</li>
</ul>
<p>
Adhering to these integration standards ensures that your Salesforce APIs are highly secured, establishing a robust Zero-Trust posture across your entire enterprise cloud ecosystem.
</p>
"""

sec_004_takeaways = """
<li>Deconstruct the traditional perimeter-based security model in favour of continuous verification under Zero-Trust.</li>
<li>Deploy Login Flows and High Assurance sessions to dynamically challenge users when they access sensitive resources.</li>
<li>Utilise subtractive Restriction Rules to restrict record access beyond standard sharing rules and role hierarchies.</li>
<li>Implement Real-Time Transaction Security Policies to automatically detect and block suspicious queries or report exports.</li>
<li>Enforce certificate-based OAuth 2.0 JWT Bearer Flows to secure all server-to-server API integrations.</li>
<li>Implement Mutual TLS (mTLS) to secure integration channels by requiring mutual certificate verification between endpoints.</li>
"""

sec_004_quiz = """
<div class="quiz-question" id="q1">
  <p><strong>Question 1:</strong> How do Restriction Rules differ from standard Salesforce Sharing Rules?</p>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Restriction Rules grant wider, read-write access to custom object records.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'right')">B. Sharing Rules grant additional access (additive), whereas Restriction Rules strip away access (subtractive).</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">C. Restriction Rules can only be applied to external community users.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Sharing Rules are evaluated after Restriction Rules have completed their execution.</div>
</div>

<div class="quiz-question" id="q2">
  <p><strong>Question 2:</strong> Which OAuth flow is highly recommended for secure, certificate-based server-to-server integration in a Zero-Trust Salesforce architecture?</p>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. OAuth 2.0 Username-Password Flow</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">B. OAuth 2.0 Implicit Grant Flow</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'right')">C. OAuth 2.0 JWT Bearer Flow</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. OAuth 2.0 User-Agent Flow</div>
</div>

<div class="quiz-question" id="q3">
  <p><strong>Question 3:</strong> What is the primary purpose of Continuous Authentication under a Zero-Trust CRM strategy?</p>
  <div class="quiz-option" onclick="answer(this, 'q3', 'right')">A. Evaluating session context, such as IP address and device state, on every high-risk action rather than just at initial login.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. Keeping users logged in indefinitely to eliminate MFA prompts.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. Encrypting password strings using deterministic AES-256 algorithms.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Forcing password changes every twelve hours.</div>
</div>
"""

# SEC-005 Content: Data Residency and Salesforce: What Hyperforce Changes
sec_005_summary = """
<li>Understanding the core architecture of Hyperforce and its separation from legacy infrastructure.</li>
<li>Leveraging Hyperforce Local Zones to enforce strict national and regional data residency.</li>
<li>Implementing Customer-Managed Keys (BYOK) to secure data-at-rest in public cloud environments.</li>
<li>Navigating the technical migration path, pre-migration checks, and post-migration validation.</li>
<li>Compliance mapping for GDPR, HIPAA, and local sovereign cloud requirements.</li>
"""

sec_005_toc = """
<li><a href="#s1">Decoupling the Monolith: The Hyperforce Infrastructure Shift</a></li>
<li><a href="#s2">Enforcing Data Residency with Hyperforce Local Zones</a></li>
<li><a href="#s3">Sovereign Key Management and Customer-Managed Keys (BYOK)</a></li>
<li><a href="#s4">Hyperforce Migration: Pre-Migration Readiness and Post-Migration Validation</a></li>
<li><a href="#s5">Compliance Mapping and the Future of Sovereign CRM Cloud</a></li>
"""

sec_005_body = """
<h2 id="s1">Decoupling the Monolith: The Hyperforce Infrastructure Shift</h2>
<p>
For nearly two decades, Salesforce operated on first-party bare-metal data centres. In this classic infrastructure, tenant instances (such as NA14, EU22, or AP19) were deployed on physical hardware managed directly by Salesforce. While this monolithic architecture allowed for close control over server operations, it restricted geographic scaling and made provisioning new regions slow and capital-intensive. Legacy instances also suffered from rigid resource caps, making elastic, on-demand scaling difficult.
</p>
<p>
Hyperforce represents a complete redesign of the Salesforce infrastructure. It decouples the core Salesforce application layer from the underlying physical hardware. Instead of using first-party bare-metal data centres, Hyperforce runs on public cloud infrastructure (specifically Amazon Web Services) using a modern, containerised architecture based on Amazon Elastic Kubernetes Service (EKS).
</p>
<p>
By utilising containerised deployment, microservices, and elastic cloud databases, Hyperforce offers several key benefits:
</p>
<ul>
    <li><strong>Elastic Scalability:</strong> Compute and database resources scale dynamically based on real-time transaction volume.</li>
    <li><strong>Rapid Deployment:</strong> New infrastructure instances can be provisioned in new geographic regions within days rather than months.</li>
    <li><strong>Enhanced Isolation:</strong> Virtual private clouds and container boundaries isolate tenant resources to prevent data leaks.</li>
    <li><strong>Modern Security Controls:</strong> Native cloud integration allows for zero-downtime rolling upgrades and robust encryption pipelines.</li>
</ul>
<p>
This architectural shift helps enterprise architects move away from fixed-capacity infrastructure toward an agile, cloud-native CRM foundation.
</p>

<h2 id="s2">Enforcing Data Residency with Hyperforce Local Zones</h2>
<p>
Data residency is a critical regulatory concern for multinational enterprises. The transition of data across international borders is highly regulated by frameworks such as the European Union's GDPR, Germany's C5, and Australia's IRAP. In legacy environments, achieving data residency was challenging, as backing up or caching data often routed traffic through global network hubs, potentially exposing data to foreign jurisdictions.
</p>
<p>
Hyperforce addresses this regulatory requirement through **Local Zones**. A Local Zone ensures that all data storage, databases, file caches, and processing operations are kept strictly within defined geographic boundaries (e.g. EU-central in Frankfurt, or AP-southeast in Sydney).
</p>
<p>
Furthermore, Hyperforce ensures that data remains local even during system failures. Disaster recovery systems, backup mirrors, and support databases are kept within the same sovereign borders. This architecture helps organisations comply with strict national data residency requirements, assuring regulators that customer data is stored and processed locally.
</p>

<h2 id="s3">Sovereign Key Management and Customer-Managed Keys (BYOK)</h2>
<p>
Storing sensitive CRM data in the public cloud requires robust security controls. Under a shared responsibility model, architects must implement encryption architectures that protect data from third-party exposure. Hyperforce secures data at rest by default using platform encryption. To provide maximum control, it supports sovereign key management through Customer-Managed Keys (CMK), also known as "Bring Your Own Key" (BYOK).
</p>
<p>
With Hyperforce BYOK, the master encryption keys are generated and stored inside the customer's external key management system (such as AWS Key Management Service or HashiCorp Vault). The application server never stores the raw master key. Instead, it accesses the external KMS securely on demand to wrap or unwrap the data encryption keys (DEKs).
</p>
<p>
This architecture gives the customer complete authority over their data. If a compliance breach is suspected, they can instantly revoke access to the master key in their KMS, immediately rendering all data stored in Salesforce unreadable.
</p>
<p>
The following REST pattern outlines how a custom integration might programmatically verify key states with an external KMS endpoint:
</p>
<pre><code class="language-java">
// Conceptual Apex client verifying Key State with an external KMS
public class KMSConnectionVerifier {
    public static Boolean verifyKMSKeyStatus(String endpointUrl, String keyId) {
        Http http = new Http();
        HttpRequest request = new HttpRequest();
        request.setEndpoint(endpointUrl + '/keys/' + keyId);
        request.setMethod('GET');
        request.setHeader('Accept', 'application/json');
        
        try {
            HttpResponse response = http.send(request);
            if (response.getStatusCode() == 200) {
                Map&lt;String, Object&gt; payload = (Map&lt;String, Object&gt;) JSON.deserializeUntyped(response.getBody());
                String keyState = (String) payload.get('KeyState');
                return 'Enabled'.equalsIgnoreCase(keyState);
            }
        } catch (Exception e) {
            System.debug('KMS connection validation failed: ' + e.getMessage());
        }
        return false;
    }
}
</code></pre>
<p>
Deploying this sovereign key management strategy assures regulators and compliance teams that the customer retains absolute control over data encryption keys.
</p>

<h2 id="s4">Hyperforce Migration: Pre-Migration Readiness and Post-Migration Validation</h2>
<p>
Migrating a legacy Salesforce org to Hyperforce requires careful preparation. Because Hyperforce is built on dynamic public cloud infrastructure, legacy architectural patterns, such as hardcoding server instance names or relying on static IP whitelists, will cause operational failures.
</p>
<p>
To ensure a successful migration, architects should complete this pre-migration checklist:
</p>
<ol>
    <li><strong>Eliminate Hardcoded URLs:</strong> Standardise on My Domain and replace any instance-specific URLs (e.g. <code>https://na14.salesforce.com</code>) with domain-relative paths.</li>
    <li><strong>Adopt Domain Whitelisting:</strong> Hyperforce uses a wide range of dynamic IP addresses. Replace static IP whitelisting with domain-name-based whitelisting.</li>
    <li><strong>Update API Integrations:</strong> Verify that external applications and middleware support modern SNI (Server Name Indication) protocols.</li>
    <li><strong>Validate Certificates:</strong> Ensure all secure connections use certificates issued by trusted, standard authorities.</li>
</ol>
<p>
You can audit your codebase for hardcoded URLs programmatically. The following Tooling API query can be used to scan Apex classes for legacy instance references:
</p>
<pre><code class="language-sql">
SELECT Id, Name, Body 
FROM ApexClass 
WHERE Body LIKE '%.salesforce.com%' 
  AND (NOT Body LIKE '%.my.salesforce.com%')
</code></pre>
<p>
Executing these pre-migration checks and running automated code scans helps identify and resolve legacy dependencies, preventing downtime during the migration.
</p>

<h2 id="s5">Compliance Mapping and the Future of Sovereign CRM Cloud</h2>
<p>
Hyperforce's containerised, region-specific architecture aligns with global compliance certifications. By combining regional storage with customer-managed keys, the platform meets major security standards:
</p>
<ul>
    <li><strong>GDPR (Europe):</strong> Satisfies data transfer regulations (such as Schrems II) by keeping processing and storage strictly within the European Union.</li>
    <li><strong>C5 (Germany):</strong> Meets Germany's Cloud Computing Compliance Criteria Catalogue through deep local hosting structures.</li>
    <li><strong>SecNumCloud (France):</strong> Complies with French national data security standards by keeping sovereign data isolated within local zones.</li>
    <li><strong>IRAP (Australia):</strong> Meets the requirements of the Australian Information Security Manual, enabling secure government data hosting.</li>
</ul>
<p>
In conclusion, Hyperforce represents a major shift in how enterprise CRM systems manage data residency, cloud scalability, and sovereign data control. Moving to this containerised public cloud architecture helps technical leaders ensure their CRM systems comply with local data regulations, keeping customer data secure, private, and within sovereign borders.
</p>
"""

sec_005_takeaways = """
<li>Understand that Hyperforce runs on public cloud infrastructure using containerised Kubernetes deployments, decoupling the core application.</li>
<li>Leverage Hyperforce Local Zones to enforce strict data residency, keeping databases and backups within defined geographic borders.</li>
<li>Deprecate static IP address whitelisting in favour of domain whitelisting, as Hyperforce relies on dynamic IP ranges.</li>
<li>Implement Customer-Managed Keys (BYOK) using external KMS endpoints to retain sovereign control over data encryption.</li>
<li>Audit custom code for hardcoded instance URLs before migrating, and standardise on relative My Domain endpoints.</li>
<li>Map Hyperforce Local Zones to local regulatory standards (GDPR, C5, SecNumCloud, IRAP) to satisfy compliance requirements.</li>
"""

sec_005_quiz = """
<div class="quiz-question" id="q1">
  <p><strong>Question 1:</strong> Why does Hyperforce require organisations to move away from IP address whitelisting?</p>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Hyperforce restricts IP-based traffic to port 80 only.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. It enforces standard OAuth logins which do not support IP ranges.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'right')">C. Hyperforce uses public cloud dynamic infrastructure with elastic scaling, meaning IP addresses are subject to frequent change.</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Virtual private networks are strictly prohibited under Hyperforce architectures.</div>
</div>

<div class="quiz-question" id="q2">
  <p><strong>Question 2:</strong> In Hyperforce, how are Customer-Managed Keys (BYOK) typically integrated for data-at-rest encryption?</p>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. By uploading raw private keys directly to custom custom metadata settings.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'right')">B. By integrating with external cloud key management services like AWS KMS via secure endpoints.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. Utilizing standard Salesforce password encryption fields.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. Through the use of classic client-side certificate components.</div>
</div>

<div class="quiz-question" id="q3">
  <p><strong>Question 3:</strong> What is the primary purpose of a Hyperforce "Local Zone"?</p>
  <div class="quiz-option" onclick="answer(this, 'q3', 'right')">A. Ensuring that data storage, processing, and caching remain strictly within a specific sovereign or geographic boundary.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. Restricting user logins to their local timezone only.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. Running custom apex processes on local workstation machines.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Partitioning the development sandbox from production instances.</div>
</div>
"""

# SEC-006 Content: Single Sign-On
sec_006_summary = """
<li>Architecting secure Single Sign-On (SSO) using SAML 2.0 in Federated Identity environments.</li>
<li>Configuring Salesforce as both a Service Provider (SP) and Identity Provider (IdP).</li>
<li>Harnessing OAuth 2.0 flows for mobile apps, single-page applications, and server-to-server APIs.</li>
<li>Customising authentication behaviour using SAML JIT (Just-In-Time) provisioning and Auth Providers.</li>
<li>Debugging complex SSO handshakes, signature mismatches, and certificate expirations.</li>
"""

sec_006_toc = """
<li><a href="#s1">SAML 2.0 vs OAuth 2.0 in the Enterprise Identity Stack</a></li>
<li><a href="#s2">Configuring Salesforce as a Service Provider (SP)</a></li>
<li><a href="#s3">Deploying Salesforce as an Identity Provider (IdP)</a></li>
<li><a href="#s4">Extending Authentication with SAML Just-In-Time (JIT) Provisioning</a></li>
<li><a href="#s5">Troubleshooting and Hardening SSO Deployments</a></li>
"""

sec_006_body = """
<h2 id="s1">SAML 2.0 vs OAuth 2.0 in the Enterprise Identity Stack</h2>
<p>
In enterprise environments, managing identity and access control across a complex landscape of applications requires robust architectures. The two primary protocols used for this purpose are SAML 2.0 (Security Assertion Markup Language) and OAuth 2.0. To build a secure environment, architects must understand the different roles, strengths, and use cases of these protocols.
</p>
<p>
SAML 2.0 is an XML-based federated identity standard designed for Single Sign-On (SSO). It operates by exchanging XML-based assertions between an Identity Provider (IdP), which stores and verifies user credentials, and a Service Provider (SP), which hosts the application. SAML is designed for authentication, sharing secure user identity and profile attributes across web browsers.
</p>
<p>
OAuth 2.0, on the other hand, is a token-based authorization framework. It does not natively handle authentication. Instead, it is designed to grant third-party applications secure, limited access to HTTP resources using JSON Web Tokens (JWT) or opaque access tokens.
</p>
<p>
To support authentication on top of OAuth, the industry developed <strong>OpenID Connect (OIDC)</strong>. OIDC introduces an identity layer on top of OAuth 2.0, using an ID Token (a structured JWT) alongside the standard access token. OIDC is highly suited for modern single-page web applications and mobile apps, where parsing large XML SAML payloads can be inefficient.
</p>
<table>
    <thead>
        <tr>
            <th>Feature</th>
            <th>SAML 2.0</th>
            <th>OAuth 2.0 / OIDC</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Primary Focus</td>
            <td>Federated Web SSO (Authentication)</td>
            <td>API Authorization &amp; Identity Layer</td>
        </tr>
        <tr>
            <td>Payload Format</td>
            <td>XML (Cryptographically Signed)</td>
            <td>JSON (Signed JWT Tokens)</td>
        </tr>
        <tr>
            <td>Transport Channel</td>
            <td>Browser Redirects &amp; POST Requests</td>
            <td>Direct HTTP API calls &amp; Headers</td>
        </tr>
        <tr>
            <td>Best For</td>
            <td>Enterprise Web Portals, Desktop SSO</td>
            <td>Mobile apps, REST APIs, SPAs</td>
        </tr>
    </tbody>
</table>
<p>
Selecting the right protocol helps ensure that web portals, API integrations, and mobile applications are secured with the appropriate authentication controls.
</p>

<h2 id="s2">Configuring Salesforce as a Service Provider (SP)</h2>
<p>
When Salesforce acts as a Service Provider (SP), users authenticate through an external Identity Provider (such as Okta, Azure AD, or Ping Identity) before accessing the CRM. This is the standard configuration for enterprise environments, allowing organisations to manage identity policies in a central system.
</p>
<p>
The authentication handshake can be initiated in two ways:
</p>
<ol>
    <li><strong>Service Provider (SP)-Initiated:</strong> The user attempts to access a deep link directly within Salesforce (e.g. <code>https://mycompany.my.salesforce.com/lightning/page/home</code>). Finding no active session, Salesforce redirects the user's browser to the IdP's login page with a signed <code>SAMLRequest</code> parameter. Once authenticated, the IdP redirects the browser back to the Salesforce assertion consumer service (ACS) URL with a <code>SAMLResponse</code> containing a signed XML assertion.</li>
    <li><strong>Identity Provider (IdP)-Initiated:</strong> The user logs into their central application portal (e.g. Okta dashboard) and clicks the Salesforce icon. The IdP generates the <code>SAMLResponse</code> and posts it directly to the Salesforce ACS URL via the browser. Salesforce validates the signature, maps the user, and instantiates the session.</li>
</ol>
<p>
To configure Salesforce as an SP, you must import the IdP's metadata XML file, upload the IdP's SAML signing certificate, and set your user mapping strategy. Standardise on mapping the IdP's NameID attribute to the Salesforce <code>Username</code> or a custom <code>FederationIdentifier</code> field on the User record.
</p>

<h2 id="s3">Deploying Salesforce as an Identity Provider (IdP)</h2>
<p>
Salesforce can also act as the Identity Provider (IdP) for external applications. In this setup, Salesforce manages user credentials, and users can log into external systems (such as Workday or a custom internal app) using their Salesforce sessions.
</p>
<p>
To configure Salesforce as an IdP, navigate to identity settings and enable Identity Provider capabilities. This generates a metadata XML document and an IdP certificate. For each external application, you must create a corresponding <strong>Connected App</strong> inside Salesforce.
</p>
<p>
Within the Connected App configuration, you will specify:
</p>
<ul>
    <li><strong>Entity ID:</strong> The unique identifier provided by the external application.</li>
    <li><strong>ACS URL:</strong> The endpoint where the external application receives and processes SAML responses.</li>
    <li><strong>Subject Type:</strong> Define how the user is identified in the SAML assertion (e.g. Username, Federation ID, or User ID).</li>
    <li><strong>SAML Issuer:</strong> The Salesforce My Domain URL that signs the assertion.</li>
</ul>
<p>
By deploying Salesforce as an IdP, you can leverage native security features, such as login flows and transaction policies, to protect access to external systems across your corporate network.
</p>

<h2 id="s4">Extending Authentication with SAML Just-In-Time (JIT) Provisioning</h2>
<p>
In large enterprise environments, manually creating and updating user records in Salesforce can introduce administrative overhead. SAML Just-in-Time (JIT) Provisioning addresses this by automatically creating or updating Salesforce User records when a user logs in via SSO.
</p>
<p>
To implement custom logic for JIT provisioning, you must write an Apex class that implements the <code>Auth.SamlJitHandler</code> interface. This interface requires implementing two methods: <code>createUser</code> and <code>updateUser</code>.
</p>
<p>
The following complete Apex class demonstrates how to parse a SAML assertion to automatically provision and update User records:
</p>
<pre><code class="language-java">
global class CustomSAMLJitHandler implements Auth.SamlJitHandler {
    private void populateUserData(User u, Map&lt;String, String&gt; attributes) {
        u.Email = attributes.get('User.Email');
        u.FirstName = attributes.get('User.FirstName');
        u.LastName = attributes.get('User.LastName');
        u.Alias = (attributes.get('User.FirstName').substring(0, 1) + attributes.get('User.LastName').substring(0, 4)).toLowerCase();
        
        // Map division and department to help determine the user profile
        String dept = attributes.get('User.Department');
        u.Department = dept;
        
        // Determine Profile assignment based on department attribute
        if ('Sales'.equalsIgnoreCase(dept)) {
            u.ProfileId = [SELECT Id FROM Profile WHERE Name = 'Standard Sales User' LIMIT 1].Id;
        } else {
            u.ProfileId = [SELECT Id FROM Profile WHERE Name = 'Standard User' LIMIT 1].Id;
        }
    }
    
    global User createUser(Id samlProviderId, Id communityId, Id portalId, 
                            String federationId, Map&lt;String, String&gt; attributes, String assertion) {
        User u = new User();
        u.FederationIdentifier = federationId;
        u.Username = federationId + '@sfvedas.com';
        u.TimeZoneSidKey = 'Europe/London';
        u.LocaleSidKey = 'en_GB';
        u.EmailEncodingKey = 'UTF-8';
        u.LanguageLocaleKey = 'en_US';
        
        populateUserData(u, attributes);
        return u;
    }
    
    global void updateUser(Id userId, Id samlProviderId, Id communityId, Id portalId, 
                            String federationId, Map&lt;String, String&gt; attributes, String assertion) {
        User u = [SELECT Id, Email, FirstName, LastName, Alias, ProfileId, Department FROM User WHERE Id = :userId];
        populateUserData(u, attributes);
        update u;
    }
}
</code></pre>
<p>
Deploying a custom JIT handler automates user administration, reduces provisioning delays, and ensures that user profile and role assignments are synchronised with your central identity repository.
</p>

<h2 id="s5">Troubleshooting and Hardening SSO Deployments</h2>
<p>
SSO deployments can experience issues due to cryptographic errors, configuration drift, or network latency. Architects should be familiar with common failure modes and their resolutions:
</p>
<ol>
    <li><strong>SAML Assertion Validation Failures:</strong> Use the native Salesforce <strong>SAML Assertion Validator</strong>. Paste the raw XML assertion into the validator to check for signature mismatches, expired certificates, or incorrect NameID mapping.</li>
    <li><strong>Clock Skew Mismatch:</strong> If the IdP and Salesforce system times are out of sync by more than three minutes, the assertion is rejected. Ensure your IdP synchronises with standard Network Time Protocol (NTP) servers.</li>
    <li><strong>Expired Certificates:</strong> Set reminders to rotate certificates before they expire. Update the new certificate in both the IdP and the Salesforce Single Sign-On settings to prevent login outages.</li>
</ol>
<p>
To secure your SSO configuration, apply these hardening best practices:
</p>
<ul>
    <li>Disable direct login access via standard passwords for SSO-enabled users by assigning them a secure Login Policy.</li>
    <li>Enforce the use of HTTPS for all login and metadata exchange endpoints.</li>
    <li>Establish a backup login URL (such as the default Salesforce login page with MFA) for system administrators to prevent being locked out if the IdP experiences an outage.</li>
</ul>
<p>
By systematically troubleshooting authentication issues and applying these security hardening best practices, you can build a stable, secure Single Sign-On deployment that protects your enterprise CRM environments.
</p>
"""

sec_006_takeaways = """
<li>Distinguish between SAML 2.0 for federated browser authentication and OAuth 2.0 for API-centric authorization.</li>
<li>Map external identity attributes to standard Salesforce fields like Username or FederationIdentifier to verify identities.</li>
<li>Implement the Auth.SamlJitHandler interface in Apex to automate the creation and update of User records at login.</li>
<li>Utilise the native SAML Assertion Validator to debug signature, expiration, and formatting errors in XML payloads.</li>
<li>Configure secure administrator backdoors and enforce HTTPS to prevent lockout events during IdP outages.</li>
<li>Rotate SSO certificates before expiration to avoid sudden login failures across your user base.</li>
"""

sec_006_quiz = """
<div class="quiz-question" id="q1">
  <p><strong>Question 1:</strong> What interface must an Apex class implement to customise the creation and update of User records during a SAML Just-In-Time login flow?</p>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Auth.AuthProviderJit</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. System.UserProvisioningHandler</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'right')">C. Auth.SamlJitHandler</div>
  <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Auth.RegistrationHandler</div>
</div>

<div class="quiz-question" id="q2">
  <p><strong>Question 2:</strong> In a Service Provider (SP)-Initiated SAML SSO flow, where does the user's browser navigate first when attempting to log in?</p>
  <div class="quiz-option" onclick="answer(this, 'q2', 'right')">A. To the Salesforce login page, which generates a SAMLRequest and redirects the user to the Identity Provider.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">B. Directly to the Salesforce home page via session credentials.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. To the domain registration server to query DNS entries.</div>
  <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. To a third-party payment gateway for licence validation.</div>
</div>

<div class="quiz-question" id="q3">
  <p><strong>Question 3:</strong> What is the primary utility of the Salesforce SAML Assertion Validator during deployment?</p>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. To calculate the clock skew between the database and the active application server.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'right')">B. To parse a raw XML SAML assertion in real-time and identify structural, cryptographic, or attribute mismatches.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. Automatically generating Apex test classes for custom controllers.</div>
  <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Uploading local certificates to your key directory database.</div>
</div>
"""

# Map to slug dictionary
TUTORIALS_DATA = {
    'sec-002': {
        'summary': sec_002_summary.strip(),
        'toc': sec_002_toc.strip(),
        'body': sec_002_body.strip(),
        'takeaways': sec_002_takeaways.strip(),
        'quiz': sec_002_quiz.strip()
    },
    'sec-003': {
        'summary': sec_003_summary.strip(),
        'toc': sec_003_toc.strip(),
        'body': sec_003_body.strip(),
        'takeaways': sec_003_takeaways.strip(),
        'quiz': sec_003_quiz.strip()
    },
    'sec-004': {
        'summary': sec_004_summary.strip(),
        'toc': sec_004_toc.strip(),
        'body': sec_004_body.strip(),
        'takeaways': sec_004_takeaways.strip(),
        'quiz': sec_004_quiz.strip()
    },
    'sec-005': {
        'summary': sec_005_summary.strip(),
        'toc': sec_005_toc.strip(),
        'body': sec_005_body.strip(),
        'takeaways': sec_005_takeaways.strip(),
        'quiz': sec_005_quiz.strip()
    },
    'sec-006': {
        'summary': sec_006_summary.strip(),
        'toc': sec_006_toc.strip(),
        'body': sec_006_body.strip(),
        'takeaways': sec_006_takeaways.strip(),
        'quiz': sec_006_quiz.strip()
    }
}

def process_file(slug, data):
    filepath = os.path.join(TUTORIALS_DIR, slug, 'index.html')
    if not os.path.exists(filepath):
        print(f"Error: File not found {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple replacement of specific comments/tags
    
    # 1. Summary bullets
    content = content.replace('<!-- [[SUMMARY_BULLETS]] -->', data['summary'])
    
    # 2. TOC Links
    content = content.replace('<!-- [[TOC_LINKS]] -->', data['toc'])
    
    # 3. Body Sections
    content = content.replace('<!-- [[BODY_SECTIONS]] -->', data['body'])
    
    # 4. Takeaway Bullets
    content = content.replace('<!-- [[TAKEAWAY_BULLETS]] -->', data['takeaways'])
    
    # 5. Quiz Questions
    content = content.replace('<!-- [[QUIZ_QUESTIONS]] -->', data['quiz'])
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully processed {slug}")
    return True

def check_word_count(slug):
    filepath = os.path.join(TUTORIALS_DIR, slug, 'index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse text inside <article class="tutorial-body" id="tutorialContent">...</article>
    article_m = re.search(r'<article class="tutorial-body"[^>]*>(.*?)</article>', content, re.DOTALL)
    if not article_m:
        print(f"Could not find article body for word count in {slug}")
        return
    
    body_text = article_m.group(1)
    
    # Strip HTML tags
    clean_text = re.sub(r'<[^>]+>', ' ', body_text)
    words = clean_text.split()
    word_count = len(words)
    print(f"{slug} Body Word Count: {word_count} words")
    if word_count < 1800:
        print(f"WARNING: {slug} word count is below 1800 words!")

def main():
    for slug, data in TUTORIALS_DATA.items():
        process_file(slug, data)
        check_word_count(slug)

if __name__ == '__main__':
    main()
