import streamlit as st
from ultralytics import YOLO

import os
from PIL import Image

from streamlit_webrtc import webrtc_streamer
import av

IMG_PATH = "./images"
model = YOLO("yolo11n.pt")


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    inference_results = infer(img)
    for result in inference_results:
        annotated = result.plot()
        annotated_rgb = annotated[:, :, ::-1]

    return av.VideoFrame.from_ndarray(annotated_rgb, format="rgb24")


def show_camera():
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback)


def infer(image_path):
    results = model(image_path)
    return results


def upload(IMG_PATH):
    file = st.file_uploader("推論する画像をアップロードしてください.", type=["jpg", "jpeg", "png"])
    if file:
        st.markdown(f"{file.name} をアップロードしました.")
        img_path = os.path.join(IMG_PATH, file.name)

        with open(img_path, "wb") as f:
            f.write(file.read())

        img = Image.open(img_path)
        st.image(img)

        inference_results = infer(img_path)

        for result in inference_results:
            annotated = result.plot()
            annotated_rgb = annotated[:, :, ::-1]
            st.image(annotated_rgb, caption="推論結果")


def main():
    st.title("Streamlit YOLO Inference App")

    # 画像保存先のディレクトリが存在しない場合は作成
    if not os.path.exists(IMG_PATH):
        os.makedirs(IMG_PATH)

    upload(IMG_PATH)
    show_camera()


if __name__ == "__main__":
    main()
