import html.parser

class HTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, data):
        self.fed.append(data)

    def get_data(self):
        return ''.join(self.fed)

def parse_html(html_content):
    parser = HTMLParser()
    parser.feed(html_content)
    return parser.get_data()

# Example usage
html_content = "<html><body><h1>Title</h1><p>Paragraph</p></body></html>"
parsed_text = parse_html(html_content)
print(parsed_text)