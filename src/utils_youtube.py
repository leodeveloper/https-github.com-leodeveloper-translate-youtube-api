from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat
import os
import json


def get_youtube_transcript(video_url,src_language, target_language) -> None:
    """get youtube transcript"""
    try:

        loader = YoutubeLoader.from_youtube_url(video_url,add_video_info=True,language=[src_language, "id"],translation=target_language, transcript_format=TranscriptFormat.TEXT)
             
        #docs = loader.load_and_split(text_splitter)
        transcript = loader.load()
        
        #no transcript is found
        if len(transcript) == 0:
           return 'No transcript found', None, None
        
        #metadata = transcript[0].metadata
        
        #title = metadata.get('title')
        #metadata['transcript'] = transcript[0].page_content
        #metadata['youtubelink']=video_url
        if not transcript:
            raise ValueError(f"{src_language} transcript not available for this video.")
        else:
            return transcript[0].page_content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    