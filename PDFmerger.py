from PyPDF2 import PdfFileReader, PdfFileMerger
from pathlib import Path
from argparse import ArgumentParser
from tqdm import tqdm


def main():
    parser = ArgumentParser(description="PDF File Merger")

    parser.add_argument(
        "path", help="Enter the path of the file containing the PDF documents"
    )
    parser.add_argument(
        "--output",
        help="Enter the name of the output document",
        default="mergedfiles.pdf",
    )

    args = parser.parse_args()

    path = Path(args.path)
    output = ensure_suffix(args.output)
    files = [filename for filename in path.iterdir() if filename.suffix == ".pdf"]

    print("\n=================================")
    print("======== PDF FILE MERGER ========")
    print("=================================\n")

    print("FILENAMES:")

    for filename in files:
        print("- {}".format(filename.name))

    print("\nNUMBER OF FILES: {}".format(len(files)))
    print("DESTINATION: '{}'".format(str(path)))
    print("OUTPUT NAME: '{}'\n".format(str(output)))

    merged = merge_files(files)

    print("~ Writing to PDF")
    merged.write(str(path / output))

    print("\nDone!\n")


def ensure_suffix(output: str):
    # if the PDF extension is not specified, add it to the output arg
    if output[-4:].lower() != ".pdf":
        output += ".pdf"
    return output


def merge_files(files: [Path]):
    merged = PdfFileMerger()
    for filename in tqdm(files, desc="~ Merging your files"):
        merged.append(PdfFileReader(str(filename)))
    return merged


if __name__ == "__main__":
    main()
