import json
import streamlit as st
from program.line_drawing import draw_lines_with_settings
import cv2 as cv
import tempfile
import os

try:
    with open('settings.json', 'r') as f:
        settings = json.load(f)
except FileNotFoundError:
    settings = {
            'line_spacing': .3,
            'line_length': .4,
            'width': 640,
            'height': 480,
            'recognized_items': {'cars': True, 'railings': True, 'poles': True, 'curbs': True},
        }


def app():
    st.set_page_config(page_title='Configurator', page_icon=':camera:', layout='wide', initial_sidebar_state='auto')

    # Sidebar
    st.sidebar.header('Video settings', anchor='right')
    width_input = st.sidebar.empty()
    height_input = st.sidebar.empty()

    settings['width'] = width_input.number_input('Width', min_value=100, max_value=1920, value=settings['width'], key='width_input_initial')
    settings['height'] = height_input.number_input('Height', min_value=100, max_value=1080, value=settings['height'], key='height_input_initial')

    st.sidebar.header('Line settings', anchor='right')
    settings['line_spacing'] = st.sidebar.slider('Line spacing', min_value=0.1, max_value=1.0, value=settings['line_spacing'], step=0.01)
    settings['line_length'] = st.sidebar.slider('Line length', min_value=0.1, max_value=1.0, value=settings['line_length'], step=0.01)

    st.sidebar.header('Recognized items', anchor='right')
    st.sidebar.checkbox('Cars', value=settings['recognized_items']['cars'])
    st.sidebar.checkbox('Railings', value=settings['recognized_items']['railings'])
    st.sidebar.checkbox('Poles', value=settings['recognized_items']['poles'])
    st.sidebar.checkbox('Curbs', value=settings['recognized_items']['curbs'])

    st.sidebar.header('Save configuration', anchor='right')
    st.sidebar.button('Save configuration', on_click=save_config)

    # Main Area
    main_header = st.empty()
    preview_window = st.empty()
    preview_file = st.file_uploader('Upload a video or image', type=['mp4', 'mov', 'avi', 'jpg', 'png'])
    st.write('or', anchor='center')
    st.button('Use webcam (not supported yet)')

    if preview_file is not None:
        main_header.header('Preview')
        temp_location = save_uploaded_file(preview_file)

        if preview_file.name.split('.')[-1] in ['jpg', 'png']:
            frame = cv.imread(temp_location)
            settings['width'] = frame.shape[1]
            settings['height'] = frame.shape[0]
            settings['width'] = width_input.number_input('Width', min_value=100, max_value=1920, value=settings['width'], key='width_input')
            settings['height'] = height_input.number_input('Height', min_value=100, max_value=1080, value=settings['height'], key='height_input')
            
            st.write(f'Image size: {settings["width"]}x{settings["height"]}')

            frame = draw_lines_with_settings(frame, settings)
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            preview_window.image(frame, channels='RGB')
        else:
            capture = cv.VideoCapture(temp_location)
            settings['width'] = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
            settings['height'] = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
            settings['width'] = width_input.number_input('Width', min_value=100, max_value=1920, value=settings['width'], key='width_input')
            settings['height'] = height_input.number_input('Height', min_value=100, max_value=1080, value=settings['height'], key='height_input')
            
            st.write(f'Video size: {settings["width"]}x{settings["height"]}')

            # video_view = st.empty()
    
            while capture.isOpened():
                ret, frame = capture.read()
                if not ret:
                    capture.set(cv.CAP_PROP_POS_FRAMES, 0)
                else:
                    frame = cv.resize(frame, (settings['width'], settings['height']))
                    frame = draw_lines_with_settings(frame, settings)
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                    preview_window.image(frame, channels='RGB')
    else:
        main_header.header('Please upload a video or image to preview your configuration.')

def save_uploaded_file(uploaded_file):
    temp_location = os.path.join(tempfile.gettempdir(), uploaded_file.name)
    with open(temp_location, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return temp_location

def save_config():
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

app()