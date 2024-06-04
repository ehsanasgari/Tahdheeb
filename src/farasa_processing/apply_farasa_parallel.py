import os
import subprocess
import argparse
import multiprocessing

def process_file(args):
    input_folder, output_folder, input_file = args
    input_path = os.path.join(input_folder, input_file)
    output_path = os.path.join(output_folder, input_file)
    subprocess.run(["java", "ParallelTextProcessing", input_path, output_path])

def process_files_parallel(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Get list of input files
    input_files = os.listdir(input_folder)
    
    # Create a list of arguments for each file to be processed
    tasks = [(input_folder, output_folder, input_file) for input_file in input_files]
    
    # Process files in parallel
    with multiprocessing.Pool(processes=45) as pool:
        pool.map(process_file, tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process files in parallel using ParallelTextProcessing.")
    parser.add_argument("input_folder", type=str, help="Path to the input folder.")
    parser.add_argument("output_folder", type=str, help="Path to the output folder.")

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    process_files_parallel(input_folder, output_folder)
