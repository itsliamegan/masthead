from argparse import ArgumentParser
from sys import exit
from .commands import build, create

parser = ArgumentParser(prog="websites")
subparser = parser.add_subparsers(title="subcommands", dest="command")

build_parser = subparser.add_parser("build", help="build an existing site")

create_parser = subparser.add_parser("create", help="create a new site")
create_parser.add_argument(
	"name",
	help="name of the site to create",
	type=str,
)

def main(argv):
	args = parser.parse_args(argv)
	params = vars(args).copy()
	del params["command"]

	if "command" not in args:
		parser.print_help()
	elif args.command == "build":
		build(**params)
	elif args.command == "create":
		create(**params)
