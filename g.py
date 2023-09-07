import streamlit as st
import tldextract
from openpyxl import load_workbook

def get_similar_links(existing_links, new_links):
    existing_domains = {tldextract.extract(link).domain for link in existing_links}
    similar_existing_links = [link for link in existing_links if tldextract.extract(link).domain in existing_domains]
    return similar_existing_links

def main():
    st.title("Vikash Goyal's New Project: Find Similar Links")

    st.write("Provide existing links and new links row-wise.")
    
    existing_links_input = st.text_area("Enter existing links row-wise (one link per row)")
    new_links_input = st.text_area("Enter new links row-wise (one link per row)")

    if existing_links_input and new_links_input:
        existing_links = [link.strip() for link in existing_links_input.split("\n") if link.strip()]
        new_links = [link.strip() for link in new_links_input.split("\n") if link.strip()]
        
        similar_links = get_similar_links(existing_links, new_links)
        
        st.write("Similar Existing Links:")
        for link in similar_links:
            st.write(link)

if __name__ == "__main__":
    main()
