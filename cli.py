import argparse
from pubmed_fetcher.fetcher import PubMedFetcher

# Command-line interface
def main():
    """Handles user input, fetches papers, and saves/prints results."""
    parser = argparse.ArgumentParser(description="Fetch PubMed research papers.")
    parser.add_argument("query", type=str, help="PubMed search query.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode.")
    
    args = parser.parse_args()
    
    # Fetch paper IDs from PubMed
    paper_ids = PubMedFetcher.fetch_pubmed_papers(args.query)
    
    if args.debug:
        print(f"Fetched Paper IDs: {paper_ids}")
    
    # Fetch details for each paper
    results = [PubMedFetcher.get_paper_details(pid) for pid in paper_ids]
    
    # Save to CSV or print to console
    if args.file:
        PubMedFetcher.save_to_csv(results, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in results:
            print(paper)

if __name__ == "__main__":
    main()
