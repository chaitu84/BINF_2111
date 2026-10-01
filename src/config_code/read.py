import argparse
from pathlib import Path

from Bio import SeqIO

#gene.fna from zip , gencode.v50.lncRNA_transcripts.fa.gz,gencode.v50.transcripts.fa.gz

def HPV_gene(file_path:str | Path) -> str:

    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        
        processed=[]
        for line in file:
            if not line.startswith(">"):
                processed.append(line).strip()
    
    finalSequence = processed.join('')
    
    return finalSequence




def read_fasta(file_path: str | Path) -> None:
    """Read a FASTA file and print information about each sequence."""
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            print(f"ID: {record.id}")
            print(f"Sequence: {record.seq}")
            print(f"Length: {len(record)}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Read and display a FASTA file.")
    parser.add_argument("file_path", help="Path to the FASTA file")
    args = parser.parse_args()

    read_fasta(args.file_path)


if __name__ == "__main__":
    main()
