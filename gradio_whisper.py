# import gradio as gr
# import whisper


# def transcribe_audio(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result["text"]


# def main():
#     audio_input = gr.inputs.Audio(source="upload", type="filepath")
#     output_text = gr.outputs.Textbox()
    
#     iface = gr.Interface(fn=transcribe_audio,
                        
                        
#                          inputs=audio_input, 
#                          outputs=output_text, title="AUDIO -TEXTO",
#                          description="Subir el Audio y Presionar el botón 'SUBMIT'\
#                              ",
#                               theme='freddyaboulton/dracula_revamped',
                               
                              
#                               #theme = gr.themes.Soft(),
#                           )\
#               .launch(share=True)
    

#                             # theme='Taithrah/Minimal'
#                             #theme='rottenlittlecreature/Moon_Goblin'
                            
                          
    
#     iface.launch(share=True)


# if __name__ == '__main__':
#     main()
##################################################
# import gradio as gr
# import whisper


# def transcribe_audio(audio_file):
#     model = whisper.load_model("base")
#     result = model.transcribe(audio_file)
#     return result["text"]


# def main():
#     audio_input = gr.inputs.Audio(source="upload", type="filepath")
#     output_text = gr.outputs.Textbox()
    
#     iface = gr.Interface(fn=transcribe_audio, inputs=audio_input, 
#                          outputs=output_text, title="AUDIO -TEXTO",
#                          description="Subir el Audio y Presionar el botón 'SUBMIT'\
#                              ",
#                               #theme='freddyaboulton/dracula_revamped'
                              
#                               theme = gr.themes.Soft(),

                              
#                               css='div {background-size: cover; background-repeat: no-repeat; margin-left: auto; margin-right: auto; width: 100%;\
#             background-image: url(""); repeat 0 0;}')\
#                   .launch(share=True)

#                             # theme='Taithrah/Minimal'
#                             #theme='rottenlittlecreature/Moon_Goblin'



#     iface.launch()


# if __name__ == '__main__':
#     main()
#############################
import gradio as gr
import whisper

def convert_to_text(audio_path : str) -> str:  
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"]

audio_input = gr.components.Audio(type="filepath")
iface = gr.Interface(fn=convert_to_text, inputs=audio_input, outputs="text")
iface.launch(share=True)