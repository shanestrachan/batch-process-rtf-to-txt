from striprtf.striprtf import rtf_to_text
import codecs
import re
import os

# Place files to convert in the same folder as this script

def create_output_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_rtf_to_txt(rtf_path, txt_path_single_space, txt_path_new_lines):
    with open(rtf_path, "r", encoding="utf-8") as file:
        rtf_content = file.read()

    text = rtf_to_text(rtf_content)
    text_single_space = re.sub(r'\s+', ' ', text)

    with codecs.open(txt_path_single_space, "w", "utf-8") as file:
        file.write(text_single_space)

    text_new_lines = re.sub(r'(\.\.\.|\.\s|\?|\!)\s*', r'\1\n\n', text_single_space)

    with codecs.open(txt_path_new_lines, "w", "utf-8") as file:
        file.write(text_new_lines)

def process_txt_file(txt_path, txt_path_single_space, txt_path_new_lines):
    with open(txt_path, "r", encoding="utf-8") as file:
        text = file.read()

    text_single_space = re.sub(r'\s+', ' ', text)

    with codecs.open(txt_path_single_space, "w", "utf-8") as file:
        file.write(text_single_space)

    text_new_lines = re.sub(r'(\.\s\.\s\.|\.\.\.|\.\s|\?|\!)\s*', r'\1\n\n', text_single_space)

    with codecs.open(txt_path_new_lines, "w", "utf-8") as file:
        file.write(text_new_lines)

output_directory = 'output'
create_output_dir(output_directory)

rtf_files = [f for f in os.listdir('.') if f.endswith('.rtf')]

for rtf_file in rtf_files:
    base_filename = os.path.splitext(rtf_file)[0]

    single_space_txt_path = f'output/{base_filename}-single-space.txt'
    new_lines_txt_path = f'output/{base_filename}-new-lines.txt'

    convert_rtf_to_txt(rtf_file, single_space_txt_path, new_lines_txt_path)


txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

for txt_file in txt_files:
    if txt_file.startswith('output'):
        continue

    base_filename = os.path.splitext(txt_file)[0]

    single_space_txt_path = f'output/{base_filename}-single-space.txt'
    new_lines_txt_path = f'output/{base_filename}-new-lines.txt'

    process_txt_file(txt_file, single_space_txt_path, new_lines_txt_path)