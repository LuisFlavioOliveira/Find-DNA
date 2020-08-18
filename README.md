# Find DNA

This is a program that I developed using Python and one of the coolest I have done. It identifies to whom a sequence of DNA belongs in a very precise way.

DNA, the carrier of genetic information in living things, has been 
used in criminal justice for decades. But how, exactly, does DNA 
profiling work? Given a sequence of DNA, how can forensic investigators 
identify to whom it belongs?

DNA is really just a sequence of molecules called nucleotides, 
arranged into a particular shape (a double helix). Each nucleotide of 
DNA contains one of four different bases: adenine (A), cytosine (C), 
guanine (G), or thymine (T). Every human cell has billions of these 
nucleotides arranged in sequence. Some portions of this sequence (i.e. 
genome) are the same, or at least very similar, across almost all 
humans, but other portions of the sequence have a higher genetic 
diversity and thus vary more across the population.

One place where DNA tends to have high genetic diversity is in Short 
Tandem Repeats (STRs). An STR is a short sequence of DNA bases that 
tends to repeat consecutively numerous times at specific locations 
inside of a person’s DNA. The number of times any particular STR repeats
 varies a lot among individuals. 
 
 Using multiple STRs, rather than just one, can improve the accuracy of 
DNA profiling. If the probability that two people have the same number 
of repeats for a single STR is 5%, and the analyst looks at 10 different
 STRs, then the probability that two DNA samples match purely by chance 
is about 1 in 1 quadrillion (assuming all STRs are independent of each 
other). So if two DNA samples match in the number of repeats for each of
 the STRs, the analyst can be pretty confident they came from the same 
person. CODIS, The FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process.

## The methodology
I think it's quite important to give an inside of how the program works in terms of a DNA sequence:

So given a sequence of DNA, how might you identify to whom it 
belongs? Well, imagine that you looked through the DNA sequence for the 
longest consecutive sequence of repeated AGATs and found that the longest sequence was 17 repeats long. If you then found that the longest sequence of AATG is 22 repeats long, and the longest sequence of TATC
 is 19 repeats long, that would provide pretty good evidence that the 
DNA comes from a person that has this same sequence in the DNA database. Of course, it’s also possible that once you take the 
counts for each of the STRs, it doesn’t match anyone in your DNA 
database, in which case you have no match.

My program takes a sequence of DNA and a CSV file containing STR counts for a list of individuals and then output to whom the DNA (most likely) belongs. 

## Specifications about the source code 

The program require as its first command-line argument the name 
of a CSV file containing the STR counts for a list of individuals and 
should require as its second command-line argument the name of a text 
file containing the DNA sequence to identify.

The program then opens the CSV file and reads its content into memory. 

Then, for each of the STRs, the program will compute the longest run of consecutive repeats of the STR in the
 DNA sequence to identify.
    
If the STR counts match exactly with any of the individuals in the CSV 
file, the program will print out the name of the matching individual.

Else, if doesn't match, the program will return `No Match`

## Tools

* You will only need Python installed on your computer. So you can get it directly from Python's website.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

You will need to settle up a compiler for C. There is many but I recommend downloading ![Visual Studio Code](https://code.visualstudio.com/) and getting the C/C++ extension that it provides. 


### Installation and Usage

Just download the repository here and open it with your TextEditor (I recommend Visual Studio Code).

To use the program, you shall use the following commands:


`$ python dna.py databases/[database].csv sequences/[text file].txt`


## License / Copyright

* Completed as the Project 6 of Harvard CS50 Curriculum

* This project is licensed under the MIT License.








    
