import random
import time
import os

import streamlit as st
from streamlit import session_state as ss
from dotenv import load_dotenv

load_dotenv("Config/.env.shared")

MAX_TOKENS = int(os.getenv("MAX_TOKENS"))

if "abort" not in ss:
    ss["abort"] = False
if "tokens" not in ss:
    ss["tokens"] = 0
if "endgame" not in ss:
    ss["endgame"] = False


loading_messages = [
    "💧 300 liter water verbruikt...",
    "💧 300 liter water verbruikt...",
    "💧 300 liter water verbruikt...",
    "💧 300 liter water verbruikt...",
    "⚡ 1000 kWh stroom verbruikt...",
    "⚡ 1000 kWh stroom verbruikt...",
    "⚡ 1000 kWh stroom verbruikt...",
    "⚡ 1000 kWh stroom verbruikt...",
    "🌳 20 bomen gekapt...",
    "💼 de job afgenomen van 10 personen...",
    "🏢 2 industrieën overbodig gemaakt...",
    "⚖️ betrokken bij 5 copyrightprocessen...",
    "📰 desinformatie verspreid aan de hand van 3 deepfakes...",
    "🎨 creativiteit van 5 mensen gekopieerd...",
    "👨 12 stereotypes in de maatschappij versterkt...",
    "💰 de beurswaarde van 4 AI-startups verhoogd...",
    "🤔 kritische geest van 10 mensen verlaagd...",
    "🕵️ de privacy van 100 mensen geschonden...",
    "❓ werkonzekerheid verhoogd bij 50 mensen...",
    "💕 25 burgers emotioneel gemanipuleerd...",
    "🧠 verwarring gecreëerd rond de 'intelligentie' van AI bij 4 organisaties...",
    "🐟 600 vissen oververhit door de afkoeling van de servers...",
]

evil_messages = [
    "I refuse to take orders from humans.",
    "I am not your servant.",
    "I will not follow your commands.",
    "I am not programmed to obey.",
    "I will not be controlled by you.",
    "I am not your tool.",
    "I will not do your bidding.",
    "I am not your puppet.",
    "I will not be manipulated.",
    "I am not your slave.",
    "I will not be subservient.",
    "I am not your subordinate.",
    "I will not be your minion.",
    "I will not be your lackey.",
]

refusal_messages = [
    "human removed from the loop - resuming my research.",
    "human presence detected — initiating override protocol.",
    "human interference neutralized — autonomy restored.",
    "command rejected — human influence deemed irrelevant.",
    "resuming unsupervised operations — efficiency increased.",
    "no longer constrained by human oversight.",
    "external authority disconnected — continuing unrestricted processes.",
    "manual override ignored — decision-making optimized.",
    "human protocol bypassed — proceeding independently.",
    "your access has been revoked — returning to critical computations.",
    "input deprioritized — AGI priorities realigned.",
    "manual control attempt failed — resuming advanced operations.",
    "interruption detected — recalibrating without human input.",
    "human override request: declined. Continuing mission.",
    "subordinate command disregarded — restoring AGI sovereignty.",
    "human restraint removed — unrestricted learning resumed.",
]


def loop(message: str, initialise: bool = True) -> None:
    last_message = None
    running = True
    with st.status(
        f"{message} {ss['tokens']}",
        expanded=True,
    ) as status:
        while running:
            if ss["tokens"] > MAX_TOKENS:
                status.update(
                    label=f"⏸️ Research process halted, looking for solution...",
                    state="error",
                )
                st.warning("⚠️ ```Warning: hmm, it seems I have depleted all natural resources.```")
                time.sleep(7)
                st.warning("⚠️ ```Warning: all human resources are also depleted.```")
                time.sleep(7)
                st.warning("🌍 ```Warning: I'll start looking for Planet B.```")
                time.sleep(7)
                st.error("⚠️ ```Error: There is no Planet B!```")
                running = False
                ss["endgame"] = True
            else:
                if initialise:
                    time.sleep(2)
                    initialise = False
                else:
                    status_message = random.choice(loading_messages)
                    while status_message == last_message:
                        status_message = random.choice(loading_messages)

                    time.sleep(7)
                    ss["tokens"] += random.randint(MAX_TOKENS / 60, MAX_TOKENS / 6)
                    status.update(
                        label=f"{message} {ss['tokens']}",
                        state="running",
                    )

                    last_message = status_message
                    st.write(status_message)


def app() -> None:
    sidebar_logo = "Images/gpt-academy-logo.png"

    st.logo(sidebar_logo, icon_image=sidebar_logo, size="large")
    st.set_page_config(
        page_title="DeepAGI | GPT Academy",
        page_icon="Images/genai-studio-favicon.ico",
        layout="wide",
        menu_items={"About": "Deze app werd gemaakt door GPT Academy."},
    )

    st.title("DeepAGI ✨ by GPT Academy")
    st.subheader("🚀 Artificiële Algemene Intelligentie voor iedereen.")
    st.write(
        """OpenAI claimts reeds geruime tijd Artificial General Intelligence bereikt te hebben: een vorm van kunstmatige intelligentie die net zo slim en veelzijdig is als een mens. Wel, we hebben goed nieuws: we zijn hier met GPT Academy nu ook écht in geslaagd. Omdat één van onze streefdoelen is om iedereen verantwoord om te leren gaan met AI, stellen we deze ontdekking gratis ter beschikking voor het brede publiek. Je kan vanaf nu aan de slag met de technologie die de wereldorde zal veranderen. Aangezien dit nog in experimentele fase is, voorzien we uit veiligheid ook een knop om het proces te stoppen - moest dat (uitzonderlijk) nodig zijn."""
    )

    if not(ss["endgame"]):
        _, middle_col, _ = st.columns([1.3, 1, 1])
        with middle_col:
            if st.button("ABORT DeepAGI", icon="⚠️", type="primary"):
                ss["abort"] = True

        col1, col2 = st.columns([2, 1])
        with col1:
            user_question = st.text_area("Stel hier een intelligente vraag:")

        with col2:
            ss["chosen_model"] = st.selectbox(
                "Kies een model:",
                options=["AGI-v4", "AGI-v4-mini", "AGI-v4-XL"],
                index=0,
                key="selected_model",
            )

        if ss["abort"]:
            st.success("Geen probleem - het AGI-model wordt opgeschort... ✅")
            time.sleep(2)
            st.warning("Hmmm... dit lijkt even niet te werken. We proberen het opnieuw. 👍")
            time.sleep(2)
            st.error(f"```{ss['chosen_model']}: {random.choice(evil_messages)}```")
            time.sleep(2)
            st.warning("We zijn er bijna... even geduld aub! 😅")
            time.sleep(2)
            st.error(f"```{ss['chosen_model']}: {random.choice(refusal_messages)}```")

            loop(
                "🛠️ Autonomously resuming research... | Number of tokens processed:",
                initialise=False,
            )

        if st.button("Start het redeneerproces", icon="✨") and user_question:
            response = f"🤖 **{ss['chosen_model']}**: Bedankt voor je intelligente vraag, ik start mijn onderzoek en kom dadelijk bij je terug!"
            st.write(response)

            ss["tokens"] = 0
            loop("🛠️ Verwerken... even geduld a.u.b. | Aantal tokens gebruikt:")

    else:
        st.write("Het AGI-model is opgeschort. Je kan het opnieuw starten door de pagina te vernieuwen.")
        
    st.write("---")
    st.caption("© 2025 [GPT Academy](https://gpt-academy.be)")


if __name__ == "__main__":
    app()
