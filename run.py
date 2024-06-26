#!/usr/bin/env python

import argparse

import gradio as gr

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default='User')
args, _ = parser.parse_known_args()

with gr.Blocks() as demo:
    gr.Markdown(f'# Greetings 1111 {args.name}!')
    inp = gr.Textbox()
    out = gr.Textbox()
    inp.change(fn=lambda x: x, inputs=inp, outputs=out)

demo.launch(server_name='0.0.0.0')
