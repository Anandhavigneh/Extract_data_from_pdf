#importing required modules
from pathlib import Path
import sys
from PyPDF2 import PdfReader

def find_pdf_path():
	# allow passing PDF path as the first argument
	if len(sys.argv) > 1:
		arg_path = Path(sys.argv[1])
		if arg_path.is_file():
			return arg_path
		print(f"Error: PDF file not found at {arg_path!s}", file=sys.stderr)
		sys.exit(1)

	# locate any .pdf next to this script
	script_dir = Path(__file__).parent
	candidates = list(script_dir.glob("*.pdf"))
	if candidates:
		return candidates[0]

	# fallback to current working directory
	cwd_candidates = list(Path.cwd().glob("*.pdf"))
	if cwd_candidates:
		return cwd_candidates[0]

	# no pdf found
	print(f"Error: No PDF file found in script directory ({script_dir}) or current working directory ({Path.cwd()}); pass a path as the first argument.", file=sys.stderr)
	sys.exit(1)

pdf_path = find_pdf_path()

# open the pdf file safely
try:
	with pdf_path.open("rb") as pdffileobj:
		# creating a pdf reader object
		pdfreader = PdfReader(pdffileobj)

		# printing number of pages in pdf file
		num_pages = len(pdfreader.pages)
		print(num_pages)

		if num_pages == 0:
			print("PDF has no pages.")
		else:
			# creating a page object
			pageobj = pdfreader.pages[0]

			# printing text of the page
			print(pageobj.extract_text() or "")
except Exception as e:
	print(f"Error reading PDF {pdf_path!s}: {e}", file=sys.stderr)
	sys.exit(1)
