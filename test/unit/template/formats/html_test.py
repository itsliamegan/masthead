from websites.template import compile, formats, Registry

def test_renders_html_verbatim():
	registry = Registry()
	template = compile("<h1>About</h1>", formats.html)
	rendered = template.render(registry)

	assert rendered == "<h1>About</h1>"
