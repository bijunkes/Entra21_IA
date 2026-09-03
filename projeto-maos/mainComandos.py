import cv2
import mediapipe as mp
import pyautogui
import subprocess
import time


# ==========================================
# CONFIGURAÇÕES
# ==========================================

COOLDOWN = 1.0
TEMPO_DESLIGAMENTO = 2.0


# ==========================================
# MEDIAPIPE
# ==========================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


# ==========================================
# CONTROLE DE AÇÕES
# ==========================================

ultimo_comando = None
ultimo_tempo = 0

desligamento_iniciado = False
inicio_desligamento = None


# ==========================================
# CÂMERA
# ==========================================

camera = cv2.VideoCapture(0)


while True:

    sucesso, frame = camera.read()

    if not sucesso:
        print("Erro ao acessar a câmera.")
        break

    # Espelha a câmera
    frame = cv2.flip(frame, 1)

    # OpenCV usa BGR
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    resultado = hands.process(rgb)

    polegar = False
    indicador = False
    medio = False
    anelar = False
    mindinho = False

    # ==========================================
    # DETECTAR MÃO
    # ==========================================

    if resultado.multi_hand_landmarks:

        hand = resultado.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        pontos = hand.landmark

        # --------------------------------------
        # POLEGAR
        # --------------------------------------
        #
        # Compara a posição horizontal.
        # Funciona para a mão direita.
        #

        if pontos[4].x < pontos[3].x:
            polegar = True

        # --------------------------------------
        # INDICADOR
        # --------------------------------------

        if pontos[8].y < pontos[6].y:
            indicador = True

        # --------------------------------------
        # MÉDIO
        # --------------------------------------

        if pontos[12].y < pontos[10].y:
            medio = True

        # --------------------------------------
        # ANELAR
        # --------------------------------------

        if pontos[16].y < pontos[14].y:
            anelar = True

        # --------------------------------------
        # MINDINHO
        # --------------------------------------

        if pontos[20].y < pontos[18].y:
            mindinho = True


    # ==========================================
    # EXIBIR ESTADO DOS DEDOS
    # ==========================================

    cv2.putText(
        frame,
        f"Polegar: {'SIM' if polegar else 'NAO'}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0) if polegar else (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Indicador: {'SIM' if indicador else 'NAO'}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0) if indicador else (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        f"Mindinho: {'SIM' if mindinho else 'NAO'}",
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0) if mindinho else (0, 0, 255),
        2
    )


    # ==========================================
    # TEMPO
    # ==========================================

    agora = time.time()


    # ==========================================
    # POLEGAR → AUMENTAR VOLUME
    # ==========================================

    if polegar and not indicador and not mindinho:

        if (
            ultimo_comando != "aumentar"
            and agora - ultimo_tempo > COOLDOWN
        ):

            pyautogui.press("volumeup")

            print("🔊 Aumentando volume")

            ultimo_comando = "aumentar"
            ultimo_tempo = agora


    # ==========================================
    # INDICADOR → DIMINUIR VOLUME
    # ==========================================

    elif indicador and not polegar and not mindinho:

        if (
            ultimo_comando != "diminuir"
            and agora - ultimo_tempo > COOLDOWN
        ):

            pyautogui.press("volumedown")

            print("🔉 Diminuindo volume")

            ultimo_comando = "diminuir"
            ultimo_tempo = agora


    # ==========================================
    # MINDINHO → DESLIGAR
    # ==========================================

    elif mindinho and not polegar and not indicador:

        if not desligamento_iniciado:

            desligamento_iniciado = True
            inicio_desligamento = agora

            print("⚠️ Desligamento iniciado...")

        else:

            tempo_passado = agora - inicio_desligamento

            restante = TEMPO_DESLIGAMENTO - tempo_passado

            cv2.putText(
                frame,
                f"DESLIGANDO EM {max(0, restante):.1f}s",
                (20, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

            if tempo_passado >= TEMPO_DESLIGAMENTO:

                print("💻 Desligando computador...")

                subprocess.run(
                    ["shutdown", "/s", "/t", "0"]
                )

                break

    else:

        # Se tirar o mindinho antes dos 2 segundos,
        # cancela o desligamento.

        if desligamento_iniciado:

            print("❌ Desligamento cancelado.")

        desligamento_iniciado = False
        inicio_desligamento = None


    # ==========================================
    # INSTRUÇÃO
    # ==========================================

    cv2.putText(
        frame,
        "Q = sair",
        (20, frame.shape[0] - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )


    # ==========================================
    # MOSTRAR CÂMERA
    # ==========================================

    cv2.imshow(
        "Controle por Gestos",
        frame
    )


    # ==========================================
    # SAIR
    # ==========================================

    tecla = cv2.waitKey(1) & 0xFF

    if tecla == ord("q"):
        break


# ==========================================
# ENCERRAR
# ==========================================

camera.release()
cv2.destroyAllWindows()
hands.close()