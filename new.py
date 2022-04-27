import argparse
parser = argparse.ArgumentParser()
# Insert your rules

# Parse my string, first splitting it into a list.
parser.add_argument(
    '-o', '--once', action='store_true', help='makes the script run once')
parser.add_argument(
    '-H', '--Help', action='store_true', help='makes the script run once')
args = parser.parse_args("--once --help".split())

print(args.once)
print(args.Help)