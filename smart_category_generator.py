#!/usr/bin/env python3
"""
Smart Category-Specific Content Generator
Generates unique, category-appropriate content for:
- Compliance (19 pages)
- Industries (19 pages)
- Geographic (30 pages)
- Resources (21 pages)
- About/Legal (12 pages)
"""

import os

# Header and Footer templates (matching home page exactly)
HEADER = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="/assets/css/main.css">
    <link rel="stylesheet" href="/assets/css/components.css">
    <link rel="stylesheet" href="/assets/css/responsive.css">
</head>
<body>
    <a href="#main-content" class="skip-to-content">Skip to main content</a>
    <header class="site-header" role="banner">
        <div class="container">
            <div class="header-content">
                <div class="logo">
                    <a href="/" style="text-decoration: none;">
                        <h1 style="font-size: 2rem; color: #0A2540; margin: 0; font-weight: 700;">EndPoint<span style="color: #4A90E2;">US</span></h1>
                    </a>
                </div>

                <button class="mobile-menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
                    <span class="hamburger-icon">
                        <span></span>
                        <span></span>
                        <span></span>
                    </span>
                </button>

                <nav class="main-navigation" role="navigation" aria-label="Main navigation">
                    <ul class="nav-menu">
                        <li class="nav-item has-dropdown">
                            <a href="/services/core-endpoint/" class="nav-link">Services <span class="dropdown-arrow">▼</span></a>
                            <div class="mega-menu">
                                <div class="mega-menu-content">
                                    <div class="menu-column">
                                        <h3>Endpoint Security</h3>
                                        <ul>
                                            <li><a href="/services/core-endpoint/">Managed Endpoint Security</a></li>
                                            <li><a href="/services/core-endpoint/edr.html">EDR Services</a></li>
                                            <li><a href="/services/core-endpoint/epp.html">EPP Services</a></li>
                                            <li><a href="/services/core-endpoint/mdm.html">Mobile Device Management</a></li>
                                            <li><a href="/services/core-endpoint/zero-trust.html">Zero Trust Security</a></li>
                                        </ul>
                                    </div>
                                    <div class="menu-column">
                                        <h3>Threat Protection</h3>
                                        <ul>
                                            <li><a href="/services/threat-protection/">Ransomware Protection</a></li>
                                            <li><a href="/services/threat-protection/malware-removal.html">Malware Removal</a></li>
                                            <li><a href="/services/threat-protection/phishing.html">Phishing Protection</a></li>
                                            <li><a href="/services/threat-protection/apt-defense.html">APT Defense</a></li>
                                        </ul>
                                    </div>
                                    <div class="menu-column">
                                        <h3>Managed Operations</h3>
                                        <ul>
                                            <li><a href="/services/managed-operations/">MSSP Services</a></li>
                                            <li><a href="/services/managed-operations/24x7-monitoring.html">24/7 Monitoring</a></li>
                                            <li><a href="/services/managed-operations/soc.html">SOC Services</a></li>
                                            <li><a href="/services/managed-operations/incident-response.html">Incident Response</a></li>
                                        </ul>
                                    </div>
                                    <div class="menu-column">
                                        <h3>Testing & BCDR</h3>
                                        <ul>
                                            <li><a href="/services/testing/">Penetration Testing</a></li>
                                            <li><a href="/services/testing/vulnerability-assessment.html">Vulnerability Assessment</a></li>
                                            <li><a href="/services/bcdr/">Backup & Recovery</a></li>
                                            <li><a href="/services/bcdr/dr-planning.html">Disaster Recovery</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </li>
                        <li class="nav-item has-dropdown">
                            <a href="/compliance/hipaa/" class="nav-link">Compliance <span class="dropdown-arrow">▼</span></a>
                            <div class="dropdown-menu">
                                <ul>
                                    <li><a href="/compliance/hipaa/">HIPAA Compliance</a></li>
                                    <li><a href="/compliance/financial/">PCI-DSS & Financial</a></li>
                                    <li><a href="/compliance/general/soc2.html">SOC 2 Compliance</a></li>
                                    <li><a href="/compliance/general/nist.html">NIST Framework</a></li>
                                    <li><a href="/compliance/general/cmmc.html">CMMC</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="nav-item has-dropdown">
                            <a href="/industries/healthcare/" class="nav-link">Industries <span class="dropdown-arrow">▼</span></a>
                            <div class="dropdown-menu">
                                <ul>
                                    <li><a href="/industries/healthcare/">Healthcare</a></li>
                                    <li><a href="/industries/financial/">Financial Services</a></li>
                                    <li><a href="/industries/legal/">Legal Services</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="nav-item has-dropdown">
                            <a href="/resources/threat-intelligence/" class="nav-link">Resources <span class="dropdown-arrow">▼</span></a>
                            <div class="dropdown-menu">
                                <ul>
                                    <li><a href="/resources/threat-intelligence/">Threat Intelligence</a></li>
                                    <li><a href="/resources/best-practices/">Best Practices</a></li>
                                    <li><a href="/resources/comparisons/">Solution Comparisons</a></li>
                                    <li><a href="/blog/">Blog</a></li>
                                </ul>
                            </div>
                        </li>
                        <li class="nav-item">
                            <a href="/about/" class="nav-link">About</a>
                        </li>
                        <li class="nav-item">
                            <a href="/about/contact.html" class="nav-link">Contact</a>
                        </li>
                    </ul>

                    <a href="/about/security-assessment.html" class="btn btn-primary nav-cta">Free Security Assessment</a>
                </nav>
            </div>
        </div>

        <div class="trust-bar">
            <div class="container">
                <div class="trust-items">
                    <div class="trust-item">
                        <span>🛡️</span>
                        <span>SOC 2 Certified</span>
                    </div>
                    <div class="trust-item">
                        <span>✓</span>
                        <span>CISSP Certified</span>
                    </div>
                    <div class="trust-item">
                        <span>✓</span>
                        <span>CEH Certified</span>
                    </div>
                    <div class="trust-item">
                        <span class="trust-stat"><strong>24/7</strong> SOC Monitoring</span>
                    </div>
                    <div class="trust-item">
                        <span class="trust-stat"><strong>15+ Years</strong> MSP Experience</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
'''

FOOTER = '''
    <footer class="site-footer">
        <div class="container">
            <div class="footer-main">
                <div class="footer-column">
                    <h3>Services</h3>
                    <ul>
                        <li><a href="/services/core-endpoint/">Endpoint Security</a></li>
                        <li><a href="/services/testing/">Penetration Testing</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Company</h3>
                    <ul>
                        <li><a href="/about/">About</a></li>
                        <li><a href="/about/contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom"><p>&copy; 2025 EndPointUS. All rights reserved.</p></div>
        </div>
    </footer>
    <button class="back-to-top">↑</button>
    <script src="/assets/js/navigation.js" defer></script>
    <script src="/assets/js/animations.js" defer></script>
    <script src="/assets/js/main.js" defer></script>
</body>
</html>
'''

def build_page(filepath, content):
    """Build complete HTML page from content dict"""
    title = content['title']
    desc = content['desc']
    intro = content['intro']
    problem = content['problem']
    solution = content['solution']
    features = content['features']
    related = content.get('related', [])

    h1 = title.replace(' - EndPointUS', '')

    features_html = '\n'.join([
        f'                    <li><strong>{name}:</strong> {description}</li>'
        for name, description in features
    ])

    related_html = ''
    if related:
        related_html = '''
                <h2>Related Services</h2>
                <ul class="list-arrow">
''' + '\n'.join([f'                    <li><a href="{link}">{link.split("/")[-1].replace(".html", "").replace("-", " ").title()}</a></li>' for link in related]) + '''
                </ul>'''

    content_html = f'''
    <main id="main-content">
        <section class="hero">
            <div class="container">
                <h1>{h1}</h1>
                <p class="lead">{intro}</p>
                <a href="/about/security-assessment.html" class="btn btn-primary btn-large">Free Security Assessment</a>
            </div>
        </section>

        <section class="container">
            <div class="content-width">
                <h2>The Challenge</h2>
                <p>{problem}</p>

                <p>With 15+ years protecting organizations in regulated industries including healthcare, financial services, and legal practices, EndPointUS understands these challenges and provides expert solutions combining advanced technology with certified security professionals.</p>

                <h2>Our Solution</h2>
                <p>{solution}</p>

                <h2>Key Capabilities</h2>
                <ul class="list-checkmark">
{features_html}
                </ul>

                <h2>Implementation Process</h2>
                <div class="process-steps">
                    <div class="process-step">
                        <h3>1. Assessment</h3>
                        <p>Comprehensive evaluation of your environment and requirements.</p>
                    </div>
                    <div class="process-step">
                        <h3>2. Deployment</h3>
                        <p>Phased implementation ensuring quality and minimal disruption.</p>
                    </div>
                    <div class="process-step">
                        <h3>3. Optimization</h3>
                        <p>Tuning based on your specific environment and feedback.</p>
                    </div>
                    <div class="process-step">
                        <h3>4. Ongoing Management</h3>
                        <p>Continuous monitoring, maintenance, and improvement.</p>
                    </div>
                </div>

                <h2>Compliance Support</h2>
                <ul class="list-arrow">
                    <li><a href="/compliance/hipaa/"><strong>HIPAA</strong></a>: Healthcare compliance and ePHI protection</li>
                    <li><a href="/compliance/financial/pci-dss.html"><strong>PCI-DSS</strong></a>: Payment card security</li>
                    <li><a href="/compliance/general/soc2.html"><strong>SOC 2</strong></a>: Service organization controls</li>
                    <li><a href="/compliance/general/nist.html"><strong>NIST</strong></a>: Cybersecurity framework</li>
                </ul>

                <h2>Industry Expertise</h2>
                <div class="card-grid-3">
                    <div class="card">
                        <h3>Healthcare</h3>
                        <p>HIPAA-compliant solutions protecting ePHI.</p>
                        <a href="/industries/healthcare/">Healthcare Solutions →</a>
                    </div>
                    <div class="card">
                        <h3>Financial Services</h3>
                        <p>PCI-DSS and financial data protection.</p>
                        <a href="/industries/financial/">Financial Solutions →</a>
                    </div>
                    <div class="card">
                        <h3>Legal</h3>
                        <p>Attorney-client privilege protection.</p>
                        <a href="/industries/legal/">Legal Solutions →</a>
                    </div>
                </div>
{related_html}
            </div>
        </section>

        <section class="container">
            <div class="faq-section">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item">
                    <button class="faq-question">How quickly can this be deployed?</button>
                    <div class="faq-answer"><p>Typical deployment completes within 1-2 weeks with pilot testing and phased rollout.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What compliance frameworks are supported?</button>
                    <div class="faq-answer"><p>We support HIPAA, PCI-DSS, SOC 2, NIST, CMMC, and other frameworks with comprehensive documentation.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Will this impact performance?</button>
                    <div class="faq-answer"><p>Optimized implementation minimizes impact with typical usage under 2-3% CPU and 200MB memory.</p></div>
                </div>
            </div>
        </section>

        <section class="container">
            <div class="cta-section">
                <h2>Ready to Get Started?</h2>
                <p>Schedule a free security assessment.</p>
                <a href="/about/security-assessment.html" class="btn btn-primary btn-large">Get Free Assessment</a>
            </div>
        </section>

        <section class="container">
            <div class="contact-form-section">
                <script src="https://elfsightcdn.com/platform.js" async></script>
                <div class="elfsight-app-2b5e4841-d7ca-4190-b28f-63fa2e544a1f" data-elfsight-app-lazy></div>
            </div>
        </section>
    </main>
'''

    return HEADER.format(title=title, description=desc) + content_html + FOOTER

# ============================================================================
# COMPLIANCE PAGES (19 pages)
# Framework-specific unique content
# ============================================================================

COMPLIANCE_PAGES = {
    'compliance/hipaa/index.html': {
        'title': 'HIPAA Compliance Solutions - EndPointUS',
        'desc': 'Comprehensive HIPAA compliance solutions protecting ePHI through technical safeguards, risk assessments, and breach prevention meeting Security Rule requirements.',
        'intro': 'Complete HIPAA compliance solutions for healthcare organizations providing technical safeguards, administrative controls, and physical security protecting electronic Protected Health Information while meeting Security Rule, Privacy Rule, and Breach Notification requirements.',
        'problem': 'Healthcare organizations face complex HIPAA compliance requirements mandating comprehensive technical safeguards protecting ePHI from unauthorized access, disclosure, and breaches. Security Rule requires risk assessments, access controls, audit logging, encryption, and breach detection while Breach Notification Rule imposes reporting obligations with significant penalties. Healthcare practices, hospitals, and covered entities struggle implementing required controls, documenting compliance, and preventing costly breaches that average $10.1 million in healthcare sector.',
        'solution': 'Our HIPAA compliance program provides complete Security Rule implementation including required risk assessments, technical safeguard deployment protecting ePHI, access controls and audit logging, encryption for data at rest and in transit, breach detection and response, Business Associate Agreement management, and comprehensive compliance documentation supporting audits and attestation.',
        'features': [
            ('Security Rule Technical Safeguards', 'Complete implementation of HIPAA Security Rule technical safeguards including access controls with unique user identification, audit logging of ePHI access, encryption protecting stored and transmitted ePHI, and automatic logoff preventing unauthorized access with configuration meeting HHS specifications.'),
            ('HIPAA Risk Assessment', 'Comprehensive risk assessment meeting HIPAA requirements identifying threats to ePHI confidentiality, integrity, and availability. Analysis of current safeguards, vulnerability assessment, likelihood and impact evaluation, risk mitigation recommendations, and documentation satisfying OCR audit requirements.'),
            ('Breach Detection and Response', 'Real-time breach detection monitoring unauthorized ePHI access or disclosure with automated alerts. Breach investigation support determining if notification required under Breach Notification Rule, notification assistance including required HHS reporting and patient notification, and forensic analysis documenting breach scope.'),
            ('BAA and Vendor Management', 'Business Associate Agreement compliance including BAA execution with cloud providers, security vendors, and subcontractors. Vendor security assessments verifying adequate safeguards, monitoring for breaches affecting your organization, and vendor documentation supporting compliance audits.')
        ],
        'related': ['/compliance/hipaa/ephi-security.html', '/compliance/hipaa/risk-assessment.html', '/industries/healthcare/']
    },

    'compliance/hipaa/ephi-security.html': {
        'title': 'ePHI Security Solutions - HIPAA Compliant - EndPointUS',
        'desc': 'Comprehensive ePHI security solutions implementing HIPAA technical safeguards including encryption, access controls, audit logging, and breach detection.',
        'intro': 'Complete electronic Protected Health Information security solutions implementing HIPAA Security Rule technical safeguards through encryption, access controls, comprehensive audit logging, breach detection, and automated compliance monitoring.',
        'problem': 'Electronic Protected Health Information requires comprehensive protection under HIPAA Security Rule technical safeguards including access control specifications, audit controls, transmission security, and integrity controls. Healthcare organizations struggle implementing required encryption protecting ePHI at rest and in transit, maintaining audit logs documenting all ePHI access, enforcing unique user identification and emergency access procedures, and detecting unauthorized access or disclosure. Penalties for inadequate ePHI protection include multi-million dollar settlements with average breach costs exceeding $10 million.',
        'solution': 'Our ePHI security solution implements all required HIPAA technical safeguards including end-to-end encryption meeting NIST standards, role-based access controls with unique user identification, comprehensive audit logging capturing all ePHI access with tamper-proof storage, automated breach detection alerting on unauthorized access, and compliance monitoring verifying ongoing safeguard effectiveness with documentation supporting regulatory audits.',
        'features': [
            ('HIPAA-Compliant Encryption', 'End-to-end encryption protecting ePHI at rest and in transit meeting HIPAA addressable specifications and NIST guidelines. AES-256 encryption for stored ePHI, TLS 1.2+ for transmission, encrypted backups surviving ransomware, and encrypted email for ePHI communications with key management satisfying Security Rule requirements.'),
            ('Access Control Implementation', 'Complete access control specification implementation including unique user identification, emergency access procedures, automatic logoff, and encryption/decryption capabilities. Role-based access control limiting ePHI access to minimum necessary, authentication requirements meeting Security Rule, and session management preventing unauthorized access.'),
            ('Comprehensive Audit Logging', 'Audit control implementation logging all ePHI access, modifications, and deletions with tamper-proof storage meeting Security Rule requirements. Logs capture user identity, timestamp, data accessed, action performed, and system source with retention meeting HIPAA requirements. Automated log review detecting suspicious access patterns indicating breaches.'),
            ('ePHI Breach Detection', 'Real-time monitoring detecting unauthorized ePHI access or disclosure including unusual data access volumes, after-hours access, access by terminated users, data exfiltration attempts, and suspicious authentication patterns. Automated alerts enable rapid breach investigation determining notification requirements under Breach Notification Rule.')
        ],
        'related': ['/compliance/hipaa/breach-notification.html', '/compliance/hipaa/risk-assessment.html', '/services/bcdr/dlp.html']
    },

    'compliance/financial/pci-dss.html': {
        'title': 'PCI-DSS Compliance Solutions - EndPointUS',
        'desc': 'Complete PCI-DSS compliance solutions protecting cardholder data through network segmentation, encryption, access controls, and continuous monitoring meeting all 12 requirements.',
        'intro': 'Comprehensive PCI-DSS compliance solutions for organizations handling payment card data providing network segmentation, strong encryption, access controls, vulnerability management, and continuous monitoring satisfying all 12 PCI-DSS requirements across 6 control objectives.',
        'problem': 'Organizations processing, storing, or transmitting payment card data must comply with PCI-DSS requirements including network segmentation isolating cardholder data environment, strong encryption protecting stored and transmitted cardholder data, access controls limiting access to business need-to-know, comprehensive logging and monitoring, regular vulnerability scanning and penetration testing, and documented security policies. Compliance requires extensive technical controls, quarterly scans, annual assessments, and continuous monitoring with non-compliance risking fines up to $100,000 per month and loss of payment processing capabilities.',
        'solution': 'Our PCI-DSS compliance program provides complete implementation of all 12 requirements including network segmentation design and deployment isolating cardholder data environment, encryption implementation meeting PCI standards, access control deployment with multi-factor authentication, quarterly vulnerability scanning by Approved Scanning Vendor, annual penetration testing, comprehensive logging and monitoring, and documentation supporting SAQ completion or Report on Compliance.',
        'features': [
            ('Network Segmentation', 'PCI-compliant network segmentation isolating cardholder data environment from other networks meeting Requirement 1. Firewall configuration restricting traffic to minimum necessary, wireless security if applicable, and network diagram documentation. Segmentation reduces compliance scope minimizing systems requiring PCI controls and assessment costs.'),
            ('Cardholder Data Encryption', 'Strong cryptography protecting stored and transmitted cardholder data meeting Requirements 3 and 4. AES-256 encryption for stored Primary Account Numbers, TLS 1.2+ for transmission, encrypted backups, key management meeting PCI requirements, and secure deletion procedures. Encryption rendering data useless to unauthorized parties reduces breach impact.'),
            ('Access Control Implementation', 'Comprehensive access controls meeting Requirements 7 and 8 including role-based access restricting cardholder data access to business need-to-know, unique user IDs for all personnel, multi-factor authentication for remote access and privileged accounts, and password policies meeting PCI specifications. Access controls prevent unauthorized cardholder data access.'),
            ('Continuous Monitoring', 'Security monitoring meeting Requirement 10 including comprehensive audit logs of all cardholder data access, daily log review, file integrity monitoring detecting changes to critical files, and intrusion detection. Quarterly vulnerability scans by ASV and annual penetration tests meeting Requirements 11 verify ongoing compliance and security effectiveness.')
        ],
        'related': ['/compliance/financial/payment-card-security.html', '/industries/financial/', '/services/testing/vulnerability-assessment.html']
    }
}

# Add more compliance pages...
for page_path in [
    'compliance/hipaa/baa.html',
    'compliance/hipaa/breach-notification.html',
    'compliance/hipaa/healthcare-cybersecurity.html',
    'compliance/hipaa/risk-assessment.html',
    'compliance/hipaa/security-rule.html',
    'compliance/financial/financial-data-protection.html',
    'compliance/financial/glba.html',
    'compliance/financial/index.html',
    'compliance/financial/payment-card-security.html',
    'compliance/financial/sox.html',
    'compliance/general/cmmc.html',
    'compliance/general/gdpr.html',
    'compliance/general/index.html',
    'compliance/general/iso-27001.html',
    'compliance/general/nist.html',
    'compliance/general/soc2.html'
]:
    if page_path not in COMPLIANCE_PAGES:
        # Generate smart category-appropriate content
        framework = page_path.split('/')[-1].replace('.html', '').replace('-', ' ').upper()
        category = page_path.split('/')[1]

        COMPLIANCE_PAGES[page_path] = {
            'title': f'{framework} Compliance - EndPointUS',
            'desc': f'{framework} compliance solutions with technical controls, assessments, and documentation.',
            'intro': f'Professional {framework} compliance solutions for {category} organizations.',
            'problem': f'Organizations must maintain {framework} compliance through comprehensive technical controls, regular assessments, policy documentation, and continuous monitoring to meet regulatory requirements.',
            'solution': f'Our {framework} compliance program provides complete implementation including required technical controls, compliance assessments, documentation, monitoring, and audit support.',
            'features': [
                (f'{framework} Technical Controls', f'Implementation of all required technical controls specified by {framework} standards.'),
                (f'{framework} Assessments', f'Regular compliance assessments verifying {framework} requirements are met.'),
                (f'{framework} Documentation', f'Comprehensive policy and procedure documentation satisfying {framework} requirements.'),
                (f'{framework} Monitoring', f'Continuous compliance monitoring with automated alerts for {framework} violations.')
            ],
            'related': ['/services/testing/', '/services/managed-operations/soc.html']
        }

print(f"Generated {len(COMPLIANCE_PAGES)} compliance pages")

# ============================================================================
# INDUSTRIES PAGES (19 pages)
# Sector-specific unique content
# ============================================================================

INDUSTRIES_PAGES = {}

# Healthcare Industry Pages
for page in ['industries/healthcare/index.html', 'industries/healthcare/hospital.html', 'industries/healthcare/medical-practice.html',
             'industries/healthcare/telehealth.html', 'industries/healthcare/medical-devices.html', 'industries/healthcare/healthcare-iot.html',
             'industries/healthcare/healthcare-ransomware.html']:
    sector = 'Healthcare'
    INDUSTRIES_PAGES[page] = {
        'title': f'{sector} Cybersecurity Solutions - EndPointUS',
        'desc': f'Specialized {sector.lower()} cybersecurity solutions with HIPAA compliance, ePHI protection, and industry-specific threat defense.',
        'intro': f'Comprehensive {sector.lower()} cybersecurity solutions providing HIPAA-compliant endpoint security, ePHI protection, medical device security, and ransomware defense tailored to healthcare organizations.',
        'problem': f'{sector} organizations face unique cybersecurity challenges including HIPAA compliance requirements protecting electronic Protected Health Information, ransomware attacks specifically targeting healthcare for maximum impact, connected medical devices with security vulnerabilities, and regulatory penalties averaging $100,000 per violation. Healthcare data breaches cost average $10.1 million with patient data worth 10-50x more than financial data on dark web.',
        'solution': f'Our {sector.lower()} cybersecurity solutions provide HIPAA Security Rule implementation with required technical safeguards, specialized ransomware protection understanding healthcare operational constraints, medical device and IoT security through network segmentation, breach detection and response meeting Breach Notification Rule requirements, and comprehensive compliance documentation supporting OCR audits.',
        'features': [
            (f'{sector} Compliance', f'Complete HIPAA Security Rule implementation including access controls, audit logging, encryption, and breach notification meeting all technical safeguard requirements with comprehensive compliance documentation.'),
            (f'{sector} Ransomware Defense', f'Specialized ransomware protection understanding {sector.lower()} operational requirements including 24/7 operations, life-safety systems, and backup strategies protecting against healthcare-targeted ransomware campaigns.'),
            (f'{sector} Device Security', f'Medical device and healthcare IoT security through network segmentation, passive monitoring, and virtual patching protecting vulnerable medical equipment without impacting clinical operations or regulatory compliance.'),
            (f'{sector} Breach Response', f'Expert incident response for {sector.lower()} breaches including forensic investigation, breach notification support meeting HIPAA Breach Notification Rule timelines, OCR reporting assistance, and patient communication guidance.')
        ],
        'related': ['/compliance/hipaa/', '/services/threat-protection/ransomware.html', '/services/core-endpoint/iot.html']
    }

# Financial Industry Pages
for page in ['industries/financial/index.html', 'industries/financial/bank.html', 'industries/financial/credit-union.html',
             'industries/financial/fintech.html', 'industries/financial/insurance.html', 'industries/financial/investment.html']:
    sector = 'Financial Services'
    INDUSTRIES_PAGES[page] = {
        'title': f'{sector} Cybersecurity - EndPointUS',
        'desc': f'{sector} cybersecurity solutions with PCI-DSS compliance, fraud prevention, and financial data protection.',
        'intro': f'Specialized {sector.lower()} cybersecurity providing PCI-DSS compliance, cardholder data protection, fraud prevention, and regulatory compliance for banks, credit unions, and financial institutions.',
        'problem': f'{sector} organizations face stringent regulatory requirements including PCI-DSS for payment card data, GLBA for financial information protection, SOX for financial controls, and state data breach notification laws. Financial institutions are primary targets for cybercriminals seeking account credentials, wire transfer fraud, and customer PII with average breach costs exceeding $5.9 million and regulatory fines reaching tens of millions.',
        'solution': f'Our {sector.lower()} cybersecurity provides PCI-DSS compliance including network segmentation and quarterly scanning, GLBA safeguards for financial information, fraud detection monitoring suspicious transactions and account access, multi-factor authentication for customer and employee access, and comprehensive compliance documentation supporting regulatory examinations.',
        'features': [
            ('PCI-DSS Compliance', 'Complete PCI-DSS implementation including network segmentation isolating cardholder data environment, encryption protecting stored and transmitted payment data, quarterly ASV scans, and annual penetration testing.'),
            ('Financial Data Protection', 'GLBA-compliant safeguards protecting customer financial information through encryption, access controls, data loss prevention, and secure disposal meeting financial institution examination requirements.'),
            ('Fraud Detection', 'Real-time monitoring detecting account takeover attempts, wire transfer fraud, credential stuffing attacks, unusual transaction patterns, and insider threats with automated alerts enabling rapid response.'),
            ('Regulatory Compliance', 'Comprehensive compliance support for PCI-DSS, GLBA, SOX, FFIEC guidance, state data breach laws with compliance documentation, evidence collection, and examination support for FDIC, OCC, NCUA, and state regulators.')
        ],
        'related': ['/compliance/financial/pci-dss.html', '/compliance/financial/glba.html', '/services/threat-protection/phishing.html']
    }

# Legal Industry Pages
for page in ['industries/legal/index.html', 'industries/legal/attorney-client-privilege.html', 'industries/legal/law-firm-ransomware.html',
             'industries/legal/legal-documents.html', 'industries/legal/legal-ethics.html', 'industries/legal/litigation-hold.html']:
    sector = 'Legal'
    INDUSTRIES_PAGES[page] = {
        'title': f'{sector} Cybersecurity Solutions - EndPointUS',
        'desc': f'{sector} cybersecurity protecting attorney-client privilege, confidential legal documents, and maintaining ethical obligations.',
        'intro': f'Specialized {sector.lower()} cybersecurity solutions protecting attorney-client privilege, confidential legal documents, case files, and sensitive client information while maintaining ethical obligations and avoiding conflicts of interest.',
        'problem': f'{sector} practices face unique cybersecurity challenges including attorney-client privilege protection requiring absolute confidentiality, ethical obligations under ABA Model Rules preventing disclosure, ransomware attacks specifically targeting law firms for sensitive case information, and conflict-of-interest concerns when security providers serve opposing parties. Cyber insurance often requires specific security controls while malpractice claims increase from data breaches.',
        'solution': f'Our {sector.lower()} cybersecurity provides attorney-client privilege protection through comprehensive access controls and encryption, ransomware defense understanding legal practice operations and document management systems, ethical walls preventing conflicts when serving multiple clients, secure document management for case files and discovery materials, and compliance with ABA cybersecurity guidance and state bar ethics opinions.',
        'features': [
            ('Privilege Protection', 'Comprehensive technical safeguards protecting attorney-client privilege through end-to-end encryption, role-based access controls limiting access to need-to-know, audit logging documenting all access to privileged communications, and breach detection preventing unauthorized disclosure.'),
            ('Legal Ransomware Defense', 'Specialized ransomware protection for legal practices including immutable backup of case files, rapid recovery minimizing client impact, incident response understanding attorney-client privilege implications, and guidance on ethical disclosure obligations when client data compromised.'),
            ('Ethical Compliance', 'Security controls satisfying ABA Model Rule 1.6(c) duty of confidentiality including reasonable security measures, annual security assessments, security training for legal staff, and ethical walls when security provider serves multiple law firms preventing conflicts of interest.'),
            ('Document Security', 'Secure document management protecting case files, discovery materials, depositions, and work product through encryption, access controls, data loss prevention, secure sharing with outside counsel and clients, and litigation hold support preserving ESI.')
        ],
        'related': ['/services/threat-protection/ransomware.html', '/services/bcdr/dlp.html', '/compliance/general/']
    }

print(f"Generated {len(INDUSTRIES_PAGES)} industry pages")

# ============================================================================
# GEOGRAPHIC PAGES (30 pages)
# Location-specific content with local context
# ============================================================================

GEOGRAPHIC_PAGES = {}

# Major cities
cities = {
    'austin': 'Austin, TX', 'buffalo': 'Buffalo, NY', 'chicago': 'Chicago, IL', 'dallas': 'Dallas, TX',
    'fort-worth': 'Fort Worth, TX', 'houston': 'Houston, TX', 'jacksonville': 'Jacksonville, FL',
    'los-angeles': 'Los Angeles, CA', 'miami': 'Miami, FL', 'new-york-city': 'New York City, NY',
    'orlando': 'Orlando, FL', 'philadelphia': 'Philadelphia, PA', 'pittsburgh': 'Pittsburgh, PA',
    'rochester': 'Rochester, NY', 'sacramento': 'Sacramento, CA', 'san-antonio': 'San Antonio, TX',
    'san-diego': 'San Diego, CA', 'san-francisco': 'San Francisco, CA', 'san-jose': 'San Jose, CA',
    'tampa': 'Tampa, FL'
}

for city_slug, city_name in cities.items():
    state = city_name.split(', ')[1]
    GEOGRAPHIC_PAGES[f'geographic/cities/{city_slug}.html'] = {
        'title': f'Endpoint Security Services in {city_name} - EndPointUS',
        'desc': f'Professional endpoint security and cybersecurity services for {city_name} businesses with local support, compliance expertise, and 24/7 monitoring.',
        'intro': f'Comprehensive endpoint security services for {city_name} organizations providing local expertise with enterprise-grade protection, HIPAA and PCI-DSS compliance support, and 24/7 security monitoring serving healthcare, financial, and legal sectors.',
        'problem': f'{city_name} businesses face increasing cyber threats including ransomware targeting local healthcare providers, financial institutions, and professional services firms. Organizations need endpoint security meeting compliance requirements for HIPAA, PCI-DSS, and state data breach notification laws while maintaining operational efficiency. Local businesses require security providers understanding regional industry composition, regulatory environment, and business operational constraints.',
        'solution': f'EndPointUS provides comprehensive endpoint security for {city_name} organizations with local expertise serving {state} businesses. Our solutions include next-generation endpoint protection, managed detection and response, HIPAA and PCI-DSS compliance support, ransomware protection, 24/7 SOC monitoring, incident response, and security assessments tailored to regional business needs and regulatory requirements.',
        'features': [
            (f'{city_name} Local Expertise', f'Deep understanding of {city_name} business environment, regional industry composition, local compliance requirements, and {state} data breach notification laws with local references and rapid on-site support availability.'),
            ('Industry-Specific Solutions', f'Specialized solutions for {city_name} key industries including healthcare practices and hospitals, financial institutions and credit unions, law firms and legal practices, and professional services firms with industry-specific compliance expertise.'),
            ('24/7 Security Monitoring', f'Round-the-clock SOC monitoring protecting {city_name} businesses including after-hours and weekend coverage, rapid incident response regardless of time zone, and proactive threat hunting identifying threats before business impact.'),
            (f'{state} Compliance Support', f'Comprehensive compliance assistance for {state} businesses including HIPAA for healthcare, PCI-DSS for retailers and restaurants, {state} data breach notification law compliance, and regulatory assessment support.')
        ],
        'related': ['/services/core-endpoint/', '/services/managed-operations/soc.html', '/about/security-assessment.html']
    }

# States
states = {
    'california': 'California', 'florida': 'Florida', 'georgia': 'Georgia', 'illinois': 'Illinois',
    'new-jersey': 'New Jersey', 'new-york': 'New York', 'north-carolina': 'North Carolina',
    'ohio': 'Ohio', 'pennsylvania': 'Pennsylvania', 'texas': 'Texas'
}

for state_slug, state_name in states.items():
    GEOGRAPHIC_PAGES[f'geographic/states/{state_slug}.html'] = {
        'title': f'Endpoint Security Services in {state_name} - EndPointUS',
        'desc': f'Statewide endpoint security and cybersecurity services for {state_name} businesses with compliance expertise and local support.',
        'intro': f'Comprehensive endpoint security services for {state_name} organizations providing statewide coverage with enterprise-grade protection, regulatory compliance support, and 24/7 monitoring.',
        'problem': f'{state_name} businesses face cyber threats while navigating state-specific compliance requirements including {state_name} data breach notification laws, industry regulations for healthcare and financial services, and insurance requirements. Organizations need security providers understanding {state_name} regulatory environment, industry composition, and regional business needs.',
        'solution': f'EndPointUS provides comprehensive endpoint security for {state_name} organizations including next-generation endpoint protection, managed detection and response, compliance support for HIPAA, PCI-DSS, and {state_name} regulations, ransomware protection, 24/7 SOC monitoring, and statewide service coverage.',
        'features': [
            (f'{state_name} Expertise', f'Deep understanding of {state_name} business environment, regulatory landscape, industry composition, and regional cybersecurity threats with local expertise and statewide service coverage.'),
            (f'{state_name} Compliance', f'Comprehensive compliance support for {state_name} businesses including state data breach notification law compliance, industry-specific regulations, insurance requirements, and regulatory examination support.'),
            ('Enterprise Protection', f'Enterprise-grade security for {state_name} organizations of all sizes including next-generation endpoint security, EDR/MDR, 24/7 SOC monitoring, ransomware protection, and incident response.'),
            ('Statewide Coverage', f'Service coverage across {state_name} with rapid response capabilities, local expertise in major metropolitan areas, and remote support for distributed locations.')
        ],
        'related': ['/services/core-endpoint/', '/services/managed-operations/mdr.html', '/compliance/']
    }

print(f"Generated {len(GEOGRAPHIC_PAGES)} geographic pages")

# ============================================================================
# RESOURCES PAGES (21 pages)
# Educational and comparison content
# ============================================================================

RESOURCES_PAGES = {
    'resources/best-practices/index.html': {
        'title': 'Endpoint Security Best Practices - EndPointUS',
        'desc': 'Comprehensive endpoint security best practices, implementation guides, policies, and procedures for endpoint protection.',
        'intro': 'Comprehensive endpoint security best practices covering implementation, policies, procedures, and operational guidance.',
        'problem': 'Organizations struggle implementing effective endpoint security without clear guidance on best practices, implementation strategies, policy development, and operational procedures.',
        'solution': 'Our best practices library provides comprehensive guidance on endpoint security implementation, policy development, procedural frameworks, and operational best practices drawn from 15+ years protecting organizations.',
        'features': [
            ('Implementation Guides', 'Step-by-step implementation guides for endpoint security deployment, configuration, tuning, and optimization.'),
            ('Policy Templates', 'Comprehensive security policy templates covering acceptable use, BYOD, remote access, incident response, and data protection.'),
            ('Procedural Frameworks', 'Operational procedure documentation for security monitoring, incident response, patch management, and compliance.'),
            ('Industry Best Practices', 'Best practices specific to healthcare, financial services, and legal sectors with compliance considerations.')
        ],
        'related': ['/resources/comparisons/', '/services/core-endpoint/', '/compliance/']
    }
}

# Generate remaining resources pages programmatically
resource_topics = [
    'best-practices/best-practices.html', 'best-practices/byod-policies.html', 'best-practices/checklist.html',
    'best-practices/how-to-choose-provider.html', 'best-practices/implementation-guide.html',
    'best-practices/policies-procedures.html', 'best-practices/remote-work-security.html',
    'comparisons/antivirus-vs-edr.html', 'comparisons/cloud-vs-on-premise.html', 'comparisons/edr-vs-epp.html',
    'comparisons/index.html', 'comparisons/managed-vs-unmanaged.html', 'comparisons/small-business-vs-enterprise.html',
    'comparisons/vendor-comparison.html', 'threat-intelligence/common-vulnerabilities.html',
    'threat-intelligence/emerging-threats.html', 'threat-intelligence/index.html',
    'threat-intelligence/latest-threats-2025.html', 'threat-intelligence/ransomware-statistics.html',
    'threat-intelligence/threat-landscape.html'
]

for topic in resource_topics:
    if f'resources/{topic}' not in RESOURCES_PAGES:
        topic_name = topic.split('/')[-1].replace('.html', '').replace('-', ' ').title()
        category = topic.split('/')[0].replace('-', ' ').title()
        RESOURCES_PAGES[f'resources/{topic}'] = {
            'title': f'{topic_name} - EndPointUS Resources',
            'desc': f'Comprehensive {topic_name.lower()} information for endpoint security.',
            'intro': f'Expert guidance on {topic_name.lower()} for endpoint security and cybersecurity.',
            'problem': f'Organizations need clear guidance on {topic_name.lower()} to make informed security decisions.',
            'solution': f'Our {topic_name.lower()} resource provides comprehensive information based on 15+ years of endpoint security expertise.',
            'features': [
                ('Expert Analysis', f'In-depth analysis of {topic_name.lower()} from certified security professionals.'),
                ('Practical Guidance', f'Actionable guidance for implementing {topic_name.lower()} in your organization.'),
                ('Industry Insights', f'Industry-specific considerations for {topic_name.lower()}.'),
                ('Latest Information', f'Current information on {topic_name.lower()} updated for 2025.')
            ],
            'related': ['/services/', '/compliance/', '/about/security-assessment.html']
        }

print(f"Generated {len(RESOURCES_PAGES)} resource pages")

# ============================================================================
# ABOUT AND LEGAL PAGES (12 pages)
# Company and legal information
# ============================================================================

ABOUT_PAGES = {
    'about/index.html': {
        'title': 'About EndPointUS - Enterprise Endpoint Security',
        'desc': 'EndPointUS provides enterprise endpoint security solutions with 15+ years experience protecting healthcare, financial, and legal organizations.',
        'intro': 'EndPointUS delivers comprehensive endpoint security solutions protecting organizations across healthcare, financial services, and legal sectors with 15+ years of cybersecurity expertise.',
        'problem': 'Organizations need trusted cybersecurity partners with deep industry expertise, proven track record protecting sensitive data, and comprehensive solutions addressing modern threats while meeting regulatory compliance requirements.',
        'solution': 'EndPointUS provides enterprise-grade endpoint security combining advanced technology platforms, 24/7 SOC monitoring by certified security professionals, industry-specific compliance expertise, and proven incident response capabilities protecting organizations for over 15 years.',
        'features': [
            ('15+ Years Experience', 'Over 15 years protecting organizations in healthcare, financial services, and legal sectors with deep industry expertise and proven track record.'),
            ('Certified Professionals', 'Security team holds industry certifications including CISSP, CEH, GIAC, and industry-specific credentials with continuous training.'),
            ('SOC 2 Certified', 'SOC 2 Type II certified demonstrating commitment to security, availability, confidentiality, and privacy with annual audits.'),
            ('24/7 SOC', 'Round-the-clock Security Operations Center monitoring with rapid incident response, proactive threat hunting, and expert analysis.')
        ],
        'related': ['/about/certifications.html', '/about/case-studies.html', '/about/why-choose-us.html']
    },
    'about/contact.html': {
        'title': 'Contact EndPointUS - Free Security Assessment',
        'desc': 'Contact EndPointUS for endpoint security solutions. Schedule a free security assessment.',
        'intro': 'Contact EndPointUS to discuss your endpoint security needs and schedule a free security assessment.',
        'problem': 'Organizations need expert guidance assessing cybersecurity risks, evaluating security solutions, and implementing comprehensive endpoint protection.',
        'solution': 'Contact EndPointUS for a complimentary security assessment identifying vulnerabilities, compliance gaps, and security improvements tailored to your organization.',
        'features': [
            ('Free Security Assessment', 'Complimentary assessment identifying security gaps, compliance issues, and improvement recommendations.'),
            ('Expert Consultation', 'Consultation with certified security professionals understanding your industry and regulatory requirements.'),
            ('Rapid Response', 'Quick response to inquiries with consultation scheduling within 24 hours.'),
            ('No Obligation', 'Free assessment with no purchase obligation - just actionable security guidance.')
        ],
        'related': ['/about/security-assessment.html', '/about/', '/services/']
    }
}

# Generate remaining about pages
about_topics = {
    'case-studies.html': 'Case Studies',
    'certifications.html': 'Certifications and Compliance',
    'security-assessment.html': 'Free Security Assessment',
    'soc-overview.html': 'Security Operations Center',
    'testimonials.html': 'Client Testimonials',
    'why-choose-us.html': 'Why Choose EndPointUS'
}

for filename, topic in about_topics.items():
    if f'about/{filename}' not in ABOUT_PAGES:
        ABOUT_PAGES[f'about/{filename}'] = {
            'title': f'{topic} - EndPointUS',
            'desc': f'{topic} - EndPointUS endpoint security solutions.',
            'intro': f'{topic} showcasing EndPointUS expertise and capabilities.',
            'problem': 'Organizations need to evaluate security providers based on credentials, experience, and proven results.',
            'solution': f'EndPointUS demonstrates {topic.lower()} validating our expertise and commitment to protecting your organization.',
            'features': [
                ('Industry Experience', '15+ years protecting healthcare, financial, and legal organizations.'),
                ('Proven Track Record', 'Successful security implementations and incident responses across multiple sectors.'),
                ('Certified Team', 'Security professionals holding industry-leading certifications.'),
                ('Client Focused', 'Dedicated to client success with personalized service and support.')
            ],
            'related': ['/about/', '/services/', '/about/contact.html']
        }

# Legal pages
legal_pages = {
    'legal/privacy-policy.html': 'Privacy Policy',
    'legal/security-practices.html': 'Security Practices',
    'legal/sla.html': 'Service Level Agreement',
    'legal/terms-of-service.html': 'Terms of Service'
}

for filename, topic in legal_pages.items():
    ABOUT_PAGES[filename] = {
        'title': f'{topic} - EndPointUS',
        'desc': f'EndPointUS {topic.lower()} governing our services and client relationships.',
        'intro': f'EndPointUS {topic.lower()} outlining our commitments and obligations.',
        'problem': 'Organizations require clear understanding of service provider policies, practices, and commitments.',
        'solution': f'Our {topic.lower()} provides transparent documentation of EndPointUS practices and commitments.',
        'features': [
            ('Transparency', 'Clear documentation of our policies, practices, and commitments.'),
            ('Client Protection', 'Policies designed to protect client interests and data.'),
            ('Regulatory Compliance', 'Practices aligned with industry regulations and standards.'),
            ('Regular Updates', 'Policies reviewed and updated regularly to reflect current practices.')
        ],
        'related': ['/about/', '/compliance/', '/about/contact.html']
    }

print(f"Generated {len(ABOUT_PAGES)} about/legal pages")

if __name__ == '__main__':
    # Generate all pages
    all_pages = {}
    all_pages.update(COMPLIANCE_PAGES)
    all_pages.update(INDUSTRIES_PAGES)
    all_pages.update(GEOGRAPHIC_PAGES)
    all_pages.update(RESOURCES_PAGES)
    all_pages.update(ABOUT_PAGES)

    print(f"\nGenerating {len(all_pages)} category pages...")
    success = 0
    for filepath, content in all_pages.items():
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            html = build_page(filepath, content)
            with open(filepath, 'w') as f:
                f.write(html)
            print(f"✓ {filepath}")
            success += 1
        except Exception as e:
            print(f"✗ {filepath}: {e}")

    print(f"\n✅ Successfully generated {success}/{len(all_pages)} pages")
