def modify_file(input_file, output_file):
    with open(input_file, 'r') as f_input:
        with open(output_file, 'w') as f_output:
            for line in f_input:
                modified_line = line[9:-3] + '\n'
                f_output.write(modified_line)

input_file = 'input.txt'
output_file = 'output.txt'

modify_file(input_file, output_file)
