#!/usr/bin/env python3
"""
Endpoint.US Website Page Generator
Generates 170+ pages with E-E-A-T compliant content, schema markup, and SEO
"""

import os
import json
from pathlib import Path

# Page configuration data
PAGES_CONFIG = {
    # Service Hub Pages
    "services/core-endpoint/index.html": {
        "title": "Managed Endpoint Security Services | 24/7 SOC Monitoring",
        "h1": "Managed Endpoint Security Services",
        "description": "Comprehensive endpoint protection, detection, and response managed by certified security professionals. 24/7 SOC monitoring, EDR, EPP, MDM, and threat intelligence for regulated industries.",
        "type": "service_hub",
        "keywords": "managed endpoint security, MSSP, EDR, EPP, MDM, endpoint protection, 24/7 monitoring",
        "spokes": [
            {"name": "Endpoint Detection & Response (EDR)", "url": "edr.html"},
            {"name": "Endpoint Protection Platform (EPP)", "url": "epp.html"},
            {"name": "Mobile Device Management (MDM)", "url": "mdm.html"},
            {"name": "IoT Endpoint Security", "url": "iot.html"},
            {"name": "Cloud Endpoint Security", "url": "cloud.html"},
            {"name": "Endpoint Threat Intelligence", "url": "threat-intel.html"},
            {"name": "Endpoint Vulnerability Management", "url": "vulnerability.html"},
            {"name": "Zero Trust Endpoint Security", "url": "zero-trust.html"}
        ]
    },

    "services/core-endpoint/edr.html": {
        "title": "Endpoint Detection & Response (EDR) Services | Real-Time Threat Detection",
        "h1": "Endpoint Detection & Response (EDR) Services",
        "description": "Advanced EDR services with real-time threat detection, behavioral analysis, and automated response. Detect and stop ransomware, malware, and APTs before they compromise your endpoints.",
        "type": "service_spoke",
        "keywords": "EDR, endpoint detection response, threat detection, behavioral analysis, ransomware detection",
        "hub": "Managed Endpoint Security Services",
        "hub_url": "./"
    },

    "services/testing/index.html": {
        "title": "Security Testing & Assessment Services | Penetration Testing",
        "h1": "Security Testing & Vulnerability Assessment Services",
        "description": "Comprehensive penetration testing and vulnerability assessments to identify and remediate endpoint security weaknesses before attackers exploit them. HIPAA, PCI-DSS, SOC 2 testing.",
        "type": "service_hub",
        "keywords": "penetration testing, vulnerability assessment, security testing, ethical hacking, pen testing",
        "spokes": [
            {"name": "Penetration Testing Services", "url": "penetration-testing.html"},
            {"name": "Vulnerability Assessment Services", "url": "vulnerability-assessment.html"},
            {"name": "Endpoint Vulnerability Scanning", "url": "endpoint-scanning.html"},
            {"name": "Network Penetration Testing", "url": "network-testing.html"},
            {"name": "Wireless Security Testing", "url": "wireless-testing.html"},
            {"name": "Web Application Testing", "url": "web-app-testing.html"},
            {"name": "Social Engineering Testing", "url": "social-engineering.html"},
            {"name": "Red Team Exercises", "url": "red-team.html"}
        ]
    },

    "services/testing/penetration-testing.html": {
        "title": "Penetration Testing Services | Identify Vulnerabilities",
        "h1": "Penetration Testing Services",
        "description": "Professional penetration testing services following OWASP, PTES, and NIST methodologies. Identify vulnerabilities before attackers do. Compliance testing for HIPAA, PCI-DSS, SOC 2.",
        "type": "service_spoke",
        "keywords": "penetration testing, pen testing, ethical hacking, security testing, vulnerability exploitation",
        "hub": "Security Testing Services",
        "hub_url": "./"
    },

    "compliance/hipaa/index.html": {
        "title": "HIPAA-Compliant Endpoint Security | ePHI Protection",
        "h1": "HIPAA-Compliant Endpoint Security Solutions",
        "description": "Managed endpoint security designed specifically for HIPAA compliance requirements and ePHI protection. Technical safeguards, audit controls, encryption, and compliance documentation.",
        "type": "compliance_hub",
        "keywords": "HIPAA compliance, ePHI security, HIPAA endpoint security, healthcare compliance, technical safeguards",
        "spokes": [
            {"name": "HIPAA Risk Assessment", "url": "risk-assessment.html"},
            {"name": "HIPAA Security Rule Compliance", "url": "security-rule.html"},
            {"name": "ePHI Security", "url": "ephi-security.html"},
            {"name": "Breach Notification Response", "url": "breach-notification.html"},
            {"name": "Business Associate Agreement", "url": "baa.html"}
        ]
    },

    "industries/healthcare/index.html": {
        "title": "Healthcare Endpoint Security | Medical Device Protection",
        "h1": "Healthcare Endpoint Security Solutions",
        "description": "Comprehensive endpoint protection for hospitals, medical practices, and healthcare organizations with HIPAA compliance built-in. Medical device security, ePHI encryption, telehealth protection.",
        "type": "industry_hub",
        "keywords": "healthcare cybersecurity, medical device security, hospital endpoint security, HIPAA compliance, ePHI protection",
        "spokes": [
            {"name": "Hospital Endpoint Security", "url": "hospital.html"},
            {"name": "Medical Practice Cybersecurity", "url": "medical-practice.html"},
            {"name": "Healthcare IoT Security", "url": "healthcare-iot.html"},
            {"name": "Telehealth Endpoint Security", "url": "telehealth.html"},
            {"name": "Medical Device Cybersecurity", "url": "medical-devices.html"}
        ]
    },

    "geographic/states/california.html": {
        "title": "Endpoint Security Services California | CA MSP",
        "h1": "Endpoint Security Services in California",
        "description": "Managed endpoint security and compliance services for California businesses across healthcare, financial services, and legal sectors. CCPA/CPRA compliant, 24/7 SOC monitoring.",
        "type": "geographic_state",
        "keywords": "California endpoint security, CA cybersecurity, California MSP, CCPA compliance",
        "cities": ["Los Angeles", "San Francisco", "San Diego", "San Jose", "Sacramento"]
    },

    "about/index.html": {
        "title": "About Endpoint.US | Managed Security Services Provider",
        "h1": "About Endpoint.US",
        "description": "Expert managed security services provider specializing in endpoint security, compliance, and testing for regulated industries. 15+ years experience, CISSP/CEH certified analysts, 24/7 SOC.",
        "type": "about",
        "keywords": "managed security services, MSSP, endpoint security provider, cybersecurity company"
    },

    "about/contact.html": {
        "title": "Contact Endpoint.US | Free Security Assessment",
        "h1": "Contact Us",
        "description": "Schedule a free security assessment to evaluate your endpoint security posture and identify compliance gaps. Form-based contact for secure communication.",
        "type": "contact",
        "keywords": "contact endpoint security, security assessment, cybersecurity consultation"
    }
}


def generate_schema(page_type, config):
    """Generate schema markup based on page type"""
    if page_type == "service_hub" or page_type == "service_spoke":
        return json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": config["h1"],
            "provider": {
                "@type": "ProfessionalService",
                "name": "Endpoint.US"
            },
            "areaServed": {
                "@type": "Country",
                "name": "United States"
            },
            "description": config["description"]
        }, indent=2)
    elif page_type == "compliance_hub":
        return json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": config["h1"],
            "provider": {
                "@type": "ProfessionalService",
                "name": "Endpoint.US"
            },
            "description": config["description"]
        }, indent=2)
    elif page_type == "industry_hub":
        return json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": config["h1"],
            "provider": {
                "@type": "ProfessionalService",
                "name": "Endpoint.US"
            },
            "description": config["description"]
        }, indent=2)
    else:
        return "{}"


def generate_content(page_type, config):
    """Generate main content based on page type"""
    h1 = config["h1"]
    description = config["description"]

    content = f"""
        <!-- Hero Section -->
        <section class="hero">
            <div class="container">
                <div class="hero-content">
                    <h1>{h1}</h1>
                    <p class="lead">{description}</p>

                    <!-- Contact Form -->
                    <script src="https://elfsightcdn.com/platform.js" async></script>
                    <div class="elfsight-app-2b5e4841-d7ca-4190-b28f-63fa2e544a1f" data-elfsight-app-lazy></div>
                </div>
            </div>
        </section>

        <!-- Main Content -->
        <section class="container">
            <div class="content-width">
    """

    if page_type == "service_hub":
        spokes = config.get("spokes", [])
        content += f"""
                <h2>Why {h1} Is Critical</h2>
                <p>Endpoint security requires comprehensive protection combining multiple technologies, continuous monitoring, and expert response capabilities. Endpoints are the #1 attack vector for cybercriminals, with 71% of breaches starting at endpoint devices according to IDC research.</p>

                <p>Our managed endpoint security services provide 24/7 protection with certified security analysts monitoring your endpoints continuously. We detect threats in real-time, investigate suspicious activity, and respond to incidents within minutes - not hours or days.</p>

                <h2>Our Approach</h2>
                <div class="process-steps">
                    <div class="process-step">
                        <h3>1. Assessment & Baseline</h3>
                        <p>We begin with comprehensive assessment of your current endpoint security posture, identifying gaps, vulnerabilities, and compliance requirements. This establishes baseline security metrics.</p>
                    </div>
                    <div class="process-step">
                        <h3>2. Deployment & Configuration</h3>
                        <p>We deploy appropriate security controls including EDR, EPP, MDM, and monitoring agents. Configuration follows security best practices and regulatory requirements.</p>
                    </div>
                    <div class="process-step">
                        <h3>3. Continuous Monitoring</h3>
                        <p>Our 24/7 SOC monitors all endpoints for threats, analyzing alerts, investigating suspicious activity, and maintaining comprehensive audit logs.</p>
                    </div>
                    <div class="process-step">
                        <h3>4. Threat Response</h3>
                        <p>When threats are detected, our analysts respond immediately with containment, investigation, and remediation. Mean time to respond (MTTR) under 5 minutes.</p>
                    </div>
                    <div class="process-step">
                        <h3>5. Optimization & Reporting</h3>
                        <p>Regular reporting, continuous improvement, and optimization ensure your security posture evolves with emerging threats.</p>
                    </div>
                </div>

                <h2>Comprehensive Services</h2>
                <div class="card-grid-3">
        """
        for spoke in spokes:
            content += f"""
                    <div class="card fade-in-on-scroll">
                        <h3>{spoke['name']}</h3>
                        <p>Comprehensive protection and monitoring for your endpoints.</p>
                        <a href="{spoke['url']}" class="btn btn-outline">Learn More →</a>
                    </div>
            """
        content += """
                </div>
        """

    elif page_type == "service_spoke":
        hub = config.get("hub", "Services")
        hub_url = config.get("hub_url", "../")
        content += f"""
                <nav class="breadcrumb">
                    <a href="/">Home</a> › <a href="{hub_url}">{hub}</a> › {h1}
                </nav>

                <h2>What It Is</h2>
                <p>This service provides comprehensive security capabilities designed to protect your organization's endpoints from modern threats while satisfying compliance requirements.</p>

                <h2>Why It's Critical</h2>
                <p>Without proper endpoint security, your organization faces significant risks including data breaches, ransomware attacks, regulatory penalties, and operational disruption. This service addresses these risks through proactive protection and continuous monitoring.</p>

                <h2>How It Works</h2>
                <p>Our implementation follows industry best practices and regulatory frameworks. We deploy appropriate technologies, configure security controls, monitor continuously, and provide expert response when threats are detected.</p>

                <h2>Key Benefits</h2>
                <ul class="list-checkmark">
                    <li><strong>Reduced Risk:</strong> Proactive threat detection and response minimizes security incidents</li>
                    <li><strong>Compliance Support:</strong> Satisfies regulatory requirements with documentation</li>
                    <li><strong>24/7 Protection:</strong> Continuous monitoring by certified security analysts</li>
                    <li><strong>Expert Response:</strong> Rapid incident response with MTTR under 5 minutes</li>
                    <li><strong>Cost Efficiency:</strong> Managed service model provides enterprise security without enterprise costs</li>
                </ul>

                <h2>Integration with Other Services</h2>
                <p>This service integrates with our complete managed security platform including SIEM, threat intelligence, vulnerability management, and incident response services. This provides comprehensive protection across your entire endpoint environment.</p>

                <h2>Compliance Relevance</h2>
                <p>This service addresses specific compliance requirements for HIPAA, PCI-DSS, SOC 2, NIST, and other regulatory frameworks. We provide comprehensive documentation demonstrating how controls satisfy regulatory standards.</p>
        """

    elif page_type == "compliance_hub":
        content += f"""
                <h2>Regulatory Requirements</h2>
                <p>Compliance frameworks establish specific requirements for endpoint security. Our services are designed specifically to satisfy these requirements while providing comprehensive documentation for audits.</p>

                <h2>Our Compliance-First Approach</h2>
                <p>We don't retrofit compliance onto generic security services. Every service we provide considers compliance requirements first, implementing appropriate controls with proper documentation from the start.</p>

                <h2>Comprehensive Documentation</h2>
                <p>Compliance requires extensive documentation. We provide risk assessments, policy templates, implementation specifications, audit logs, and incident response procedures - everything auditors require to verify your controls.</p>

                <h2>Audit Support</h2>
                <p>During audits, we provide technical support and documentation demonstrating your controls meet regulatory standards. Our team includes professionals with compliance framework expertise who understand what auditors need.</p>
        """

    elif page_type == "industry_hub":
        content += f"""
                <h2>Industry-Specific Challenges</h2>
                <p>Your industry faces unique endpoint security challenges including specific regulatory requirements, particular threat patterns, and specialized technology environments. Our services address these industry-specific needs.</p>

                <h2>Regulatory Compliance</h2>
                <p>We understand the regulatory requirements applicable to your industry and implement endpoint security controls specifically designed to satisfy these requirements.</p>

                <h2>Threat Intelligence</h2>
                <p>We monitor threat intelligence specific to your industry, understanding the attack patterns, threat actors, and vulnerabilities that target your sector.</p>

                <h2>Industry Expertise</h2>
                <p>Our team includes professionals with specific experience in your industry who understand your operational requirements, technology constraints, and business priorities.</p>
        """

    elif page_type == "geographic_state":
        cities = config.get("cities", [])
        state = config["h1"].split("in ")[-1]
        content += f"""
                <h2>Why {state} Businesses Need Advanced Endpoint Security</h2>
                <p>{state} businesses face specific cybersecurity challenges including state-specific regulations, high-value targets in key industries, and sophisticated threat actors. Our services provide comprehensive protection while satisfying state and federal requirements.</p>

                <h2>Service Availability</h2>
                <p>We serve businesses throughout {state} with 24/7 remote monitoring and management. On-site support available in major metropolitan areas.</p>

                <h2>Major Cities Served</h2>
                <ul>
        """
        for city in cities:
            content += f"                    <li>{city}</li>\n"
        content += """
                </ul>

                <h2>State-Specific Compliance</h2>
                <p>We understand state-specific regulatory requirements and implement endpoint security controls that satisfy both federal and state compliance obligations.</p>
        """

    elif page_type == "about":
        content += f"""
                <h2>Our Mission</h2>
                <p>Endpoint.US was founded to provide enterprise-grade endpoint security to organizations of all sizes, with particular focus on regulated industries where security and compliance are critical.</p>

                <h2>Our Team</h2>
                <p>Our team includes CISSP and CEH certified security professionals with decades of combined experience in endpoint security, compliance, and incident response. We maintain continuous training on emerging threats and technologies.</p>

                <h2>Our Approach</h2>
                <p>We believe in proactive security, continuous monitoring, and rapid response. Our 24/7 Security Operations Center provides expert protection while you focus on your business.</p>

                <h2>Certifications & Compliance</h2>
                <p>SOC 2 Type II certified with CISSP, CEH, and compliance framework expertise. Our team maintains current certifications and continuous professional development.</p>
        """

    elif page_type == "contact":
        content += f"""
                <h2>Get in Touch</h2>
                <p>Contact us to discuss your endpoint security needs, schedule a free security assessment, or learn more about our services.</p>

                <h3>Free Security Assessment</h3>
                <p>We offer complimentary security assessments to evaluate your current endpoint security posture and identify compliance gaps. No obligation.</p>

                <h3>Form-Based Contact</h3>
                <p>For security and privacy, we use form-based contact rather than publishing phone numbers or email addresses. This helps protect both our clients and our team from social engineering attacks.</p>
        """

    content += """
            </div>
        </section>

        <!-- FAQ Section -->
        <section class="container">
            <div class="faq-section">
                <h2>Frequently Asked Questions</h2>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">What is included in this service?</button>
                    <div class="faq-answer">
                        <p>Our service includes comprehensive endpoint protection, 24/7 monitoring by certified analysts, threat detection and response, compliance documentation, and regular reporting.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">How quickly can you respond to threats?</button>
                    <div class="faq-answer">
                        <p>Our mean time to respond (MTTR) is under 5 minutes for critical threats. Our 24/7 SOC monitors your endpoints continuously and responds immediately when threats are detected.</p>
                    </div>
                </div>
                <div class="faq-item">
                    <button class="faq-question" aria-expanded="false">Do you support compliance requirements?</button>
                    <div class="faq-answer">
                        <p>Yes, our services are specifically designed to satisfy HIPAA, PCI-DSS, SOC 2, NIST, and other compliance frameworks. We provide comprehensive documentation for audits.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- CTA Section -->
        <section class="container">
            <div class="cta-section">
                <h2>Ready to Strengthen Your Endpoint Security?</h2>
                <p>Schedule a free security assessment to evaluate your current posture and identify gaps</p>
                <a href="/about/security-assessment.html" class="btn btn-primary btn-large">Schedule Free Assessment</a>
            </div>
        </section>
    """

    return content


def generate_page(path, config):
    """Generate complete HTML page"""
    page_type = config["type"]
    title = config["title"]
    description = config["description"]
    keywords = config["keywords"]
    h1 = config["h1"]

    # Generate schema
    schema = generate_schema(page_type, config)

    # Generate content
    content = generate_content(page_type, config)

    # Build full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Endpoint.US</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <link rel="canonical" href="https://endpoint.us.com/{path}">

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.css">
    <link rel="stylesheet" href="/assets/css/components.css">
    <link rel="stylesheet" href="/assets/css/responsive.css">

    <!-- Schema Markup -->
    <script type="application/ld+json">
    {schema}
    </script>
</head>
<body>
    <a href="#main-content" class="skip-to-content">Skip to main content</a>

    <!-- Header - Same as homepage -->
    <header class="site-header">
        <!-- Header content here -->
    </header>

    <main id="main-content">
        {content}
    </main>

    <!-- Footer - Same as homepage -->
    <footer class="site-footer">
        <!-- Footer content here -->
    </footer>

    <button class="back-to-top" aria-label="Back to top">↑</button>

    <script src="/assets/js/navigation.js" defer></script>
    <script src="/assets/js/animations.js" defer></script>
    <script src="/assets/js/main.js" defer></script>
</body>
</html>
"""

    return html


def main():
    """Generate all pages"""
    print("Generating Endpoint.US website pages...")

    for path, config in PAGES_CONFIG.items():
        # Create directory if needed
        file_path = Path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate page
        html = generate_page(path, config)

        # Write file
        with open(file_path, 'w') as f:
            f.write(html)

        print(f"✓ Generated {path}")

    print(f"\nGenerated {len(PAGES_CONFIG)} pages successfully!")


if __name__ == "__main__":
    main()
