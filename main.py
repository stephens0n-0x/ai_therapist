import pygame, settings
from core import llm_client, tts_client, env_predict, ui

pygame.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Pixel Therapist")
clock     = pygame.time.Clock()
idle, talk = ui.load_avatar()
avatar     = idle
history    = [{"role":"system",
               "content":open("dialogue/system_prompts.md").read()}]
input_buf  = ""
reply_text = "Hi, I'm Elizabeth. How are you feeling today?"

tts_client.speak(reply_text)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN and input_buf.strip():
                user_msg = input_buf
                history.append({"role":"user","content":user_msg})
                input_buf = ""
                avatar = talk
                reply_text = llm_client.chat(history)
                history.append({"role":"assistant","content":reply_text})
                tts_client.speak(reply_text)
                avatar = idle
            elif e.key == pygame.K_BACKSPACE:
                input_buf = input_buf[:-1]
            else:
                input_buf += e.unicode

    screen.fill(settings.BG_COLOR)
    screen.blit(avatar, (40, 40))
    ui.draw_text(screen, reply_text, 200, 40, 700)
    ui.draw_text(screen, "> " + input_buf, 40, 460, 860)
    pygame.display.flip()
    clock.tick(settings.FPS)

pygame.quit()
