#!/usr/bin/env python3
"""
Generate comprehensive sitemap.xml for all 144 pages
"""

import os
from datetime import datetime
import glob

# Base URL
BASE_URL = "https://endpoint.us.com"

# Get current date in YYYY-MM-DD format
CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")

# Priority and changefreq rules
PAGE_RULES = {
    'index.html': {'priority': '1.0', 'changefreq': 'weekly'},
    'services/': {'priority': '0.9', 'changefreq': 'weekly'},
    'compliance/': {'priority': '0.9', 'changefreq': 'weekly'},
    'industries/': {'priority': '0.9', 'changefreq': 'weekly'},
    'geographic/': {'priority': '0.7', 'changefreq': 'monthly'},
    'resources/': {'priority': '0.7', 'changefreq': 'weekly'},
    'about/': {'priority': '0.8', 'changefreq': 'monthly'},
    'legal/': {'priority': '0.3', 'changefreq': 'yearly'},
}

def get_priority_changefreq(filepath):
    """Determine priority and changefreq based on file path"""
    # Index pages get higher priority
    if '/index.html' in filepath:
        return '0.9', 'weekly'

    # Check each rule
    for pattern, rules in PAGE_RULES.items():
        if pattern in filepath:
            return rules['priority'], rules['changefreq']

    # Default
    return '0.6', 'monthly'

def generate_sitemap():
    """Generate complete sitemap.xml"""

    # Find all HTML files
    html_files = []

    # Home page
    if os.path.exists('index.html'):
        html_files.append('index.html')

    # All other pages
    for pattern in ['services/**/*.html', 'compliance/**/*.html', 'industries/**/*.html',
                    'geographic/**/*.html', 'resources/**/*.html', 'about/*.html', 'legal/*.html']:
        html_files.extend(glob.glob(pattern, recursive=True))

    # Sort for consistency
    html_files.sort()

    # Start XML
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">

'''

    # Add each URL
    for filepath in html_files:
        # Convert file path to URL
        if filepath == 'index.html':
            url = f"{BASE_URL}/"
        else:
            url = f"{BASE_URL}/{filepath}"

        priority, changefreq = get_priority_changefreq(filepath)

        xml_content += f'''    <url>
        <loc>{url}</loc>
        <lastmod>{CURRENT_DATE}</lastmod>
        <changefreq>{changefreq}</changefreq>
        <priority>{priority}</priority>
    </url>
'''

    # Close XML
    xml_content += '''
</urlset>'''

    # Write sitemap
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml_content)

    print(f"✅ Generated sitemap.xml with {len(html_files)} URLs")
    print(f"   Date: {CURRENT_DATE}")

    # Show breakdown by section
    sections = {}
    for filepath in html_files:
        section = filepath.split('/')[0] if '/' in filepath else 'root'
        sections[section] = sections.get(section, 0) + 1

    print("\n📊 Page breakdown:")
    for section, count in sorted(sections.items()):
        print(f"   {section}: {count} pages")

if __name__ == '__main__':
    generate_sitemap()
