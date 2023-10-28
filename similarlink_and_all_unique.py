import streamlit as st
import tldextract
import pandas as pd

def get_similar_links(existing_links, new_link):
    existing_domains = {tldextract.extract(link).domain for link in existing_links}
    new_domain = tldextract.extract(new_link).domain
    return [link for link in existing_links if tldextract.extract(link).domain == new_domain]

def main():
    st.title("Find Similar Links")
    st.write("Developed by Vikash Goyal")
    st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/vikash-goyal-20692924b/)")
    
    st.write("Provide existing links and enter a new link.")

    existing_links_input = st.text_area("Enter existing links (one link per line)")
    new_links_input = st.text_area("Enter new links (one link per line)")

    if existing_links_input and new_links_input:
        existing_links = [link.strip() for link in existing_links_input.split("\n") if link.strip()]
        new_links = [link.strip() for link in new_links_input.split("\n") if link.strip()]
        
        if "current_link_idx" not in st.session_state:
            st.session_state.current_link_idx = 0

        if st.button("Get Unique New Links"):
            unique_new_links = list(set(new_links) - set(existing_links))
            st.write("Unique New Links:")
            st.write(unique_new_links)

        if st.session_state.current_link_idx < len(new_links):
            new_link = new_links[st.session_state.current_link_idx]
            similar_links = get_similar_links(existing_links, new_link)

            st.write(f"New Link: {new_link}")
            
            if similar_links:
                st.write("Similar Existing Links:")
                for link in similar_links:
                    st.write(link)
            
            if st.session_state.current_link_idx > 0:
                if st.button("Back"):
                    st.session_state.previous_link_idx = st.session_state.current_link_idx
                    st.session_state.current_link_idx -= 1

            if st.session_state.current_link_idx < len(new_links) - 1:
                if st.button("Next"):
                    st.session_state.previous_link_idx = st.session_state.current_link_idx
                    st.session_state.current_link_idx += 1

if __name__ == "__main__":
    main()
