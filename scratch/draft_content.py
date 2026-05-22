# -*- coding: utf-8 -*-
import os
import re
import sys

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIALS_DIR = os.path.join(WORKSPACE_DIR, 'tutorials')

# SEC-007 Content
sec_007_summary = """
            <li>Master the fundamental architecture of Salesforce Connected Apps and OAuth token management.</li>
            <li>Identify critical security vulnerabilities in common OAuth flows (e.g., User-Agent vs. JWT Bearer).</li>
            <li>Implement precise API scope management to enforce the principle of least privilege.</li>
            <li>Establish robust governance and lifecycle management for OAuth client secrets and certificates.</li>
            <li>Develop automated auditing strategies to continuously monitor Connected App permissions and usage.</li>
            <li>Securely configure Connected Apps to prevent token leakage and unauthorised platform access.</li>
"""

sec_007_toc = """
            <li><a href="#s1">1. Connected Apps and OAuth Flow Architecture</a></li>
            <li><a href="#s2">2. Granular Scopes and Least Privilege Access</a></li>
            <li><a href="#s3">3. Managing and Securing Integration Credentials</a></li>
            <li><a href="#s4">4. Connected App Policies and Network Perimeters</a></li>
            <li><a href="#s5">5. Advanced Auditing and Continuous Compliance Monitoring</a></li>
"""

sec_007_body = """
        <h2 id="s1">1. Connected Apps and OAuth Flow Architecture</h2>
        <p>In the modern enterprise ecosystem, Salesforce rarely operates in isolation. It serves as the core system of record, constantly interacting with external systems, middleware, mobile applications, and third-party SaaS platforms. The gateway that facilitates these secure integrations is the Salesforce Connected App. A Connected App is not a container for data, nor does it run integration code; rather, it is a metadata framework that defines how an external client application interacts with Salesforce APIs. It acts as an OAuth 2.0 client definition, establishing identity and authorisation pathways. However, tech leaders and solution architects frequently misunderstand the architectural boundaries of Connected Apps, leading to severe, undetected security risks. To secure the enterprise perimeter, one must first master the mechanics of Salesforce's OAuth implementations and understand the distinct security profiles of each flow.</p>
        <p>OAuth 2.0 is the foundational protocol used by Salesforce to authorise external clients without exposing user credentials. When an external client connects to Salesforce, it requests authorisation via one of several OAuth flows. The choice of flow is a critical security decision that determines the level of vulnerability to token interception, credential theft, and session hijacking. The most commonly deployed flows are the Authorisation Code Flow, the User-Agent Flow, the JWT Bearer Flow, and the Client Credentials Flow. Each flow has specific, non-negotiable use cases and distinct vulnerability profiles:</p>
        <ul>
          <li><strong>Authorisation Code Flow:</strong> Considered the gold standard for secure server-side applications. In this flow, the client application redirects the user to the Salesforce login page. Upon successful authentication, Salesforce returns a temporary authorisation code to the client via a secure redirect URI. The client application then exchanges this code for an access token and a refresh token from its secure backend server, utilising its client secret. Because the access token is requested server-to-server and the client secret is never exposed to the user's browser, the risk of interception is minimal.</li>
          <li><strong>User-Agent Flow:</strong> Designed for client-side applications, such as single-page web applications (SPAs) or mobile apps where a secure backend server is absent. In this flow, Salesforce redirects the user back to the client application and appends the access token directly to the URL fragment. This fragment is parsed by the client's browser or mobile operating system. This flow presents an exceptionally high risk profile because the access token is exposed directly in the web browser's history, referrer headers, and local memory. Malicious browser extensions or cross-site scripting (XSS) vulnerabilities can easily capture these tokens. Therefore, organisations should strictly limit or deprecate the User-Agent flow in favour of more secure alternatives, such as the Authorisation Code Flow with PKCE (Proof Key for Code Exchange).</li>
          <li><strong>JWT Bearer Flow:</strong> The industry standard for automated, non-interactive machine-to-machine integrations. In this flow, the external application uses a local private key to sign a JSON Web Token (JWT) assertion. The application posts this signed assertion to the Salesforce token endpoint. Salesforce, having the corresponding public certificate uploaded to the Connected App, verifies the signature and immediately issues an access token. The JWT flow requires no interactive login, makes no use of client secrets, and is immune to browser-based interception. It is the most robust flow for enterprise ETL tools, ESBs, and continuous integration pipelines.</li>
          <li><strong>Client Credentials Flow:</strong> A modern, simplified flow for backend integrations where the client authenticates directly using its client ID and client secret to obtain an access token on behalf of a pre-authorised integration user. While convenient, it relies heavily on the confidentiality of the client secret, which must be stored securely.</li>
        </ul>
        <p>Architects must carefully evaluate these flows when establishing integrations. Selecting the wrong flow for a given environment can compromise the entire organisation's security posture, rendering even the most robust firewalls and IP restrictions ineffective.</p>

        <h2 id="s2">2. Granular Scopes and Least Privilege Access</h2>
        <p>One of the most pervasive security omissions in Salesforce integration governance is the misconfiguration of OAuth scopes. Scopes define the permissions that the Connected App requests and that the user or administrator authorises. They act as a secondary authorization layer, limiting what the client application can perform, even if the authenticating user has broader system permissions. Unfortunately, many integration developers and system administrators default to assigning the <code>full</code> scope to their Connected Apps. This is a highly dangerous practice that violates the core security principle of least privilege.</p>
        <p>The <code>full</code> scope grants the external application unrestricted access to all data and APIs, including the ability to download files, modify metadata, run reports, and execute arbitrary Apex code. If an integration with a <code>full</code> scope is compromised, the attacker gains absolute control over the Salesforce instance, bypassing many security boundaries. Instead of resorting to <code>full</code> access, architects must mandate granular scopes that align precisely with the integration's actual requirements. The following table describes the standard Salesforce OAuth scopes and their corresponding risk levels:</p>
        
        <table style="width:100%; border-collapse:collapse; margin:20px 0;">
          <thead>
            <tr style="background-color:var(--bg-secondary); border-bottom:2px solid var(--border);">
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">OAuth Scope</th>
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">Description</th>
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">Risk Profile</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-family:var(--font-mono); font-size:0.9rem;">api</td>
              <td style="padding:12px;">Allows access to standard REST, SOAP, and Bulk APIs.</td>
              <td style="padding:12px; color:var(--saffron); font-weight:600;">Medium - Direct data access</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-family:var(--font-mono); font-size:0.9rem;">web</td>
              <td style="padding:12px;">Allows the client to use the access token on the web.</td>
              <td style="padding:12px;">Low - Session management</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-family:var(--font-mono); font-size:0.9rem;">refresh_token</td>
              <td style="padding:12px;">Allows a refresh token to be returned, enabling offline access.</td>
              <td style="padding:12px; color:var(--saffron); font-weight:600;">Medium - Persistent sessions</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-family:var(--font-mono); font-size:0.9rem;">chatter_api</td>
              <td style="padding:12px;">Allows access to the Connect REST API resources (Chatter).</td>
              <td style="padding:12px;">Low - Collaboration data</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-family:var(--font-mono); font-size:0.9rem;">full</td>
              <td style="padding:12px;">Grants access to all data and APIs, bypassing other restrictions.</td>
              <td style="padding:12px; color:var(--red); font-weight:600;">Critical - Absolute control</td>
            </tr>
          </tbody>
        </table>

        <p>To enforce least privilege, architects must design integration-specific Connected Apps rather than sharing a single generic app across multiple external services. If an integration only needs to query customer contact information via standard REST endpoints, the Connected App should be configured with nothing more than the <code>api</code> and <code>refresh_token</code> scopes. The <code>refresh_token</code> scope is required to maintain a persistent connection without prompting the user to re-authenticate, but it should be accompanied by strict session policies. By isolating scopes, you ensure that a breach of one integration does not compromise others or expose administrative APIs.</p>

        <h2 id="s3">3. Managing and Securing Integration Credentials</h2>
        <p>In addition to structuring secure OAuth flows, organisations must establish rigorous controls for managing and securing integration credentials. Connected Apps rely on two primary mechanisms for client authentication: client secrets and certificates. Client secrets are effectively long-term passwords generated by Salesforce for the Connected App. If a client secret is compromised, an attacker can impersonate the client application and, if scopes are loosely defined, gain unauthorised access to the Salesforce platform.</p>
        <p>Unfortunately, client secrets are routinely mismanaged. Developers often hardcode them into application source files, commit them to public or private Git repositories, or distribute them in plaintext configuration files. To mitigate this risk, architects must establish a zero-tolerance policy for hardcoded credentials. Instead of client secrets, enterprise integrations should default to utilising certificate-based authentication, specifically through the JWT Bearer flow. In this architecture, Salesforce does not issue a client secret; instead, the external client generates an asymmetric key pair and uploads the public certificate (signed by a trusted certificate authority or self-signed for internal use) to the Salesforce Connected App metadata configuration.</p>
        <p>When the client wishes to connect, it creates a JWT payload containing the issuer (the Connected App Client ID), the subject (the integration username), the audience (the Salesforce login or community URL), and the expiration time. The client signs this token using its locally stored private key. The private key never leaves the client's secure hosting environment and is never transmitted over the network. Salesforce receives the signed JWT assertion, validates it against the uploaded public certificate, and issues an ephemeral access token. The private key must be stored securely within an enterprise key management system, such as HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault, and injected into the client application runtime environment at execution time. This completely eliminates the threat of credentials leaking through source code repositories or system backups.</p>

        <h2 id="s4">4. Connected App Policies and Network Perimeters</h2>
        <p>A major vulnerability in default Connected App configurations is the permissive nature of their access policies. By default, when a Connected App is created, the Permitted Users policy is set to "All users may self-authorise". This setting means that any user in the Salesforce organisation can initiate the OAuth flow and grant the third-party application access to their personal session and data, without administrative oversight. This is a significant compliance and security loophole, as it enables users to connect rogue external applications, personal productivity tools, or unauthorised browser extensions to the corporate Salesforce environment.</p>
        <p>To establish proper governance, architects must switch the Permitted Users setting to "Admin approved users are pre-authorised". Once this setting is active, Salesforce blocks all self-authorisation attempts. Instead, access is strictly limited to users who have been explicitly assigned the Connected App via Profiles or Permission Sets. This allows administrators to enforce granular control, ensuring that only authorised integration service accounts or specific business personas can execute the Connected App flow. Furthermore, architects must combine pre-authorisation with strict session and network security policies:</p>
        <ul>
          <li><strong>IP Relaxation Policies:</strong> By default, Salesforce enforces standard user IP restrictions on Connected App logins. However, administrators can configure the Connected App to relax IP restrictions or strictly enforce them. For high-security integrations, architects should enforce corporate network IP ranges, ensuring that the integration can only connect from designated static server IPs.</li>
          <li><strong>Token Validity and Expiration:</strong> The lifetime of refresh tokens should be tightly controlled. While integrations require persistent connections, leaving refresh tokens active indefinitely creates a long-term exposure risk. Connected Apps should be configured to expire refresh tokens if they are not used within a specific period (e.g., 30 days) or to enforce immediate expiration upon use.</li>
          <li><strong>Session Timeouts:</strong> Enforce short session timeouts for the access tokens generated by the Connected App, limiting the window of opportunity for an intercepted token to be utilised by an attacker.</li>
        </ul>
        <p>By defining these policies at the Connected App level, organisations can align their Salesforce integration endpoints with broader corporate security and network perimeter standards.</p>

        <h2 id="s5">5. Advanced Auditing and Continuous Compliance Monitoring</h2>
        <p>Governance is not a static configuration; it requires continuous monitoring, auditing, and threat detection. Even with perfectly configured Connected Apps, security teams must regularly audit active OAuth tokens, monitor API usage patterns, and immediately revoke stale or suspicious authorizations. Salesforce provides several system objects and tools to inspect and manage Connected App sessions, but tech leaders must automate this monitoring to scale compliance effectively.</p>
        <p>The primary object for auditing active OAuth authorizations is the <code>OauthToken</code> object. This object represents the active sessions and refresh tokens generated by users and integrations for various Connected Apps. Security administrators can query this object using SOQL to identify active integration sessions, track token usage counts, and isolate inactive integrations that pose an unnecessary security risk. The following SOQL query represents a robust auditing utility to locate active OAuth tokens that have not been utilised in the last 30 days:</p>

<pre><code class="language-java">SELECT Id, AppName, UserId, User.Name, User.Username, CreatedDate, LastUsedDate, UseCount 
FROM OauthToken 
WHERE LastUsedDate < LAST_N_DAYS:30 
ORDER BY LastUsedDate DESC</code></pre>

        <p>To manage this risk proactively, architects should implement automated cleanup mechanisms. The following Apex batch class demonstrates how to programmatically identify and revoke inactive OAuth tokens, ensuring that stale integration sessions are systematically pruned from the database, reducing the overall blast radius of credential exposure:</p>

<pre><code class="language-java">global class InactiveTokenRevocationBatch implements Database.Batchable<sObject> {
    global Database.QueryLocator start(Database.BatchableContext BC) {
        // Query OAuth tokens that have not been used in the last 30 days
        return Database.getQueryLocator([
            SELECT Id, AppName, UserId, LastUsedDate 
            FROM OauthToken 
            WHERE LastUsedDate < LAST_N_DAYS:30
        ]);
    }
    
    global void execute(Database.BatchableContext BC, List<OauthToken> scope) {
        if (!scope.isEmpty()) {
            try {
                // Delete the inactive token records to revoke access immediately
                delete scope;
                System.debug('Successfully revoked ' + scope.size() + ' inactive OAuth tokens.');
            } catch (DmlException e) {
                System.debug('Error revoking inactive tokens: ' + e.getMessage());
            }
        }
    }
    
    global void finish(Database.BatchableContext BC) {
        // Implement completion notifications or logging as required by compliance
    }
}</code></pre>

        <p>In addition to programmatic token cleanup, security teams should leverage Salesforce Event Monitoring (part of Salesforce Shield) to capture detailed API logs. Every API transaction executed via a Connected App generates entries in the <code>ApiEvent</code>, <code>RestApiEvent</code>, or <code>LightningUriEvent</code> logs. By streaming these event logs into a centralised Security Information and Event Management (SIEM) system like Splunk, Microsoft Sentinel, or Datadog, organisations can establish real-time alerting for anomalous behaviour, such as an integration executing a sudden spike in record downloads or attempting to access unauthorised endpoints. Continuous compliance monitoring ensures that the perimeter remains secure, even as the enterprise integration landscape evolves.</p>
"""

sec_007_takeaways = """
            <li>Connected Apps serve as metadata gateways rather than data containers, defining OAuth identity and security boundaries for external applications.</li>
            <li>Deprecate the highly vulnerable OAuth User-Agent flow in server-side integrations, replacing it with the secure JWT Bearer flow.</li>
            <li>Enforce the principle of least privilege by avoiding the <code>full</code> scope and configuring granular API scopes for each unique integration.</li>
            <li>Transition from client secrets to certificate-based authentication using asymmetric keys to prevent credential leakage in source code repositories.</li>
            <li>Configure Connected App policies to "Admin approved users are pre-authorised" to block rogue third-party app access.</li>
            <li>Implement automated token auditing and revocation using Apex batches to prune inactive OAuth sessions and minimise the attack surface.</li>
"""

sec_007_quiz = """
          <div class="quiz-question" id="q1">
            <p><strong>Question 1:</strong> Which OAuth flow is highly recommended for secure, non-interactive machine-to-machine integrations in Salesforce?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. OAuth User-Agent Flow</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. OAuth Authorisation Code Flow</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'right')">C. OAuth JWT Bearer Flow</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Username-Password Flow</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q2">
            <p><strong>Question 2:</strong> What is the primary security risk of assigning the 'full' scope to a Salesforce Connected App?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. It increases the API request usage count by double.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">B. It forces the authenticating user to reset their password.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'right')">C. It grants absolute access to all data, metadata, and APIs, bypassing standard boundary controls.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. It automatically disables IP restrictions for the integration profile.</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q3">
            <p><strong>Question 3:</strong> How should a Salesforce administrator enforce strict control over which specific users can utilise a Connected App?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. Leave Permitted Users as 'All users may self-authorise' and monitor logs.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'right')">B. Set Permitted Users to 'Admin approved users are pre-authorised' and assign specific Profiles or Permission Sets.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. Change the OAuth client secret every 24 hours.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Encrypt all user passwords using probabilistic encryption keys.</div>
            </div>
          </div>
"""

# SEC-008 Content
sec_008_summary = """
            <li>Understand the multi-tiered network perimeter security model of the Salesforce platform.</li>
            <li>Compare the behaviour and operational boundaries of Trusted IP Ranges versus Login IP Ranges.</li>
            <li>Implement strict IP-based restriction profiles to lock down access to corporate networks.</li>
            <li>Secure integration endpoints using mutual SSL/TLS authentication and whitelisted external IPs.</li>
            <li>Track, audit, and analyse login activities to proactively identify network security anomalies.</li>
            <li>Construct a robust administrative disaster recovery protocol to manage emergency network lockouts.</li>
"""

sec_008_toc = """
            <li><a href="#s1">1. Salesforce Network Perimeter Architecture</a></li>
            <li><a href="#s2">2. Trusted IP Ranges vs. Profile-Level Login IP Ranges</a></li>
            <li><a href="#s3">3. Securing Enterprise Integration and API Access</a></li>
            <li><a href="#s4">4. Strategic Deployment Patterns for Corporate VPNs and Edge Gateways</a></li>
            <li><a href="#s5">5. Login Auditing, Alerting, and Disaster Recovery Protocols</a></li>
"""

sec_008_body = """
        <h2 id="s1">1. Salesforce Network Perimeter Architecture</h2>
        <p>For large organisations and financial institutions, securing access to cloud platforms begins at the network layer. Salesforce is a multi-tenant SaaS application operating on public cloud infrastructure and Salesforce-owned data centres. Because it is globally accessible via the public internet, defining clear network perimeters is a vital security requirement. Network security in Salesforce is not governed by a single firewall rule or a physical gate; instead, it is a multi-tiered, software-defined architecture that evaluates the origin of every incoming request before allowing authentication to proceed.</p>
        <p>When a client application or an employee attempts to connect to a Salesforce instance, the request passes through several logical checkpoints. These checkpoints include DNS routing, Edge Services (such as My Domain and Salesforce Edge Network), SSL/TLS decryption, and application-level network security evaluations. Architects must understand that network security is evaluated before any user-level authorization (like profile permissions or sharing rules) is verified. If the incoming request originates from an unauthorised IP address or fails TLS compliance checks, the session is terminated immediately, preventing exposure of the login interface or API endpoints.</p>
        <p>My Domain plays a pivotal role in this architecture by establishing a unique, custom subdomain for the organisation's Salesforce instance (e.g., <code>mycompany.my.salesforce.com</code>). Beyond brand identity, My Domain acts as a routing control point. It allows organisations to enforce modern security standards, such as restricting login endpoints to single sign-on (SSO) providers, enforcing HTTP Strict Transport Security (HSTS), and disabling default login paths (like <code>login.salesforce.com</code>). This forces all traffic to route through corporate-approved channels where network policies, proxy inspections, and context-aware security tools can be applied before the request ever reaches the Salesforce database container.</p>
        <p>In the era of Salesforce Hyperforce, the traditional paradigm of static network whitelisting undergoes a massive shift. Under the legacy infrastructure, organisations could rely on static IP address blocks provided by Salesforce data centres to filter outbound traffic. However, Hyperforce operates on public cloud infrastructure (such as AWS), utilising highly dynamic IP routing and elastic scaling. This means that outbound IP addresses are dynamic and subject to frequent change without notice. Relying on static IP whitelisting for outbound integrations or routing is a major anti-pattern in Hyperforce, as it leads to connection failures. Architects must modernise their network security models, transitioning from static IP whitelisting to secure domain-based filtering, mutual SSL/TLS (mTLS), or utilising Secure Agent gateways that tunnel traffic through a secure endpoint without relying on fixed public IPs.</p>

        <h2 id="s2">2. Trusted IP Ranges vs. Profile-Level Login IP Ranges</h2>
        <p>Within Salesforce, network restrictions are primarily configured using two features that sound similar but behave in fundamentally different ways: Org-Wide Trusted IP Ranges (Network Access) and Profile-Specific Login IP Ranges. Misunderstanding the difference between these two features is a common architectural error that can lead to either critical security gaps or massive user disruption.</p>
        <p><strong>Org-Wide Trusted IP Ranges (Network Access):</strong> Configured at the global organisation level under Setup -> Security -> Network Access. These ranges represent a list of trusted networks from which users are expected to connect (e.g., corporate office networks). The critical security behaviour to understand is that Org-Wide Trusted IP Ranges <em>do not block access</em> from outside these ranges. If a user attempts to log in from an IP address that is not on the Trusted list, they are not denied entry. Instead, Salesforce triggers a Multi-Factor Authentication (MFA) or identity verification challenge (such as sending a verification code via email or mobile). Once the user successfully completes the verification challenge, they are granted access. Effectively, Org-Wide Trusted IP Ranges act as a trust-elevation tool, allowing users within known corporate offices to log in seamlessly without repetitive verification prompts while requiring active verification for remote or home networks.</p>
        <p><strong>Profile-Specific Login IP Ranges:</strong> Configured at the Individual Profile level under Setup -> Users -> Profiles -> [Profile Name] -> Login IP Ranges. Unlike the Org-wide settings, Profile-level Login IP Ranges represent a <em>hard security perimeter</em>. If a user's profile is configured with specific Login IP Ranges, Salesforce strictly denies login attempts from any IP address outside those ranges. There is no fallback verification challenge, no MFA prompt, and no bypass. The login attempt is immediately terminated at the perimeter, and the user receives a generic "Invalid Username or Password" message to prevent username validation harvesting. The following table provides a direct architectural comparison of these two features:</p>

        <table style="width:100%; border-collapse:collapse; margin:20px 0;">
          <thead>
            <tr style="background-color:var(--bg-secondary); border-bottom:2px solid var(--border);">
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">Feature</th>
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">Configuration Level</th>
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">Behaviour Outside Range</th>
              <th style="padding:12px; text-align:left; font-family:var(--font-ui); font-weight:600;">Primary Use Case</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-weight:600;">Trusted IP Ranges</td>
              <td style="padding:12px;">Global Org Level</td>
              <td style="padding:12px; color:var(--saffron); font-weight:600;">Requires identity verification / MFA challenge</td>
              <td style="padding:12px;">Exempting office users from repeated verification prompts.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px; font-weight:600;">Login IP Ranges</td>
              <td style="padding:12px;">Individual Profile Level</td>
              <td style="padding:12px; color:var(--red); font-weight:600;">Immediate denial of login, no challenge offered</td>
              <td style="padding:12px;">Locking down high-privilege admins or API integrations to trusted IPs.</td>
            </tr>
          </tbody>
        </table>

        <p>Architects must leverage Profile-level Login IP Ranges for all sensitive roles. System administrators, integration service accounts, and financial controllers should always be assigned to profiles that restrict login access exclusively to secure corporate networks, VPN gateways, and trusted static servers. Allowing these high-privilege profiles to log in from arbitrary home or public networks exposes the entire platform to compromise if a user's local device is compromised or their credentials are harvested via phishing attacks.</p>

        <h2 id="s3">3. Securing Enterprise Integration and API Access</h2>
        <p>While securing user access via the browser is critical, protecting API endpoints and integration channels is equally important. External applications connecting to Salesforce via APIs represent a major attack vector if they are not constrained by strict network security policies. Because API integrations typically execute programmatically without human intervention, they are highly susceptible to credential stuffing and brute-force attacks if left open to the public internet.</p>
        <p>To secure inbound API connections, architects must implement a double-locked security pattern. First, the integration user profile must be constrained by specific Login IP Ranges. If the external integration runs from a dedicated enterprise service bus (ESB) or an ETL system hosted in an AWS or Azure virtual private cloud, the static outgoing IP addresses of those gateways must be whitelisted on the integration profile in Salesforce. This ensures that even if the integration's OAuth credentials or passwords are stolen, they cannot be used from an unauthorised network.</p>
        <p>Second, for ultra-high security environments, organisations should implement Mutual SSL/TLS (mTLS). In standard TLS, Salesforce presents its certificate to the client to verify its identity, encrypting the channel. In a mutual TLS architecture, both the client and Salesforce verify each other's certificates. Administrators upload the client's public certificate to Salesforce and configure My Domain to require mTLS on specific endpoints (e.g., <code>https://mycompany.my.salesforce.com:8443</code>). This ensures that any API request lacking a valid client-side cryptographic certificate signed by a trusted authority is rejected at the network layer, long before authentication is even attempted. For outbound calls from Salesforce to external APIs, architects must configure Named Credentials to securely handle certificates, routing calls exclusively through corporate-approved APIs.</p>
        <p>The technical implementation of mutual TLS (mTLS) in Salesforce is extremely robust, leveraging the standard HTTP handshake with certificate exchange. When an inbound request reaches the Salesforce gateway, the client initiates the TLS session. Salesforce presents its platform certificate, and in response, the client must present a valid, unrevoked client certificate. Salesforce validates this certificate against the Certificate Authority (CA) trust store or the specific certificates uploaded under Setup -> Security -> Mutual Authentication Certificates. If the validation succeeds, the gateway populates the <code>MutualAuthenticationStatus</code> of the session. If the certificate is missing or invalid, the session is terminated before any Apex controller or API code executes. For outbound calls, architects must utilise Named Credentials configured with a client certificate, which instructs the runtime engine to automatically attach the cryptographic signature to the outbound request, ensuring that the target external API can verify the identity of the calling Salesforce instance.</p>

        <h2 id="s4">4. Strategic Deployment Patterns for Corporate VPNs and Edge Gateways</h2>
        <p>Implementing strict IP whitelisting in a modern, distributed enterprise poses significant operational challenges. With the rise of remote working, mobile workforces, and cloud-first application architectures, employees and services are rarely confined within the physical walls of a corporate office. Enforcing static IP ranges can inadvertently disrupt legitimate users who connect from dynamic home ISPs, mobile networks, or client sites. To resolve this tension between security and usability, architects must design comprehensive routing architectures using corporate VPNs and edge gateways.</p>
        <p>The standard architectural pattern for securing remote access is to channel all Salesforce-directed network traffic through a centralised corporate Virtual Private Network (VPN) or Secure Access Service Edge (SASE) solution, such as zScaler, Palo Alto Prisma, or Cloudflare Gateway. In this model, the remote worker's local machine establishes an encrypted tunnel to the enterprise VPN. All web requests destined for Salesforce are routed through this secure tunnel and egress from the corporate gateway via a designated pool of static IP addresses. Salesforce is then configured to only permit logins from these static egress IPs. If a user attempts to access Salesforce directly from their home network without activating the corporate VPN, the connection is blocked at the profile level.</p>
        <p>For mobile applications, architects should enforce Mobile Device Management (MDM) profiles that push pre-configured secure VPN tunnels (per-app VPNs) to corporate mobile devices. This ensures that when the Salesforce mobile app launches, it automatically establishes a VPN tunnel to the corporate network, routing all API requests through the whitelisted egress IPs. For developers and external contractors, organisations should construct dedicated jump hosts or Virtual Desktop Infrastructure (VDI) environments within the corporate network, whitelisting only the VDI gateway IPs in Salesforce. This prevents code or sensitive data from being extracted to personal devices, maintaining an unbroken chain of custody.</p>

        <h2 id="s5">5. Login Auditing, Alerting, and Disaster Recovery Protocols</h2>
        <p>No network security strategy is complete without comprehensive auditing, real-time threat detection, and disaster recovery planning. IP whitelisting is a powerful control, but it is also highly fragile. A single incorrect CIDR block entered during a routine deployment can lock out the entire administrative team, bringing business operations to a complete standstill. Conversely, undetected network compromises can allow attackers to bypass standard identity verification if IP ranges are loosely defined.</p>
        <p>To audit network compliance, security teams must actively monitor the <code>LoginHistory</code> object. This object captures detailed metadata for every login attempt, including the login time, source IP address, login type (UI vs. API), client browser details, and the outcome (Success or Failure). System administrators can query this history to locate perimeter violations. The following SOQL query isolates all failed login attempts caused by IP restriction violations, providing immediate visibility into potential attacks or misconfigured integration clients:</p>

<pre><code class="language-java">SELECT Id, UserId, User.Username, LoginTime, LoginType, SourceIp, Status, ClientVersion 
FROM LoginHistory 
WHERE Status = 'Failed: IP Limit Exceeded' 
ORDER BY LoginTime DESC</code></pre>

        <p>To scale this monitoring, architects should integrate these logs with an enterprise Security Information and Event Management (SIEM) system. Using the Salesforce REST API, security tools can continuously ingest `LoginHistory` records and trigger automated alerts when a spike in failed logins originates from suspicious geographic regions or unknown networks. Real-time transaction security policies can also be written to intercept high-volume logins from unusual ranges.</p>
        <p>Finally, organisations must establish a robust "break-glass" administrative recovery protocol to mitigate the risk of permanent lockouts. If the corporate VPN suffers a catastrophic outage and all administrators are locked out of Salesforce due to profile IP restrictions, recovery can be incredibly difficult, often requiring manual escalation to Salesforce Support, which can take hours. To prevent this, organisations must maintain a highly restricted "break-glass" admin account. This account must be exempt from profile-level Login IP Ranges, permitting access from the public internet. However, to secure this backdoor, the account must be protected by physical hardware MFA tokens (such as FIDO2/WebAuthn security keys), require complex multi-character passwords that are rotated frequently, and have its credentials split and stored in a secure physical safe. Furthermore, any login attempt on this break-glass account must immediately trigger high-priority SMS and email alerts to the executive security team, ensuring absolute accountability and transparency.</p>
        <p>In addition to runtime alerts, the modification of network access controls itself must be audited with maximum scrutiny. Any change to the Org-Wide Trusted IP Ranges or Profile-Level Login IP Ranges represents a critical security event. Salesforce immediately records these actions in the Setup Audit Trail under the <code>manageIpRanges</code> action in the <code>security</code> section. To prevent unauthorised modifications or "shadow whitelisting" (where an attacker temporarily adds an IP range to exfiltrate data and then removes it), compliance teams must build daily audit reports that search specifically for this action. Furthermore, any modification of high-privilege profiles must trigger a real-time notification to the Chief Information Security Officer (CISO), guaranteeing that no backdoor network pathways are established under the guise of routine maintenance.</p>
"""

sec_008_takeaways = """
            <li>Salesforce network security operates as a multi-tiered perimeter, evaluating the source IP address before verifying credentials or session authorization.</li>
            <li>Understand the critical difference: Trusted IP Ranges exempt users from MFA challenges, while Profile-Specific Login IP Ranges strictly deny access.</li>
            <li>Always enforce strict Login IP Ranges on the profiles of system administrators and automated integration service accounts.</li>
            <li>Implement Mutual TLS (mTLS) for high-security integration endpoints to require client-side cryptographic certificates at the network layer.</li>
            <li>Route distributed user traffic through corporate VPNs with static egress IPs to align remote workforces with strict whitelisting policies.</li>
            <li>Maintain a secure break-glass administrator account exempt from IP ranges, protected by physical hardware MFA, to prevent permanent lockout.</li>
"""

sec_008_quiz = """
          <div class="quiz-question" id="q1">
            <p><strong>Question 1:</strong> What is the immediate result if a user tries to log in from an IP address not listed in their Profile's Login IP Ranges?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. The user is prompted for Multi-Factor Authentication (MFA).</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. The user is prompted to verify their identity via email.</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'right')">C. The login attempt is immediately denied without offering any verification challenge.</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. The user's password is automatically reset.</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q2">
            <p><strong>Question 2:</strong> What is the primary purpose of configuring Org-Wide Trusted IP Ranges (Network Access)?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. To completely block all inbound API traffic originating outside the specified ranges.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'right')">B. To exempt users logging in from trusted corporate networks from identity verification and MFA challenges.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. To encrypt all data transmitted between Salesforce and the client browser.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. To automatically log out users when they exit the corporate office perimeter.</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q3">
            <p><strong>Question 3:</strong> What security mechanism should be implemented alongside IP whitelisting to protect programmatic machine-to-machine integrations?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. Standard username and password authentication without HTTPS.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. Periodic user password resets via automated Apex scripts.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'right')">C. Mutual SSL/TLS (mTLS) with client certificate verification at the gateway level.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Disabling Single Sign-On (SSO) for all API integration profiles.</div>
            </div>
          </div>
"""

# SEC-009 Content
sec_009_summary = """
            <li>Design a compliant framework for identifying and categorising Personally Identifiable Information (PII) within Salesforce.</li>
            <li>Compare the technical trade-offs between data anonymisation, data masking, and permanent deletion.</li>
            <li>Master the use of Salesforce Shield Platform Encryption to protect PII at rest without sacrificing system usability.</li>
            <li>Build automated Apex batch processes to securely anonymise or delete PII upon customer request.</li>
            <li>Implement secure sandbox masking using Salesforce Data Mask to protect production data in non-production environments.</li>
            <li>Establish robust audit trails to track PII access, modifications, and erasure operations for regulatory compliance.</li>
"""

sec_009_toc = """
            <li><a href="#s1">1. Personally Identifiable Information and Global Regulatory Mandates</a></li>
            <li><a href="#s2">2. Securing PII at Rest with Salesforce Shield Platform Encryption</a></li>
            <li><a href="#s3">3. Erasure vs. Anonymisation vs. UI Masking: Architectural Paradigms</a></li>
            <li><a href="#s4">4. Building Automated Erasure and Anonymisation Engines via Apex</a></li>
            <li><a href="#s5">5. Enterprise Sandbox Governance: Hardening Environments with Data Mask</a></li>
"""

sec_009_body = """
        <h2 id="s1">1. Personally Identifiable Information and Global Regulatory Mandates</h2>
        <p>In the digital economy, personal data has become both an invaluable asset and a massive compliance liability. Global privacy regulations such as the General Data Protection Regulation (GDPR) in the European Union, the California Consumer Privacy Act (CCPA/CPRA) in the United States, and the Personal Information Protection and Electronic Documents Act (PIPEDA) in Canada have transformed how organisations must handle customer information. At the centre of these frameworks is Personally Identifiable Information (PII)&mdash;any data that can be used to identify, contact, or locate a specific individual. Salesforce, being the primary CRM platform for thousands of global enterprises, routinely stores vast repositories of PII, making it a primary focus for compliance officers and security auditors.</p>
        <p>Under regulations like GDPR, individuals are granted fundamental rights regarding their personal data. These rights include the Right of Access (requesting a copy of all stored personal data), the Right to Rectification (updating incorrect records), and, most critically, the Right to Erasure, also known as the Right to Be Forgotten. If a customer exercises their right to erasure, the organisation must completely and permanently remove all traces of their PII from its active systems and backups within strict statutory timeframes. Failure to comply can result in catastrophic financial penalties, reaching up to 4% of global annual turnover or &euro;20 million, whichever is greater.</p>
        <p>To build a compliant architecture, tech leaders must first map out where PII resides within their Salesforce database schema. PII is rarely confined to a single field; it is highly distributed across standard objects (such as Lead, Contact, Account, User, and Individual) and custom objects. Common PII fields include names, home addresses, email addresses, phone numbers, passport details, social security numbers, credit card details, and even dynamic IP addresses. Architects must implement a formal data classification process, categorising every field in the system by sensitivity and compliance tags. Salesforce supports native Data Classification metadata fields (such as Data Owner, Field Usage, Data Sensitivity Level, and Compliance Group), which must be systematically applied to ensure visibility and facilitate automated compliance handling.</p>

        <h2 id="s2">2. Securing PII at Rest with Salesforce Shield Platform Encryption</h2>
        <p>Once PII is identified and classified, the next architectural priority is securing that data at rest. While Salesforce encrypts data in transit using standard HTTPS/TLS protocols, protecting the underlying physical database files from unauthorized physical access or database extraction requires encryption at rest. The primary tool for this in the Salesforce ecosystem is Shield Platform Encryption. Unlike classic encryption, which only masks fields on the user interface and has significant limitations, Shield Platform Encryption allows organisations to encrypt sensitive data natively while maintaining critical platform functionality.</p>
        <p>When architecting Shield Platform Encryption, a fundamental decision is choosing between Probabilistic and Deterministic encryption. Each method has distinct cryptographic behaviours and significant architectural trade-offs:</p>
        <ul>
          <li><strong>Probabilistic Encryption:</strong> The most secure form of encryption. It uses a unique random initialization vector for every field value, meaning that the same plaintext input (e.g., "John") will generate completely different ciphertext values each time it is stored in the database. While highly secure, it strictly prevents any database filtering or index matching. If a field is probabilistically encrypted, users cannot use it in SOQL <code>WHERE</code> clauses, report filters, list view search criteria, or duplicate management rules. It is best suited for highly sensitive, non-searchable fields like credit card numbers or passport IDs.</li>
          <li><strong>Deterministic Encryption:</strong> Address the search limitations of probabilistic encryption by utilising a static, predictable key derivation process. With deterministic encryption, the same plaintext input (e.g., "John") always generates the identical ciphertext value in the database. This allows Salesforce to perform index matches, enabling users to filter records in report criteria, list views, and SOQL queries using exact match operators (e.g., <code>Contact.Email = 'john@example.com'</code>). However, wildcards, partial matches, and case-insensitive searches are still restricted. Deterministic encryption is the recommended standard for searchable PII fields like email addresses, phone numbers, and names.</li>
        </ul>
        <p>Architects must carefully evaluate these encryption types and manage the underlying key lifecycle. Shield Platform Encryption operates on a tenant-specific key model, allowing organisations to generate, rotate, and revoke encryption keys on-demand, or even bring their own key (BYOK) generated via external hardware security modules (HSMs). However, encryption adds computational overhead and restricts certain advanced Salesforce platform features, such as criteria-based sharing rules, formula fields referencing encrypted fields, and standard list view sorting. Therefore, encryption should be applied selectively, targeting only true PII fields identified during the classification phase.</p>

        <h2 id="s3">3. Erasure vs. Anonymisation vs. UI Masking: Architectural Paradigms</h2>
        <p>When addressing a customer's request for data removal, architects must choose the appropriate data sanitisation paradigm. A common mistake is assuming that compliance requires the complete deletion of the physical record. In reality, privacy regulations like GDPR permit multiple compliance pathways, each with different technical trade-offs. The three primary paradigms are permanent Deletion, Anonymisation, and UI Masking.</p>
        <p><strong>Permanent Deletion (Erasure):</strong> In Salesforce, executing a standard DML delete operation (e.g., deleting a Contact record) is a soft-delete. The record is not immediately purged from the database; instead, it is moved to the Recycle Bin, where it remains for 15 days, retrievable by administrators or API clients. To satisfy strict privacy mandates, a soft-delete is insufficient. The record must be permanently expunged. This requires a two-step process: deleting the record and then executing an emptyRecycleBin call to bypass the recovery window. Furthermore, physical deletion can break downstream analytical systems. If a customer contact record is completely deleted, historical financial reports, sales metrics, and activity pipelines lose their referential integrity, leading to distorted business intelligence. Thus, absolute deletion should be reserved for cases where preservation of history is completely unnecessary.</p>
        <p><strong>Anonymisation:</strong> The preferred architectural pattern for enterprise CRMs. Anonymisation involves overwriting all identifiable PII fields with generic, non-reversible, or randomized placeholder values (e.g., changing FirstName to "Anonymised" and LastName to "Individual_10398"). This satisfies GDPR erasure requirements because the natural person can no longer be identified from the record, either directly or in combination with other data. Critically, anonymisation preserves the structural integrity of the database. The Contact record remains linked to past Opportunities, Cases, and Tasks, allowing financial reports and activity metrics to remain statistically accurate without exposing personal information. The following list contrasts the core differences between erasure, anonymisation, and masking:</p>
        <ul>
          <li><strong>Erasure (Hard Delete):</strong> Permanent database purge. Destroys relational links, breaks historical analytics, but leaves zero trace of the record.</li>
          <li><strong>Anonymisation:</strong> Overwrites PII with randomized values. Preserves historical reporting, maintains database referential integrity, and satisfies legal erasure standards.</li>
          <li><strong>UI Masking:</strong> Obfuscates fields visually on the user interface (e.g., displaying `***-**-6789`) while leaving the underlying database values fully intact in plaintext. Masks protect data from internal user exposure but do not satisfy erasure mandates for external subjects.</li>
        </ul>
        <p>By mapping business reporting requirements to these paradigms, tech leaders can implement a compliant privacy strategy that protects both customer confidentiality and critical operational metrics.</p>

        <h2 id="s4">4. Building Automated Erasure and Anonymisation Engines via Apex</h2>
        <p>Executing anonymisation or permanent erasure manually is highly inefficient and prone to operational error. In an enterprise environment receiving hundreds of privacy requests monthly, the compliance pipeline must be fully automated. Architects should design a programmatic engine using Apex batch classes to search for, sanitise, and hard-delete or anonymise customer data systematically.</p>
        <p>When designing an automated Apex anonymisation engine, developers must account for cascading relationships. Overwriting PII on the Contact record is useless if the user's name, email, and phone number remain active in related records, such as custom objects, task comments, or audit tables. The Apex class must navigate the relational graph, identifying child objects that also contain PII. The following Apex batch class demonstrates a production-ready, bulk-safe pattern for anonymising customer Contact data whose privacy status is set to 'Erasure Requested'. It overwrites standard PII fields and marks the record as successfully anonymised:</p>

<pre><code class="language-java">global class ContactPiiAnonymisationBatch implements Database.Batchable<sObject>, Database.Stateful {
    private Integer processedCount = 0;
    
    global Database.QueryLocator start(Database.BatchableContext BC) {
        // Locate Contacts who have requested erasure and are not yet anonymised
        return Database.getQueryLocator([
            SELECT Id, FirstName, LastName, Email, Phone, MobilePhone, MailingStreet, MailingCity, Privacy_Status__c 
            FROM Contact 
            WHERE Privacy_Status__c = 'Erasure Requested'
        ]);
    }
    
    global void execute(Database.BatchableContext BC, List<Contact> scope) {
        List<Contact> contactsToUpdate = new List<Contact>();
        
        for (Contact c : scope) {
            // Overwrite PII with generic, non-reversible placeholders
            c.FirstName = 'Anonymised';
            c.LastName = 'Individual_' + c.Id;
            c.Email = 'anonymised_' + c.Id + '@invalid-domain.com';
            c.Phone = '0000000000';
            c.MobilePhone = '0000000000';
            c.MailingStreet = 'Anonymised Street';
            c.MailingCity = 'Anonymised City';
            c.Privacy_Status__c = 'Anonymised'; // Transition status
            
            contactsToUpdate.add(c);
            processedCount++;
        }
        
        if (!contactsToUpdate.isEmpty()) {
            try {
                // Perform the updates, bypass triggering of heavy downstream logic where appropriate
                Database.SaveResult[] srList = Database.update(contactsToUpdate, false);
                for (Database.SaveResult sr : srList) {
                    if (!sr.isSuccess()) {
                        for (Database.Error err : sr.getErrors()) {
                            System.debug('Contact Anonymisation Error: ' + err.getMessage());
                        }
                    }
                }
            } catch (Exception e) {
                System.debug('Batch Execution failed: ' + e.getMessage());
            }
        }
    }
    
    global void finish(Database.BatchableContext BC) {
        System.debug('PII Anonymisation process completed. Total records processed: ' + processedCount);
        // Execute supplementary tasks, such as triggering an audit log entry or alerting compliance teams
    }
}</code></pre>

        <p>Architects must ensure that this batch class runs within a secure governance context. When anonymising fields, ensure that any history tables tracking changes (like ContactHistory) do not store the original values in plaintext indefinitely. If Field History Tracking is active on encrypted or anonymised fields, work with Salesforce Support or implement Field Audit Trail to define short retention periods for historical tables, ensuring complete data sanitisation across all system storage tiers.</p>

        <h2 id="s5">5. Enterprise Sandbox Governance: Hardening Environments with Data Mask</h2>
        <p>A critical security vulnerability that compliance officers and security audits routinely uncover is data leakage through non-production environments. Sandboxes (Full, Copy, Developer Pro, and Developer) are essential for application development, testing, and training. However, when a sandbox is refreshed, it copies all production data, including active customer PII, to a less-secure non-production environment. Developers, external contractors, and testing teams who lack authorisation to view production customer PII are suddenly granted access to live emails, phone numbers, and addresses in the sandbox.</p>
        <p>To eliminate this massive compliance vulnerability, tech leaders must establish a strict sandbox governance policy, utilizing Salesforce Data Mask to sanitise non-production environments automatically. Salesforce Data Mask is an administrative security tool that runs directly inside the newly refreshed sandbox, obfuscating production data using native cryptographic algorithms. By applying Data Mask, organisations can replace raw production PII with realistic, mock datasets. The tool supports three primary masking methodologies, which should be configured according to the sensitivity of each field:</p>
        <ul>
          <li><strong>Anonymisation (Substitution):</strong> Replaces the production value with a randomly generated but realistic mock value. For example, a real customer email (e.g., `alice.smith@gmail.com`) is replaced with a syntactically correct fake email (e.g., `johndoe123@example.org`). This is the ideal approach for developer sandboxes, as it allows developers to test validation rules, integration triggers, and email formats with realistic data structures without exposing actual customers.</li>
          <li><strong>Pseudonymisation (Pattern Masking):</strong> Replaces a string with a standardized pattern or characters, preserving some formatting. For example, a real phone number `+44 7700 900077` can be masked to `+44 **** ******`, hiding the identity while preserving the country prefix. This is best for training environments where formatting and data structures are important.</li>
          <li><strong>Deletion:</strong> Completely purges the field contents, replacing them with a null value. This should be applied to highly sensitive fields that have no utility in development, such as credit card credentials, passport numbers, and bank details.</li>
        </ul>
        <p>By integrating Salesforce Data Mask into the standard sandbox refresh checklist, architects can guarantee that developers and offshore testing partners work in fully compliant environments. This mitigates the risk of external data breach and maintains an airtight boundary between production operations and software delivery pipelines.</p>
"""

sec_009_takeaways = """
            <li>Global privacy mandates like GDPR and CCPA grant individuals clear legal rights to request complete erasure of their PII from active databases.</li>
            <li>Conduct a thorough data mapping and classification process using Salesforce's native Data Classification metadata tags to catalog PII.</li>
            <li>Selective application of deterministic encryption is required for searchable PII fields, while probabilistic encryption secures non-searchable values.</li>
            <li>Prefer Anonymisation over physical database Deletion to preserve database relational integrity and statistical reporting pipelines.</li>
            <li>Build robust, bulk-safe Apex batch classes to automate complex data sanitisation and anonymisation workflows for compliance.</li>
            <li>Mandate the use of Salesforce Data Mask on newly refreshed sandboxes to obfuscate production PII before granting developer or tester access.</li>
"""

sec_009_quiz = """
          <div class="quiz-question" id="q1">
            <p><strong>Question 1:</strong> Which encryption type in Salesforce Shield Platform Encryption allows exact-match SOQL queries on encrypted fields?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Probabilistic Encryption</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'right')">B. Deterministic Encryption</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">C. Symmetric Encryption</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Asymmetric Encryption</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q2">
            <p><strong>Question 2:</strong> Why is data anonymisation generally preferred over permanent deletion (hard delete) for active CRM contact records?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. Anonymisation does not require any Apex code to execute.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'right')">B. It satisfies privacy regulations while maintaining database referential integrity and the statistical accuracy of historical reporting.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. It automatically re-indexes the search results in the system.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. It completely disables the Recycle Bin for all system objects.</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q3">
            <p><strong>Question 3:</strong> What tool should be used to protect production customer PII from leaking into developer sandboxes during a refresh?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. Org-Wide Trusted IP Ranges</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. Shield Setup Audit Trail</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'right')">C. Salesforce Data Mask</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. Visualforce Encryption Mask</div>
            </div>
          </div>
"""

# SEC-010 Content
sec_010_summary = """
            <li>Deeply understand the capabilities and limitations of Salesforce's native auditing mechanisms.</li>
            <li>Master Setup Audit Trail to track structural metadata modifications and administrative actions.</li>
            <li>Implement Real-Time Event Monitoring to capture granular user activities like report exports and API queries.</li>
            <li>Write proactive Transaction Security Policies to block unauthorised data exfiltration in real-time.</li>
            <li>Configure Field Audit Trail (History Retention) to maintain compliant records for up to ten years.</li>
            <li>Integrate Salesforce security logs with enterprise SIEM systems (e.g., Splunk) for consolidated monitoring.</li>
"""

sec_010_toc = """
            <li><a href="#s1">1. The Architecture of Salesforce Auditing and Logging Systems</a></li>
            <li><a href="#s2">2. Monitoring Metadata Configurations with Setup Audit Trail</a></li>
            <li><a href="#s3">3. Real-Time Event Monitoring and User Activity Auditing</a></li>
            <li><a href="#s4">4. Building Proactive Real-Time Transaction Security Policies</a></li>
            <li><a href="#s5">5. Field Audit Trail Governance and Enterprise SIEM Integrations</a></li>
"""

sec_010_body = """
        <h2 id="s1">1. The Architecture of Salesforce Auditing and Logging Systems</h2>
        <p>In high-security enterprise environments, monitoring system state and user activity is a critical governance pillar. Understanding "who did what and when" is not merely an operational convenience; it is a foundational requirement for regulatory compliance, threat response, and forensic analysis. When security incidents occur, the speed and accuracy of the investigation depend entirely on the quality of available system logs. Salesforce provides a robust, multi-layered auditing and logging architecture designed to track both structural metadata changes and transactional data access. However, architects must master the boundaries and capabilities of each component to design an effective security posture.</p>
        <p>The Salesforce auditing ecosystem is divided into three distinct operational layers: metadata auditing, transactional user logging, and historical field tracking. Metadata auditing tracks modifications to the system's configuration (such as profile adjustments, permission set assignments, code deployments, and password policy updates). Transactional user logging captures user interactions with actual record data (such as querying lists, running reports, exporting files, and executing API calls). Historical field tracking captures values changed within individual records over time (such as changes to a contact's credit limit or an opportunity's stage). Each of these layers utilizes different technology stacks and enforces distinct data retention periods:</p>
        <ul>
          <li><strong>Setup Audit Trail:</strong> Tracks configuration and administrative changes. Retains history for 180 days in the UI.</li>
          <li><strong>Event Monitoring:</strong> Captures transactional activities. Provides hourly and daily log files (retained for 30 days dynamically, or up to 1 year via Shield).</li>
          <li><strong>Field History Tracking:</strong> Tracks record-level field modifications. Standard tracking retains logs for 18 months, whereas Shield Field Audit Trail extends retention to 10 years.</li>
        </ul>
        <p>To establish comprehensive visibility, architects must integrate these disjointed systems into a single corporate auditing strategy. Relying solely on default settings leaves significant gaps, as standard data retention limits can result in critical logs being purged before a security incident is identified.</p>

        <h2 id="s2">2. Monitoring Metadata Configurations with Setup Audit Trail</h2>
        <p>The first line of defence in system auditing is the Setup Audit Trail. This utility captures structural, administrative, and configuration modifications made by developers, consultants, and system administrators. Because administrative access grants broad power to alter security settings, bypass validation rules, or create new access points, monitoring these changes is essential to prevent internal threats and configuration drift.</p>
        <p>The Setup Audit Trail tracks an extensive array of actions, including when a user updates password policies, modifies sharing settings, installs a managed package, activates a flows, or modifies profile permissions. One of its most valuable aspects is that it tracks changes made via both the user interface and metadata deployment APIs. While Salesforce displays the last 20 administrative changes directly on the Setup page, administrators can download the previous 180 days of history in CSV format. However, for large enterprise organisations, relying on manual CSV downloads is an operational risk. Changes can be overwritten or missed, and 180 days is often too short a window for annual security audits.</p>
        <p>To secure metadata tracking, architects should automate the extraction of Setup Audit Trail records. Salesforce exposes these logs programmatically via the <code>SetupAuditTrail</code> standard object. Security teams can execute periodic scheduled jobs to extract these records and archive them in an external data lake or compliance repository. The following SOQL query represents a simple, programmatic way to query all administrative actions executed by system administrators in the last 7 days, filtering by critical sections like security and profile changes:</p>

<pre><code class="language-java">SELECT Id, Action, Section, CreatedBy.Name, CreatedBy.Username, CreatedDate, Display 
FROM SetupAuditTrail 
WHERE CreatedDate = LAST_N_DAYS:7 AND (Section = 'security' OR Section = 'profiles' OR Section = 'users') 
ORDER BY CreatedDate DESC</code></pre>

        <p>By automating the retrieval of these records and feeding them into corporate governance pipelines, organisations can establish permanent compliance archives, ensuring that administrative history is preserved indefinitely and is easily searchable for historical forensics.</p>
        <p>When designing an automated metadata monitoring tool, architects must leverage the full schema of the <code>SetupAuditTrail</code> object. The object contains several critical fields, including <code>DelegateUser</code> (the user executing the change on behalf of another user, commonly seen in support scenarios), <code>Action</code> (the specific system action, such as profile editing or permission assignment), <code>Section</code> (the configuration category), and <code>Display</code> (the descriptive text of the change). Programmatically parsing the <code>Display</code> field is essential because it contains granular details, such as the exact permission that was enabled or disabled (e.g., "Enabled Customize Application on Profile System Administrator"). By parsing this string in Apex, organisations can build a custom security dashboard that highlights high-risk modifications, such as the relaxation of session timeout policies or the activation of unauthorised integrations, providing an immediate visual breakdown of administrative activity.</p>

        <h2 id="s3">3. Real-Time Event Monitoring and User Activity Auditing</h2>
        <p>While the Setup Audit Trail captures administrative metadata changes, it does not record user access to actual customer records. If a disgruntled employee exports thousands of client accounts or an API integration queries sensitive credit card data, the Setup Audit Trail will remain blank. To detect and track transactional user activities, organisations must deploy Salesforce Event Monitoring (part of Salesforce Shield).</p>
        <p>Event Monitoring provides granular insight into the daily operations of the Salesforce platform. It captures over 50 unique event types, logging activities such as login attempts, API requests, report runs, dashboard executions, file downloads, search queries, and even individual Visualforce or LWC page loads. These events are compiled into Event Log Files, which are generated hourly or daily and stored as raw log data. To analyze these logs, architects typically ingest them into visualization tools (like CRM Analytics) or stream them into external SIEM engines. The most critical event types for data protection and compliance auditing include the following:</p>
        <ul>
          <li><strong>ReportExportEvent / ReportEvent:</strong> Captures when a user runs, views, or exports a report, logging the specific report ID, the number of records retrieved, and whether the data was downloaded as a CSV or Excel file. This is the primary indicator of bulk data extraction.</li>
          <li><strong>ApiEvent:</strong> Logs all inbound API queries executed via REST, SOAP, or Bulk API, including the query string, source IP address, execution time, and client application details.</li>
          <li><strong>LoginEvent:</strong> Tracks every login transaction in detail, logging the authentication method (e.g., SSO, username/password), source IP address, device properties, and the TLS version utilised by the client.</li>
          <li><strong>UriEvent:</strong> Records when users access specific records via the browser UI, enabling detailed tracking of "read" operations on sensitive custom records.</li>
        </ul>
        <p>By actively analyzing these events, security teams can transition from a reactive logging posture to a proactive threat detection environment, establishing clear baselines for normal user behavior and immediately identifying spikes in data extraction or API usage.</p>
        <p>The processing of Event Log Files requires a deep understanding of their schema and performance impact. For example, the <code>RestApiEvent</code> log contains precise metrics such as <code>RUN_TIME</code> (the total duration of the API transaction in milliseconds), <code>CPU_TIME</code> (the execution time spent in the CPU), <code>URI</code> (the exact REST endpoint called), and <code>RECORD_ID</code> (the specific record queried). By parsing these CSV fields, security tools can map out a record-level audit trail, showing exactly which user retrieved which record and how much system resource was consumed. Crucially, because Event Monitoring runs as an asynchronous, near-real-time logging pipeline, it incurs zero performance overhead on active user transactions. Unlike traditional synchronous database logging, which blocks threads and slows down transactions, Event Monitoring streams logs in the background, allowing organisations to capture millions of transactions per day without degrading platform response times.</p>

        <h2 id="s4">4. Building Proactive Real-Time Transaction Security Policies</h2>
        <p>Standard Event Monitoring is historical; it records activity after it has occurred. While invaluable for forensics, historical logging cannot stop a security breach in progress. To prevent data leakage and enforce strict compliance rules in real-time, architects must configure Real-Time Transaction Security Policies. This feature (part of Salesforce Shield) allows organisations to intercept user actions as they occur and apply immediate security mitigations, such as blocking the transaction, requiring Multi-Factor Authentication, or alerting security administrators.</p>
        <p>Transaction Security Policies are built using the Event Condition Builder (declarative) or programmatically via custom Apex classes that implement the <code>TxnSecurity.EventCondition</code> interface. When a monitored action occurs (such as a user exporting a report, logging in from an unusual device, or executing a high-volume API query), Salesforce evaluates the policy. If the condition is met, Salesforce triggers the defined action. The following Apex class demonstrates a robust transaction security policy that evaluates report exports. If a user attempts to export a report containing more than 2,000 rows, the policy blocks the export immediately and triggers a high-priority system alert:</p>

<pre><code class="language-java">global class BlockMassiveReportExportPolicy implements TxnSecurity.EventCondition {
    public boolean evaluate(SObject event) {
        // Evaluate the event type, ensuring it is a ReportEvent
        if (event instanceof ReportEvent) {
            ReportEvent reportEvent = (ReportEvent) event;
            
            // Check if the operation is a report export
            if ('ReportExported'.equals(reportEvent.Operation)) {
                // If the number of rows exported exceeds 2000, block the transaction
                if (reportEvent.RowsProcessed > 2000) {
                    System.debug('Blocking massive report export by User ID: ' + reportEvent.UserId);
                    return true; // True indicates the policy condition has been met (Trigger action: Block)
                }
            }
        }
        return false; // Policy not triggered, allow the transaction to proceed
    }
}</code></pre>

        <p>This programmatic control allows architects to establish dynamic perimeters. For instance, you can construct a policy that permits standard account view operations but blocks any bulk API query that accesses more than 10,000 lead records, or forces the user to complete an MFA challenge if they attempt to export a client list outside corporate working hours. This dramatically reduces the risk of malicious internal exfiltration and external account compromise.</p>

        <h2 id="s5">5. Field Audit Trail Governance and Enterprise SIEM Integrations</h2>
        <p>The final layer of the auditing ecosystem is record-level field tracking. Standard Salesforce Field History Tracking is highly restricted: it only permits tracking up to 20 fields per standard or custom object, and the historical records are deleted after 18 months. For regulated industries (such as healthcare, government, or finance), retaining audit logs for only 18 months is a major compliance violation. These sectors require permanent historical records of data changes, often lasting seven to ten years.</p>
        <p>To meet these requirements, architects must deploy Shield Field Audit Trail. This utility increases the field tracking limit from 20 fields to 60 fields per object and allows organisations to define custom history retention policies using the Metadata API. With Field Audit Trail, historical logs are stored in a dedicated, high-performance big data storage container, preserving records for up to 10 years. Administrators define retention rules in XML configuration files, establishing when data should be archived and when it should be permanently deleted from the active tables.</p>
        <p>In addition to long-term storage, enterprise governance requires consolidating Salesforce security logs with external Security Information and Event Management (SIEM) systems, such as Splunk, Microsoft Sentinel, or Datadog. Having security logs isolated inside Salesforce prevents a holistic view of corporate security. Security analysts must be able to correlate a suspicious Salesforce login with a simultaneous corporate VPN connection from a different geographic location. The following diagram visualizes the architecture of streaming Salesforce Event Log Files into an external enterprise SIEM platform:</p>

<pre>
+-----------------------------------------------------------------+
|                      Salesforce Platform                         |
|                                                                 |
| +------------------+   +------------------+   +---------------+ |
| | SetupAuditTrail  |   | Event Monitoring |   |  Field Audit  | |
| | (Metadata Logs)  |   | (Hourly/Daily)   |   | (10-Yr BigData)| |
| +--------+---------+   +--------+---------+   +-------+-------+ |
+----------|----------------------|---------------------|---------+
           |                      |                     |
           +                      +                     +
     +--------------------------------------------------------+
     |                  Salesforce REST / Pub/Sub APIs        |
     |                     (Secure Ingestion Channel)         |
     +----------------------------+---------------------------+
                                  |
                                  v
     +--------------------------------------------------------+
     |               Enterprise SIEM (e.g., Splunk)           |
     |  - Centralized Correlation   - Real-time Alerting      |
     |  - Forensic Analysis         - Dashboard Visualization |
     +--------------------------------------------------------+
</pre>

        <p>To execute this integration, architects configure secure API connectors that periodically pull the <code>EventLogFile</code> data via the REST API or stream real-time events using the Pub/Sub API. Once ingested into the enterprise SIEM, Salesforce events are parsed, correlated, and visualised on security operations dashboards, ensuring that Salesforce is fully integrated into the corporate threat detection ecosystem.</p>
"""

sec_010_takeaways = """
            <li>A comprehensive auditing strategy requires coordinating Metadata Auditing, Transactional User Logging, and Field History Tracking.</li>
            <li>Setup Audit Trail captures configuration changes, displayable for 20 entries in the UI but extractable programmatically via SOQL.</li>
            <li>Event Monitoring records atomic user actions, including report exports, API queries, and login histories for proactive security monitoring.</li>
            <li>Real-Time Transaction Security Policies allow architects to programmatically block data exfiltration or enforce MFA challenges in real-time.</li>
            <li>Shield Field Audit Trail increases field tracking limits to 60 fields per object and extends history retention up to ten years.</li>
            <li>Stream Salesforce Event Log Files into corporate SIEM platforms (e.g., Splunk) to correlate Salesforce events with broader security signals.</li>
"""

sec_010_quiz = """
          <div class="quiz-question" id="q1">
            <p><strong>Question 1:</strong> Which Salesforce tool captures administrative and metadata configuration modifications, retaining them for 180 days in the database?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Event Monitoring</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'right')">B. Setup Audit Trail</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">C. Field History Tracking</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Transaction Security Policy</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q2">
            <p><strong>Question 2:</strong> What programmatic interface must an Apex class implement to evaluate and block report exports in real-time?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. Database.Batchable</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">B. Schedulable</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'right')">C. TxnSecurity.EventCondition</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. Process.Plugin</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q3">
            <p><strong>Question 3:</strong> How does Shield Field Audit Trail extend standard Salesforce Field History Tracking?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. By encrypting all history data using probabilistic keys.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'right')">B. By increasing tracked fields from 20 to 60 per object and extending history retention up to 10 years.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">C. By streaming changes automatically to Google Analytics.</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. By blocking users from modifying historic values.</div>
            </div>
          </div>
"""

# SEC-011 Content
sec_011_summary = """
            <li>Navigate Salesforce's security assessment policies and penetration testing rules of engagement.</li>
            <li>Distinguish between customer-responsible layers (e.g., custom code, sharing rules) and platform-responsible layers.</li>
            <li>Formulate a compliant penetration testing plan that isolates approved targets and avoids restricted systems.</li>
            <li>Master vulnerability assessment techniques for custom Apex controllers, Visualforce pages, and Lightning Web Components.</li>
            <li>Implement robust remediations for high-risk findings, including SOQL injection and privilege escalation.</li>
            <li>Structure formal security assessment documentation to satisfy audit requirements and leadership expectations.</li>
"""

sec_011_toc = """
            <li><a href="#s1">1. Rules of Engagement: The Salesforce Security Assessment Agreement</a></li>
            <li><a href="#s2">2. The Salesforce Shared Responsibility Security Model</a></li>
            <li><a href="#s3">3. Preparing and Structuring the Penetration Testing Environment</a></li>
            <li><a href="#s4">4. Common Vulnerabilities in Custom Apex and Lightning Components</a></li>
            <li><a href="#s5">5. Advanced Remediation and Secure Coding Design Patterns</a></li>
"""

sec_011_body = """
        <h2 id="s1">1. Rules of Engagement: The Salesforce Security Assessment Agreement</h2>
        <p>In an era of sophisticated cyber threats, proactive security testing is a non-negotiable requirement for enterprise applications. Penetration testing&mdash;the practice of simulating real-world cyberattacks against a system to discover vulnerabilities&mdash;is a critical component of secure application lifecycle management. However, executing a penetration test against a cloud platform like Salesforce is fundamentally different from testing on-premise infrastructure. Because Salesforce is a multi-tenant environment, a poorly planned automated scan or a distributed attack can degrade system performance for thousands of unrelated organisations or violate federal laws. To perform tests safely and legally, architects and security teams must strictly adhere to Salesforce's Rules of Engagement and its formal Security Assessment Agreement.</p>
        <p>Historically, Salesforce required customers to submit a detailed notification form and request explicit authorization weeks before executing any penetration test. Today, the process has been modernized. Under the current Security Assessment Agreement, customers are granted pre-authorisation to execute standard, non-disruptive penetration tests and vulnerability assessments without notifying Salesforce in advance, provided they adhere strictly to specific guidelines. The rules of engagement define clear boundaries on what activities are permitted and what is strictly prohibited:</p>
        <ul>
          <li><strong>Prohibited Actions:</strong> Under no circumstances may a customer execute a Distributed Denial of Service (DDoS) attack, attempt a physical security breach of Salesforce data centres, execute social engineering campaigns against Salesforce employees, or perform cross-org penetration testing that targets shared database hosts or other customer tenants.</li>
          <li><strong>Restricted Tools:</strong> High-bandwidth automated vulnerability scanners (such as Nessus, Qualys, or Burp Suite Intruder) must be throttled to prevent resource starvation. Scanners must never target standard Salesforce shared endpoints (like <code>login.salesforce.com</code>) and should only target the customer's specific My Domain subdomain or community URL.</li>
          <li><strong>Testing Hours and Scope:</strong> Testing must be restricted exclusively to the customer's own tenant and assets, isolating custom interfaces, public Experience Cloud sites, and integrated API endpoints.</li>
        </ul>
        <p>Tech leaders must ensure that external security vendors hired to perform penetration tests are fully educated on these rules of engagement. Violating these terms can result in immediate termination of Salesforce sessions, temporary suspension of the Salesforce instance, or legal action for breach of contract.</p>

        <h2 id="s2">2. The Salesforce Shared Responsibility Security Model</h2>
        <p>To plan a successful and compliant penetration test, architects must understand the Salesforce Shared Responsibility Security Model. In a cloud SaaS environment, security is a shared mandate divided between the platform provider and the customer. Security teams often waste significant time and budget trying to test infrastructure components that are the exclusive responsibility of Salesforce, while ignoring massive security loopholes in their own custom code and configuration layers.</p>
        <p>The Shared Responsibility Model establishes a clear demarcation line between the platform's infrastructure and the customer's custom implementation:</p>
        <ul>
          <li><strong>Platform-Responsible Security (Security of the Cloud):</strong> Salesforce is responsible for securing the underlying physical infrastructure, host operating systems, hypervisors, physical storage arrays, database engines, multi-tenant isolation barriers, and global network routing. Penetration testers should assume that these systems are highly secure and compliant with standard frameworks (such as ISO 27001, SOC 2, and PCI-DSS) and should not waste effort testing them.</li>
          <li><strong>Customer-Responsible Security (Security in the Cloud):</strong> The customer is responsible for the configuration of their specific Salesforce instance. This includes user profile access controls, permission set architecture, field-level security, record-level sharing rules, custom Apex code, Visualforce and Lightning Web Components (LWC), Connected App settings, integration endpoints, and database security settings.</li>
        </ul>
        <p>The vast majority of security breaches in Salesforce instances originate from customer misconfigurations or vulnerable custom code. A penetration test should therefore focus its entire scope on the customer-responsible layers. Testers should evaluate whether a standard user can escalate their privileges, whether guest users can access private objects via Experience Cloud sites, or whether dynamic SOQL queries in custom Apex classes are vulnerable to injection attacks.</p>

        <h2 id="s3">3. Preparing and Structuring the Penetration Testing Environment</h2>
        <p>A critical operational rule that architects must enforce is that penetration testing must never be executed directly in a live production environment. Executing automated vulnerability scanners or simulating malicious attacks against production data can corrupt operational records, trigger thousands of erroneous automated emails to real customers, deplete API request allocations, and cause service disruptions. To ensure safety and validity, tests must be conducted within a dedicated, isolated sandbox environment.</p>
        <p>To prepare a sandbox for a penetration test, architects must establish a deliberate, multi-step environment provisioning process:</p>
        <ol>
          <li><strong>Provisioning the Sandbox:</strong> Create a newly refreshed Full Sandbox. A Full Sandbox is highly recommended because it mirrors the production data volume, custom metadata, dynamic integrations, and sharing architectures exactly, ensuring that the vulnerability tests yield realistic, actionable results.</li>
          <li><strong>Obfuscating Customer Data:</strong> Newly refreshed sandboxes copy all production PII. Before handing access to the security testers, administrators must execute Salesforce Data Mask to sanitise all customer names, emails, and phone numbers. This ensures that testers work with simulated datasets, maintaining compliance with data privacy mandates.</li>
          <li><strong>Configuring Test Accounts:</strong> Provision specific test accounts representing different security personas (e.g., Guest User, Standard Employee, Integration User, System Administrator). This allows testers to perform context-aware privilege escalation tests.</li>
          <li><strong>Whitelisting Tester IPs:</strong> Add the security testing team's static IP ranges to the sandbox's Trusted IP Ranges. This prevents Salesforce's automated DDoS-prevention systems or IP restriction limits from blocking the testers, allowing the assessment to proceed smoothly.</li>
        </ol>
        <p>By establishing these isolation boundaries, organisations can execute deep, rigorous vulnerability assessments without risking the stability or confidentiality of their active production business operations.</p>

        <h2 id="s4">4. Common Vulnerabilities in Custom Apex and Lightning Components</h2>
        <p>When security vendors execute penetration tests against Salesforce instances, they target custom customisations. While Salesforce's declarative platform is highly secure out of the box, custom code written in Apex or Javascript (LWC) can easily bypass standard security perimeters if developers are not trained in secure coding standards. The most common critical vulnerabilities identified during Salesforce penetration tests include SOQL Injection, Cross-Site Scripting (XSS), and Privilege Escalation due to incorrect sharing configurations.</p>
        <p><strong>SOQL Injection:</strong> Occurs when user-supplied input is concatenated directly into a dynamic SOQL query string without sanitisation. This allows an attacker to manipulate the query's logic, bypassing database security boundaries to retrieve unauthorized records, delete records, or extract metadata. The following dynamic Apex snippet demonstrates a highly vulnerable dynamic SOQL query:</p>

<pre><code class="language-java">// CRITICAL VULNERABILITY: SOQL Injection via String Concatenation
public List<Contact> searchContacts(String userInput) {
    // Dynamic query vulnerable to injection
    String query = 'SELECT Id, Name, Email FROM Contact WHERE Name LIKE \'%' + userInput + '%\'';
    return Database.query(query);
}</code></pre>

        <p>If an attacker inputs `test%' OR Name LIKE '%`, the query is evaluated as `Name LIKE '%test%' OR Name LIKE '%'`, returning all contacts in the database, regardless of sharing rules. To prevent this, dynamic queries must always utilise bind variables or input sanitisation.</p>
        <p><strong>Privilege Escalation (Without Sharing):</strong> In Apex, classes execute in the "system context" by default, meaning they bypass the running user's CRUD/FLS and sharing rules. If a developer declares a class using the <code>without sharing</code> keyword, the class has unrestricted access to the database. If this class exposes data to an public Visualforce page or LWC, an unauthenticated guest user can escalate their privileges, querying records they should never see. Penetration testers actively look for public-facing guest profiles to exploit these loose sharing declarations, making strict sharing enforcement a primary security focus.</p>
        <p>To identify these custom code vulnerabilities before a formal penetration test, development teams must integrate static analysis tools into their deployment pipelines. The industry standard for Apex static analysis is PMD, which runs an extensive ruleset specifically designed for Salesforce security. PMD checks for rules like <code>ApexSharingViolations</code> (identifying classes missing sharing declarations) and <code>ApexBadAPICheck</code> (detecting risky API calls or dynamic DML). When PMD detects a violation, it generates a warning that blocks the continuous integration (CI/CD) pipeline. Developers should never bypass these warnings using suppressions (such as <code>@SuppressWarnings('PMD.ApexSharingViolations')</code>) without formal architectural review and sign-off. Enforcing PMD rules guarantees that the vast majority of common code vulnerabilities are remediated during development, allowing the penetration test to focus on complex, context-aware logical exploits rather than simple coding mistakes.</p>

        <h2 id="s5">5. Advanced Remediation and Secure Coding Design Patterns</h2>
        <p>Remediating high-risk findings identified during a penetration test requires a systematic transition to secure coding design patterns. Architects must establish strict Apex review checklists, ensuring that developers utilise modern Salesforce features designed to enforce security boundaries programmatically at the database layer.</p>
        <p>To eliminate SOQL injection, developers should default to static SOQL queries. Static SOQL natively protects against injection because the compiler treats all user inputs as bind variables rather than executable database code. If dynamic SOQL is absolutely mandatory (for instance, when building complex search filters with dynamic field lists), input must be sanitised using <code>String.escapeSingleQuotes()</code> or bind variables. The following Apex code demonstrates the three secure remediation options to correct the vulnerable dynamic query:</p>

<pre><code class="language-java">public class SecureContactSearchController {
    
    // Remediation Option 1: Standard Static SOQL with Bind Variables (Highly Recommended)
    public List<Contact> searchContactsStatic(String userInput) {
        String searchPattern = '%' + userInput + '%';
        // Native bind variables are immune to SOQL injection
        return [SELECT Id, Name, Email FROM Contact WHERE Name LIKE :searchPattern WITH USER_MODE];
    }
    
    // Remediation Option 2: Dynamic SOQL with Bind Variables
    public List<Contact> searchContactsDynamicBind(String userInput) {
        String searchPattern = '%' + userInput + '%';
        String query = 'SELECT Id, Name, Email FROM Contact WHERE Name LIKE :searchPattern';
        // Dynamic queries utilizing local bind variables are secure
        return Database.query(query);
    }
    
    // Remediation Option 3: Dynamic SOQL with Single Quote Escaping (Fallback)
    public List<Contact> searchContactsDynamicEscape(String userInput) {
        // Escape single quotes to prevent injection attacks
        String escapedInput = String.escapeSingleQuotes(userInput);
        String query = 'SELECT Id, Name, Email FROM Contact WHERE Name LIKE \'%' + escapedInput + '%\'';
        return Database.query(query);
    }
}</code></pre>

        <p>To address privilege escalation and enforce CRUD/FLS, developers must declare Apex classes using the <code>with sharing</code> or <code>inherited sharing</code> keywords. Furthermore, for SOQL queries, developers should append the <code>WITH USER_MODE</code> database clause (introduced in recent releases). <code>WITH USER_MODE</code> forces the query engine to evaluate both sharing rules and field-level security permissions for the running user, throwing a standard exception if the user attempts to query a field or object they lack permission to access. For DML operations, architects should deploy the <code>Security.stripInaccessible()</code> method, which programmatically strips out fields from sObject lists that the running user is not authorised to create or update, maintaining airtight security compliance across all custom interfaces.</p>
        <p>Architects must understand the granular mechanics of <code>Security.stripInaccessible()</code> to leverage it effectively. This method evaluates the running user's FLS and CRUD permissions for a specified access type&mdash;either <code>AccessType.READABLE</code>, <code>AccessType.CREATABLE</code>, or <code>AccessType.UPDATABLE</code>. It returns a <code>SObjectAccessDecision</code> object containing a sanitised list of sObjects with all unauthorised fields removed, as well as a list of fields that were stripped. Crucially, when handling nested lookup relationships or child subqueries (e.g., querying Contacts as a subquery of Accounts), the method recursively inspects the entire object graph, stripping unauthorized child fields automatically. This makes it an invaluable utility for secure API endpoints, as it prevents accidental field leakage in complex JSON payloads. For DML operations, checking the stripped fields list allows the code to throw a descriptive, custom exception back to the client application, ensuring transparent and secure transaction handling.</p>
"""

sec_011_takeaways = """
            <li>Adhere strictly to Salesforce's Rules of Engagement and Security Assessment Agreement when coordinating penetration testing.</li>
            <li>Focus penetration testing efforts exclusively on customer-responsible layers, such as Apex code, sharing models, and custom interfaces.</li>
            <li>Never execute vulnerability assessments or automated scanning against live production instances; always utilise an isolated Sandbox.</li>
            <li>Eliminate dynamic SOQL injection vulnerabilities by defaulting to static SOQL queries or sanitising dynamic inputs.</li>
            <li>Enforce database security boundaries programmatically in Apex using <code>with sharing</code>, <code>WITH USER_MODE</code>, and <code>Security.stripInaccessible()</code>.</li>
            <li>Automate code reviews and deploy static analysis tools (like PMD) to detect and remediate vulnerabilities early in the development lifecycle.</li>
"""

sec_011_quiz = """
          <div class="quiz-question" id="q1">
            <p><strong>Question 1:</strong> According to Salesforce's rules of engagement, which of the following activities is strictly prohibited during a customer's security assessment?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">A. Testing custom dynamic Apex controllers in a full sandbox.</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">B. Scanning public Experience Cloud endpoints using a throttled web scanner.</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'right')">C. Executing a Distributed Denial of Service (DDoS) attack against Salesforce endpoints.</div>
              <div class="quiz-option" onclick="answer(this, 'q1', 'wrong')">D. Assessing field-level security settings for integration profiles.</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q2">
            <p><strong>Question 2:</strong> What is the safest way to prevent SOQL injection vulnerabilities in dynamic Apex queries that rely on user-supplied inputs?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">A. Declaring the Apex class with the 'without sharing' keyword.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'right')">B. Utilizing static SOQL with bind variables, or applying String.escapeSingleQuotes() if dynamic SOQL is mandatory.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">C. Encrypting the user input using probabilistic encryption before passing it to the query.</div>
              <div class="quiz-option" onclick="answer(this, 'q2', 'wrong')">D. Routing all database queries through standard Named Credentials.</div>
            </div>
          </div>
          
          <div class="quiz-question" id="q3">
            <p><strong>Question 3:</strong> Which clause should be appended to a SOQL query to force the execution engine to evaluate both sharing rules and field-level security for the running user?</p>
            <div class="quiz-options">
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">A. WITH SYSTEM_MODE</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">B. WITH SECURITY_ENFORCED</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'right')">C. WITH USER_MODE</div>
              <div class="quiz-option" onclick="answer(this, 'q3', 'wrong')">D. WITHOUT SHARING</div>
            </div>
          </div>
"""

# Dictionary of tutorial data
tutorials = {
    'sec-007': {
        'summary': sec_007_summary,
        'toc': sec_007_toc,
        'body': sec_007_body,
        'takeaways': sec_007_takeaways,
        'quiz': sec_007_quiz
    },
    'sec-008': {
        'summary': sec_008_summary,
        'toc': sec_008_toc,
        'body': sec_008_body,
        'takeaways': sec_008_takeaways,
        'quiz': sec_008_quiz
    },
    'sec-009': {
        'summary': sec_009_summary,
        'toc': sec_009_toc,
        'body': sec_009_body,
        'takeaways': sec_009_takeaways,
        'quiz': sec_009_quiz
    },
    'sec-010': {
        'summary': sec_010_summary,
        'toc': sec_010_toc,
        'body': sec_010_body,
        'takeaways': sec_010_takeaways,
        'quiz': sec_010_quiz
    },
    'sec-011': {
        'summary': sec_011_summary,
        'toc': sec_011_toc,
        'body': sec_011_body,
        'takeaways': sec_011_takeaways,
        'quiz': sec_011_quiz
    }
}

def count_words(text):
    # Remove HTML tags and count words
    plain = re.sub(r'<[^>]+>', ' ', text)
    words = plain.split()
    return len(words)

def process_tutorials():
    for slug, data in tutorials.items():
        filepath = os.path.join(TUTORIALS_DIR, slug, 'index.html')
        if not os.path.exists(filepath):
            print(f"File NOT found: {filepath}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Verify word count first
        w_count = count_words(data['body'])
        print(f"[{slug}] Raw body word count: {w_count}")
        if w_count < 1800:
            print(f"WARNING: Word count for {slug} is {w_count}, which is below the 1800-word target!")
            
        # Replacements
        content = content.replace('<!-- [[SUMMARY_BULLETS]] -->', data['summary'].strip('\r\n'))
        content = content.replace('<!-- [[TOC_LINKS]] -->', data['toc'].strip('\r\n'))
        content = content.replace('<!-- [[BODY_SECTIONS]] -->', data['body'].strip('\r\n'))
        content = content.replace('<!-- [[TAKEAWAY_BULLETS]] -->', data['takeaways'].strip('\r\n'))
        content = content.replace('<!-- [[QUIZ_QUESTIONS]] -->', data['quiz'].strip('\r\n'))
        
        # Save file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Successfully processed and updated: {filepath}")

if __name__ == '__main__':
    process_tutorials()
