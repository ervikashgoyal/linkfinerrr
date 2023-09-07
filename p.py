import streamlit as st
import tldextract

def get_similar_links(existing_links, new_link):
    existing_domains = {tldextract.extract(link).domain for link in existing_links}
    new_domain = tldextract.extract(new_link).domain
    return [link for link in existing_links if tldextract.extract(link).domain == new_domain]

def main():
    st.title("Find Similar Links")

    st.write("Provide existing links and enter a new link.")
    
    existing_links_input = st.text_area("Enter existing links (one link per line)")
    new_links_input = st.text_area("Enter new links (one link per line)")

    if existing_links_input and new_links_input:
        existing_links = [link.strip() for link in existing_links_input.split("\n") if link.strip()]
        new_links = [link.strip() for link in new_links_input.split("\n") if link.strip()]
        
        if "current_link_idx" not in st.session_state:
            st.session_state.current_link_idx = 0
        
        if st.session_state.current_link_idx < len(new_links):
            new_link = new_links[st.session_state.current_link_idx]
            similar_links = get_similar_links(existing_links, new_link)
            
            st.write(f"New Link: {new_link}")
            st.write("Similar Existing Links:")
            for link in similar_links:
                st.write(link)
            
            st.session_state.current_link_idx += 1
            if st.session_state.current_link_idx < len(new_links):
                st.button("Next")

if __name__ == "__main__":
    main()
