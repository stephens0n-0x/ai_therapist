import pygame, settings
import core.llm_client   as llm
import core.tts_client   as tts
import core.stt_client   as stt
import core.env_predict  as envp
import core.ui           as ui
import traceback, time

# ------------------------- Pygame init -------------------------
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption("Pixel Therapist – SPACE‑to‑talk build")
clock = pygame.time.Clock()

idle_img, talk_img = ui.load_avatar()
avatar = idle_img

# ------------------------- Dialogue state ----------------------
history = [{
    "role": "system",
    "content": open("dialogue/system_prompts.md", encoding="utf-8").read()
}]

input_buf  = ""
reply_text = "Hi, I'm Elizabeth. Hold SPACE, talk, release to send."
print("[BOOT] Speaking intro line …")
snd = tts.speak(reply_text)
if not snd:
    print("[WARN] Intro TTS returned None – check TTS config")

# ------------------------- Helpers -----------------------------

def bg_colour():
    palette = {
        "Green": (30, 30, 40),
        "Amber": (60, 50, 20),
        "Red":   (90, 20, 20),
    }
    return palette.get(envp.today().get("aqi", "Green"), (30, 30, 40))


# ------------------------- Main loop ---------------------------
print("[BOOT] Entering main loop …")
running       = True
capturing     = False   # True while SPACE is held
captured_text = ""       # interim transcript (unused for single‑shot)

while running:
    user_msg = None

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

        # ------------- keyboard text entry -------------
        elif e.type == pygame.KEYDOWN and not capturing:
            if e.key == pygame.K_RETURN and input_buf.strip():
                user_msg, input_buf = input_buf, ""
            elif e.key == pygame.K_BACKSPACE:
                input_buf = input_buf[:-1]
            elif 32 <= e.key < 127:  # printable range
                input_buf += e.unicode

        # ------------- voice capture with SPACE -------------
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and settings.USE_STT:
            capturing = True            # start capture when space pressed
            print("[STT] Capture started – hold SPACE and speak …")

        if e.type == pygame.KEYUP and e.key == pygame.K_SPACE and capturing:
            capturing = False           # released → run STT once
            print("[STT] Processing …")
            user_msg = stt.listen()
            print("[STT] Result:", user_msg)

    # ---- handle a completed user message ----
    if user_msg:
        history.append({"role": "user", "content": user_msg})
        avatar = talk_img

        try:
            t0 = time.time()
            print("[LLM] Sending →", user_msg)
            reply_text = llm.chat(history)
            print(f"[LLM] Reply in {time.time()-t0:.2f}s →", reply_text)
        except Exception:
            print("[ERR] LLM failed:\n", traceback.format_exc())
            reply_text = "Sorry, I couldn't think of a response right now."

        history.append({"role": "assistant", "content": reply_text})

        try:
            print("[TTS] Speaking …")
            snd = tts.speak(reply_text)
            if snd is None:
                print("[WARN] TTS returned None – silent reply")
        except Exception:
            print("[ERR] TTS failed:\n", traceback.format_exc())
            snd = None
        avatar = idle_img

    # ---- draw frame ----
    screen.fill(bg_colour())
    screen.blit(avatar, (40, 40))
    ui.draw_text(screen, reply_text, 200, 40, 700)
    ui.draw_text(screen, "> "+input_buf, 40, 460, 860)
    ui.draw_text(screen, "Hold SPACE to speak", 40, 500, 860)
    pygame.display.flip()

    # mouth animation while sound plays
    if snd and pygame.mixer.get_busy():
        avatar = talk_img if (pygame.time.get_ticks() // 120) % 2 else idle_img
    else:
        avatar = idle_img

    clock.tick(settings.FPS)

pygame.quit()
print("[BOOT] Graceful shutdown")
