import os

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIALS_DIR = os.path.join(WORKSPACE_DIR, 'tutorials')

TUTORIALS_DATA = [
    {
        'id': 'SEC-002',
        'slug': 'sec-002',
        'title': 'GDPR Compliance in Salesforce: A Technical Implementation Guide',
        'subtitle': 'A deep technical roadmap for enforcing data subject rights, implementing restricted processing, and setting up automated compliance audits under EU regulations.',
        'desc': 'GDPR Compliance in Salesforce: A Technical Implementation Guide for CTOs, Data Protection Officers, and Lead Architects.',
        'read_time': '25',
        'audience': 'CTOs & Data Protection Officers',
        'prev_slug': 'sec-001',
        'prev_id': 'SEC-001',
        'prev_title': 'Salesforce Security Architecture',
        'next_slug': 'sec-003',
        'next_id': 'SEC-003',
        'next_title': 'Salesforce Shield: Platform Encryption, Event Monitoring, and Field Audit Trail',
        'related': [
            {'slug': 'sec-005', 'id': 'SEC-005', 'title': 'Data Residency and Hyperforce'},
            {'slug': 'sec-009', 'id': 'SEC-009', 'title': 'Handling PII in Salesforce'},
            {'slug': 'sec-019', 'id': 'SEC-019', 'title': 'Data Classification'}
        ]
    },
    {
        'id': 'SEC-003',
        'slug': 'sec-003',
        'title': 'Salesforce Shield: Platform Encryption, Event Monitoring, and Field Audit Trail',
        'subtitle': 'An architectural deep dive into key lifecycle management, real-time event logging, and long-retention policy audits for highly regulated environments.',
        'desc': 'Salesforce Shield: Platform Encryption, Event Monitoring, and Field Audit Trail. Technical deep dive.',
        'read_time': '22',
        'audience': 'Lead Security Architects',
        'prev_slug': 'sec-002',
        'prev_id': 'SEC-002',
        'prev_title': 'GDPR Compliance in Salesforce',
        'next_slug': 'sec-004',
        'next_id': 'SEC-004',
        'next_title': 'Zero-Trust Security in Salesforce: The Modern Approach',
        'related': [
            {'slug': 'sec-010', 'id': 'SEC-010', 'title': 'Audit Trail and Event Monitoring'},
            {'slug': 'sec-016', 'id': 'SEC-016', 'title': 'Encryption in Salesforce: Classic vs Shield'},
            {'slug': 'sec-019', 'id': 'SEC-019', 'title': 'Data Classification'}
        ]
    },
    {
        'id': 'SEC-004',
        'slug': 'sec-004',
        'title': 'Zero-Trust Security in Salesforce: The Modern Approach',
        'subtitle': 'How to transition from network perimeter defence to context-aware transaction validation, continuous threat modeling, and dynamic FLS overrides.',
        'desc': 'Zero-Trust Security in Salesforce: The Modern Approach. Context-aware transaction validation and continuous threat modeling.',
        'read_time': '20',
        'audience': 'CTOs & Lead Security Architects',
        'prev_slug': 'sec-003',
        'prev_id': 'SEC-003',
        'prev_title': 'Salesforce Shield: Platform Encryption, Event Monitoring, and Field Audit Trail',
        'next_slug': 'sec-005',
        'next_id': 'SEC-005',
        'next_title': 'Data Residency and Salesforce: What Hyperforce Changes',
        'related': [
            {'slug': 'sec-006', 'id': 'SEC-006', 'title': 'Single Sign-On with Salesforce'},
            {'slug': 'sec-008', 'id': 'SEC-008', 'title': 'IP Whitelisting and Network Security'},
            {'slug': 'sec-020', 'id': 'SEC-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-005',
        'slug': 'sec-005',
        'title': 'Data Residency and Salesforce: What Hyperforce Changes',
        'subtitle': 'Navigating sovereignty constraints, local data storage regulations, and architectural patterns for Hyperforce deployments.',
        'desc': 'Data Residency and Salesforce: What Hyperforce Changes. Navigating sovereignty and local data storage constraints.',
        'read_time': '22',
        'audience': 'Solution Architects & CTOs',
        'prev_slug': 'sec-004',
        'prev_id': 'SEC-004',
        'prev_title': 'Zero-Trust Security in Salesforce: The Modern Approach',
        'next_slug': 'sec-006',
        'next_id': 'SEC-006',
        'next_title': 'Single Sign-On with Salesforce: SAML, OAuth, and Identity Provider Setup',
        'related': [
            {'slug': 'sec-002', 'id': 'SEC-002', 'title': 'GDPR Compliance in Salesforce'},
            {'slug': 'sec-009', 'id': 'SEC-009', 'title': 'Handling PII in Salesforce'},
            {'slug': 'sec-014', 'id': 'SEC-014', 'title': 'SOC 2 and Salesforce'}
        ]
    },
    {
        'id': 'SEC-006',
        'slug': 'sec-006',
        'title': 'Single Sign-On with Salesforce: SAML, OAuth, and Identity Provider Setup',
        'subtitle': 'A technical guide to configuring enterprise federated identity, configuring JIT user provisioning, and securing active sessions.',
        'desc': 'Single Sign-On with Salesforce: SAML, OAuth, and Identity Provider Setup. Enterprise federated identity and JIT user provisioning.',
        'read_time': '22',
        'audience': 'Identity & Security Architects',
        'prev_slug': 'sec-005',
        'prev_id': 'SEC-005',
        'prev_title': 'Data Residency and Salesforce: What Hyperforce Changes',
        'next_slug': 'sec-007',
        'next_id': 'SEC-007',
        'next_title': 'Salesforce Connected Apps: Security Risks Most Leaders Miss',
        'related': [
            {'slug': 'sec-004', 'id': 'SEC-004', 'title': 'Zero-Trust Security in Salesforce'},
            {'slug': 'sec-007', 'id': 'SEC-007', 'title': 'Salesforce Connected Apps'},
            {'slug': 'sec-008', 'id': 'SEC-008', 'title': 'IP Whitelisting and Network Security'}
        ]
    },
    {
        'id': 'SEC-007',
        'slug': 'sec-007',
        'title': 'Salesforce Connected Apps: Security Risks Most Leaders Miss',
        'subtitle': 'Architecting secure OAuth authorization flows, managing integration credentials, and auditing API access scopes at scale.',
        'desc': 'Salesforce Connected Apps: Security Risks Most Leaders Miss. OAuth authorization flows and auditing API scopes.',
        'read_time': '20',
        'audience': 'Solution Architects & CTOs',
        'prev_slug': 'sec-006',
        'prev_id': 'SEC-006',
        'prev_title': 'Single Sign-On with Salesforce: SAML, OAuth, and Identity Provider Setup',
        'next_slug': 'sec-008',
        'next_id': 'SEC-008',
        'next_title': 'IP Whitelisting and Network Security in Salesforce',
        'related': [
            {'slug': 'sec-006', 'id': 'SEC-006', 'title': 'Single Sign-On with Salesforce'},
            {'slug': 'sec-017', 'id': 'SEC-017', 'title': 'Third-Party App Security'},
            {'slug': 'sec-020', 'id': 'SEC-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-008',
        'slug': 'sec-008',
        'title': 'IP Whitelisting and Network Security in Salesforce',
        'subtitle': 'Designing network perimeter boundaries, configuring login IP ranges, and securing API endpoints from unauthorized networks.',
        'desc': 'IP Whitelisting and Network Security in Salesforce. Network perimeter boundaries and login IP ranges.',
        'read_time': '15',
        'audience': 'Network & Security Engineers',
        'prev_slug': 'sec-007',
        'prev_id': 'SEC-007',
        'prev_title': 'Salesforce Connected Apps: Security Risks Most Leaders Miss',
        'next_slug': 'sec-009',
        'next_id': 'SEC-009',
        'next_title': 'Handling PII in Salesforce: Anonymisation, Masking, and Deletion',
        'related': [
            {'slug': 'sec-004', 'id': 'SEC-004', 'title': 'Zero-Trust Security in Salesforce'},
            {'slug': 'sec-006', 'id': 'SEC-006', 'title': 'Single Sign-On with Salesforce'},
            {'slug': 'sec-020', 'id': 'SEC-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-009',
        'slug': 'sec-009',
        'title': 'Handling PII in Salesforce: Anonymisation, Masking, and Deletion',
        'subtitle': 'Developing robust policies and automated Apex pipelines to mask, scrub, and pseudonymise sensitive customer data.',
        'desc': 'Handling PII in Salesforce: Anonymisation, Masking, and Deletion. Automated Apex masking pipelines and data scrubbing.',
        'read_time': '22',
        'audience': 'Lead Architects & Data Officers',
        'prev_slug': 'sec-008',
        'prev_id': 'SEC-008',
        'prev_title': 'IP Whitelisting and Network Security in Salesforce',
        'next_slug': 'sec-010',
        'next_id': 'SEC-010',
        'next_title': 'Audit Trail and Event Monitoring: Who Did What and When',
        'related': [
            {'slug': 'sec-002', 'id': 'SEC-002', 'title': 'GDPR Compliance in Salesforce'},
            {'slug': 'sec-005', 'id': 'SEC-005', 'title': 'Data Residency and Hyperforce'},
            {'slug': 'sec-019', 'id': 'SEC-019', 'title': 'Data Classification'}
        ]
    },
    {
        'id': 'SEC-010',
        'slug': 'sec-010',
        'title': 'Audit Trail and Event Monitoring: Who Did What and When',
        'subtitle': 'How to ingest, visualize, and alert on raw CSV EventLogFile data, and building real-time alerts for suspect operations.',
        'desc': 'Audit Trail and Event Monitoring: Who Did What and When. Real-time alerting and log parsing pipelines.',
        'read_time': '18',
        'audience': 'Security Operations & Tech Leaders',
        'prev_slug': 'sec-009',
        'prev_id': 'SEC-009',
        'prev_title': 'Handling PII in Salesforce: Anonymisation, Masking, and Deletion',
        'next_slug': 'sec-011',
        'next_id': 'SEC-011',
        'next_title': 'Penetration Testing Salesforce: What\'s Allowed and What Isn\'t',
        'related': [
            {'slug': 'sec-003', 'id': 'SEC-003', 'title': 'Salesforce Shield Encryption'},
            {'slug': 'sec-018', 'id': 'SEC-018', 'title': 'Incident Response for Salesforce'},
            {'slug': 'sec-020', 'id': 'SEC-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-011',
        'slug': 'sec-011',
        'title': 'Penetration Testing Salesforce: What\'s Allowed and What Isn\'t',
        'subtitle': 'Understanding the Salesforce security assessment agreement, structuring authorization requests, and typical enterprise vulnerabilities to test.',
        'desc': 'Penetration Testing Salesforce: What\'s Allowed and What Isn\'t. Security assessment agreements and standard vulnerability testing.',
        'read_time': '20',
        'audience': 'Penetration Testers & CTOs',
        'prev_slug': 'sec-010',
        'prev_id': 'SEC-010',
        'prev_title': 'Audit Trail and Event Monitoring: Who Did What and When',
        'next_slug': 'sec-012',
        'next_id': 'SEC-012',
        'next_title': 'Security Review for AppExchange: What the Process Actually Tests',
        'related': [
            {'slug': 'sec-012', 'id': 'sec-012', 'title': 'Security Review for AppExchange'},
            {'slug': 'sec-017', 'id': 'sec-017', 'title': 'Third-Party App Security'},
            {'slug': 'sec-020', 'id': 'sec-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-012',
        'slug': 'sec-012',
        'title': 'Security Review for AppExchange: What the Process Actually Tests',
        'subtitle': 'A guide to preparing your product package, scanning for security flaws, and passing Salesforce\'s stringent certification gates.',
        'desc': 'Security Review for AppExchange: What the Process Actually Tests. AppExchange certification gates and code scans.',
        'read_time': '18',
        'audience': 'AppExchange Partners & Lead Developers',
        'prev_slug': 'sec-011',
        'prev_id': 'SEC-011',
        'prev_title': 'Penetration Testing Salesforce: What\'s Allowed and What Isn\'t',
        'next_slug': 'sec-013',
        'next_id': 'SEC-013',
        'next_title': 'HIPAA Compliance on Salesforce: The Healthcare Leader\'s Guide',
        'related': [
            {'slug': 'sec-011', 'id': 'sec-011', 'title': 'Penetration Testing Salesforce'},
            {'slug': 'sec-017', 'id': 'sec-017', 'title': 'Third-Party App Security'},
            {'slug': 'sec-020', 'id': 'sec-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-013',
        'slug': 'sec-013',
        'title': 'HIPAA Compliance on Salesforce: The Healthcare Leader\'s Guide',
        'subtitle': 'Configuring Salesforce to protect Protected Health Information (PHI) under US federal guidelines, and auditing Business Associate Agreements.',
        'desc': 'HIPAA Compliance on Salesforce: The Healthcare Leader\'s Guide. Protecting PHI under federal rules and managing BAAs.',
        'read_time': '22',
        'audience': 'Healthcare CTOs & Compliance Officers',
        'prev_slug': 'sec-012',
        'prev_id': 'SEC-012',
        'prev_title': 'Security Review for AppExchange: What the Process Actually Tests',
        'next_slug': 'sec-014',
        'next_id': 'SEC-014',
        'next_title': 'SOC 2 and Salesforce: What Compliance Means for Your Implementation',
        'related': [
            {'slug': 'sec-002', 'id': 'SEC-002', 'title': 'GDPR Compliance in Salesforce'},
            {'slug': 'sec-009', 'id': 'SEC-009', 'title': 'Handling PII in Salesforce'},
            {'slug': 'sec-014', 'id': 'SEC-014', 'title': 'SOC 2 and Salesforce'}
        ]
    },
    {
        'id': 'SEC-014',
        'slug': 'sec-014',
        'title': 'SOC 2 and Salesforce: What Compliance Means for Your Implementation',
        'subtitle': 'Aligning Salesforce configuration, deployment processes, and access governance policies to pass independent Trust Services Criteria audits.',
        'desc': 'SOC 2 and Salesforce: What Compliance Means for Your Implementation. Passing Trust Services Criteria audits.',
        'read_time': '20',
        'audience': 'Compliance Managers & Solution Architects',
        'prev_slug': 'sec-013',
        'prev_id': 'SEC-013',
        'prev_title': 'HIPAA Compliance on Salesforce: The Healthcare Leader\'s Guide',
        'next_slug': 'sec-015',
        'next_id': 'SEC-015',
        'next_title': 'Role Hierarchy Design: Balancing Security and Reporting Access',
        'related': [
            {'slug': 'sec-002', 'id': 'SEC-002', 'title': 'GDPR Compliance in Salesforce'},
            {'slug': 'sec-005', 'id': 'SEC-005', 'title': 'Data Residency and Hyperforce'},
            {'slug': 'sec-013', 'id': 'SEC-013', 'title': 'HIPAA Compliance on Salesforce'}
        ]
    },
    {
        'id': 'SEC-015',
        'slug': 'sec-015',
        'title': 'Role Hierarchy Design: Balancing Security and Reporting Access',
        'subtitle': 'Architecting the visibility tree to maintain strict data segregation while avoiding sharing calculations bottlenecks at scale.',
        'desc': 'Role Hierarchy Design: Balancing Security and Reporting Access. Avoiding sharing recalculation bottlenecks.',
        'read_time': '18',
        'audience': 'Salesforce Solution Architects',
        'prev_slug': 'sec-014',
        'prev_id': 'SEC-014',
        'prev_title': 'SOC 2 and Salesforce: What Compliance Means for Your Implementation',
        'next_slug': 'sec-016',
        'next_id': 'SEC-016',
        'next_title': 'Encryption in Salesforce: Classic vs Shield — When Do You Need It?',
        'related': [
            {'slug': 'sec-001', 'id': 'SEC-001', 'title': 'Salesforce Security Architecture'},
            {'slug': 'sec-016', 'id': 'SEC-016', 'title': 'Encryption in Salesforce'},
            {'slug': 'sec-020', 'id': 'SEC-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-016',
        'slug': 'sec-016',
        'title': 'Encryption in Salesforce: Classic vs Shield — When Do You Need It?',
        'subtitle': 'Analyzing technical overhead, search and filter restrictions, and functional limitations of database encryption vs field history logs.',
        'desc': 'Encryption in Salesforce: Classic vs Shield. Technical overhead, search restrictions, and functional limitations.',
        'read_time': '20',
        'audience': 'Lead Architects & Security Officers',
        'prev_slug': 'sec-015',
        'prev_id': 'SEC-015',
        'prev_title': 'Role Hierarchy Design: Balancing Security and Reporting Access',
        'next_slug': 'sec-017',
        'next_id': 'SEC-017',
        'next_title': 'Third-Party App Security: Evaluating AppExchange Packages',
        'related': [
            {'slug': 'sec-003', 'id': 'SEC-003', 'title': 'Salesforce Shield Encryption'},
            {'slug': 'sec-015', 'id': 'SEC-015', 'title': 'Role Hierarchy Design'},
            {'slug': 'sec-019', 'id': 'SEC-019', 'title': 'Data Classification'}
        ]
    },
    {
        'id': 'SEC-017',
        'slug': 'sec-017',
        'title': 'Third-Party App Security: Evaluating AppExchange Packages',
        'subtitle': 'A structured playbook for auditing external app package permissions, verifying data flow boundaries, and monitoring OAuth authorizations.',
        'desc': 'Third-Party App Security: Evaluating AppExchange Packages. Auditing package permissions and verifying data flow boundaries.',
        'read_time': '18',
        'audience': 'CTOs & Solution Architects',
        'prev_slug': 'sec-016',
        'prev_id': 'SEC-016',
        'prev_title': 'Encryption in Salesforce: Classic vs Shield — When Do You Need It?',
        'next_slug': 'sec-018',
        'next_id': 'SEC-018',
        'next_title': 'Incident Response for Salesforce: What to Do When Something Goes Wrong',
        'related': [
            {'slug': 'sec-007', 'id': 'SEC-007', 'title': 'Salesforce Connected Apps'},
            {'slug': 'sec-011', 'id': 'SEC-011', 'title': 'Penetration Testing Salesforce'},
            {'slug': 'sec-012', 'id': 'SEC-012', 'title': 'Security Review for AppExchange'}
        ]
    },
    {
        'id': 'SEC-018',
        'slug': 'sec-018',
        'title': 'Incident Response for Salesforce: What to Do When Something Goes Wrong',
        'subtitle': 'Establishing data breach workflows, dynamic session termination mechanisms, and operational response checklists for the CRM.',
        'desc': 'Incident Response for Salesforce: What to Do When Something Goes Wrong. Data breach workflows and session termination mechanisms.',
        'read_time': '20',
        'audience': 'CTOs & Security Operations',
        'prev_slug': 'sec-017',
        'prev_id': 'SEC-017',
        'prev_title': 'Third-Party App Security: Evaluating AppExchange Packages',
        'next_slug': 'sec-019',
        'next_id': 'SEC-019',
        'next_title': 'Data Classification in Salesforce: Tagging, Handling, and Governance',
        'related': [
            {'slug': 'sec-010', 'id': 'SEC-010', 'title': 'Audit Trail and Event Monitoring'},
            {'slug': 'sec-019', 'id': 'SEC-019', 'title': 'Data Classification'},
            {'slug': 'sec-020', 'id': 'SEC-020', 'title': 'Security Hardening Checklist'}
        ]
    },
    {
        'id': 'SEC-019',
        'slug': 'sec-019',
        'title': 'Data Classification in Salesforce: Tagging, Handling, and Governance',
        'subtitle': 'Deploying standard metadata schema policies, enforcing field classification compliance, and mapping fields to sensitivity tiers.',
        'desc': 'Data Classification in Salesforce: Tagging, Handling, and Governance. Enforcing field compliance and sensitivity tiers.',
        'read_time': '18',
        'audience': 'Solution Architects & Data Protection Officers',
        'prev_slug': 'sec-018',
        'prev_id': 'SEC-018',
        'prev_title': 'Incident Response for Salesforce: What to Do When Something Goes Wrong',
        'next_slug': 'sec-020',
        'next_id': 'SEC-020',
        'next_title': 'Security Hardening Checklist for Salesforce Enterprise Orgs',
        'related': [
            {'slug': 'sec-002', 'id': 'SEC-002', 'title': 'GDPR Compliance in Salesforce'},
            {'slug': 'sec-009', 'id': 'SEC-009', 'title': 'Handling PII in Salesforce'},
            {'slug': 'sec-016', 'id': 'SEC-016', 'title': 'Encryption in Salesforce: Classic vs Shield'}
        ]
    },
    {
        'id': 'SEC-020',
        'slug': 'sec-020',
        'title': 'Security Hardening Checklist for Salesforce Enterprise Orgs',
        'subtitle': 'The definitive checklist of settings, profiles restrictions, Session settings, and administrative audits to secure Salesforce.',
        'desc': 'Security Hardening Checklist for Salesforce Enterprise Orgs. Setting profiles restrictions and Session audits.',
        'read_time': '20',
        'audience': 'CTOs, Security Officers & Lead Architects',
        'prev_slug': 'sec-019',
        'prev_id': 'SEC-019',
        'prev_title': 'Data Classification in Salesforce: Tagging, Handling, and Governance',
        'next_slug': '',
        'next_id': '',
        'next_title': '',
        'related': [
            {'slug': 'sec-001', 'id': 'SEC-001', 'title': 'Salesforce Security Architecture'},
            {'slug': 'sec-004', 'id': 'SEC-004', 'title': 'Zero-Trust Security in Salesforce'},
            {'slug': 'sec-015', 'id': 'SEC-015', 'title': 'Role Hierarchy Design'}
        ]
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <link rel="canonical" href="https://sfvedas.com/tutorials/{slug}/"/>
  <link rel="icon" type="image/svg+xml" href="/images/favicon.svg"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{id}: {title} — SFVedas</title>
  <meta name="description" content="{desc}"/>
  <meta property="og:title" content="{id}: {title} — SFVedas"/>
  <meta property="og:description" content="{desc}"/>
  <meta property="og:type" content="article"/>
  <meta property="og:url" content="https://sfvedas.com/tutorials/{slug}/"/>
  <meta property="og:image" content="https://sfvedas.com/images/og-default.png"/>
  <meta property="og:site_name" content="SFVedas"/>
  <meta name="twitter:card" content="summary_large_image"/>
  <meta name="twitter:title" content="{id}: {title} — SFVedas"/>
  <meta name="twitter:description" content="{desc}"/>
  <meta name="twitter:image" content="https://sfvedas.com/images/og-default.png"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link rel="dns-prefetch" href="https://www.googletagmanager.com"/>
  <link rel="dns-prefetch" href="https://cdnjs.cloudflare.com"/>
  <link rel="preconnect" href="https://www.googletagmanager.com" crossorigin/>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"/>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" media="print" onload="this.media='all'"/>
  <noscript><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=DM+Serif+Display:ital@0;1&family=Source+Serif+4:ital,wght@0,300;0,400;0,600;1,400&family=DM+Sans:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/></noscript>
  <link rel="stylesheet" href="/css/main.css"/>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-99QW4K310Y"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-99QW4K310Y');
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"/>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{id}: {title} — SFVedas",
    "description": "{desc}",
    "url": "https://sfvedas.com/tutorials/{slug}/",
    "mainEntityOfPage": "https://sfvedas.com/tutorials/{slug}/",
    "author": {{
      "@type": "Person",
      "name": "Vishal Sharma",
      "url": "https://sfvedas.com/about/"
    }},
    "publisher": {{
      "@type": "Organization",
      "name": "SFVedas",
      "url": "https://sfvedas.com",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://sfvedas.com/images/logo.svg"
      }}
    }},
    "image": "https://sfvedas.com/images/og-default.png"
  }}
  </script>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4584420180521124" crossorigin="anonymous"></script>
</head>
<body class="light-mode">

  <div class="reading-progress" id="readingProgress"></div>

  <nav class="navbar" id="navbar">
    <div class="nav-inner">
      <a href="/" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>
      <ul class="nav-links">
        <li><a href="/" class="nav-link">Home</a></li>
        <li><a href="/tutorials/" class="nav-link active">Tutorials</a></li>
        <li><a href="/learning-paths/" class="nav-link">Learning Paths</a></li>
        <li><a href="/about/" class="nav-link">About</a></li>
        <li><a href="/advertise/" class="nav-link">Advertise</a></li>
      </ul>
      <div class="nav-actions">
        <button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode"><span class="theme-icon">☀</span></button>
        <button class="nav-hamburger" id="hamburger"><span></span><span></span><span></span></button>
      </div>
    </div>
    <div class="nav-mobile" id="navMobile">
      <a href="/" class="nav-link">Home</a>
      <a href="/tutorials/" class="nav-link">Tutorials</a>
      <a href="/learning-paths/" class="nav-link">Learning Paths</a>
      <a href="/about/" class="nav-link">About</a>
      <a href="/advertise/" class="nav-link">Advertise</a>
    </div>
  </nav>

  <section style="background: var(--bg-secondary); border-bottom: 1px solid var(--border); padding: 56px 0 40px;">
    <div class="container">
      <div style="margin-bottom: 16px;">
        <a href="/tutorials/?tag=security-compliance" style="font-family:var(--font-ui);font-size:0.8rem;color:var(--sage-green);text-decoration:none;">← Back to Security &amp; Compliance</a>
      </div>
      <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap;">
        <span class="card-id">{id}</span>
        <span class="card-tag" style="background:rgba(232,147,10,0.08);color:var(--saffron);border-color:rgba(232,147,10,0.2);">Security &amp; Compliance</span>
        <span class="card-read">{read_time} min read</span>
        <span style="font-family:var(--font-ui);font-size:0.78rem;color:var(--text-secondary);">For: {audience}</span>
      </div>
      <h1 style="font-family:var(--font-display);font-size:clamp(1.8rem,4vw,2.8rem);font-weight:700;color:var(--text-primary);line-height:1.2;max-width:820px;margin-bottom:16px;">
        {title}
      </h1>
      <p style="font-family:var(--font-body);font-size:1.05rem;color:var(--text-secondary);max-width:700px;line-height:1.75;margin-bottom:24px;">
        {subtitle}
      </p>
      <div style="display:flex;align-items:center;gap:12px;">
        <div class="author-avatar" style="width:40px;height:40px;font-size:0.85rem;">VS</div>
        <div>
          <p style="font-family:var(--font-ui);font-size:0.85rem;font-weight:600;color:var(--text-primary);margin:0;">Vishal Sharma</p>
          <p style="font-family:var(--font-ui);font-size:0.75rem;color:var(--text-secondary);margin:0;">Salesforce Architecture Specialist · Updated May 2026</p>
        </div>
      </div>
    </div>
  </section>

  <div class="ad-unit">
    <ins class="adsbygoogle"
         style="display:block;text-align:center;"
         data-ad-layout="in-article"
         data-ad-format="fluid"
         data-ad-client="ca-pub-4584420180521124"
         data-ad-slot=""></ins>
    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
  </div>

  <div class="container">
    <div class="tutorial-layout">

      <article class="tutorial-body" id="tutorialContent">

        <!-- SECTION SUMMARY -->
        <div class="section-summary">
          <span class="ss-label">What you will learn in this tutorial</span>
          <ul>
            <!-- [[SUMMARY_BULLETS]] -->
          </ul>
        </div>

        <!-- [[BODY_SECTIONS]] -->

        <!-- KEY TAKEAWAYS -->
        <div class="key-takeaways" id="takeaways">
          <h2>Key Takeaways</h2>
          <ul>
            <!-- [[TAKEAWAY_BULLETS]] -->
          </ul>
        </div>

        <!-- QUIZ -->
        <div class="quiz-section" id="quiz">
          <h2>Checkpoint: Test Your Understanding</h2>
          <!-- [[QUIZ_QUESTIONS]] -->
        </div>

        <!-- RELATED TUTORIALS -->
        <div class="related-tutorials">
          <h2>Continue Reading</h2>
          <div class="related-grid">
            {related_cards}
          </div>
        </div>

      </article>

      <aside class="tutorial-sidebar">
        <div class="sidebar-toc">
          <h4>In This Tutorial</h4>
          <ul class="toc-list">
            <!-- [[TOC_LINKS]] -->
            <li><a href="#takeaways">Key Takeaways</a></li>
            <li><a href="#quiz">Checkpoint: Test Your Understanding</a></li>
          </ul>
        </div>
        <div class="sidebar-progress">
          <h4>Reading Progress</h4>
          <div class="progress-track"><div class="progress-fill" id="sidebarProgress"></div></div>
          <span class="progress-pct" id="progressPct">0%</span>
        </div>
        
        {next_block}
        
        {prev_block}
      </aside>

    </div>
  </div>

  <footer class="footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="/" class="nav-brand"><span class="brand-sf">SF</span><span class="brand-vedas">Vedas</span></a>
          <p class="footer-tagline">Deep Salesforce Knowledge<br/>for Tech Leaders</p>
          <p class="footer-domain">sfvedas.com</p>
        </div>
        <div class="footer-links">
          <div class="footer-col"><h4>Learn</h4><a href="/tutorials/">All Tutorials</a><a href="/learning-paths/">Learning Paths</a></div>
          <div class="footer-col"><h4>About</h4><a href="/about/">Our Story</a></div>
          <div class="footer-col"><h4>Topics</h4><a href="/tutorials/">Architecture</a><a href="/tutorials/">Delivery</a></div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 SFVedas · Vishal Sharma · sfvedas.com</p>
        <p class="footer-philosophy">Deep knowledge. For the decisions that matter.</p>
      </div>
    </div>
  </footer>

  <script>
    function updateProgress() {{
      const article = document.getElementById('tutorialContent');
      const bar = document.getElementById('readingProgress');
      const sidebar = document.getElementById('sidebarProgress');
      const pct = document.getElementById('progressPct');
      if (!article) return;
      const rect = article.getBoundingClientRect();
      const scrolled = Math.max(0, -rect.top);
      const total = article.offsetHeight - window.innerHeight;
      const progress = total > 0 ? Math.min(100, Math.round((scrolled / total) * 100)) : 0;
      if (bar) bar.style.width = progress + '%';
      if (sidebar) sidebar.style.width = progress + '%';
      if (pct) pct.textContent = progress + '%';
    }}
    window.addEventListener('scroll', updateProgress, {{ passive: true }});
    updateProgress();

    function answer(el, questionId, result) {{
      const question = document.getElementById(questionId);
      question.querySelectorAll('.quiz-option').forEach(opt => {{
        opt.classList.remove('correct', 'incorrect');
        opt.style.pointerEvents = 'none';
      }});
      el.classList.add(result === 'right' ? 'correct' : 'incorrect');
      if (result === 'wrong') {{
        question.querySelectorAll('.quiz-option').forEach(opt => {{
          if (opt.getAttribute('onclick') && opt.getAttribute('onclick').includes("'right'")) {{
            opt.classList.add('correct');
          }}
        }});
      }}
    }}
  </script>
  <script src="/js/main.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js" defer></script>
</body>
</html>
"""

def generate_skeleton(tut):
    # Related cards
    related_cards_html = ""
    for r in tut['related']:
        related_cards_html += f'''            <a href="../{r['slug']}/" class="related-card">
              <span class="card-id">{r['id'].upper()}</span>
              <h4>{r['title']}</h4>
            </a>\\n'''
            
    # Prev/Next Blocks
    prev_block = ""
    if tut['prev_slug']:
        prev_block = f'''        <div class="sidebar-next">
          <h4>Previous Tutorial</h4>
          <a href="../{tut['prev_slug']}/" class="sidebar-next-link">
            <span class="sidebar-next-id">{tut['prev_id'].upper()}</span>
            <span class="sidebar-next-title">{tut['prev_title']}</span>
            <span class="sidebar-next-arrow">&#8592;</span>
          </a>
        </div>'''
        
    next_block = ""
    if tut['next_slug']:
        next_block = f'''        <div class="sidebar-next">
          <h4>Next Tutorial</h4>
          <a href="../{tut['next_slug']}/" class="sidebar-next-link">
            <span class="sidebar-next-id">{tut['next_id'].upper()}</span>
            <span class="sidebar-next-title">{tut['next_title']}</span>
            <span class="sidebar-next-arrow">&#8594;</span>
          </a>
        </div>'''
        
    content = HTML_TEMPLATE.format(
        slug=tut['slug'],
        id=tut['id'],
        title=tut['title'],
        subtitle=tut['subtitle'],
        desc=tut['desc'],
        read_time=tut['read_time'],
        audience=tut['audience'],
        related_cards=related_cards_html.strip().replace('\\n', '\n'),
        prev_block=prev_block,
        next_block=next_block
    )
    
    # Save to file
    tut_dir = os.path.join(TUTORIALS_DIR, tut['slug'])
    os.makedirs(tut_dir, exist_ok=True)
    filepath = os.path.join(tut_dir, 'index.html')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Generated skeleton for {tut['id']} at {filepath}")

if __name__ == '__main__':
    for tut in TUTORIALS_DATA:
        generate_skeleton(tut)
