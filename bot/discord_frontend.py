from bot.vlm_model import Model


def setup_bot(bot):
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    @bot.command()
    async def act(ctx):
        if ctx.message.attachments:
            user_input_image = ctx.message.attachments[0] 
            user_input_text = ctx.message.content[len("$image "):]  
            if user_input_image.content_type.startswith('image/'):  
                image_data = await user_input_image.read()
                vlm_model = Model()
                response_text = vlm_model.pred(image_data, user_input_text)
                await ctx.send(f"#####Model Response: {response_text}")
                #await ctx.send(f"Received image and text: {output}")
            else:
                await ctx.send("Please attach a valid image.")
        else:
            await ctx.send("No image detected. Please attach an image with your command.")
            
