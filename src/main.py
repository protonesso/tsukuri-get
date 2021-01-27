import argparse

def index(args):
	for i in args.package:
		print("a")

def install(args):
	for i in args.package:
		print("a")

def main():
	parser = argparse.ArgumentParser()
	subparser = parser.add_subparsers(title='subcommands',
					description='valid subcommands',
					help='description')

	install_parser = subparser.add_parser('install')
	install_parser.add_argument('package', nargs='+')
	install_parser.add_argument('-f', '--force', dest='force', action='store_true')
	install_parser.set_defaults(operation=install)

	list_parser = subparser.add_parser('list')
	list_parser.add_argument('package', nargs='+')
	list_parser.add_argument('-n', '--number', dest='number', action='store_true')
	list_parser.set_defaults(operation=index)

	args = parser.parse_args()
	if not vars(args):
		parser.print_usage()
	else:
		args.operation(args)
