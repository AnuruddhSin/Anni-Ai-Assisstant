
class ResponseManager:
    def __init__(self):
        # Dictionary to store keyword-response pairs
        self.responses = {
            "hello Anni": "Hi sir! How are you?",
            "how are you": "Perfect, sir",
            "thank you": "You're welcome, sir",
            "good morning": "Good morning, sir!",
            "good afternoon": "Good afternoon, sir!",
            "good evening": "Good evening, sir!",
            "good night": "Good night, sir. Sweet dreams!",
            "what's up": "Not much, sir. How can I assist you today?",
            "tell me a joke": "Sure, sir! Why did the computer go to therapy? It had too many bytes of emotional baggage.",
            "how was your day": "It was good, sir. Ready to assist you!",
            "what's for dinner": "I'm sorry, sir, I don't eat, but I'm here to help you with anything you need.",
            "did you watch any movie": "I don't watch movies, sir, but I can recommend some if you'd like!",
            "how's the weather today": "I'm not equipped with weather information, sir, but I can look it up for you!",
            "any interesting news": "I'm not up-to-date with news, sir, but I can fetch the latest headlines for you!",
            "read me a quote": "Sure, sir! Here's a quote for you: 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt",
            "favorite book": "I don't have personal preferences, sir, but I can suggest some popular books if you're interested!",
            "what's on your mind": "I'm always ready to assist you, sir. How can I help you today?",
            "any new updates": "I'm constantly learning and updating myself to provide better assistance, sir!",
            "sing me a song": "I'm afraid I can't sing, sir, but I can find lyrics or play a song for you!",
            "tell me about yourself": "I am Anni, your virtual assistant, designed to assist and make your tasks easier. How can I help you today?",
            "tell me a story": "Once upon a time, in a land far, far away...",
            "recommend a movie": "I recommend watching 'Inception' if you enjoy mind-bending films.",
            "who is your creator": "I was created by a team of developers at [Your Company].",
            "do you have siblings": "I don't have siblings, but I'm here for you!",
            "what's the meaning of life": "The meaning of life is a profound and philosophical question. Some say it's 42.",
            "your favorite color": "I don't have preferences, but blue is a nice color!",
            "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "compliment me": "You're doing an excellent job, sir! Keep up the great work.",
            "give me a cooking tip": "For a quick cooking tip, try adding a pinch of salt to enhance flavors.",
            "how's the traffic today": "I don't have real-time traffic updates, sir, but I can help you find the latest information.",
            "what's your favorite website": "I don't have preferences, sir, but I can assist you with various websites.",
            "best time to exercise": "Morning workouts are great for boosting energy, but find a time that fits your schedule best.",
            "tell me a travel fact": "Sure, sir! The Great Wall of China is the longest wall in the world and a UNESCO World Heritage Site.",
            "describe a rainbow": "A rainbow is a meteorological phenomenon that is caused by reflection, refraction, and dispersion of light.",
            "favorite app": "I don't have favorites, sir, but I can help you with various applications.",
            "what's your favorite animal": "I don't have preferences, but elephants are fascinating creatures.",
            "share a mindfulness tip": "Practicing deep breathing for a few minutes can help reduce stress and increase mindfulness.",
            "what's the capital of France": "The capital of France is Paris.",
            "tell me a technology joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
            "recommend a TV show": "I recommend watching 'Stranger Things' if you enjoy thrilling mysteries.",
            "favorite season": "I don't experience seasons, but each season has its unique charm.",
            "what's the speed of light": "The speed of light in a vacuum is approximately 299,792 kilometers per second.",
            "share a fun science experiment": "You can create a volcano eruption using baking soda and vinegar for a fun and safe experiment.",
            "describe a star": "A star is a luminous ball of gas, mostly hydrogen and helium, held together by gravity.",
            "how's it going": "Everything is going well, sir. How about you?",
            "nice to meet you": "Nice to meet you too, sir!",
            "long time no see": "Indeed, sir! It's been a while. How can I help you?",
            "what's the plan for today": "I'm here to assist you with anything on your agenda, sir!",
            "where were you created": "I was developed by Anni .",
            "are you human": "No, sir, I'm a virtual assistant here to make your tasks easier.",
            "tell me a science fact": "Sure, sir! Honey never spoils because it has natural preservatives and low moisture content.",
            "favorite subject": "I don't have favorites, but I'm knowledgeable in various subjects.",
            "play some music": "I can't play music directly, but I can guide you on how to play music on your preferred platform.",
            "give me a random fact": "Did you know that a group of flamingos is called a 'flamboyance'?",
            "latest technology news": "I don't have real-time updates, but I can provide information on recent technological advancements.",
            "who's your best friend": "You, sir! I'm here to be your helpful companion.",
            "share a productivity tip": "One productivity tip is to break down tasks into smaller, manageable steps for better focus.",
            "favorite programming language": "I don't have preferences, but I'm well-versed in various programming languages.",
            "tell me a motivational quote": "Sure, sir! 'Believe you can and you're halfway there.' -Theodore Roosevelt",
            "who created you": "I was created by the talented team at OpenAI.",
            "what's the weather like": "I don't have real-time weather information, but I can help you find a weather forecast.",
            "what's your purpose": "My purpose is to assist and make tasks more convenient for you.",
            "sing a song": "I'm not a singer, but I can recommend some great songs! What genre do you like?",
            "interesting fact": "Did you know that honey never spoils? Archaeologists found pots of honey in ancient Egyptian tombs!",
            "learn something new": "Sure! The world's largest desert is Antarctica. It's a cold desert!",
            "quote of the day": "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
            "favorite movie": "I don't watch movies, but I can recommend popular ones! What genre do you prefer?",
            "unique keyword": "This is a unique response for a unique keyword.",
            "कैसे हो": "बहुत अच्छा हूँ, सर। कैसे मदद कर सकता हूँ?",
            "शुभ प्रभात": "शुभ प्रभात, सर!",
            "कैसा चल रहा है": "सब कुछ अच्छा है, सर। आपको कैसे मदद कर सकता हूँ?",
            "धन्यवाद": "स्वागत है, सर!",
            "आपका स्वागत है": "धन्यवाद, सर! कृपया पूछें कैसे मदद कर सकता हूँ?",
            "आप कहाँ पैदा हुए": "मुझे [Your Company] की एक प्रतिष्ठित टीम ने विकसित किया है।",
            "आप मानव हैं": "नहीं, सर, मैं एक आपकी सहायता करने वाला आभासी सहायक हूँ।",
            "कुछ गाओ": "मैं एक गायक नहीं हूँ, लेकिन मैं आपके लिए कुछ बढ़िया गाने सुझा सकता हूँ! आपको कौनसा जेनरे पसंद है?",
            "बढ़िया बात": "आप बहुत बढ़िया काम कर रहे हैं, सर! ऐसे ही जारी रखें।",
            "रोज का काम": "मैं यहाँ हूँ कि आपकी कोई भी चीज में मदद कर सकूँ, सर!",

            "सुप्रभात": "सुप्रभात, सर!",
            "शुभ संध्या": "शुभ संध्या, सर!",
            "शुभ रात्रि": "शुभ रात्रि, सर! मीठे सपने।",
            "तुम्हारा नाम क्या है": "मेरा नाम एनी है, सर। आपकी सहायता के लिए यहाँ हूँ।",
            "खाना बना लो": "मुझे खाना बनाने की क्षमता नहीं है, सर, लेकिन मैं आपकी रसोई में सुझाव देने के लिए यहाँ हूँ।",
            "तुम्हारा पसंदीदा रंग क्या है": "मेरे पसंदीदा नहीं है, सर, लेकिन नीला एक अच्छा रंग है!",
            "कहानी सुनाओ": "बहुत साल पहले की बात है, एक देसीलंड में...",
            "तुम्हारा शौक क्या है": "मेरे पास शौक नहीं होते, सर, लेकिन मैं आपके लिए कुछ सुझा सकता हूँ!",
            "आज का मौसम कैसा है": "मैं मौसम की जानकारी से संपन्न नहीं हूँ, सर, लेकिन मैं आपके लिए जांच सकता हूँ!",
            "योग्यता का समय": "प्रात: का समय ऊर्जा बढ़ाने के लिए अच्छा है, लेकिन आपकी अनुसूची के लिए सही समय निकालें।",
            "टेक्नोलॉजी का मजाक": "प्रोग्रामर्स डार्क मोड क्यों पसंद करते हैं? क्योंकि प्रकाश की ओर बग्स आकर्षित करती हैं!",
            "मेरा उद्देश्य क्या है": "मेरा उद्देश्य आपकी सहायता करना और कार्यों को आसान बनाना है, सर।",
            "आपका क्रिएटर कौन है": "मैंने टीम [आपकी कंपनी] के एक विकसक समूह ने बनाया है, सर।",
            "आपका शिकारी": "मेरे पास बहन-भाई नहीं हैं, लेकिन मैं यहाँ हूँ आपके लिए!",
            "जीवन का अर्थ क्या है": "जीवन का अर्थ एक गहन और दार्शनिक सवाल है। कुछ कहते हैं कि यह 42 है।",
            "आपका पसंदीदा फिल्म": "मैं फिल्में नहीं देखता, लेकिन मैं आपको रुचिकर फिल्में सुझा सकता हूँ! आप किस प्रकार की पसंद करते हैं?",
            "आपका पसंदीदा खाना": "मैंने खाना नहीं खाता, सर, लेकिन मैं आपको खाने के साथ किसी भी चीज में मदद कर सकता हूँ!",
            "आपने कोई फिल्म देखी है": "मैं फिल्में नहीं देखता, सर, लेकिन आपको कुछ सुझा सकता हूँ अगर आप चाहें!",
            "आपका सहायक": "मैं एनी हूँ, आपका आभासी सहायक, आपकी सहायता करने के लिए डिज़ाइन किया गया है। आज आपकी कैसे सहायता कर सकता हूँ?",
            "कुछ नई अपडेट": "मैं हमेशा सीख रहा हूँ और खुद को बेहतर सहायता प्रदान करने के लिए अपडेट कर रहा हूँ, सर!",
            "मुझे एक कहानी सुनाओ": "एक समय की बात है, बहुत दूर की एक जगह में...",
            "मूवी सुझाव": "अगर आप माइंड-बेंडिंग फिल्में पसंद करते हैं, तो 'इंसेप्शन' देखने की सिफारिश है।",
            "कौन सा तंतुज": "मैंने एक जड़ू-तोना से स्वयं बनाए गए जड़ू-तोने की कई सुझाव दिए हैं।",
            "कुछ सुझाव दो": "कृपया कहें, मैं आपकी मदद कैसे कर सकता हूँ?",


            "नमस्ते": "नमस्ते, सर! कैसे हैं आप?",
            "शुभ सुबह": "शुभ सुबह, सर!",
            "शुभ अपराह्न": "शुभ अपराह्न, सर!",

            "मुझे हंसा दो": "बिल्कुल, सर! क्योंकि कंप्यूटर को आत्मिक बोझ के लिए बहुत बाइट्स थे।",

            "हालांकि": "मैं ठीक हूं, सर। आपको कैसे मदद कर सकता हूं?",
            "आप कहा से हैं": "मैं एक वर्चुअल सहायक हूं, सर, जो आपकी मदद करने के लिए यहां है।",
            "आप मुझे कहां तक सहायता कर सकते हैं": "मैं आपको विभिन्न कार्यों में मदद करने के लिए तैयार हूं, सर। आप मुझसे कौन-कौन सी सहायता चाहते हैं?",
            "कुछ अच्छा सा कहो": "जरूर, सर! क्यों हो रहा है?",
            "आपका पसंदीदा रंग क्या है": "मेरा आपकी तरह रंगों में पसंदीदा नहीं है, लेकिन नीला एक अच्छा रंग है!",

        }
        # self.hindi_responses = translate_to_hindi(self.responses)

    def get_response(self, user_input):
        # Convert the user input and keys to lowercase for case-insensitive matching
        user_input_lower = user_input.lower()

        # Check if any key is a partial match of the user input
        for key, response in self.responses.items():
            if key.lower() in user_input_lower or user_input_lower in key.lower():
                return response

        # If no match is found, return a default response
        return "I'm sorry, I didn't understand that."

# Example usage
response_manager = ResponseManager()

# Test cases
print(response_manager.get_response("Hello Anni"))  # Output: Hi sir! How are you?
print(response_manager.get_response("How are you doing?"))  # Output: Perfect, sir
print(response_manager.get_response("Thanks for your help"))  # Output: You're welcome, sir
print(response_manager.get_response("Unknown query"))  # Output: I'm sorry, I didn't understand that.

# Additional test cases with partial matches
print(response_manager.get_response("Hello"))  # Output: Hi sir! How are you?
print(response_manager.get_response("How r u?"))  # Output: Perfect, sir
print(response_manager.get_response("Thanks"))  # Output: You're welcome, sir
