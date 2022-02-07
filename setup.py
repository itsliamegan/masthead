from setuptools import setup, find_packages

setup(
	name="websites",
	version="0.1.0",
	packages=find_packages(where=".", include=["websites*"]),
	install_requires=[
		"cmarkgfm",
		"pybars3",
		"toml",
	],
	extras_require={
		"dev": [
			"mypy",
			"pytest",
		],
	},
	zip_safe=False,
)
