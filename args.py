import argparse

msg = "Manual do importador"

# Initialize parser
parser = argparse.ArgumentParser(description = msg)
parser.add_argument("-f", "--File", help = "Caminho do arquivo para importação")
args = parser.parse_args()

print(args.File)
