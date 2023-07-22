from src.utils.all_utils import read_yaml, create_directory
import streamlit as st
import os
import base64
from PIL import Image
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
from sklearn.neighbors import NearestNeighbors
from numpy.linalg import norm



config = read_yaml('config/config.yaml')
params = read_yaml('params.yaml')

artifacts = config['artifacts']
artifacts_dir = artifacts['artifacts_dir']

#upload
upload_image_dir = artifacts['upload_image_dir']
uploadn_path = os.path.join(artifacts_dir, upload_image_dir)

# pickle_format_data_dir
pickle_format_data_dir = artifacts['pickle_format_data_dir']
img_pickle_file_name = artifacts['img_pickle_file_name']

raw_local_dir_path = os.path.join(artifacts_dir, pickle_format_data_dir)
pickle_file = os.path.join(raw_local_dir_path, img_pickle_file_name)

#Feature path
feature_extraction_dir = artifacts['feature_extraction_dir']
extracted_features_name = artifacts['extracted_features_name']

feature_extraction_path = os.path.join(artifacts_dir, feature_extraction_dir)
features_name = os.path.join(feature_extraction_path, extracted_features_name)

#params_path
weight = params['base']['weights']
include_tops = params['base']['include_top']

#loading
feature_list = np.array(pickle.load(open(features_name,'rb')))
filenames = pickle.load(open(pickle_file,'rb'))


#model
model = ResNet50(weights= weight,include_top=include_tops,input_shape=(224,224,3))
model.trainable = False

model = tf.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

# print(model.summary())

# Custom CSS style for changing the font
custom_css = """
<style>
body {
    font-family: 'Arial', sans-serif;
    color: black;
    background-color: black
}
h1 {
    font-family: 'Helvetica', sans-serif;
    font-size: 36px;
    color: black;
}
</style>
"""
page_bg_img = '''
<style>
body {
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf_Qg0e_Y2-S-QoQT_JMmic1aYDJacpYLgxg&usqp=CAU");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Display the custom CSS style using Markdown
st.markdown(custom_css, unsafe_allow_html=True)

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack("bg6.png")

st.title('Fashion Dopplefinder : Discover similar fashion picks!')

def save_uploaded_file(uploaded_file):
    try:
        create_directory(dirs=[uploadn_path])
        with open(os.path.join(uploadn_path,uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1
    except:
        return 0


def feature_extraction(img_path,model):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result


def recommend(features,feature_list):
    neighbors = NearestNeighbors(n_neighbors=6, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)

    distances, indices = neighbors.kneighbors([features])

    return indices

# steps
# file upload -> save
uploaded_file = st.file_uploader("Choose an image")
if uploaded_file is not None:
    if save_uploaded_file(uploaded_file):
        # display the file
        display_image = Image.open(uploaded_file)
        st.image(display_image)
        # feature extract
        features = feature_extraction(os.path.join(uploadn_path,uploaded_file.name),model)
        # recommendention
        indices = recommend(features,feature_list)
        # show
        col1,col2,col3,col4,col5 = st.columns(5)

        with col1:
            st.image(filenames[indices[0][0]])
        with col2:
            st.image(filenames[indices[0][1]])
        with col3:
            st.image(filenames[indices[0][2]])
        with col4:
            st.image(filenames[indices[0][3]])
        with col5:
            st.image(filenames[indices[0][4]])
    else:
        st.header("Some error occured in file upload")
