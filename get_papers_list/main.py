import argparse
import sys
from get_papers_list.fetcher import fetch_pubmed_ids, fetch_article_details
from get_papers_list.writer import save_to_csv

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch research papers based on query and save to CSV.")
    parser.add_argument("query", type=str, help="Query string for PubMed search.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename.")

    args = parser.parse_args()

    try:
        pubmed_ids = fetch_pubmed_ids(args.query, args.debug)
        if not pubmed_ids:
            print("No articles found for the given query.")
            return

        results = fetch_article_details(pubmed_ids, args.debug)
        if not results:
            print("No papers found with pharma/biotech-affiliated authors.")
            return

        save_to_csv(results, args.file)
        print(f"Results saved to {args.file}")

    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
