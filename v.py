import streamlit as st
import tldextract
from openpyxl import load_workbook

def get_unique_links(existing_links, new_links):
    existing_domains = {tldextract.extract(link).domain for link in existing_links}
    unique_new_links = [link for link in new_links if tldextract.extract(link).domain not in existing_domains]
    return unique_new_links

def main():
    st.title("Vikash Goyal's New Project: Find Links")

    st.write("Provide existing links and new links row-wise.")
    
    existing_links_input = st.text_area("Enter existing links row-wise (one link per row)")
    new_links_input = st.text_area("Enter new links row-wise (one link per row)")

    if existing_links_input and new_links_input:
        existing_links = [link.strip() for link in existing_links_input.split("\n") if link.strip()]
        new_links = [link.strip() for link in new_links_input.split("\n") if link.strip()]
        
        unique_links = get_unique_links(existing_links, new_links)
        
        st.write("Unique Links:")
        for link in unique_links:
            st.write(link)

if __name__ == "__main__":
    main()
