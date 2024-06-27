import os
import json
import streamlit as st
from src.utils_json import get_json
from src.utils_fileid import get_json_drive
from src.utils_dycrypt import decrypt_string
from src.utils_method import get_query_params
from readfromgoogledrive import getfilefromdrive

from dotenv import load_dotenv
load_dotenv()

key=os.getenv("encryptkey")

mystyle = '''
    <style>
        p {
            text-align: right;
        }
    </style>
    '''

#st.markdown(mystyle, unsafe_allow_html=True)

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
                title = response.get('title')
                thumbnail_url = decrypt_string(response.get('thumbnail_url'),key)
                publish_date = response.get('publish_date')
                # Print the values
                st.markdown(f"Title: {title}",  unsafe_allow_html=True)
                st.image(thumbnail_url,caption=None, width=200, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                st.write(f"Publish Date: {publish_date}")
                
                with st.spinner("Please wait......"):
                    fileidobj = get_json_drive(source)
                    st.write("<a href='#italian'>Italian</a> | <a href='#english'>English</a> | <a href='#urdu'>Urdu</a> | <a href='#arabic'>Arabic</a> | <a href='#spanish'>Spanish</a>", unsafe_allow_html=True)
                    
                    #print(fileidobj['id'])
                    #if fileidobj:
                        #file id is used for google drive file id
                    translation = getfilefromdrive('',source)
                    if translation:
                        translation = json.loads(translation)
                        st.title("English")
                        st.markdown(f"<div style='text-align: left;'>{translation['t_english']}</div>", unsafe_allow_html=True)
                        st.title("Urdu")
                        st.markdown("<a href='#translation'>Top</a>", unsafe_allow_html=True)
                        st.markdown(f"<div style='text-align: right;'>{translation['t_urdu']}</div>", unsafe_allow_html=True)
                        st.title("Arabic")
                        st.markdown("<a href='#translation'>Top</a>", unsafe_allow_html=True)
                        st.markdown(f"<div style='text-align: right;'>{translation['t_arabic']}</div>", unsafe_allow_html=True)
                        st.title("Spanish")
                        st.markdown("<a href='#translation'>Top</a>", unsafe_allow_html=True)
                        st.markdown(f"<div style='text-align: left;'>{translation['t_spanish']}</div>", unsafe_allow_html=True)
                        st.title("Italian")
                        st.markdown("<a href='#translation'>Top</a>", unsafe_allow_html=True)
                        st.markdown(f"<div style='text-align: left;'>{translation['t_italian']}</div>", unsafe_allow_html=True)
                    else:
                        st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
                    #else:
                        #st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
                    

            else:
                st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
        else:
            st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
    else:
        st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")

if __name__ == "__main__":
    main()
