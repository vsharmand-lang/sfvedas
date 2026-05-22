import os
import re
import sys

# Directory configuration
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TUTORIALS_DIR = os.path.join(WORKSPACE_DIR, 'tutorials')

class TutorialValidator:
    def __init__(self, directory_name):
        self.slug = directory_name
        self.filepath = os.path.join(TUTORIALS_DIR, self.slug, 'index.html')
        self.errors = []
        self.warnings = []
        self.content = ""

    def log_error(self, message):
        self.errors.append(message)

    def log_warning(self, message):
        self.warnings.append(message)

    def validate(self):
        if not os.path.exists(self.filepath):
            self.log_error(f"index.html file NOT found at {self.filepath}")
            return False

        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

        self._check_placeholders()
        self._check_canonical()
        self._check_title()
        self._check_assets()
        self._check_breadcrumbs()
        self._check_ad_units()
        self._check_section_summary()
        self._check_sections_and_toc()
        self._check_key_takeaways()
        self._check_quiz()
        self._check_related_tutorials()
        
        return len(self.errors) == 0

    def _check_placeholders(self):
        # Allow the specific Git workflow string in arch-015, but for CRM it should be clean
        placeholders = re.findall(r'\{\{[^}]*\}\}', self.content)
        for p in placeholders:
            self.log_error(f"Contains unreplaced placeholder: {p}")
        
        if 'PLACEHOLDER' in self.content:
            self.log_error("Contains keyword 'PLACEHOLDER'")
        if 'TODO' in self.content:
            self.log_error("Contains keyword 'TODO'")

    def _check_canonical(self):
        # Look for canonical link
        m = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', self.content)
        if not m:
            self.log_error("Missing canonical link tag")
            return
        
        expected_url = f"https://sfvedas.com/tutorials/{self.slug}/"
        actual_url = m.group(1)
        if actual_url != expected_url:
            self.log_error(f"Canonical URL mismatch. Expected '{expected_url}', got '{actual_url}'")

    def _check_title(self):
        m = re.search(r'<title>(.*?)</title>', self.content, re.IGNORECASE)
        if not m:
            self.log_error("Missing <title> tag")
            return
        
        title_text = m.group(1)
        expected_prefix = f"{self.slug.upper()}:"
        if not title_text.startswith(expected_prefix):
            self.log_error(f"Title does not start with expected prefix '{expected_prefix}'. Title is: '{title_text}'")
        
        if " — SFVedas" not in title_text:
            self.log_warning(f"Title might be missing standard suffix ' — SFVedas' (using em dash). Title is: '{title_text}'")

    def _check_assets(self):
        # Check standard stylesheet and script absolute paths
        if '/css/main.css' not in self.content:
            self.log_error("Main stylesheet href does not use absolute path '/css/main.css'")
        
        if '/js/main.js' not in self.content:
            self.log_error("Main JS src does not use absolute path '/js/main.js'")

    def _check_breadcrumbs(self):
        # Back breadcrumb should point to tag page absolute URL
        if '/tutorials/?tag=crm-comparison' not in self.content:
            self.log_error("Breadcrumb backlink does not use expected absolute path '/tutorials/?tag=crm-comparison'")

    def _check_ad_units(self):
        # Exactly one ad-unit
        ad_count = self.content.count('class="ad-unit"')
        if ad_count != 1:
            self.log_error(f"Page should have exactly one ad-unit. Found {ad_count}")
        
        # Check empty ad slot
        m = re.findall(r'data-ad-slot="([^"]*)"', self.content)
        for slot in m:
            if slot != "":
                self.log_warning(f"Found non-empty data-ad-slot '{slot}'. Grammar requires it to be empty.")

    def _check_section_summary(self):
        # Check for section summary block
        if 'class="section-summary"' not in self.content:
            self.log_error("Missing <div class=\"section-summary\"> block")
            return
        
        # Extract section-summary block and count bullets
        summary_m = re.search(r'<div class="section-summary">.*?<ul>(.*?)</ul>', self.content, re.DOTALL)
        if not summary_m:
            self.log_error("Section summary does not contain a <ul> list")
            return
        
        bullets = re.findall(r'<li>(.*?)</li>', summary_m.group(1))
        bullet_count = len(bullets)
        if not (5 <= bullet_count <= 7):
            self.log_warning(f"Section summary has {bullet_count} bullet points (target range is 5-7)")

    def _check_sections_and_toc(self):
        # Find all h2 tags inside article
        article_m = re.search(r'<article class="tutorial-body"[^>]*>(.*?)</article>', self.content, re.DOTALL)
        if not article_m:
            self.log_error("Missing <article class=\"tutorial-body\"> container")
            return
        
        article_content = article_m.group(1)
        h2_elements = re.findall(r'<h2\s+id="([^"]+)"[^>]*>(.*?)</h2>', article_content)
        
        if not h2_elements:
            self.log_error("No <h2> sections found in article body")
            return
        
        # Check number of sections
        if not (4 <= len(h2_elements) <= 8):
            self.log_warning(f"Found {len(h2_elements)} sections (grammar states 4 to 8 sections)")
        
        # Check ID sequence: s1, s2, s3...
        for idx, (h2_id, h2_title) in enumerate(h2_elements, start=1):
            expected_id = f"s{idx}"
            if h2_id != expected_id:
                self.log_error(f"Section {idx} ID mismatch: expected '{expected_id}', got '{h2_id}' (title: '{h2_title.strip()}')")

        # Verify TOC matches in the sidebar
        sidebar_m = re.search(r'<aside class="tutorial-sidebar">(.*?)</aside>', self.content, re.DOTALL)
        if not sidebar_m:
            self.log_error("Missing <aside class=\"tutorial-sidebar\">")
            return
        
        sidebar_content = sidebar_m.group(1)
        toc_items = re.findall(r'<li><a href="#([^"]+)">([^<]+)</a></li>', sidebar_content)
        
        # Match each H2 to the TOC
        h2_ids = [h[0] for h in h2_elements]
        toc_hrefs = [t[0] for t in toc_items]
        
        # Filter out key takeaways and quiz links from TOC check (they go at the end)
        core_toc_hrefs = [h for h in toc_hrefs if h.startswith('s')]
        
        if core_toc_hrefs != h2_ids:
            self.log_error(f"Sidebar TOC does not match H2 IDs. Core TOC has: {core_toc_hrefs}, Body has H2s: {h2_ids}")
            
        # Last items should be takeaways and quiz
        last_toc_hrefs = [h for h in toc_hrefs if not h.startswith('s')]
        if 'takeaways' not in last_toc_hrefs and 'quiz' not in last_toc_hrefs:
            self.log_error(f"Sidebar TOC missing link to Key Takeaways (#takeaways) or Checkpoint Quiz (#quiz). Last links found: {last_toc_hrefs}")

    def _check_key_takeaways(self):
        if 'class="key-takeaways"' not in self.content:
            self.log_error("Missing <div class=\"key-takeaways\"> block")
            return
            
        takeaways_m = re.search(r'class="key-takeaways"\s+id="([^"]+)"', self.content)
        if not takeaways_m or takeaways_m.group(1) != 'takeaways':
            self.log_error("Key Takeaways container must have id=\"takeaways\"")
            
        takeaways_list_m = re.search(r'<div class="key-takeaways".*?<ul>(.*?)</ul>', self.content, re.DOTALL)
        if not takeaways_list_m:
            self.log_error("Key Takeaways does not contain a <ul> list")
            return
            
        bullets = re.findall(r'<li>(.*?)</li>', takeaways_list_m.group(1))
        bullet_count = len(bullets)
        if bullet_count < 5:
            self.log_error(f"Key Takeaways has only {bullet_count} bullet points (minimum is 5)")

    def _check_quiz(self):
        if 'class="quiz-section"' not in self.content:
            self.log_error("Missing Checkpoint Quiz <div class=\"quiz-section\"> block")
            return
            
        quiz_m = re.search(r'class="quiz-section"\s+id="([^"]+)"', self.content)
        if not quiz_m or quiz_m.group(1) != 'quiz':
            self.log_error("Quiz container must have id=\"quiz\"")

        # Count questions
        questions = re.findall(r'<div class="quiz-question"\s+id="([^"]+)">', self.content)
        if len(questions) != 3:
            self.log_error(f"Quiz should have exactly 3 questions. Found {len(questions)}")

        # Check options for each question
        for q_id in questions:
            q_start = self.content.find(f'<div class="quiz-question" id="{q_id}"')
            if q_start == -1:
                self.log_error(f"Quiz question '{q_id}' NOT found")
                continue
                
            next_q_idx = len(self.content)
            for other_q in questions:
                if other_q != q_id:
                    other_idx = self.content.find(f'<div class="quiz-question" id="{other_q}"')
                    if other_idx > q_start and other_idx < next_q_idx:
                        next_q_idx = other_idx
            
            # Use slice to locate the options for this question
            q_html = self.content[q_start:next_q_idx]
            
            options = re.findall(r'<div class="quiz-option"[^>]*onclick="answer\(this,\s*(\'|")[^\'"]+(\'|"),\s*(\'|")(right|wrong)(\'|")\)"[^>]*>(.*?)</div>', q_html)
            if len(options) != 4:
                self.log_error(f"Quiz question '{q_id}' should have exactly 4 options. Found {len(options)}")
                
            # Verify options labels A., B., C., D.
            for idx, opt in enumerate(options):
                opt_text = opt[5].strip()
                expected_letter = chr(65 + idx) + "."  # A., B., C., D.
                if not opt_text.startswith(expected_letter):
                    self.log_error(f"Quiz question '{q_id}' option {idx+1} does not start with '{expected_letter}'. Option text: '{opt_text}'")

    def _check_related_tutorials(self):
        if 'class="related-tutorials"' not in self.content:
            self.log_error("Missing <div class=\"related-tutorials\"> block")
            return
            
        cards = re.findall(r'<a href="\.\./([^"/]+)/"\s+class="related-card">', self.content)
        if len(cards) != 3:
            self.log_error(f"Related tutorials section must have exactly 3 cards using the '../slug/' relative URL format. Found {len(cards)}: {cards}")


def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    crm_dirs = sorted([d for d in os.listdir(TUTORIALS_DIR) if d.startswith('crm-') and os.path.isdir(os.path.join(TUTORIALS_DIR, d))])
    
    print("============================================================")
    print(f"RUNNING AUTOMATED GRAMMAR TESTS ON {len(crm_dirs)} CRM TUTORIALS")
    print("============================================================")
    
    all_ok = True
    for directory in crm_dirs:
        validator = TutorialValidator(directory)
        success = validator.validate()
        
        status_str = "PASS" if success else "FAIL"
        warn_str = f" ({len(validator.warnings)} Warnings)" if validator.warnings else ""
        print(f"[{status_str}] {directory}: {validator.filepath}{warn_str}")
        
        if validator.errors:
            all_ok = False
            for err in validator.errors:
                print(f"   ↳ ERROR: {err}")
        if validator.warnings:
            for warn in validator.warnings:
                print(f"   ↳ WARNING: {warn}")
        print()
        
    print("============================================================")
    if all_ok:
        print("SUCCESS: ALL CRM TUTORIALS COMPLIED WITH THE SITE GRAMMAR SPECIFICATIONS!")
        sys.exit(0)
    else:
        print("FAILURE: SOME CRM TUTORIALS HAVE COMPLIANCE ISSUES THAT NEED FIXING.")
        sys.exit(1)

if __name__ == '__main__':
    main()
