import io
import re

import lxml.html as hl

file_no_regex = r"^(\s)*([0-9]{4}\s)?K(\s[0-9]{4})\/([0-9]{4})"

def parse_html(raw_html):
    doc = hl.fromstring(raw_html)
    no_results = doc.cssselect("#inhalt h3")[0].text_content().split()[3]
    print(no_results, "Ergebnisse für deine Suchanfrage")
    infos = doc.cssselect("#inhalt tr td b")
    for el in infos:
        match = re.match(file_no_regex, el.text_content())
        if match:
            print(" ".join(match.string.strip().split()[:-1]))
    return
