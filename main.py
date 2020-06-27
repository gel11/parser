import argparse

from parser import Parser


def main():
    argument_parser = argparse.ArgumentParser(description='Add some integers.')
    argument_parser.add_argument('--input_file', type=str)
    argument_parser.add_argument('--output_file', type=str)
    args = argument_parser.parse_args()

    parser = Parser()
    parser.parse_input_file(args.input_file)
    parser.save_to_file(args.output_file)


if __name__ == "__main__":
    main()
