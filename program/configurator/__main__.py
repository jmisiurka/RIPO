import streamlit as st
from program.line_drawing import draw_lines
import cv2 as cv
import tempfile
import os

def main():
    st.set_page_config(page_title='Configurator', page_icon=':camera:', layout='wide', initial_sidebar_state='auto')

    preview_file = st.file_uploader('Upload a video', type=['mp4', 'mov', 'avi', 'jpg', 'png'])

    # Main Area
    if preview_file is not None:
        st.header('Preview')
        temp_location = save_uploaded_file(preview_file)

        if preview_file.name.split('.')[-1] in ['jpg', 'png']:
            frame = cv.imread(temp_location)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = draw_lines(frame, frame.shape[1], frame.shape[0])
            st.image(frame, channels='RGB')
        else:
            capture = cv.VideoCapture(temp_location)
    
            video_view = st.empty()
    
            while capture.isOpened():
                ret, frame = capture.read()
                if not ret:
                    break
                
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                frame = draw_lines(frame, frame.shape[1], frame.shape[0])
                video_view.image(frame, channels='RGB')
    else:
        st.header('Please upload a video or image for preview of your configuration.')

    # Sidebar
    st.sidebar.header('Controls', anchor='right')
    line_spacing = st.sidebar.slider('Line Spacing', min_value=10, max_value=100, value=50)
    line_length = st.sidebar.slider('Line Length', min_value=10, max_value=100, value=50)
    # slider_val = st.sidebar.slider('Slider', min_value=0, max_value=100, value=50)
    # text_val = st.sidebar.text_input('Text Input', 'Streamlit App')

    # Display the values from the controls
    print(line_spacing)

def save_uploaded_file(uploaded_file):
    temp_location = os.path.join(tempfile.gettempdir(), uploaded_file.name)
    with open(temp_location, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return temp_location

if __name__ == '__main__':
    main()