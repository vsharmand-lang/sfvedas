import os

WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIALS_DIR = os.path.join(WORKSPACE_DIR, 'tutorials')

TUTORIALS_DATA = [
    {
        'id': 'DEL-002',
        'slug': 'del-002',
        'title': 'Agile vs Waterfall for Salesforce Implementations: The Real Answer',
        'subtitle': 'An analytical breakdown of why pure Agile fails in enterprise Salesforce, why pure Waterfall is too slow, and how to construct a hybrid model that works.',
        'desc': 'Agile vs Waterfall for Salesforce Implementations: The Real Answer. A practical guide for Delivery Managers and Programme Leaders.',
        'read_time': '20',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-001',
        'prev_id': 'DEL-001',
        'prev_title': 'Running a Discovery Workshop for a Salesforce Programme',
        'next_slug': 'del-003',
        'next_id': 'DEL-003',
        'next_title': 'Sprint Cadence in Salesforce Projects: What Actually Works',
        'related': [
            {'slug': 'del-003', 'id': 'DEL-003', 'title': 'Sprint Cadence in Salesforce Projects'},
            {'slug': 'del-001', 'id': 'DEL-001', 'title': 'Running a Discovery Workshop'},
            {'slug': 'del-004', 'id': 'DEL-004', 'title': 'Technical Debt in Salesforce'}
        ]
    },
    {
        'id': 'DEL-003',
        'slug': 'del-003',
        'title': 'Sprint Cadence in Salesforce Projects: What Actually Works',
        'subtitle': 'Why the standard two-week sprint is often a disaster for Salesforce configuration, and how to optimise cadence for team velocity and platform stability.',
        'desc': 'Sprint Cadence in Salesforce Projects: What Actually Works. A deep dive into sprint planning and release cadence.',
        'read_time': '18',
        'audience': 'Delivery Managers · Solution Architects',
        'prev_slug': 'del-002',
        'prev_id': 'DEL-002',
        'prev_title': 'Agile vs Waterfall for Salesforce Implementations: The Real Answer',
        'next_slug': 'del-004',
        'next_id': 'DEL-004',
        'next_title': 'Technical Debt in Salesforce: How to Measure and Manage It',
        'related': [
            {'slug': 'del-004', 'id': 'DEL-004', 'title': 'Technical Debt in Salesforce'},
            {'slug': 'del-002', 'id': 'DEL-002', 'title': 'Agile vs Waterfall'},
            {'slug': 'del-001', 'id': 'DEL-001', 'title': 'Running a Discovery Workshop'}
        ]
    },
    {
        'id': 'DEL-004',
        'slug': 'del-004',
        'title': 'Technical Debt in Salesforce: How to Measure and Manage It',
        'subtitle': 'The delivery leader\'s tactical guide to quantifying customisation bloat, prioritising refactoring, and enforcing limits on technical debt.',
        'desc': 'Technical Debt in Salesforce: How to Measure and Manage It. Enforcing limits on customisation bloat.',
        'read_time': '22',
        'audience': 'Salesforce Architects · Delivery Managers',
        'prev_slug': 'del-003',
        'prev_id': 'DEL-003',
        'prev_title': 'Sprint Cadence in Salesforce Projects: What Actually Works',
        'next_slug': 'del-005',
        'next_id': 'DEL-005',
        'next_title': 'UAT Strategy for Salesforce: Beyond Click-Testing',
        'related': [
            {'slug': 'del-005', 'id': 'DEL-005', 'title': 'UAT Strategy for Salesforce'},
            {'slug': 'del-003', 'id': 'DEL-003', 'title': 'Sprint Cadence'},
            {'slug': 'del-002', 'id': 'DEL-002', 'title': 'Agile vs Waterfall'}
        ]
    },
    {
        'id': 'DEL-005',
        'slug': 'del-005',
        'title': 'UAT Strategy for Salesforce: Beyond Click-Testing',
        'subtitle': 'Why typical Salesforce user acceptance testing fails to prevent post-launch bugs, and how to structure scenarios that represent actual business operations.',
        'desc': 'UAT Strategy for Salesforce: Beyond Click-Testing. Structuring scenarios that represent actual operations.',
        'read_time': '20',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-004',
        'prev_id': 'DEL-004',
        'prev_title': 'Technical Debt in Salesforce: How to Measure and Manage It',
        'next_slug': 'del-006',
        'next_id': 'DEL-006',
        'next_title': 'Release Management for Salesforce: Environments, Pipelines, Approvals',
        'related': [
            {'slug': 'del-006', 'id': 'DEL-006', 'title': 'Release Management for Salesforce'},
            {'slug': 'del-004', 'id': 'DEL-004', 'title': 'Technical Debt in Salesforce'},
            {'slug': 'del-003', 'id': 'DEL-003', 'title': 'Sprint Cadence'}
        ]
    },
    {
        'id': 'DEL-006',
        'slug': 'del-006',
        'title': 'Release Management for Salesforce: Environments, Pipelines, Approvals',
        'subtitle': 'The architecture of a Salesforce sandbox pipeline, deployment branching strategies, and governance gates for continuous delivery.',
        'desc': 'Release Management for Salesforce: Environments, Pipelines, Approvals. Sandbox pipelines and branching strategies.',
        'read_time': '22',
        'audience': 'Salesforce Architects · Tech Leaders',
        'prev_slug': 'del-005',
        'prev_id': 'DEL-005',
        'prev_title': 'UAT Strategy for Salesforce: Beyond Click-Testing',
        'next_slug': 'del-007',
        'next_id': 'DEL-007',
        'next_title': 'Managing a Big Bang Go-Live: Risks, Mitigations, and the Decision to Flip',
        'related': [
            {'slug': 'del-007', 'id': 'DEL-007', 'title': 'Managing a Big Bang Go-Live'},
            {'slug': 'del-005', 'id': 'DEL-005', 'title': 'UAT Strategy'},
            {'slug': 'del-004', 'id': 'DEL-004', 'title': 'Technical Debt'}
        ]
    },
    {
        'id': 'DEL-008',
        'slug': 'del-008',
        'title': 'Phased Rollout Strategy: How to Phase Without Losing Momentum',
        'subtitle': 'How to design a phased roll-out plan by business unit, geography, or functionality, and avoid the pitfalls of maintaining parallel legacy systems.',
        'desc': 'Phased Rollout Strategy: How to Phase Without Losing Momentum. Phased roll-out plans by unit, geography, or function.',
        'read_time': '20',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-007',
        'prev_id': 'DEL-007',
        'prev_title': 'Managing a Big Bang Go-Live: Risks, Mitigations, and the Decision to Flip',
        'next_slug': 'del-009',
        'next_id': 'DEL-009',
        'next_title': 'Salesforce Project Estimation: The Honest Guide',
        'related': [
            {'slug': 'del-009', 'id': 'DEL-009', 'title': 'Salesforce Project Estimation'},
            {'slug': 'del-007', 'id': 'DEL-007', 'title': 'Managing a Big Bang Go-Live'},
            {'slug': 'del-010', 'id': 'DEL-010', 'title': 'Vendor Management on Salesforce'}
        ]
    },
    {
        'id': 'DEL-010',
        'slug': 'del-010',
        'title': 'Vendor Management on Salesforce Programmes: Holding Partners Accountable',
        'subtitle': 'The delivery leader\'s playbook for evaluating system integrators, enforcing contract SLAs, and navigating relationship friction without project delays.',
        'desc': 'Vendor Management on Salesforce Programmes. Playbook for evaluating system integrators and enforcing SLAs.',
        'read_time': '20',
        'audience': 'Delivery Managers · CTOs',
        'prev_slug': 'del-009',
        'prev_id': 'DEL-009',
        'prev_title': 'Salesforce Project Estimation: The Honest Guide',
        'next_slug': 'del-011',
        'next_id': 'DEL-011',
        'next_title': 'Offshore and Hybrid Delivery Models for Salesforce',
        'related': [
            {'slug': 'del-011', 'id': 'DEL-011', 'title': 'Offshore & Hybrid Delivery Models'},
            {'slug': 'del-009', 'id': 'DEL-009', 'title': 'Salesforce Project Estimation'},
            {'slug': 'del-012', 'id': 'DEL-012', 'title': 'Cutover Planning'}
        ]
    },
    {
        'id': 'DEL-011',
        'slug': 'del-011',
        'title': 'Offshore and Hybrid Delivery Models for Salesforce',
        'subtitle': 'Strategic orchestration of offshore developer pipelines and onshore business analysis to optimise cost-per-story-point without quality sacrifice.',
        'desc': 'Offshore and Hybrid Delivery Models for Salesforce. Strategic orchestration of offshore pipelines.',
        'read_time': '18',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-010',
        'prev_id': 'DEL-010',
        'prev_title': 'Vendor Management on Salesforce Programmes: Holding Partners Accountable',
        'next_slug': 'del-012',
        'next_id': 'DEL-012',
        'next_title': 'Cutover Planning: The 30-60-90 Day Plan Before Go-Live',
        'related': [
            {'slug': 'del-012', 'id': 'DEL-012', 'title': 'Cutover Planning'},
            {'slug': 'del-010', 'id': 'DEL-010', 'title': 'Vendor Management'},
            {'slug': 'del-009', 'id': 'DEL-009', 'title': 'Salesforce Project Estimation'}
        ]
    },
    {
        'id': 'DEL-012',
        'slug': 'del-012',
        'title': 'Cutover Planning: The 30-60-90 Day Plan Before Go-Live',
        'subtitle': 'A granular blueprint for the critical weeks preceding launch, mapping data migrations, freeze periods, dry runs, and team assignments.',
        'desc': 'Cutover Planning: The 30-60-90 Day Plan Before Go-Live. A granular blueprint for the critical weeks before launch.',
        'read_time': '25',
        'audience': 'Delivery Managers · Senior Practitioners',
        'prev_slug': 'del-011',
        'prev_id': 'DEL-011',
        'prev_title': 'Offshore and Hybrid Delivery Models for Salesforce',
        'next_slug': 'del-013',
        'next_id': 'DEL-013',
        'next_title': 'Hypercare After Go-Live: What Success Looks Like',
        'related': [
            {'slug': 'del-013', 'id': 'DEL-013', 'title': 'Hypercare After Go-Live'},
            {'slug': 'del-011', 'id': 'DEL-011', 'title': 'Offshore & Hybrid Delivery Models'},
            {'slug': 'del-010', 'id': 'DEL-010', 'title': 'Vendor Management'}
        ]
    },
    {
        'id': 'DEL-013',
        'slug': 'del-013',
        'title': 'Hypercare After Go-Live: What Success Looks Like',
        'subtitle': 'Defining critical triage support structures, response SLA targets, and user adoption metrics to secure stability in the post-launch window.',
        'desc': 'Hypercare After Go-Live: What Success Looks Like. Triage support structures and response SLAs.',
        'read_time': '18',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-012',
        'prev_id': 'DEL-012',
        'prev_title': 'Cutover Planning: The 30-60-90 Day Plan Before Go-Live',
        'next_slug': 'del-014',
        'next_id': 'DEL-014',
        'next_title': 'Running a Salesforce Programme Retrospective That Actually Changes Things',
        'related': [
            {'slug': 'del-014', 'id': 'DEL-014', 'title': 'Running a Salesforce Retrospective'},
            {'slug': 'del-012', 'id': 'DEL-012', 'title': 'Cutover Planning'},
            {'slug': 'del-011', 'id': 'DEL-011', 'title': 'Offshore & Hybrid Delivery Models'}
        ]
    },
    {
        'id': 'DEL-014',
        'slug': 'del-014',
        'title': 'Running a Salesforce Programme Retrospective That Actually Changes Things',
        'subtitle': 'How to move beyond performative post-mortems and extract real, actionable improvements to your environment, backlog, and team governance.',
        'desc': 'Running a Salesforce Programme Retrospective. Extracting real improvements to environment and team.',
        'read_time': '18',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-013',
        'prev_id': 'DEL-013',
        'prev_title': 'Hypercare After Go-Live: What Success Looks Like',
        'next_slug': 'del-015',
        'next_id': 'DEL-015',
        'next_title': 'Requirements Management: Stories, Epics, and the Gap Nobody Talks About',
        'related': [
            {'slug': 'del-015', 'id': 'DEL-015', 'title': 'Requirements Management'},
            {'slug': 'del-013', 'id': 'DEL-013', 'title': 'Hypercare After Go-Live'},
            {'slug': 'del-012', 'id': 'DEL-012', 'title': 'Cutover Planning'}
        ]
    },
    {
        'id': 'DEL-015',
        'slug': 'del-015',
        'title': 'Requirements Management: Stories, Epics, and the Gap Nobody Talks About',
        'subtitle': 'How to model Salesforce features to prevent translation gaps between non-technical stakeholders and technical Salesforce developers.',
        'desc': 'Requirements Management: Stories, Epics, and the Gap Nobody Talks About. Preventing translation gaps.',
        'read_time': '20',
        'audience': 'Delivery Managers · Salesforce Architects',
        'prev_slug': 'del-014',
        'prev_id': 'DEL-014',
        'prev_title': 'Running a Salesforce Programme Retrospective That Actually Changes Things',
        'next_slug': 'del-016',
        'next_id': 'DEL-016',
        'next_title': 'Change Request Management on Salesforce Projects',
        'related': [
            {'slug': 'del-016', 'id': 'DEL-016', 'title': 'Change Request Management'},
            {'slug': 'del-014', 'id': 'DEL-014', 'title': 'Running a Salesforce Retrospective'},
            {'slug': 'del-013', 'id': 'DEL-013', 'title': 'Hypercare After Go-Live'}
        ]
    },
    {
        'id': 'DEL-016',
        'slug': 'del-016',
        'title': 'Change Request Management on Salesforce Projects',
        'subtitle': 'A structured, zero-ambiguity workflow for evaluating, estimating, and approving change requests without stalling existing delivery sprint velocity.',
        'desc': 'Change Request Management on Salesforce Projects. Evaluating, estimating, and approving CRs.',
        'read_time': '18',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-015',
        'prev_id': 'DEL-015',
        'prev_title': 'Requirements Management: Stories, Epics, and the Gap Nobody Talks About',
        'next_slug': 'del-017',
        'next_id': 'DEL-017',
        'next_title': 'Dependency Management in Multi-Workstream Salesforce Programmes',
        'related': [
            {'slug': 'del-017', 'id': 'DEL-017', 'title': 'Dependency Management'},
            {'slug': 'del-015', 'id': 'DEL-015', 'title': 'Requirements Management'},
            {'slug': 'del-014', 'id': 'DEL-014', 'title': 'Running a Salesforce Retrospective'}
        ]
    },
    {
        'id': 'DEL-017',
        'slug': 'del-017',
        'title': 'Dependency Management in Multi-Workstream Salesforce Programmes',
        'subtitle': 'Mapping shared metadata components, resolving sequence blockages, and aligning release paths across concurrent Salesforce teams.',
        'desc': 'Dependency Management in Multi-Workstream Salesforce Programmes. Mapping shared metadata.',
        'read_time': '20',
        'audience': 'Salesforce Architects · Delivery Managers',
        'prev_slug': 'del-016',
        'prev_id': 'DEL-016',
        'prev_title': 'Change Request Management on Salesforce Projects',
        'next_slug': 'del-018',
        'next_id': 'DEL-018',
        'next_title': 'Risk Management for Salesforce Implementations',
        'related': [
            {'slug': 'del-018', 'id': 'DEL-018', 'title': 'Risk Management'},
            {'slug': 'del-016', 'id': 'DEL-016', 'title': 'Change Request Management'},
            {'slug': 'del-015', 'id': 'DEL-015', 'title': 'Requirements Management'}
        ]
    },
    {
        'id': 'DEL-018',
        'slug': 'del-018',
        'title': 'Risk Management for Salesforce Implementations',
        'subtitle': 'How to construct a predictive risk register tailored to specific Salesforce pitfalls like data volume limitations, sandbox drift, and legacy API deprecation.',
        'desc': 'Risk Management for Salesforce Implementations. Constructing a predictive risk register.',
        'read_time': '22',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-017',
        'prev_id': 'DEL-017',
        'prev_title': 'Dependency Management in Multi-Workstream Salesforce Programmes',
        'next_slug': 'del-019',
        'next_id': 'DEL-019',
        'next_title': 'Configuration Management: Tracking What Was Changed, When, and Why',
        'related': [
            {'slug': 'del-019', 'id': 'DEL-019', 'title': 'Configuration Management'},
            {'slug': 'del-017', 'id': 'DEL-017', 'title': 'Dependency Management'},
            {'slug': 'del-016', 'id': 'DEL-016', 'title': 'Change Request Management'}
        ]
    },
    {
        'id': 'DEL-019',
        'slug': 'del-019',
        'title': 'Configuration Management: Tracking What Was Changed, When, and Why',
        'subtitle': 'Best practices for source of truth configuration, mapping user stories to physical metadata changes, and enforcing audit trials for compliance.',
        'desc': 'Configuration Management: Tracking What Was Changed. Enforcing audit trails for compliance.',
        'read_time': '18',
        'audience': 'Salesforce Architects · Delivery Managers',
        'prev_slug': 'del-018',
        'prev_id': 'DEL-018',
        'prev_title': 'Risk Management for Salesforce Implementations',
        'next_slug': 'del-020',
        'next_id': 'DEL-020',
        'next_title': 'User Training Strategy for Salesforce Rollouts',
        'related': [
            {'slug': 'del-020', 'id': 'DEL-020', 'title': 'User Training Strategy'},
            {'slug': 'del-018', 'id': 'DEL-018', 'title': 'Risk Management'},
            {'slug': 'del-017', 'id': 'DEL-017', 'title': 'Dependency Management'}
        ]
    },
    {
        'id': 'DEL-020',
        'slug': 'del-020',
        'title': 'User Training Strategy for Salesforce Rollouts',
        'subtitle': 'Moving past generic classroom instruction to construct role-based sandbox labs, on-demand videos, and integrated in-app guidance.',
        'desc': 'User Training Strategy for Salesforce Rollouts. Constructing role-based sandbox labs.',
        'read_time': '18',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-019',
        'prev_id': 'DEL-019',
        'prev_title': 'Configuration Management: Tracking What Was Changed, When, and Why',
        'next_slug': 'del-021',
        'next_id': 'DEL-021',
        'next_title': 'Managing Scope Creep on Salesforce Programmes',
        'related': [
            {'slug': 'del-021', 'id': 'DEL-021', 'title': 'Managing Scope Creep'},
            {'slug': 'del-019', 'id': 'DEL-019', 'title': 'Configuration Management'},
            {'slug': 'del-018', 'id': 'DEL-018', 'title': 'Risk Management'}
        ]
    },
    {
        'id': 'DEL-021',
        'slug': 'del-021',
        'title': 'Managing Scope Creep on Salesforce Programmes',
        'subtitle': 'Practical methods for holding the line against low-value stakeholder requests while preserving positive relationships and program velocity.',
        'desc': 'Managing Scope Creep on Salesforce Programmes. Holding the line against low-value requests.',
        'read_time': '20',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-020',
        'prev_id': 'DEL-020',
        'prev_title': 'User Training Strategy for Salesforce Rollouts',
        'next_slug': 'del-022',
        'next_id': 'DEL-022',
        'next_title': 'Salesforce Data Migration: The Delivery Leader\'s Checklist',
        'related': [
            {'slug': 'del-022', 'id': 'DEL-022', 'title': 'Salesforce Data Migration'},
            {'slug': 'del-020', 'id': 'DEL-020', 'title': 'User Training Strategy'},
            {'slug': 'del-019', 'id': 'DEL-019', 'title': 'Configuration Management'}
        ]
    },
    {
        'id': 'DEL-022',
        'slug': 'del-022',
        'title': 'Salesforce Data Migration: The Delivery Leader\'s Checklist',
        'subtitle': 'The absolute checklists for deduplication, mapping relational tables, dry runs, and schema preparations to guarantee zero-loss go-live loads.',
        'desc': 'Salesforce Data Migration: The Delivery Leader\'s Checklist. Schema preparations for zero-loss.',
        'read_time': '22',
        'audience': 'Salesforce Architects · Delivery Managers',
        'prev_slug': 'del-021',
        'prev_id': 'DEL-021',
        'prev_title': 'Managing Scope Creep on Salesforce Programmes',
        'next_slug': 'del-023',
        'next_id': 'DEL-023',
        'next_title': 'Testing Strategy: Unit, Integration, and Regression in Salesforce',
        'related': [
            {'slug': 'del-023', 'id': 'DEL-023', 'title': 'Testing Strategy: Unit, Int, Reg'},
            {'slug': 'del-021', 'id': 'DEL-021', 'title': 'Managing Scope Creep'},
            {'slug': 'del-020', 'id': 'DEL-020', 'title': 'User Training Strategy'}
        ]
    },
    {
        'id': 'DEL-023',
        'slug': 'del-023',
        'title': 'Testing Strategy: Unit, Integration, and Regression in Salesforce',
        'subtitle': 'Balancing local Apex unit coverage demands with full regression frameworks and functional end-to-end interface validations.',
        'desc': 'Testing Strategy: Unit, Integration, and Regression. Balancing Apex coverage and regression frameworks.',
        'read_time': '22',
        'audience': 'Salesforce Architects · Tech Leaders',
        'prev_slug': 'del-022',
        'prev_id': 'DEL-022',
        'prev_title': 'Salesforce Data Migration: The Delivery Leader\'s Checklist',
        'next_slug': 'del-024',
        'next_id': 'DEL-024',
        'next_title': 'Running a Salesforce Steering Committee That Actually Steers',
        'related': [
            {'slug': 'del-024', 'id': 'DEL-024', 'title': 'Running a Salesforce SteerCo'},
            {'slug': 'del-022', 'id': 'DEL-022', 'title': 'Salesforce Data Migration'},
            {'slug': 'del-021', 'id': 'DEL-021', 'title': 'Managing Scope Creep'}
        ]
    },
    {
        'id': 'DEL-024',
        'slug': 'del-024',
        'title': 'Running a Salesforce Steering Committee That Actually Steers',
        'subtitle': 'Structuring executive committee meetings to yield actionable decisions, resolve escalated programme risks, and maintain strategic support.',
        'desc': 'Running a Salesforce Steering Committee That Actually Steers. Yielding executive actions and decisions.',
        'read_time': '18',
        'audience': 'Delivery Managers · CTOs',
        'prev_slug': 'del-023',
        'prev_id': 'DEL-023',
        'prev_title': 'Testing Strategy: Unit, Integration, and Regression in Salesforce',
        'next_slug': 'del-025',
        'next_id': 'DEL-025',
        'next_title': 'Post-Go-Live Support Models: In-House vs Partner vs Hybrid',
        'related': [
            {'slug': 'del-025', 'id': 'DEL-025', 'title': 'Post-Go-Live Support Models'},
            {'slug': 'del-023', 'id': 'DEL-023', 'title': 'Testing Strategy'},
            {'slug': 'del-022', 'id': 'DEL-022', 'title': 'Salesforce Data Migration'}
        ]
    },
    {
        'id': 'DEL-025',
        'slug': 'del-025',
        'title': 'Post-Go-Live Support Models: In-House vs Partner vs Hybrid',
        'subtitle': 'The economic and operational trade-offs of building an internal Center of Excellence vs retaining external managed services.',
        'desc': 'Post-Go-Live Support Models. Trade-offs of internal CoE vs external managed services.',
        'read_time': '20',
        'audience': 'Delivery Managers · CTOs',
        'prev_slug': 'del-024',
        'prev_id': 'DEL-024',
        'prev_title': 'Running a Salesforce Steering Committee That Actually Steers',
        'next_slug': 'del-026',
        'next_id': 'DEL-026',
        'next_title': 'Programme Governance for Large-Scale Salesforce Implementations',
        'related': [
            {'slug': 'del-026', 'id': 'DEL-026', 'title': 'Programme Governance'},
            {'slug': 'del-024', 'id': 'DEL-024', 'title': 'Running a Salesforce SteerCo'},
            {'slug': 'del-023', 'id': 'DEL-023', 'title': 'Testing Strategy'}
        ]
    },
    {
        'id': 'DEL-026',
        'slug': 'del-026',
        'title': 'Programme Governance for Large-Scale Salesforce Implementations',
        'subtitle': 'Aligning business architecture, solution design authority, and sprint execution models under a unified operational governance framework.',
        'desc': 'Programme Governance for Large-Scale Salesforce Implementations. Solution design authority models.',
        'read_time': '22',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-025',
        'prev_id': 'DEL-025',
        'prev_title': 'Post-Go-Live Support Models: In-House vs Partner vs Hybrid',
        'next_slug': 'del-027',
        'next_id': 'DEL-027',
        'next_title': 'The Delivery Leader\'s Guide to Salesforce Technical Reviews',
        'related': [
            {'slug': 'del-027', 'id': 'DEL-027', 'title': 'Salesforce Technical Reviews'},
            {'slug': 'del-025', 'id': 'DEL-025', 'title': 'Post-Go-Live Support Models'},
            {'slug': 'del-024', 'id': 'DEL-024', 'title': 'Running a Salesforce SteerCo'}
        ]
    },
    {
        'id': 'DEL-027',
        'slug': 'del-027',
        'title': 'The Delivery Leader\'s Guide to Salesforce Technical Reviews',
        'subtitle': 'How to run independent code and architecture reviews to audit vendor quality, catch security gaps, and secure long-term org health.',
        'desc': 'The Delivery Leader\'s Guide to Salesforce Technical Reviews. Catching security and quality gaps.',
        'read_time': '20',
        'audience': 'Delivery Managers · Tech Leaders',
        'prev_slug': 'del-026',
        'prev_id': 'DEL-026',
        'prev_title': 'Programme Governance for Large-Scale Salesforce Implementations',
        'next_slug': None,
        'next_id': None,
        'next_title': None,
        'related': [
            {'slug': 'del-026', 'id': 'DEL-026', 'title': 'Programme Governance'},
            {'slug': 'del-025', 'id': 'DEL-025', 'title': 'Post-Go-Live Support Models'},
            {'slug': 'del-001', 'id': 'DEL-001', 'title': 'Running a Discovery Workshop'}
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
        <a href="/tutorials/?tag=delivery-management" style="font-family:var(--font-ui);font-size:0.8rem;color:var(--sage-green);text-decoration:none;">← Back to Delivery Management</a>
      </div>
      <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px;flex-wrap:wrap;">
        <span class="card-id">{id}</span>
        <span class="card-tag" style="background:rgba(232,147,10,0.08);color:var(--saffron);border-color:rgba(232,147,10,0.2);">Delivery Management</span>
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
          <p style="font-family:var(--font-ui);font-size:0.75rem;color:var(--text-secondary);margin:0;">Salesforce Delivery Specialist · Updated May 2026</p>
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
              <span class="card-id">{r['id']}</span>
              <h4>{r['title']}</h4>
            </a>\\n'''
            
    # Prev/Next Blocks
    prev_block = ""
    if tut['prev_slug']:
        prev_block = f'''        <div class="sidebar-next">
          <h4>Previous Tutorial</h4>
          <a href="../{tut['prev_slug']}/" class="sidebar-next-link">
            <span class="sidebar-next-id">{tut['prev_id']}</span>
            <span class="sidebar-next-title">{tut['prev_title']}</span>
            <span class="sidebar-next-arrow">&#8592;</span>
          </a>
        </div>'''
        
    next_block = ""
    if tut['next_slug']:
        next_block = f'''        <div class="sidebar-next">
          <h4>Next Tutorial</h4>
          <a href="../{tut['next_slug']}/" class="sidebar-next-link">
            <span class="sidebar-next-id">{tut['next_id']}</span>
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
        related_cards=related_cards_html.strip(),
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
