import gradio as gr
import cv2
import torch
from segment_anything import SamAutomaticMaskGenerator, sam_model_registry
import sys
import os

import sys
#sys.path.append('/content/drive/MyDrive/X:AI ADV/DiffStyler')

from DiffStyler.preprocess import run_gradio
from DiffStyler.diffstyler import PNP

import os
import yaml
import subprocess

from PIL import Image
import os

# SAM 모델 초기화 함수
def init_sam_model(model_type, checkpoint, device):
    sam = sam_model_registry[model_type](checkpoint=checkpoint)
    sam.to(device=device)
    return sam

# 마스크 생성 함수
def generate_masks(image):
    model_type = "vit_h"
    checkpoint = "/content/drive/MyDrive/X:AI ADV/segment_anything/ckpt/sam_vit_h_4b8939.pth"
    device = "cuda"
    sam = init_sam_model(model_type, checkpoint, device)
    generator = SamAutomaticMaskGenerator(sam)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    masks = generator.generate(image_rgb)
    return masks  # 마스크 리스트를 그대로 반환

# 마스크 선택 및 저장 함수
def mask_selection(mask_image, masks, mask_index):
    selected_mask = masks[int(mask_index)]["segmentation"] * 255  # 선택한 마스크 이미지
    save_path = f"/content/drive/MyDrive/2024_ADV_Toy/DiffStyler/mask/selected_mask.png"
    cv2.imwrite(save_path, selected_mask.astype('uint8'))
    return f"Mask {mask_index} saved as {save_path}"

# Mask 저장
def update_gallery(image):
        masks = generate_masks(image)
        masks_state.value = masks  # 상태 변수에 마스크 저장
        mask_images = [(mask["segmentation"] * 255).astype('uint8') for mask in masks]
        return mask_images

def save_selected_mask(evt: gr.SelectData):
    mask_index = evt.index  # 사용자가 선택한 마스크의 인덱스
    mask_selection(evt.value, masks_state.value, mask_index)

# 입력 이미지 저장
def save_image(image):
    save_dir = "input"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, "uploaded_image.png")
    image_pil = Image.fromarray(image.astype('uint8'))
    image_pil.save(save_path)
    return save_path

def create_yaml_config(image_path, lora_name, mask_name):
    config = {
        'seed': 1,
        'device': 'cuda',
        'output_path': 'results/output',
        'image_path': image_path,
        'latents_path': "/content/drive/MyDrive/2024_ADV_Toy/DiffStyler/save_diff_forward",
        'sd_version': '2.1',
        'guidance_scale': 10.5,
        'n_timesteps': 50,
        'prompt': '',
        'prompt_gene': 'painting of <sss>, human',
        'lora_name': lora_name,
        'mask': mask_name,
        'negative_prompt': 'ugly, blurry, black, low res, unrealistic',
        'pnp_attn_t': 0.5,
        'pnp_f_t': 0.8
      }

    with open('/content/drive/MyDrive/2024_ADV_Toy/DiffStyler/configs/config.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(config, file)

    return "YAML configuration file created!"

def diff_live(image,style,video):
    save_path = save_image(image)
    run_gradio(save_path)
    create_yaml_config(save_path,style,'selected_mask')

    # Config
    with open('/content/drive/MyDrive/2024_ADV_Toy/DiffStyler/configs/config.yaml', "r", encoding='utf-8') as f:  # 인코딩을 명시적으로 지정
        config = yaml.safe_load(f)
    os.makedirs(config["output_path"], exist_ok=True)
    with open(os.path.join(config["output_path"], "config.yaml"), "w", encoding='utf-8') as f:  # 인코딩을 명시적으로 지정
        yaml.dump(config, f)

    # Diffstyler
    #seed_everything(config["seed"])
    print(config)
    pnp = PNP(config)
    pnp.prompt_gene_list = config['prompt_gene'].split(';')
    pnp.lora_name_list = config['lora_name'].split(';')
    pnp.mask_name_list = config['mask'].split(';')
    pnp.load_lora()
    pnp.run_pnp()

    # Liveportrait
    os.chdir('/content/drive/MyDrive/X:AI ADV/LivePortrait')
    command = f"python inference.py -s '/content/drive/MyDrive/2024_ADV_Toy/results/output/output-.png' -d '/content/drive/MyDrive/2024_ADV_Toy/LivePortrait/assets/examples/driving/{video}'"
    subprocess.run(command, shell=True)

    return 'success'

def get_generated_video_path(selected_video):
    if selected_video == "기쁨.mp4":
        return "./animations/output---기쁨.mp4"
    elif selected_video == "놀라움.mp4":
        return "./animations/output---놀라움.mp4"
    elif selected_video == "두려움.mp4":
        return "./animations/output---두려움.mp4"
    elif selected_video == "분노1.mp4":
        return "./animations/output---분노1.mp4"
    else:
        return "./animations/output---분노2.mp4"

def output_fn(image_input,style,video):
  t = diff_live(image_input,style,video)
  return get_generated_video_path(video)


with gr.Blocks() as demo:
    gr.Markdown("# 프로필 이미지 만들기")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="numpy", label="Upload Image")
        with gr.Column():
            mask_gallery = gr.Gallery(label="Generated Masks", elem_id="mask-gallery")
        with gr.Column():
            gr.Image("/content/drive/MyDrive/2024_ADV_Toy/Gradio/ADV_Gradio.png")
        with gr.Column():
            gr.Video("/content/drive/MyDrive/2024_ADV_Toy/Gradio/ADV_Gradio.mp4")
    with gr.Row():
        submit_btn = gr.Button("Generate Masks")
        generate_btn = gr.Button("Generate Profile gif")
    with gr.Row():
        style = gr.Radio(['키키','우미','정바름','카게야마','나유연','하쿠'], label="스타일을 골라주세요")
        video = gr.Radio(['기쁨.mp4','놀라움.mp4','두려움.mp4','분노1.mp4','분노2.mp4'], label="Video를 골라주세요")
    with gr.Row():
        with gr.Column():
            generated_video = gr.Video(label="Generated Video")  
    masks_state = gr.State([])  # 마스크 리스트를 저장하기 위한 상태 변수
    submit_btn.click(fn=update_gallery, inputs=[image_input], outputs=mask_gallery)
    mask_gallery.select(fn=save_selected_mask)
    generate_btn.click(fn=output_fn, inputs=[image_input,style,video], outputs=generated_video)

demo.launch(share=True)