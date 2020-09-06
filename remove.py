
def count_lines(file='no_line_script.txt'):
    with open(file, 'r') as file:
        for index, line in enumerate(file):
            pass
    file.close()
    return index + 1

def remove_lines(original='mormon.txt', empty='no_line_script.txt'):
    script = open(original, 'r')
    empty_script = open(empty, 'w')

    script_length = count_lines(original)
    for i in range(script_length):
        line = script.readline()
        if line.replace(" ","") not in ['\n','\r\n']:
            empty_script.write(line)

if __name__ == '__main__':
    remove_lines()
    print ("done")

