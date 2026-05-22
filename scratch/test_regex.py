import re

filepath = r'c:\Users\vshar\OneDrive\Desktop\SFVedas_Website\sfvedas\tutorials\crm-002\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

q_id = 'q1'
questions = ['q1', 'q2', 'q3']
q_start = content.find(f'<div class="quiz-question" id="{q_id}"')
if q_start != -1:
    print("Found q1 block via slicing:")
    next_q_idx = len(content)
    for other_q in questions:
        if other_q != q_id:
            other_idx = content.find(f'<div class="quiz-question" id="{other_q}"')
            if other_idx > q_start and other_idx < next_q_idx:
                next_q_idx = other_idx
    
    # Slice the question block
    q_html = content[q_start:next_q_idx]
    
    # Let's try the validator's option regex on this sliced block
    pattern = r'<div class="quiz-option"[^>]*onclick="answer\(this,\s*(\'|")[^\'"]+(\'|"),\s*(\'|")(right|wrong)(\'|")\)"[^>]*>(.*?)</div>'
    matches = re.findall(pattern, q_html)
    print("Matches count:", len(matches))
    for m in matches:
        print("Match:", m[-1])

