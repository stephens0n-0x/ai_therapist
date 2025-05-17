import pygame, settings
import core.llm_client   as llm
import core.tts_client   as tts
import core.stt_client   as stt
import core.env_predict  as envp
import core.ui           as ui

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Pixel Therapist")
clock             = pygame.time.Clock()
idle, talk        = ui.load_avatar()
avatar            = idle
history           = [{"role": "system",
                      "content": open("dialogue/system_prompts.md").read()}]
input_buf, reply_text = "", "Hi, I'm Elizabeth. How are you feeling today?"
snd = tts.speak(reply_text)

def bg_colour():
    return {"Green": (30,30,40), "Amber": (60,50,20), "Red": (90,20,20)}\
           .get(envp.today().get("aqi","Green"), (30,30,40))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RETURN and input_buf.strip():
                user_msg, input_buf = input_buf, ""
            elif e.key == pygame.K_BACKSPACE:
                input_buf = input_buf[:-1]
            elif e.key == pygame.K_SPACE and settings.USE_STT:
                user_msg = stt.listen()
            else:
                input_buf += e.unicode
        else:
            user_msg = None

    if 'user_msg' in locals() and user_msg:
        history.append({"role":"user","content":user_msg})
        avatar = talk
        reply_text = llm.chat(history)
        history.append({"role":"assistant","content":reply_text})
        snd = tts.speak(reply_text)
        avatar = idle
        del user_msg

    screen.fill(bg_colour())
    screen.blit(avatar, (40,40))
    ui.draw_text(screen, reply_text, 200, 40, 700)
    ui.draw_text(screen, "> "+input_buf, 40, 460, 860)
    pygame.display.flip()

    if snd and pygame.mixer.get_busy():
        avatar = talk if pygame.time.get_ticks()//120 %2 else idle
    else:
        avatar = idle
    clock.tick(settings.FPS)

pygame.quit()
