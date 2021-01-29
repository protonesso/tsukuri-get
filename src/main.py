import argparse
import cli.index as cindex
import cli.info as cinfo
import cli.install as cinstall
import cli.remove as cremove
import cli.search as csearch
import cli.update as cupdate
import cli.upgrade as cupgrade

def main():
	parser = argparse.ArgumentParser()
	subparser = parser.add_subparsers(title='subcommands')

	info_parser = subparser.add_parser('info', help='Show package information')
	info_parser.add_argument('package')
	info_parser.set_defaults(operation=cinfo.info)

	install_parser = subparser.add_parser('install', help='Install packages')
	install_parser.add_argument('package', nargs='+')
	install_parser.add_argument('-f', '--force', help='Force installation', dest='force', action='store_true')
	install_parser.add_argument('-b', '--nobackup', help='Do not save old files/configs', dest='nobackup', action='store_true')
	install_parser.add_argument('-d', '--nodeps', help='Do not check for deps', dest='nodeps', action='store_true')
	install_parser.add_argument('-r', '--noreinstall', help='Do not reinstall package', dest='noreinst', action='store_true')
	install_parser.add_argument('-s', '--noscripts', help='Do not execute package scripts', dest='noscripts', action='store_true')
	install_parser.add_argument('-t', '--nohooks', help='Do not execute package hooks', dest='nohooks', action='store_true')
	install_parser.set_defaults(operation=cinstall.install)

	list_parser = subparser.add_parser('list', help='List packages')
	list_parser.add_argument('-n', '--number', help='Show number of packages', dest='number', action='store_true')
	list_parser.set_defaults(operation=cindex.index)

	remove_parser = subparser.add_parser('remove', help='Remove packages')
	remove_parser.add_argument('package', nargs='+')
	remove_parser.add_argument('-f', '--force', help='Force removal', dest='force', action='store_true')
	remove_parser.add_argument('-b', '--nobackup', help='Do not save old files/configs', dest='nobackup', action='store_true')
	remove_parser.add_argument('-d', '--nodeps', help='Do not check for deps', dest='nodeps', action='store_true')
	remove_parser.add_argument('-s', '--noscripts', help='Do not execute package scripts', dest='noscripts', action='store_true')
	remove_parser.add_argument('-t', '--nohooks', help='Do not execute package hooks', dest='nohooks', action='store_true')
	remove_parser.set_defaults(operation=cremove.remove)

	search_parser = subparser.add_parser('search', help='Search for packages')
	search_parser.add_argument('package', nargs='+')
	search_parser.set_defaults(operation=csearch.search)

	update_parser = subparser.add_parser('update', help='Update repositories')
	update_parser.set_defaults(operation=cupdate.update)

	upgrade_parser = subparser.add_parser('upgrade', help='Upgrade system')
	upgrade_parser.add_argument('-f', '--force', help='Force system upgrade', dest='force', action='store_true')
	upgrade_parser.set_defaults(operation=cupgrade.upgrade)

	args = parser.parse_args()
	if not vars(args):
		parser.print_usage()
	else:
		args.operation(args)
