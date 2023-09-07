import streamlit as st
import tldextract
from openpyxl import load_workbook

def get_similar_domains(existing_links, new_links):
    new_domains = {tldextract.extract(link).domain for link in new_links}
    similar_domains = {tldextract.extract(link).domain for link in existing_links if tldextract.extract(link).domain in new_domains}
    return similar_domains

def main():
    st.title("Vikash Goyal's New Project: Find Similar Domains")

    st.write("Provide existing links and new links row-wise.")
    
    existing_links_input = st.text_area("Enter existing links row-wise (one link per row)")
    new_links_input = st.text_area("Enter new links row-wise (one link per row)")

    if existing_links_input and new_links_input:
        existing_links = [link.strip() for link in existing_links_input.split("\n") if link.strip()]
        new_links = [link.strip() for link in new_links_input.split("\n") if link.strip()]
        
        similar_domains = get_similar_domains(existing_links, new_links)
        
        st.write("Similar Domains in Existing Links:")
        for domain in similar_domains:
            st.write(domain)

if __name__ == "__main__":
    main()
