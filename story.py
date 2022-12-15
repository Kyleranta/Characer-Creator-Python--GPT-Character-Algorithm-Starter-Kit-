import random
import nltk
import json
import requests

# Generate a random name
# Set the API endpoint and any necessary parameters
endpoint = "https://randomuser.me/api"
params = {"gender": "male", "nat": "us"}

# Make the API call and handle the response
response = requests.get(endpoint, params)

if response.status_code == 200:
    data = json.loads(response.text)

    # Get the list of random names from the response data
    names = [
        user["name"]["first"] + " " + user["name"]["last"]
        for user in data["results"]
    ]

    # Generate a random index and use it to get a random name from the list
    index = random.randint(0, len(names) - 1)
    random_name = names[index]
    name = random.choice(names)
    # Print the random name
    print(random_name)
else:
    print("An error occurred:", response.text)

# Generate a random age
age = random.randint(18, 65)

# Generate a random list of attributes
attributes = ["Abrasive", "Abrupt","Agonizing","Aimless","Airy","Aloof","Amoral","Angry","Anxious","Apathetic","Arbitrary","Argumentative","Arrogant","Artificial","Asocial","Assertive","Astigmatic","Barbaric","Bewildered","Bizarre","Bland","Blunt","Boisterous","Brittle","Brutal","Calculating","Callous","Cantankerous","Careless","Cautious","Charmless","Childish","Clumsy","Coarse","Cold","Colorless","Complacent","Complaintive","Compulsive","Conceited","Condemnatory","Conformist","Confused","Contemptible","Conventional","Cowardly","Crafty","Crass","Crazy","Criminal","Critical","Crude","Cruel","Cynical","Decadent","Deceitful","Delicate","Demanding","Dependent","Desperate","Destructive","Devious","Difficult","Dirty","Disconcerting","Discontented","Discouraging","Discourteous","Dishonest","Disloyal","Disobedient","Disorderly","Disorganized","Disputatious","Disrespectful","Disruptive","Dissolute","Dissonant","Distractible","Disturbing","Dogmatic","Domineering","Dull","Easily Discouraged","Egocentric","Enervated","Envious","Erratic","Escapist","Excitable","Expedient","Extravagant","Extreme","Faithless","False","Fanatical","Fanciful","Fatalistic","Fawning","Fearful","Fickle","Fiery","Fixed","Flamboyant","Foolish","Forgetful","Fraudulent","Frightening","Frivolous","Gloomy","Graceless","Grand","Greedy","Grim","Gullible","Hateful","Haughty","Hedonistic","Hesitant","Hidebound","High-handed","Hostile","Ignorant","Imitative","Impatient","Impractical","Imprudent","Impulsive","Inconsiderate","Incurious","Indecisive","Indulgent","Inert","Inhibited","Insecure","Insensitive","Insincere","Insulting","Intolerant","Irascible","Irrational","Irresponsible","Irritable","Lazy","Libidinous","Loquacious","Malicious","Mannered","Mannerless","Mawkish","Mealy Mouthed","Mechanical","Meddlesome","Melancholic","Meretricious","Messy","Miserable","Miserly","Misguided","Mistaken","Money-minded","Monstrous","Moody","Morbid","Muddle-headed","Naive","Narcissistic","Narrow","Narrow-minded","Natty","Negativistic","Neglectful","Neurotic","Nihilistic","Obnoxious","Obsessive","Obvious","Odd","Offhand","One-dimensional","One-sided","Opinionated","Opportunistic","Oppressed","Outrageous","Over Imaginative","Paranoid","Passive","Pedantic","Perverse","Petty","Pharisaical","Phlegmatic","Plodding","Pompous","Possessive","Power-hungry","Predatory","Prejudiced","Presumptuous","Pretentious","Prim","Procrastinating","Profligate","Provocative","Pugnacious","Puritanical","Quirky","Reactionary","Reactive","Regimental","Regretful","Repentant","Repressed","Resentful","Ridiculous","Rigid","Ritualistic","Rowdy","Ruined","Sadistic","Sanctimonious","Scheming","Scornful","Secretive","Sedentary","Selfish","Self-indulgent","Shallow","Shortsighted","Shy","Silly","Single-minded","Sloppy","Slow","Sly","Small-thinking","Soft Headed","Sordid","Steely","Stiff","Strong-willed","Stupid","Submissive","Superficial","Superstitious","Suspicious","Tactless","Tasteless","Tense","Thievish","Thoughtless","Timid","Transparent","Treacherous","Trendy","Troublesome","Unappreciative","Uncaring","Uncharitable","Unconvincing","Uncooperative","Uncreative","Uncritical","Unctuous","Undisciplined","Unfriendly","Ungrateful","Unhealthy","Unimaginative","Unimpressive","Unlovable","Unpolished","Unprincipled","Unrealistic","Unreflective","Unreliable","Unrestrained","Unself-critical","Unstable","Vacuous","Vague","Venal","Venomous","Vindictive","Vulnerable","Weak","Weak-willed","Well-meaning","Willful","Wishful","Zany","Accessible","Active","Adaptable","Admirable","Adventurous","Agreeable","Alert","Allocentric","Amiable","Anticipative","Appreciative","Articulate","Aspiring","Athletic","Attractive","Balanced","Benevolent","Brilliant","Calm","Capable","Captivating","Caring","Challenging","Charismatic","Charming","Cheerful","Clean","Clear-headed","Clever","Colorful","Companionly","Compassionate","Conciliatory","Confident","Conscientious","Considerate","Constant","Contemplative","Cooperative","Courageous","Courteous","Creative","Cultured","Curious","Daring","Debonair","Decent","Decisive","Dedicated","Deep","Dignified","Directed","Disciplined","Discreet","Dramatic","Dutiful","Dynamic","Earnest","Ebullient","Educated","Efficient","Elegant","Eloquent","Empathetic","Energetic","Enthusiastic","Esthetic","Exciting","Extraordinary","Fair","Faithful","Farsighted","Felicific","Firm","Flexible","Focused","Forecful","Forgiving","Forthright","Freethinking","Friendly","Fun-loving","Gallant","Generous","Gentle","Genuine","Good-natured","Gracious","Hardworking","Healthy","Hearty","Helpful","Herioc","High-minded","Honest","Honorable","Humble","Humorous","Idealistic","Imaginative","Impressive","Incisive","Incorruptible","Independent","Individualistic","Innovative","Inoffensive","Insightful","Insouciant","Intelligent","Intuitive","Invulnerable","Kind","Knowledge","Leaderly","Leisurely","Liberal","Logical","Lovable","Loyal","Lyrical","Magnanimous","Many-sided","Masculine (Manly)","Mature","Methodical","Maticulous","Moderate","Modest","Multi-leveled","Neat","Nonauthoritarian","Objective","Observant","Open","Optimistic","Orderly","Organized","Original","Painstaking","Passionate","Patient","Patriotic","Peaceful","Perceptive","Perfectionist","Personable","Persuasive","Planful","Playful","Polished","Popular","Practical","Precise","Principled","Profound","Protean","Protective","Providential","Prudent","Punctual","Purposeful","Rational","Realistic","Reflective","Relaxed","Reliable","Resourceful","Respectful","Responsible","Responsive","Reverential","Romantic","Rustic","Sage","Sane","Scholarly","Scrupulous","Secure","Selfless","Self-critical","Self-defacing","Self-denying","Self-reliant","Self-sufficient","Sensitive","Sentimental","Seraphic","Serious","Sexy","Sharing","Shrewd","Simple","Skillful","Sober","Sociable","Solid","Sophisticated","Spontaneous","Sporting","Stable","Steadfast","Steady","Stoic","Strong","Studious","Suave","Subtle","Sweet","Sympathetic","Systematic","Tasteful","Teacherly","Thorough","Tidy","Tolerant","Tractable","Trusting","Uncomplaining","Understanding","Undogmatic","Unfoolable","Upright","Urbane","Venturesome","Vivacious","Warm","Well-bred","Well-read","Well-rounded","Winning","Wise","Witty","Youthful","Absentminded","Aggressive","Ambitious","Amusing","Artful","Ascetic","Authoritarian","Big-thinking","Boyish","Breezy","Businesslike","Busy","Casual","Cerebral","Chummy","Circumspect","Competitive","Complex","Confidential","Conservative","Contradictory","Crisp","Cute","Deceptive","Determined","Dominating","Dreamy","Driving","Droll","Dry","Earthy","Effeminate","Emotional","Enigmatic","Experimental","Familial","Folksy","Formal","Freewheeling","Frugal","Glamorous","Guileless","High-spirited","Huried","Hypnotic","Iconoclastic","Idiosyncratic","Impassive","Impersonal","Impressionable","Intense","Invisible","Irreligious","Irreverent","Maternal","Mellow","Modern","Moralistic","Mystical","Neutral","Noncommittal","Noncompetitive","Obedient","Old-fashioned","Ordinary","Outspoken","Paternalistic","Physical","Placid","Political","Predictable","Preoccupied","Private","Progressive","Proud","Pure","Questioning","Quiet","Religious","Reserved","Restrained","Retiring","Sarcastic","Self-conscious","Sensual","Skeptical","Smooth","Soft","Solemn","Solitary","Stern","Stolid","Strict","Stubborn","Stylish","Subjective","Surprising","Soft","Tough","Unaggressive","Unambitious","Unceremonious","Unchanging","Undemanding","Unfathomable","Unhurried","Uninhibited","Unpatriotic","Unpredictable","Unreligious","Unsentimental","Whimsical",
]
attributes = random.sample(attributes, 3)

# Generate a random list of emotions
emotions = emotions = ["Anger", "Annoyance", "Contempt", "Disgust", "Irritation", "Anxiety", "Embarrassment", "Fear", "Helplessness", "Powerlessness", "Worry", "Pride", "Doubt", "Envy", "Frustration", "Guilt", "Shame", "Boredom", "Despair", "Disappointment", "Hurt", "Sadness", "Agitation", "Stress", "Shock", "Tension", "Amusement", "Delight", "Elation", "Excitement", "Happiness", "Joy", "Pleasure", "Affection", "Empathy", "Friendliness", "Love", "Courage", "Hope", "Humility", "Satisfaction", "Trust", "Calmness", "Contentment", "Relaxation", "Relief", "Serenity", "Interest", "Politeness", "Surprise"]
emotions = random.sample(emotions, 3)

# Generate a random environmental factor
environmental_factors = ["rural", "urban", "suburban", "coastal", "mountainous", "desert", "tropical"]
environment = random.choice(environmental_factors)

# Generate a random list of words that must be included in the story
required_words = ["journey", "adventure", "experience", "discovery", "exploration", "achievement"]
required_words = random.sample(required_words, 3)
