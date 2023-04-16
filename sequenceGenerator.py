import random

fileName = "Oryza glumipatula.txt"

# Read the input file
with open(fileName, "r") as file:
    genomeSeq = file.read().replace("\n", "")

# Generate the sequences 
i = 0
while i < 10:
    start = random.randint(0, len(genomeSeq) - 1000)
    end = start + 1000
    randomS = genomeSeq[start:end].replace(" ", "")
    
    #create title, file name and the output for the file
    title = "Random sequence " + str(i+1) + " from whole genome"
    file_name = "output123Sequence" + str(i+1) + ".fasta"
    
    with open(file_name, "w") as output_file:
        #header for the file
        header_line = ">" + title + " (start=" + str(start) + ", end=" + str(end) + ")\n"
        output_file.write(header_line)
    
        output_file.write(randomS)
    
    i += 1



