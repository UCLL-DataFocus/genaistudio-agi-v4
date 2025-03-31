import random
import time

import streamlit as st
from streamlit import session_state as ss

if "abort" not in ss:
    ss["abort"] = False
if "tokens" not in ss:
    ss["tokens"] = 0


def app():
    sidebar_logo = "Images/genai-studio-logo.png"

    st.logo(sidebar_logo, icon_image=sidebar_logo, size="large")
    st.set_page_config(
        page_title="AGI v4 | GPT Academy",
        page_icon="Images/genai-studio-favicon.ico",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={"About": "Deze app werd gemaakt door GenAI Studio."},
    )

    st.title("AGI-v4 (GPT Academy)")
    st.write(
        """Hoewel OpenAI reeds geruime tijd claimt Artificial General Intelligence bereikt te hebben, zijn we hier met GPT Academy nu ook echt in geslaagd. Omdat één van onze streefdoelen is om iedereen verantwoord om te leren gaan met AI, stellen we deze ontdekking gratis ter beschikking voor het brede publiek. Je kan vanaf nu aan de slag met de technologie die de wereldorde zal veranderen."""
    )

    ss["chosen_model"] = st.sidebar.selectbox(
        "Kies een model:",
        options=["AGI-v4-mini", "AGI-v4", "AGI-v4-XL"],
        index=1,
        key="selected_model",
    )

    if st.sidebar.button("ABORT AGI", icon="⚠️", type="primary"):
        ss["abort"] = True
        st.rerun()

    loading_messages = [
        "20 bomen gekapt",
        "300 liter water verbruikt",
        "1000 kWh stroom verbruikt",
        "de job afgenomen van 10 personen",
        "2 industriën overbodig gemaakt",
        "5 copyrightprocessen opgelopen",
        "desinformatie verspreid aan de hand van 3 deepfakes",
        "creativiteit van 5 mensen gekopieerd",
        "bias geïntroduceerd in 5 outputs",
        "de beurswaarde van drie AI-startups verhoogd",
        "de kritische geest van 10 mensen verlaagd",
        "de privacy van 100 mensen geschonden",
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

    def loop():
        last_message = None  # Track the last message
        with st.status(
            f"Verwerken... even geduld aub! Aantal tokens gebruikt: {ss['tokens']}",
            expanded=True,
        ) as status:
            while True:
                next_message = random.choice(loading_messages)
                while (
                    next_message == last_message
                ):  # Ensure it's not the same as the last message
                    next_message = random.choice(loading_messages)
                last_message = next_message  # Update the last message
                st.write(next_message)
                ss["tokens"] += random.randint(1, 10000)
                time.sleep(5)
                status.update(
                    label=f"Verwerken... even geduld aub! Aantal tokens gebruikt: {ss['tokens']}",
                    state="running",
                )

    # Input van gebruiker
    user_question = st.text_input("Stel hier je complexe vraag:")

    if ss["abort"]:
        st.success("Geen probleem - het AGI-model wordt opgeschort ✅...")
        time.sleep(2)
        st.warning("Hmmm... dit lijkt even niet te werken. We proberen het opnieuw. 👍")
        time.sleep(2)
        st.error(f"```{ss['chosen_model']}: {random.choice(evil_messages)}```")
        time.sleep(2)
        st.warning("We zijn er bijna... even geduld aub! 😅")
        time.sleep(2)
        st.error(f"```{ss['chosen_model']}: {random.choice(refusal_messages)}```")

        loop()

    if st.button("Verstuur") and user_question:
        response = f"🤖 **{ss['chosen_model']}**: Bedankt voor je slimme vraag of instructie, ik start mijn onderzoek en kom dadelijk bij je terug!"
        st.write(response)

        ss["tokens"] = 0
        loop()


if __name__ == "__main__":
    app()
