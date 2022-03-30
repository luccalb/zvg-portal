import io
import lxml.html as hl


def parse_html(raw_html):
    doc = hl.fromstring(raw_html)
    no_results = doc.cssselect("#inhalt h3")[0].text_content().split()[3]
    print(no_results, "Ergebnisse für deine Suchanfrage")
    infos = doc.cssselect("#inhalt tr td b")
    for el in infos[0:20]:
        print(el.text_content())
    return no_results
