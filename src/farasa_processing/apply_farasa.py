import os
import subprocess
import argparse

def process_file(input_folder, output_folder, input_file):
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, input_file)
    subprocess.run(["java", "ParallelTextProcessing", input_path, output_path])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a single file using ParallelTextProcessing.")
    parser.add_argument("input_folder", type=str, help="Path to the input folder.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder.")
    parser.add_argument("input_file", type=str, help="Name of the file to be processed.")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    input_file = args.input_file

    os.makedirs(output_folder, exist_ok=True)
    process_file(input_folder, output_folder, input_file)
