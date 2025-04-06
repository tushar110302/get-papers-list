import xml.etree.ElementTree as ET
from typing import List, Dict
from Bio import Entrez
from get_papers_list.utils import is_non_academic, is_pharma_or_biotech, extract_email, clean_affiliation

Entrez.email = "your.email@example.com"  # Replace with your email

def fetch_pubmed_ids(query: str, debug: bool) -> List[str]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=1000)
    record = Entrez.read(handle)
    handle.close()
    if debug:
        print(f"[DEBUG] Found {record['Count']} articles for query.")
    return record["IdList"]

def fetch_article_details(pubmed_ids: List[str], debug: bool) -> List[Dict[str, str]]:
    handle = Entrez.efetch(db="pubmed", id=",".join(pubmed_ids), retmode="xml")
    root = ET.parse(handle).getroot()
    handle.close()

    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle", default="N/A")
        pubdate = article.findtext(".//PubDate/Year") or article.findtext(".//PubDate/MedlineDate", default="N/A")

        non_academic_authors = []
        company_affiliations = []

        for author in article.findall(".//AuthorList/Author"):
            lastname = author.findtext("LastName") or ""
            forename = author.findtext("ForeName") or ""
            fullname = f"{forename} {lastname}".strip()

            for affiliation in author.findall(".//AffiliationInfo/Affiliation"):
                aff_text = affiliation.text or ""
                aff_text = clean_affiliation(aff_text) or ""
                email = extract_email(affiliation.text or "")

                if is_non_academic(aff_text) and is_pharma_or_biotech(aff_text) and email:
                    non_academic_authors.append(fullname)
                    company_affiliations.append(aff_text)
                    corresponding_email = email

        if non_academic_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pubdate,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": corresponding_email or "N/A",
            })

    return results