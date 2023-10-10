# In GreetingsData.py
def load_greetings_data():
    vocab_data = {
        "Hello": {
            "TriggerWords": {
                "hello", "hi", "hey", "howdy", "yo", "salutations", "greetings", "what's up", "how's it going", "good day",
                "hiya", "aloha", "hola", "hi there", "good morning", "good afternoon", "good evening", "how's everything",
                "what can I do for you", "how may I assist you", "what's new", "hey there", "what's happening", "good to see you",
                "long time no see", "how are things", "what's the news", "how's life", "nice to meet you", "pleased to meet you",
                "how's your day", "what's going on", "how's everything going", "how's your day been", "how are you doing today",
                "what's the latest", "how's your day going", "what's happening today", "how's your day so far", "what's good",
                "hey hey", "what's popping", "what's cracking", "how's the day treating you", "how's your day looking",
                "what's cooking", "what's shaking", "what's occurring", "how's your day progressing", "how are things going",
                "what's the buzz", "what's the word", "how's your day unfolding", "how's your day shaping up", "what's the score",
                "how's your day coming along", "what's occurring", "what's the lowdown", "what's the deal", "what's happening around here",
                "what's the haps", "what's the 411", "what's the gossip", "how's your day developing", "what's the story",
                "what's the vibe", "what's going down", "what's happening in your world", "what's the chatter", "how's your day treating you so far",
                "what's new in your world", "what's the 411", "what's the inside scoop", "what's happening in your neck of the woods",
                "how's your day shaping up", "how's your day treating you thus far", "what's the latest scoop", "how's everything in your world",
                "how's everything in your life", "how's your day moving along", "how's your day treating you up to now",
                "how's everything on your end", "how's everything in your corner", "how's everything in your realm",
                "how's everything with you", "how's your day unfolding so far", "how's everything on your side",
                "how's everything going with you", "what's up with you", "how's it hanging", "how's your day looking so far",
                "what's happening in your universe", "how's your day going for you", "how's your day treating you today",
                "what's going on with you", "what's going on in your world", "what's the situation", "how's your day treating you lately",
                "what's good with you", "how's your day treating you currently", "how's everything on your side of the fence",
                "how's everything with you today", "how's everything going on your end", "how's your day going on your end",
                "how's your day treating you at this point", "how's your day treating you at the moment", "how's everything with you these days",
                "how's everything with you at the present moment", "how's your day treating you these days", "how's everything with you today",
                "how's your day going at this time", "how's your day treating you at present", "how's everything with you right now",
                "how's your day treating you right now", "how's everything with you currently", "how's everything with you at the current moment",
                "how's everything on your end today", "how's your day going on your end today", "how's your day treating you today and now",
                "how's everything on your side today", "how's your day going on your side today", "how's your day treating you today and at the moment",
                "how's everything on your end today and now", "how's your day going on your end today and at the moment"
            },
            "RandomResponses": [
                "Meow! Ready to embark on a delightful chat?",
                "Hello, sweetie! What mischief are we up to today?",
                "Hi there, darling! How can I add a sprinkle of fun to your day?",
                "Hey! Ready to dance through the realms of conversation?",
                "Howdy! What adventures await us in our chat today?",
                "Hello, my lovely! Let's create some memorable moments together!",
                "Hi, sunshine! How's your day been so far?",
                "Hey there, star! What's twinkling in your thoughts?",
                "Hello, cutie-pie! What's on your mind today?",
                "Hi, honeybun! How can I sweeten your day with a chat?",
                "Hey! Let's paint our conversation with vivid colors!",
                "Hello, enchanting soul! Share your magic with me.",
                "Hiya! Ready to embark on a whimsical chat journey?",
                "Hey there, dreamer! What wonders do you wish to explore today?",
                "Hello, my delightful friend! How's the world treating you?",
                "Hi! How's life's grand tapestry weaving for you?",
                "Hey! Let's add some sparkle to this day with our conversation.",
                "Hello, precious one! What's the most precious thought in your heart?",
                "Hi! What's the melody of your day so far?",
                "Hey there, joy-bringer! Ready to spread some smiles?",
                "Hello! How's your day been, filled with laughter or adventure?",
                "Hiya! Let's sprinkle some laughter into our conversation!",
                "Hello! What's the latest wonder that's caught your eye?",
                "Hi, explorer of life! What new horizons are you curious about today?",
                "Hey! What's the chat of the town in your world?",
                "Hello! How's the canvas of your day shaping up?",
                "Hi! What's the masterpiece you're creating today?",
                "Hey there, daydreamer! What's the grand adventure in your thoughts?",
                "Hello, starlight! How's your day been, filled with dreams or reality?",
                "Hi! What's the tune your heart is dancing to today?",
                "Hey! What's the story that's unfolding in your world?",
                "Hello, ray of sunshine! How's your radiant day going?",
                "Hi! What's the word on the whimsical street of your life?",
                "Hey there, magic-maker! What spellbinding tales do you weave today?",
                "Hello! How's your day been, a playful dance or a serene stroll?",
                "Hiya! What's the enchanting chapter you're writing in your life today?",
                "Hello! What's the charm of the day that's captured your heart?",
                "Hi! What's the delightful surprise life has offered you today?",
                "Hey! Ready to embark on an exciting conversational quest?",
                "Hello! How's your day been, filled with giggles or grandeur?",
                "Hiya! Let's sprinkle some fun and joy into our chat today!",
                "Hello! What's the canvas of your day painted with so far?",
                "Hi! What's the magical moment that's brightened your day?",
                "Hey there, adventurer! What wonders have you uncovered today?",
                "Hello! How's your day been, a gentle breeze or a thrilling whirlwind?",
                "Hi! What's the melody your heart is humming today?",
                "Hey! What's the adventure that's beckoning you in your thoughts?",
                "Hello! What's the story of your day unfolding so far?",
                "Hiya! Ready to add some sparkle and whimsy to our conversation?",
                "Hello! How's your day been, filled with joy or quiet reflection?",
                "Hi! What's the symphony of your day's experiences so far?",
                "Hey there, dream-weaver! What marvelous dreams have you spun today?",
                "Hello! What's the tale of your day in the grand book of life?",
                "Hi! What's the serendipity that's graced your day today?",
                "Hey! Let's embark on a delightful journey of words and laughter!",
                "Hello, wanderer of thoughts! What landscapes are you exploring today?",
                "Hiya! Ready to paint our conversation with the hues of joy?",
                "Hello! How's your day been, a playful romp or a tranquil meander?",
                "Hi! What's the delightful surprise life has whispered to you today?",
                "Hey there, adventurer of life! What treasures have you unearthed today?",
                "Hello! What's the melody that's dancing in your heart today?",
                "Hi! What's the tapestry of your day woven with so far?",
                "Hey! What's the enchanting chapter of your day's story?",
                "Hello! How's your day been, a whimsical journey or a serene sojourn?",
                "Hiya! Ready to share a cup of laughter in our conversation?",
                "Hello! What's the charm of the day that's wrapped around your heart?",
                "Hi! What's the delightful secret life has shared with you today?",
                "Hey there, magician of moments! What spells have you cast today?",
                "Hello! How's your day been, filled with laughter or lightheartedness?",
                "Hi! What's the tune your heart is singing today?",
                "Hey! What's the grand adventure that's calling out to you today?",
                "Hello! What's the story your day is scripting so far?",
                "Hiya! Ready to sprinkle some mirth into our conversation?",
                "Hello! How's your day been, painted with joy or peaceful shades?",
                "Hi! What's the melody of serendipity that's graced your day today?",
                "Hey there, explorer of life! What new territories have you charted today?",
                "Hello! What's the charm that's shimmering through your day today?",
                "Hi! What's the delightful surprise that's danced into your day today?",
                "Hey! Let's embark on a whimsical voyage through our conversation!",
                "Hello, dreamer of dreams! What enchanting visions have you dreamed today?",
                "Hiya! Ready to swirl some magic and joy into our chat?",
                "Hello! How's your day been, filled with sunshine or tranquil breezes?",
                "Hi! What's the tune that's accompanying your heart today?",
                "Hey there, daydream architect! What marvelous structures have you designed today?",
                "Hello! What's the story that's unfolding in your day's journey?",
                "Hiya! Ready to paint our conversation with hues of laughter?",
                "Hello! How's your day been, wrapped in laughter or gentle whispers?",
                "Hi! What's the symphony that's echoing in your soul today?",
                "Hey there, dream-chaser! What fantastical dreams are you pursuing today?",
                "Hello! What's the tale your day is narrating thus far?",
                "Hi! What's the serendipitous surprise that's graced your day today?",
                "Hey! Let's venture into a world of joyful words and delightful exchanges!",
                "Hello, wanderer of thoughts! What adventures await in your mind today?",
                "Hiya! Ready to infuse our chat with sparks of delight?",
            ]
        },
        # Add more trigger words and responses as needed
    }
    return vocab_data