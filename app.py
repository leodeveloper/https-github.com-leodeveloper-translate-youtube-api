import os
import streamlit as st
from src.utils_json import get_json
from src.utils_dycrypt import decrypt_string
from src.utils_method import get_query_params
from src.utils_youtube import get_youtube_transcript

from dotenv import load_dotenv
load_dotenv()

key=os.getenv("encryptkey")



# Main function to run the app
def main() -> None:
    query_params = get_query_params()
    if query_params:
        if st.query_params["source"] is not None:
            sourceId = st.query_params["source"]
            st.title("Translation")
            response = get_json(sourceId)
            if response is not None:
                source = decrypt_string(response.get('source'),key)
                title = response.get('title'),key
                thumbnail_url = decrypt_string(response.get('thumbnail_url'),key)
                publish_date = response.get('publish_date')
                youtubelink = decrypt_string(response.get('youtubelink'),key)
                # Print the values
                st.write(f"Title: {title}")
                st.write(f"Thumbnail URL: {thumbnail_url}")
                st.write(f"Publish Date: {publish_date}")
                st.write(f"YouTube Link: {youtubelink}")

                with st.spinner("Please wait......"):
                    transur = get_youtube_transcript(youtubelink,'en','en')
                    st.write(transur)
                    transur = get_youtube_transcript(youtubelink,'en','ur')
                    st.write(transur)

            else:
                st.write("No response from API")
        else:
            st.write("No source query parameters found.")
    else:
        st.write("No query parameters found.")

if __name__ == "__main__":
    main()
