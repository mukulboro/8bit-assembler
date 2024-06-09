from assembler import Assembler
import argparse

CONFIG_FILE_NAME = "config"
CODE_FILE_NAME = "multiples5.a"
OUTPUT_FILE_NAME = "program"
HEADER = "v2.0 raw"

cli_description = "Generate logisim RAM image from custom 8 bit assembly"
parser = argparse.ArgumentParser(description=cli_description)

parser.add_argument('-c', '--code', type=str, help='Assembly code file', required=True)
parser.add_argument('-o', '--output', type=str, help='Output File Name', default="program")
parser.add_argument('-u', '--header', type=str, help='Output File Name', default="v2.0 raw")
parser.add_argument('-x', '--config', type=str, help='Config File for assembler', default="config")

args = parser.parse_args()


a = Assembler(cfg_file=args.config, 
              code_file=args.code, 
              op_file=args.output, 
              header=args.header)
a.compile()