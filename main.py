import random
import nltk

# Import the wordnet corpus from the nltk package
from nltk.corpus import wordnet

# Download the wordnet corpus
nltk.download('wordnet')

# Create a dictionary to store the words by their length
words = {
    3: [],
    4: [],
    5: [],
    6: [],
    7: []
}

# Create a list to store the letters
letters = []

# Generate 10 random letters
for i in range(10):
    # Choose a random letter
    letter = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    
    # Add the letter to the list
    letters.append(letter)
    
# Print the list of letters
print(letters)

# Search the wordnet corpus for words starting with the specified letter
for word in wordnet.words():
    if word.startswith(letter):
        # Check if the dictionary contains an entry for this length
        if len(word) in words:
            # Add the word to the dictionary
            words[len(word)].append(word)

# Print the words organized by their length
for key, value in words.items():
    print(f"{key}-letter words starting with {letter}: {value}")

# Select a random sample of 5 words from the list of 6-letter words
sample = random.sample(words[6], 24)

# Print the sample
print(sample)

# List of first names
first_names = ["John", "Jane", "Jack", "Jill", "Michael", "Mary", "Mike", "Molly"]

# List of last names
last_names = ["Smith", "Jones", "Brown", "Johnson", "Williams", "Miller", "Taylor", "Davis"]

# Generate a random index for the first and last name list
first_index = random.randint(0, len(first_names) - 1)
last_index = random.randint(0, len(last_names) - 1)

# Use the random indices to get a random first and last name
random_first = first_names[first_index]
random_last = last_names[last_index]

# Concatenate the first and last name to generate a random name
random_name = random_first + " " + random_last

# Print the random name
print(random_name)

# Define the emotional states
emotions = ["Anger", "Annoyance", "Contempt", "Disgust", "Irritation", "Anxiety", "Embarrassment", "Fear", "Helplessness", "Powerlessness", "Worry", "Pride", "Doubt", "Envy", "Frustration", "Guilt", "Shame", "Boredom", "Despair", "Disappointment", "Hurt", "Sadness", "Agitation", "Stress", "Shock", "Tension", "Amusement", "Delight", "Elation", "Excitement", "Happiness", "Joy", "Pleasure", "Affection", "Empathy", "Friendliness", "Love", "Courage", "Hope", "Humility", "Satisfaction", "Trust", "Calmness", "Contentment", "Relaxation", "Relief", "Serenity", "Interest", "Politeness", "Surprise"]

# define a list of social environmental factors
social_factors = [
    "Social stigma (such as coming out as gay or lesbian)",
    "History of abuse",
    "Family discord during childhood",
    "Early loss of a parent",
    "Poverty",
    "Lack of spirituality or religious affiliation",
    "Lack of meaningful work or hobbies",
    "Toxic relationships",
    "Lack of self-care and/or relaxation"
]

# define a list of physical environmental factors
physical_factors = [
    "Sleep deprivation",
    "Smoking",
    "Substance abuse",
    "Pollution",
    "Exposure to toxins during childhood",
    "Extreme weather conditions (such as excessive rain or snow)",
    "Hazardous conditions at work"
]

# Define the actions
actions = ["Talking", "Walking", "Running", "Sitting", "Sleeping", "Eating", "Drinking", "Smiling", "Crying", "Laughing", "Yelling", "Hugging", "Kissing", "Fighting"]

# List of negative human characteristics and attributes
characteristics = ["Abrasive", "Abrupt","Agonizing","Aimless","Airy","Aloof","Amoral","Angry","Anxious","Apathetic","Arbitrary","Argumentative","Arrogant","Artificial","Asocial","Assertive","Astigmatic","Barbaric","Bewildered","Bizarre","Bland","Blunt","Boisterous","Brittle","Brutal","Calculating","Callous","Cantankerous","Careless","Cautious","Charmless","Childish","Clumsy","Coarse","Cold","Colorless","Complacent","Complaintive","Compulsive","Conceited","Condemnatory","Conformist","Confused","Contemptible","Conventional","Cowardly","Crafty","Crass","Crazy","Criminal","Critical","Crude","Cruel","Cynical","Decadent","Deceitful","Delicate","Demanding","Dependent","Desperate","Destructive","Devious","Difficult","Dirty","Disconcerting","Discontented","Discouraging","Discourteous","Dishonest","Disloyal","Disobedient","Disorderly","Disorganized","Disputatious","Disrespectful","Disruptive","Dissolute","Dissonant","Distractible","Disturbing","Dogmatic","Domineering","Dull","Easily Discouraged","Egocentric","Enervated","Envious","Erratic","Escapist","Excitable","Expedient","Extravagant","Extreme","Faithless","False","Fanatical","Fanciful","Fatalistic","Fawning","Fearful","Fickle","Fiery","Fixed","Flamboyant","Foolish","Forgetful","Fraudulent","Frightening","Frivolous","Gloomy","Graceless","Grand","Greedy","Grim","Gullible","Hateful","Haughty","Hedonistic","Hesitant","Hidebound","High-handed","Hostile","Ignorant","Imitative","Impatient","Impractical","Imprudent","Impulsive","Inconsiderate","Incurious","Indecisive","Indulgent","Inert","Inhibited","Insecure","Insensitive","Insincere","Insulting","Intolerant","Irascible","Irrational","Irresponsible","Irritable","Lazy","Libidinous","Loquacious","Malicious","Mannered","Mannerless","Mawkish","Mealy Mouthed","Mechanical","Meddlesome","Melancholic","Meretricious","Messy","Miserable","Miserly","Misguided","Mistaken","Money-minded","Monstrous","Moody","Morbid","Muddle-headed","Naive","Narcissistic","Narrow","Narrow-minded","Natty","Negativistic","Neglectful","Neurotic","Nihilistic","Obnoxious","Obsessive","Obvious","Odd","Offhand","One-dimensional","One-sided","Opinionated","Opportunistic","Oppressed","Outrageous","Over Imaginative","Paranoid","Passive","Pedantic","Perverse","Petty","Pharisaical","Phlegmatic","Plodding","Pompous","Possessive","Power-hungry","Predatory","Prejudiced","Presumptuous","Pretentious","Prim","Procrastinating","Profligate","Provocative","Pugnacious","Puritanical","Quirky","Reactionary","Reactive","Regimental","Regretful","Repentant","Repressed","Resentful","Ridiculous","Rigid","Ritualistic","Rowdy","Ruined","Sadistic","Sanctimonious","Scheming","Scornful","Secretive","Sedentary","Selfish","Self-indulgent","Shallow","Shortsighted","Shy","Silly","Single-minded","Sloppy","Slow","Sly","Small-thinking","Soft Headed","Sordid","Steely","Stiff","Strong-willed","Stupid","Submissive","Superficial","Superstitious","Suspicious","Tactless","Tasteless","Tense","Thievish","Thoughtless","Timid","Transparent","Treacherous","Trendy","Troublesome","Unappreciative","Uncaring","Uncharitable","Unconvincing","Uncooperative","Uncreative","Uncritical","Unctuous","Undisciplined","Unfriendly","Ungrateful","Unhealthy","Unimaginative","Unimpressive","Unlovable","Unpolished","Unprincipled","Unrealistic","Unreflective","Unreliable","Unrestrained","Unself-critical","Unstable","Vacuous","Vague","Venal","Venomous","Vindictive","Vulnerable","Weak","Weak-willed","Well-meaning","Willful","Wishful","Zany","Accessible","Active","Adaptable","Admirable","Adventurous","Agreeable","Alert","Allocentric","Amiable","Anticipative","Appreciative","Articulate","Aspiring","Athletic","Attractive","Balanced","Benevolent","Brilliant","Calm","Capable","Captivating","Caring","Challenging","Charismatic","Charming","Cheerful","Clean","Clear-headed","Clever","Colorful","Companionly","Compassionate","Conciliatory","Confident","Conscientious","Considerate","Constant","Contemplative","Cooperative","Courageous","Courteous","Creative","Cultured","Curious","Daring","Debonair","Decent","Decisive","Dedicated","Deep","Dignified","Directed","Disciplined","Discreet","Dramatic","Dutiful","Dynamic","Earnest","Ebullient","Educated","Efficient","Elegant","Eloquent","Empathetic","Energetic","Enthusiastic","Esthetic","Exciting","Extraordinary","Fair","Faithful","Farsighted","Felicific","Firm","Flexible","Focused","Forecful","Forgiving","Forthright","Freethinking","Friendly","Fun-loving","Gallant","Generous","Gentle","Genuine","Good-natured","Gracious","Hardworking","Healthy","Hearty","Helpful","Herioc","High-minded","Honest","Honorable","Humble","Humorous","Idealistic","Imaginative","Impressive","Incisive","Incorruptible","Independent","Individualistic","Innovative","Inoffensive","Insightful","Insouciant","Intelligent","Intuitive","Invulnerable","Kind","Knowledge","Leaderly","Leisurely","Liberal","Logical","Lovable","Loyal","Lyrical","Magnanimous","Many-sided","Masculine (Manly)","Mature","Methodical","Maticulous","Moderate","Modest","Multi-leveled","Neat","Nonauthoritarian","Objective","Observant","Open","Optimistic","Orderly","Organized","Original","Painstaking","Passionate","Patient","Patriotic","Peaceful","Perceptive","Perfectionist","Personable","Persuasive","Planful","Playful","Polished","Popular","Practical","Precise","Principled","Profound","Protean","Protective","Providential","Prudent","Punctual","Purposeful","Rational","Realistic","Reflective","Relaxed","Reliable","Resourceful","Respectful","Responsible","Responsive","Reverential","Romantic","Rustic","Sage","Sane","Scholarly","Scrupulous","Secure","Selfless","Self-critical","Self-defacing","Self-denying","Self-reliant","Self-sufficient","Sensitive","Sentimental","Seraphic","Serious","Sexy","Sharing","Shrewd","Simple","Skillful","Sober","Sociable","Solid","Sophisticated","Spontaneous","Sporting","Stable","Steadfast","Steady","Stoic","Strong","Studious","Suave","Subtle","Sweet","Sympathetic","Systematic","Tasteful","Teacherly","Thorough","Tidy","Tolerant","Tractable","Trusting","Uncomplaining","Understanding","Undogmatic","Unfoolable","Upright","Urbane","Venturesome","Vivacious","Warm","Well-bred","Well-read","Well-rounded","Winning","Wise","Witty","Youthful","Absentminded","Aggressive","Ambitious","Amusing","Artful","Ascetic","Authoritarian","Big-thinking","Boyish","Breezy","Businesslike","Busy","Casual","Cerebral","Chummy","Circumspect","Competitive","Complex","Confidential","Conservative","Contradictory","Crisp","Cute","Deceptive","Determined","Dominating","Dreamy","Driving","Droll","Dry","Earthy","Effeminate","Emotional","Enigmatic","Experimental","Familial","Folksy","Formal","Freewheeling","Frugal","Glamorous","Guileless","High-spirited","Huried","Hypnotic","Iconoclastic","Idiosyncratic","Impassive","Impersonal","Impressionable","Intense","Invisible","Irreligious","Irreverent","Maternal","Mellow","Modern","Moralistic","Mystical","Neutral","Noncommittal","Noncompetitive","Obedient","Old-fashioned","Ordinary","Outspoken","Paternalistic","Physical","Placid","Political","Predictable","Preoccupied","Private","Progressive","Proud","Pure","Questioning","Quiet","Religious","Reserved","Restrained","Retiring","Sarcastic","Self-conscious","Sensual","Skeptical","Smooth","Soft","Solemn","Solitary","Stern","Stolid","Strict","Stubborn","Stylish","Subjective","Surprising","Soft","Tough","Unaggressive","Unambitious","Unceremonious","Unchanging","Undemanding","Unfathomable","Unhurried","Uninhibited","Unpatriotic","Unpredictable","Unreligious","Unsentimental","Whimsical",
]

# Choose a random number of characteristics between 5 and 13
num_characteristics = random.randint(5, 13)

# Choose the characteristics
chosen_characteristics = random.sample(characteristics, num_characteristics)

# Print the chosen characteristics
print("The chosen characteristics are:")
for characteristic in chosen_characteristics:
    print(f"- {characteristic}")

# Choose a random number of emotional states between 1 and 3
num_emotions = random.randint(1, 3)

# Choose the emotions
chosen_emotions = random.sample(emotions, num_emotions)

# Print the chosen emotions
print("The chosen emotions are:")
for emotions in chosen_emotions:
    print(f"- {emotions}")

# Choose a random number of social factors states between 0 and 2
num_social_factors = random.randint(0, 1)

# Choose the social factors
chosen_social_factors = random.sample(social_factors, num_social_factors)

# Print the chosen social factors
print("The chosen social factors are:")
for social_factors in chosen_social_factors:
    print(f"- {social_factors}")

# Choose a random number of physical factors states between 0 and 2
num_physical_factors = random.randint(0, 1)

# Choose the physical factors
chosen_physical_factors = random.sample(physical_factors, num_physical_factors)

# Print the chosen physical factors
print("The chosen physical factors are:")
for physical_factors in chosen_physical_factors:
    print(f"- {physical_factors}")

# Choose a random number of actions states between 1 and 2
num_actions = random.randint(1, 2)

# Choose the actions
chosen_actions = random.sample(actions, num_actions)

    # Print the chosen actions
print("The chosen actions are:")
for actions in chosen_actions:
    print(f"- {actions}")

# Generate a random character
character = {
    "characteristics": random.choice(characteristics),
    "emotional state": random.choice(emotions),
    "actions": random.choice(actions),
    "physical": random.choice(physical_factors),
    "social": random.choice(social_factors),  
}

# Print the character's characteristics, emotional state, and environment
print(character["characteristics"])
print
print(character["emotional state"])
print
print(character["physical"])
print
print(character["social"])
print
print(character["actions"])