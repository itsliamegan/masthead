from websites.inflect import titleize, dasherize

def test_titleizes_single_word():
	name = "about"
	title = titleize(name)

	assert title == "About"

def test_titleizes_multiple_words():
	name = "contact_us"
	title = titleize(name)

	assert title == "Contact Us"

def test_dasherizes_single_word():
	name = "about"
	dashed = dasherize(name)

	assert dashed == "about"

def test_dasherizes_multiple_words():
	name = "contact_us"
	dashed = dasherize(name)

	assert dashed == "contact-us"
