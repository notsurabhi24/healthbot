def get_forward_rules():
    return [
        (["anxious", "racing thoughts"], "suggest_breathing"),
        (["sad", "no energy"], "suggest_therapy"),
        (["tired", "overworked"], "suggest_rest"),
        (["anxious"], "suggest_grounding"),
        (["sad"], "suggest_talk_to_friend"),
        (["happy", "grateful"], "suggest_journal_more"),
    ]

def get_backward_rules():
    return {
        "suggest_therapy": ["sad", "hopeless", "no energy"],
        "suggest_breathing": ["anxious", "racing thoughts"],
        "suggest_rest": ["tired", "burned out"]
    }

def extract_facts(mood_str, text):
    mood = mood_str.split()[1].lower()
    text = text.lower()
    facts = [mood]
    if any(w in text for w in ["racing thoughts", "can't sleep", "overthinking"]):
        facts.append("racing thoughts")
    if any(w in text for w in ["tired", "exhausted", "burned out", "overworked"]):
        facts.append("overworked")
    if "grateful" in text or "thankful" in text:
        facts.append("grateful")
    if "hopeless" in text or "no point" in text or "worthless" in text:
        facts.append("hopeless")
    if "can't focus" in text or "stuck" in text:
        facts.append("confused")
    return list(set(facts))

def get_empathetic_responses():
    return {
        "suggest_breathing": {
            "title": "🌬️ Breathe With Me",
            "advice": "When anxiety rises, your breath can anchor you. Try this now: Inhale slowly for 4 seconds, hold for 7, exhale for 8. Repeat 3 times. You're not alone."
        },
        "suggest_rest": {
            "title": "🛌 You’re Allowed to Rest",
            "advice": "You’ve been pushing hard. Burnout isn’t weakness — it’s a signal. Step back. Drink water. Lie down. Your worth isn’t tied to productivity."
        },
        "suggest_therapy": {
            "title": "💬 It’s Okay to Ask for Help",
            "advice": "Feeling hopeless doesn’t mean you’re broken — it means you’ve been fighting quietly for too long. Talking to a counselor isn’t defeat. It’s courage."
        },
        "suggest_talk_to_friend": {
            "title": "📞 Reach Out",
            "advice": "You don’t have to carry this alone. Text one person you trust: *'I’m not okay.'* Most people will surprise you with their care."
        },
        "suggest_grounding": {
            "title": "🌍 Ground Yourself",
            "advice": "When thoughts race, come back to your body. Name 5 things you see, 4 you can touch, 3 you hear, 2 you smell, 1 you taste. You are here. You are safe."
        },
        "suggest_journal_more": {
            "title": "📖 Keep Going",
            "advice": "You’re building self-awareness — one of the bravest things a person can do. Keep writing. Keep noticing. You’re growing."
        }
    }
