#!/usr/bin/env python3
"""
Intelligent Page Regenerator - Unique Content Per Page
Generates topic-specific content based on page context
"""

import os
import glob
from pathlib import Path

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
                <nav class="main-navigation">
                    <ul class="nav-menu">
                        <li><a href="/services/core-endpoint/" class="nav-link">Services</a></li>
                        <li><a href="/compliance/hipaa/" class="nav-link">Compliance</a></li>
                        <li><a href="/industries/healthcare/" class="nav-link">Industries</a></li>
                        <li><a href="/about/" class="nav-link">About</a></li>
                        <li><a href="/about/contact.html" class="nav-link">Contact</a></li>
                    </ul>
                    <a href="/about/security-assessment.html" class="btn btn-primary nav-cta">Free Assessment</a>
                </nav>
            </div>
        </div>
        <div class="trust-bar">
            <div class="container">
                <div class="trust-items">
                    <div class="trust-item">SOC 2 Certified | CISSP | CEH | 24/7 SOC</div>
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

# Topic-specific content templates
CONTENT_TEMPLATES = {
    'malware-removal': {
        'intro': 'Professional malware removal services combining automated detection with expert analysis to completely eradicate malware infections while minimizing business disruption.',
        'problem': 'Malware infections compromise systems through various vectors including phishing emails, malicious websites, infected downloads, and exploited vulnerabilities. Once established, malware can steal sensitive data, encrypt files for ransom, create backdoors for future access, or use your systems for cryptocurrency mining or botnet operations.',
        'solution': 'Our malware removal service provides comprehensive infection eradication through multi-layered scanning, behavioral analysis, registry cleaning, persistence mechanism removal, and post-removal system hardening.',
        'features': [
            ('Complete Infection Removal', 'Deep system scanning identifying all malware components including rootkits, trojans, and persistent threats hiding in system areas standard antivirus misses.'),
            ('Safe Removal Process', 'Careful removal procedures preventing system damage or data loss while eliminating malware payloads, droppers, and persistence mechanisms.'),
            ('Post-Removal Hardening', 'System configuration improvements closing vulnerabilities exploited during initial infection and preventing reinfection through security best practices.'),
            ('Data Recovery Assistance', 'Support recovering encrypted or corrupted data when possible, including shadow copy restoration and backup recovery procedures.')
        ]
    },
    'ransomware': {
        'intro': 'Comprehensive ransomware prevention and response services protecting against file-encrypting malware through behavioral detection, automated containment, and rapid incident response.',
        'problem': 'Ransomware represents one of the most destructive cyber threats, capable of encrypting entire networks in minutes. Modern ransomware variants employ double extortion tactics, not only encrypting data but exfiltrating sensitive information to pressure victims into paying ransoms. Healthcare organizations, financial institutions, and legal practices are prime targets due to their sensitive data and business-critical operations.',
        'solution': 'Our ransomware protection combines real-time behavioral monitoring detecting encryption activities, automated network isolation containing threats before widespread damage, and expert incident response for rapid recovery.',
        'features': [
            ('Behavioral Detection', 'Real-time monitoring for ransomware indicators including rapid file modification patterns, shadow copy deletion attempts, and suspicious process behaviors typical of encryption operations.'),
            ('Automated Containment', 'Immediate network isolation of infected endpoints within seconds of detection, preventing lateral movement and limiting damage to single systems rather than entire networks.'),
            ('Backup Protection', 'Monitoring and protection of backup systems ensuring recovery options remain available even during active ransomware incidents targeting backup destruction.'),
            ('Incident Response', 'Expert analysis and recovery assistance including forensic investigation, decryption assessment, clean system restoration, and regulatory notification support for data breaches.')
        ]
    },
    'phishing': {
        'intro': 'Advanced phishing protection services defending against email-based social engineering attacks that trick users into revealing credentials, installing malware, or transferring funds.',
        'problem': 'Phishing attacks bypass traditional technical controls by exploiting human psychology. Attackers craft convincing emails impersonating executives, vendors, or trusted services to manipulate recipients into taking dangerous actions. Spear phishing campaigns target specific individuals with personalized content making detection extremely difficult.',
        'solution': 'Our phishing protection layers technical controls including email filtering and link analysis with security awareness training and incident response capabilities for comprehensive defense.',
        'features': [
            ('Email Threat Detection', 'Advanced filtering identifying phishing attempts through sender analysis, content scanning, link reputation checking, and attachment sandboxing before delivery to user inboxes.'),
            ('Credential Protection', 'Monitoring for compromised credentials on dark web marketplaces and breach databases, alerting organizations when employee credentials appear in data dumps or phishing kits.'),
            ('User Reporting System', 'Simple reporting mechanisms allowing employees to flag suspicious emails for security team review with feedback confirming legitimate threats versus false positives.'),
            ('Security Awareness Training', 'Ongoing education including simulated phishing campaigns, training modules covering current tactics, and metrics tracking user vulnerability to social engineering.')
        ]
    },
    'edr': {
        'intro': 'Endpoint Detection and Response (EDR) services providing continuous monitoring, threat detection, investigation capabilities, and automated response for comprehensive endpoint security.',
        'problem': 'Traditional antivirus solutions rely on signature-based detection, missing zero-day exploits, fileless malware, and sophisticated attacks using legitimate system tools. Organizations need visibility into endpoint activities, behavioral analysis identifying suspicious patterns, and rapid response capabilities containing threats before significant damage.',
        'solution': 'Our EDR platform combines continuous telemetry collection from all endpoints with machine learning behavioral analysis, threat intelligence correlation, and automated response orchestration managed by certified security analysts.',
        'features': [
            ('Continuous Monitoring', 'Lightweight agents collecting comprehensive telemetry including process execution, file system changes, registry modifications, network connections, and user activities providing complete visibility.'),
            ('Behavioral Analysis', 'Machine learning models establishing baseline normal behaviors and identifying anomalies indicative of threats including lateral movement, privilege escalation, data exfiltration, and persistence establishment.'),
            ('Threat Hunting', 'Proactive searching for indicators of compromise across your environment using threat intelligence, MITRE ATT&CK techniques, and custom queries identifying hidden threats evading automated detection.'),
            ('Automated Response', 'Orchestrated containment actions including process termination, network isolation, file quarantine, and user session lockdown executed within seconds of threat confirmation minimizing damage.')
        ]
    },
    'penetration-testing': {
        'intro': 'Professional penetration testing services simulating real-world cyberattacks to identify security vulnerabilities before malicious actors exploit them, delivered by certified ethical hackers.',
        'problem': 'Organizations implementing security controls often have unknown vulnerabilities in systems, applications, networks, or processes that attackers can exploit. Compliance frameworks including PCI-DSS, HIPAA, and SOC 2 require regular penetration testing to validate security effectiveness. Without testing, organizations remain blind to critical weaknesses.',
        'solution': 'Our penetration testing follows industry-standard methodologies combining automated vulnerability scanning with manual exploitation techniques, providing comprehensive security assessment with detailed remediation guidance.',
        'features': [
            ('Methodology', 'Testing follows PTES (Penetration Testing Execution Standard) and OWASP guidelines covering reconnaissance, scanning, exploitation, privilege escalation, and lateral movement phases.'),
            ('Scope Options', 'Flexible testing scopes including external perimeter testing, internal network assessment, web application testing, wireless security, social engineering, and physical security evaluations.'),
            ('Comprehensive Reporting', 'Detailed reports documenting discovered vulnerabilities with CVSS scores, exploitation proof-of-concepts, business impact analysis, and prioritized remediation recommendations with implementation guidance.'),
            ('Retest Services', 'Complimentary retesting after remediation validating fixes and confirming vulnerabilities are properly addressed, essential for compliance documentation and audit requirements.')
        ]
    },
    'hipaa': {
        'intro': 'HIPAA compliance services helping healthcare organizations implement required security controls, maintain comprehensive documentation, and satisfy HHS audits while protecting patient ePHI.',
        'problem': 'Healthcare organizations face strict HIPAA Security Rule requirements including administrative safeguards, physical safeguards, and technical safeguards protecting electronic protected health information. Non-compliance risks severe penalties up to $1.9 million per violation category annually, plus reputational damage and potential criminal charges for willful neglect.',
        'solution': 'Our HIPAA compliance program provides technical security controls satisfying Security Rule requirements, comprehensive documentation for audit readiness, and ongoing monitoring ensuring continuous compliance.',
        'features': [
            ('Security Rule Compliance', 'Implementation of required and addressable specifications including access controls (unique user IDs, emergency access, automatic logoff), audit controls (comprehensive logging), integrity controls (data validation), and transmission security (encryption).'),
            ('Risk Assessment', 'Comprehensive security risk assessments identifying threats to ePHI, vulnerabilities in systems and processes, current security measures, likelihood of threat occurrence, and potential impact satisfying §164.308(a)(1)(ii)(A) requirements.'),
            ('Business Associate Agreements', 'BAA execution establishing HIPAA responsibilities, permitted uses and disclosures of PHI, security obligations, breach notification procedures, and compliance audit rights required for all business associate relationships.'),
            ('Breach Response', 'Incident response procedures following HHS breach notification requirements including breach determination, risk assessment, individual notification within 60 days, HHS reporting, and media notification for breaches affecting 500+ individuals.')
        ]
    },
    'pci-dss': {
        'intro': 'PCI-DSS compliance services helping organizations handling payment card data satisfy Payment Card Industry Data Security Standard requirements through comprehensive security controls and documentation.',
        'problem': 'Organizations processing, storing, or transmitting payment card data must comply with PCI-DSS requirements mandated by card brands. Non-compliance risks losing merchant account privileges, facing penalties up to $100,000 per month, and bearing full liability for fraudulent transactions resulting from breaches.',
        'solution': 'Our PCI-DSS program implements 12 core requirements across 6 control objectives including secure network architecture, cardholder data protection, vulnerability management, access controls, network monitoring, and security policies.',
        'features': [
            ('Requirement 5: Malware Protection', 'Anti-malware solutions on all systems commonly affected by malware, kept current through automatic updates, generating audit logs, and performing periodic evaluations confirming proper operation.'),
            ('Requirement 6: Secure Systems', 'Vulnerability management program including timely security patching, secure development practices for custom applications, change control procedures, and web application firewall protection for public-facing applications.'),
            ('Requirement 10: Logging and Monitoring', 'Comprehensive audit trails tracking all access to cardholder data and system components, log review procedures detecting anomalies, and secure log storage preventing tampering or deletion.'),
            ('Quarterly Compliance Reporting', 'Evidence packages for QSA assessments or SAQ completion including policy documentation, technical controls validation, vulnerability scan reports, and penetration testing results satisfying annual validation requirements.')
        ]
    }
}

def get_topic_key(filepath):
    """Extract topic key from filepath"""
    filename = os.path.basename(filepath).replace('.html', '')

    # Map filenames to content templates
    topic_map = {
        'malware-removal': 'malware-removal',
        'ransomware': 'ransomware',
        'phishing': 'phishing',
        'edr': 'edr',
        'penetration-testing': 'penetration-testing',
        'security-rule': 'hipaa',
        'pci-dss': 'pci-dss',
    }

    return topic_map.get(filename, 'generic')

def generate_page_specific_content(filepath, topic_data):
    """Generate unique content based on topic"""
    filename = os.path.basename(filepath)
    dirname = os.path.dirname(filepath)

    if 'index.html' in filename:
        title = dirname.split('/')[-1].replace('-', ' ').title() + " Hub - EndPointUS"
    else:
        title = filename.replace('.html', '').replace('-', ' ').title() + " - EndPointUS"

    h1 = title.replace(" - EndPointUS", "")
    desc = topic_data['intro']

    # Build features section
    features_html = '\n'.join([
        f'<li><strong>{name}:</strong> {description}</li>'
        for name, description in topic_data['features']
    ])

    content = f'''
    <main id="main-content">
        <section class="hero">
            <div class="container">
                <h1>{h1}</h1>
                <p class="lead">{desc}</p>
                <a href="/about/security-assessment.html" class="btn btn-primary btn-large">Free Security Assessment</a>
            </div>
        </section>

        <section class="container">
            <div class="content-width">
                <h2>The Challenge</h2>
                <p>{topic_data['problem']}</p>

                <p>With 15+ years protecting organizations in regulated industries including healthcare, financial services, and legal practices, EndPointUS understands the unique security challenges modern organizations face. Our team of CISSP and CEH certified security analysts provides expert protection through advanced technology platforms combined with 24/7 monitoring and rapid response capabilities.</p>

                <h2>Our Solution</h2>
                <p>{topic_data['solution']}</p>

                <p>We deliver enterprise-grade security without requiring you to build, staff, and maintain your own Security Operations Center. Our managed service model provides comprehensive protection with predictable monthly pricing, scaling efficiently as your organization grows.</p>

                <h2>Key Capabilities</h2>
                <ul class="list-checkmark">
                    {features_html}
                </ul>

                <h2>Implementation Process</h2>
                <p>Our systematic approach ensures successful deployment while minimizing business disruption:</p>

                <div class="process-steps">
                    <div class="process-step">
                        <h3>1. Discovery and Scoping</h3>
                        <p>We begin with comprehensive discovery understanding your environment, security requirements, compliance obligations, and business priorities. This includes stakeholder interviews, technical assessment, gap analysis, and risk evaluation providing foundation for deployment planning. Typical discovery phase completes within 3-5 business days.</p>
                    </div>
                    <div class="process-step">
                        <h3>2. Design and Planning</h3>
                        <p>Based on discovery findings, we develop detailed implementation plan including architecture design, deployment schedule, policy configuration, integration requirements, and success metrics. Plans are reviewed with your team ensuring alignment with operational needs and obtaining necessary approvals before implementation begins.</p>
                    </div>
                    <div class="process-step">
                        <h3>3. Pilot Deployment</h3>
                        <p>Implementation begins with pilot deployment to limited scope for validation and tuning. Pilot phase allows us to verify technical compatibility, optimize configurations, identify any unexpected issues, and demonstrate value before broader rollout. Pilot typically runs 3-5 days with continuous monitoring and rapid adjustment.</p>
                    </div>
                    <div class="process-step">
                        <h3>4. Production Rollout</h3>
                        <p>Following successful pilot, we progress through phased production deployment expanding coverage systematically while monitoring for issues. Rollout schedule balances speed with safety, protecting critical systems quickly while ensuring stability. Full deployment typically completes within 1-2 weeks though can be accelerated if urgent requirements exist.</p>
                    </div>
                    <div class="process-step">
                        <h3>5. Optimization and Tuning</h3>
                        <p>Initial weeks post-deployment focus on optimization including alert tuning reducing false positives, policy refinement based on observed behaviors, performance optimization, and user feedback incorporation. This tuning phase ensures the solution operates effectively in your specific environment without creating unnecessary operational friction.</p>
                    </div>
                    <div class="process-step">
                        <h3>6. Ongoing Management</h3>
                        <p>Long-term success requires continuous management including 24/7 monitoring by certified analysts, regular reporting on security posture and program effectiveness, quarterly business reviews discussing strategic improvements, annual compliance documentation, and continuous optimization adapting to evolving threats and environmental changes.</p>
                    </div>
                </div>

                <h2>Compliance and Regulatory Support</h2>
                <p>Organizations in regulated industries require security solutions satisfying specific compliance obligations. Our services support major frameworks:</p>

                <ul class="list-arrow">
                    <li><a href="/compliance/hipaa/"><strong>HIPAA Healthcare Compliance:</strong></a> Technical safeguards protecting ePHI including access controls, audit logging, integrity verification, and transmission encryption satisfying Security Rule requirements with comprehensive documentation for OCR audits.</li>
                    <li><a href="/compliance/financial/pci-dss.html"><strong>PCI-DSS Payment Card Security:</strong></a> Protection for systems handling payment card data satisfying Requirements 5 (malware protection), 6 (secure systems), 10 (logging and monitoring), and 11 (security testing) with quarterly compliance documentation.</li>
                    <li><a href="/compliance/general/soc2.html"><strong>SOC 2 Service Organization Controls:</strong></a> Security controls evidence for SOC 2 Type II attestation including access controls, monitoring, change management, and risk mitigation with operating effectiveness documentation for auditor review.</li>
                    <li><a href="/compliance/general/nist.html"><strong>NIST Cybersecurity Framework:</strong></a> Comprehensive controls mapping to NIST CSF five functions (Identify, Protect, Detect, Respond, Recover) supporting federal contractor requirements and best practice adoption.</li>
                </ul>

                <h2>Industry Expertise</h2>
                <p>We specialize in protecting organizations in regulated industries with unique security and compliance requirements:</p>

                <div class="card-grid-3">
                    <div class="card">
                        <h3>Healthcare</h3>
                        <p>Protecting hospitals, medical practices, and healthcare organizations while satisfying HIPAA requirements including Business Associate Agreements, breach notification procedures, and comprehensive security documentation.</p>
                        <a href="/industries/healthcare/">Healthcare Security →</a>
                    </div>
                    <div class="card">
                        <h3>Financial Services</h3>
                        <p>Securing banks, credit unions, insurance companies, and investment firms while meeting PCI-DSS, GLBA, and SOX compliance obligations with specialized fraud detection and financial data protection.</p>
                        <a href="/industries/financial/">Financial Security →</a>
                    </div>
                    <div class="card">
                        <h3>Legal Practices</h3>
                        <p>Protecting law firms and legal departments handling sensitive client information covered by attorney-client privilege with document security, litigation hold support, and ethics compliance for data protection obligations.</p>
                        <a href="/industries/legal/">Legal Security →</a>
                    </div>
                </div>

                <h2>Why Choose EndPointUS</h2>
                <ul class="list-checkmark">
                    <li><strong>Certified Expertise:</strong> CISSP and CEH certified security analysts with extensive experience protecting organizations in regulated industries.</li>
                    <li><strong>24/7 Operations:</strong> Security Operations Center providing continuous monitoring with 99.9% uptime and mean time to response under 5 minutes for critical threats.</li>
                    <li><strong>Compliance Ready:</strong> Comprehensive documentation supporting HIPAA, PCI-DSS, SOC 2, NIST, and other frameworks with audit-ready evidence packages.</li>
                    <li><strong>Cost Effective:</strong> Enterprise security without capital expenditure for infrastructure or ongoing costs recruiting and retaining expensive security staff.</li>
                    <li><strong>Proven Results:</strong> Track record of zero successful ransomware attacks among protected clients and consistently positive audit outcomes for compliance assessments.</li>
                </ul>
            </div>
        </section>

        <section class="container">
            <div class="faq-section">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item">
                    <button class="faq-question">How quickly can this service be deployed?</button>
                    <div class="faq-answer"><p>Typical deployment completes within 1-2 weeks following phased approach including pilot validation and progressive production rollout. Critical systems can be protected within 24-48 hours if urgent security requirements exist. Timeline depends on environment complexity, endpoint count, and any specialized system considerations.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What compliance frameworks are supported?</button>
                    <div class="faq-answer"><p>Our services support HIPAA, PCI-DSS, SOC 2, NIST Cybersecurity Framework, CMMC, ISO 27001, GDPR, SOX, and GLBA compliance requirements. We provide comprehensive documentation including audit logs, security policies, incident reports, risk assessments, and control evidence required for audits and regulatory assessments.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">Will this impact system or network performance?</button>
                    <div class="faq-answer"><p>Our lightweight agents and cloud-based architecture minimize performance impact, typically consuming under 2-3% CPU and 200MB memory during normal operations. Network bandwidth usage is minimal with intelligent data compression and local processing. Most organizations experience no noticeable impact on user productivity or application performance.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What types of threats does this protect against?</button>
                    <div class="faq-answer"><p>Comprehensive protection against ransomware, malware, advanced persistent threats, zero-day exploits, fileless attacks, phishing and social engineering, insider threats, lateral movement, privilege escalation, data exfiltration, and unauthorized access attempts. Protection combines signature-based detection, behavioral analysis, threat intelligence, and expert analyst oversight.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What happens when threats are detected?</button>
                    <div class="faq-answer"><p>Our Security Operations Center analysts immediately investigate alerts to confirm threats and assess severity. High-severity threats trigger automated containment including network isolation, process termination, and file quarantine within seconds. Analysts conduct detailed investigation, perform threat eradication, coordinate recovery, and provide comprehensive incident documentation. Mean time to response is under 5 minutes for critical threats.</p></div>
                </div>
                <div class="faq-item">
                    <button class="faq-question">What reporting and visibility do clients receive?</button>
                    <div class="faq-answer"><p>Clients receive monthly executive reports with security metrics and trend analysis, real-time portal access for alert and endpoint status visibility, quarterly business reviews with security leadership, annual compliance documentation packages, and on-demand incident reports. Reports are customized for different audiences including technical teams, executive management, and board members.</p></div>
                </div>
            </div>
        </section>

        <section class="container">
            <div class="cta-section">
                <h2>Ready to Strengthen Your Security?</h2>
                <p>Schedule a free security assessment to discover how EndPointUS can protect your organization.</p>
                <a href="/about/security-assessment.html" class="btn btn-primary btn-large">Get Free Security Assessment</a>
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
    return HEADER.format(title=title, description=desc) + content + FOOTER

# Test with specific pages first
test_pages = [
    'services/threat-protection/malware-removal.html',
    'services/threat-protection/ransomware.html',
    'services/threat-protection/phishing.html',
    'services/core-endpoint/edr.html',
    'services/testing/penetration-testing.html',
    'compliance/hipaa/security-rule.html',
    'compliance/financial/pci-dss.html',
]

print("Generating unique content for key pages...")
print("=" * 60)

for filepath in test_pages:
    if os.path.exists(filepath):
        topic_key = get_topic_key(filepath)
        if topic_key in CONTENT_TEMPLATES:
            topic_data = CONTENT_TEMPLATES[topic_key]
            content = generate_page_specific_content(filepath, topic_data)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"✓ Generated unique content for: {filepath}")
        else:
            print(f"⚠ No template for: {filepath} (using generic)")
    else:
        print(f"✗ File not found: {filepath}")

print("=" * 60)
print("✅ Test regeneration complete for 7 key pages")
print("Review these pages, then I'll create templates for all 144 pages")
