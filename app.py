import streamlit as st
import pandas as pd
from urllib.parse import urlparse

# Load existing links from an Excel file
existing_links_file = "existing_links.xlsx"
try:
    df_existing = pd.read_excel(existing_links_file)
except FileNotFoundError:
    df_existing = pd.DataFrame(columns=["Link"])

# Streamlit app header
st.title("Link Deduplicator")

# Input box for pasting links
st.subheader("Paste your links here (one per line):")
links_input = st.text_area("Links", "", height=200)

# Function to extract and deduplicate links
def extract_and_deduplicate_links(links_input):
    new_links = links_input.split('\n')
    new_domains = set()
    unique_new_links = []

    for link in new_links:
        if link.strip():
            parsed_url = urlparse(link)
            domain = parsed_url.netloc
            if domain not in df_existing["Link"] and domain not in new_domains:
                new_domains.add(domain)
                unique_new_links.append(link)

    return unique_new_links

if st.button("Process Links"):
    unique_new_links = extract_and_deduplicate_links(links_input)
    
    # Append unique new links to the existing DataFrame
    df_new = pd.DataFrame({'Link': unique_new_links})
    df_updated = pd.concat([df_existing, df_new], ignore_index=True)

    # Save the updated Excel file
    df_updated.to_excel(existing_links_file, index=False)

    st.success(f"Processed {len(unique_new_links)} unique links!")

# Display the existing links
st.subheader("Existing Links:")
st.write(df_existing)

# Download the updated Excel file
st.subheader("Download Updated Excel File:")
st.download_button(
    label="Download Updated Links",
    data=df_updated.to_excel(None, index=False),
    key="download-link"
)

# Note: You can customize the appearance and layout of the Streamlit app as per your preferences.
