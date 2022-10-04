from local_parser import put_data
from local_parser import FILENAME
import argparse


def run_pipeline(args):
   return  put_data(args.file_name)


if __name__=="__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("--file-name", type=str, default=FILENAME)
   args = parser.parse_args()
   run_pipeline(args)
