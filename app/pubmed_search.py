from metapub import PubMedFetcher

def search_pubmed(query: str):
    fetch = PubMedFetcher()
    articles = fetch.pmids_for_query(query, retmax=10)  # Limits to 10 results
    results = []

    for pmid in articles:
        article = fetch.article_by_pmid(pmid)
        results.append({
            "title": article.title,
            "authors": article.authors,
            "journal": article.journal,
            "year": article.year,
            "doi": article.doi,
            "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"
        })

    return results
