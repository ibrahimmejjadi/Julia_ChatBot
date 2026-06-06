

from time import*
start = time()



word_music = "music" 
word_movie = "movie"
word_news = "news"
word_life = "life tips"
word_python = "python"
word_games = "game"

name = input("Hi, My name is Julia\n-What is your name?")

conversation = input("Nice to meet you '"+ name+"' \nHow can I help you?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()

while conversation != "end":
    if "menu" in conversation  :
        menu_input = input("\nHere  are some of my suggestions :\n\n-Music 🎵 \n-Movies 📽️\n-Latest news 📰 \n-Life tips 💡\n-Python home practice 🐍💻🏠  \n-Games 🧩 (more Soon!)  \n-Weights converting system(Not yet, On the future updates) \n ").lower()
        if  word_music in menu_input :

            music_preference = input("\nHmm, let see what we have here: \n-Actually it depends on your music preference, which type of music do you  prefer '"+ name+"' ? \n\n-Rap \n-Pop  \n-Jazz \n-Classic music \n-Heavy metal \n ").lower()
            if "rap" in music_preference:
                print("Rap music was always a way for the musiscians to express love, loyalty or even treir life strugles. \nIf I were you, I will enjoy listening to: \n\n-Mockingbird -by 'Eminem' \n-Keep Ya Head Up -by '2Pac' \n-Dear Mama -by '2Pac' \n-Al Rissala -by 'Muslim' \n-Mama -by 'Muslim' \nYou can start your journey from here and then explore this art within yourself \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()          
            elif "pop" in music_preference:
                print("Modern pop, there are my suggestions: \n\n-Bad Guy -by 'Billie Eilish' \n-Shake It Off -by 'Taylor Swift' \n-Smooth Criminal -by 'Michael Jackson' \n-On the Floor -by 'Jennifer Lopez' \n\n____________________________________________________________\n____________________________________________________________\n ")              
                conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "jazz" in music_preference:
                print("Sure! here are of  some the iconic songs: \n\n-Take Five -by 'The Dave Brubeck Quartet' \n-So What -by 'Miles Davis' \n-Fly Me to the Moon -by 'Frank Sinatra' \n-My Favorite Things -by 'John Coltrane' \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("What else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()        
            elif "classic" in music_preference:
                print("OH! I admire your taste in music; classical music is a wonderful piece of art. these are my suggestions \n\n-Eine Kleine Nachtmusik -by 'Mozart' \n-Rondo Alla Turca -by 'Mozart' \n-Symphony No.5 -by 'Beethoven \n-Ode to Joy -by 'Beethoven' \n-Bagatelle in a minor Woo 59 or Für Elise -by 'Beethoven' \n-Four seasons -by 'Vilvadi' \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "heavy metal" in music_preference:
                print("Let's see what we have: \n\n-Black Sabbath \n-Iron Maiden \n-Metallica \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()    
            else:
                conversation = input("Sorry our current update don't fulfill your request \n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
        
        elif word_movie in menu_input:
         
            Movies_preference = input("Ah! I see that we have a cinema lover here, which type of movies do you  prefer '"+ name+"' ? \n\n-Action \n-Comedy \n-Drama \n-Fantasy \n-Horror \n-Science Fiction \n-Documentary \n ")  
            if "action" in Movies_preference:
                print("Great! let's see our list of oscar award winners: \n\n-Inception -by 'Christopher Nolan' \n-Braveheart -by 'Mel Gibson' \n-Gladiator -by 'Ridley Scott' \n-The Lord of the Rings: The Return of the King -by 'Peter Jackson' \n-The Dark Knight -by 'Christopher Nolan' \n-The Matrix -by 'Lana Wachowski & Lilly Wachowski' \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "comedy" in Movies_preference:
                print("Ah! it look like a cheerful soul is here,  enjoy : \n-Asal Eswed -by 'Khaled Marei' \n-Excuse My French (La Mo'akhza) -by 'Amr Salama' \n-Green Book -by 'Peter Farrelly' \n-El-Limbi -by 'Wael Ihsan' \n-Shaun of the Dead -by 'Edgar Wright' \n(but the last movie may contain some scary scenes that may be distributing to some people ) \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "drama" in Movies_preference:
                print("OK, here some of the best drama films: \n-The Godfather -by 'Francis Ford Coppola' \n-Forrest Gump -by 'Robert Zemeckis' \n-12 Years a Slave -by 'Steve McQueen' \n-The Departed -by 'Martin Scorsese \n-The King's Speech -by 'Tom Hooper \n\n____________________________________________________________\n____________________________________________________________\n" )
                conversation = input("change to another topic??\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()     
            elif "fantasy" in Movies_preference:
                print("Sure, Take a look: \n-The Lord of the Rings: The Return of the King -by 'Peter Jackson' \n-Kubo and the Two Strings -by 'Travis Knight' \n-The Witcher: Nightmare of the Wolf -by 'Kwang Il Han' \n-Howl’s Moving Castle -by 'Hayao Miyazaki' \n-The Green Knight -by 'David Lowery' \n-Spirited Away -by 'Hayao Miyazaki' \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "horror" in Movies_preference:
                print("Here are my horror films suggestions: \n-The Witch -by 'Robert Eggers' \n-The Babadook -by 'Jennifer Kent' \n-The Conjuring -by 'James Wan' \n-The Others -by 'Alejandro Amenábar' \n Shutter Island -by 'Martin Scorsese' \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "science fiction" in Movies_preference:
                print("That all what I can give for the moment: \n-Interstellar -by 'Christopher Nolan' \n-Ex Machina -by 'Alex Garland' \n-Avatar -by 'James Cameron' \n-The Martian -by 'Ridley Scott' \n-Snowpiercer -by 'Bong Joon-ho' \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("What else??\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()                            
            elif "documentary" in Movies_preference:
                print("Oh, these are my best masterpieces: \n\n-American Factory -by 'Steven Bognar & Julia Reichert' \n-13th -by 'Ava DuVernay' \n-20 Feet Stardom -by 'Morgan Neville' \n-Chasing Ice -by 'Jeff Orlowski' \n-The Great Hack -by 'Karim Amer & Jehane Noujaim' \n-Hackers: Outlaws and Angels -by 'Stephen McGann' \n-DARK WEB: GUNS, Kidnapping & More - The Disturbing Side of the Internet |-by ENDEVR Documentary\n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()    
            else:
                conversation = input("Sorry our current update don't fulfill your request \n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()       
        
        elif word_news in menu_input:
          
            news_preference = input("There is a lot of News to discover, \nPlease give a specific topic to talk about: \n\n-Morocco \n-Africa  \n-Europe \n-Asia \n-Australia \n-North America \n-South America ").lower()
            if "morocco" in news_preference:
                print("Here there are the latest news about Kingdom of Morocco: \n\n-Climate Crisis:\n Morocco faces challenges such as desertification and water scarcity; however, ambitious initiatives like the Green Morocco Plan are helping to modernize agriculture and improve water management, paving the way for a more sustainable future.\n\n-'Environment':\n The nation is investing heavily in renewable energy projects—especially in solar and wind power—to reduce emissions and protect its diverse natural heritage, setting a regional example in environmental stewardship.\n\n-'Science':\n Moroccan research institutions and universities are making strides in areas like renewable energy, sustainable agriculture, and water conservation, building a foundation for future innovation and growth.\n\n-'Global Development':\n By partnering with international organizations, Morocco is focused on improving infrastructure, healthcare, and education, which is crucial for driving inclusive development across both urban and rural communities.\n\n-'Sports':\n Moroccan athletes continue to excel on the international stage, uniting the nation and inspiring a new generation through achievements in football and other sports.\n\n-'Tech':\n The tech landscape in Morocco is rapidly evolving, with emerging start-ups and digital initiatives, particularly in fintech and e-commerce, contributing to economic diversification and modernization.\n\n-'Business':\n With its strategic location and reform-driven policies, Morocco is attracting significant foreign investment in sectors such as tourism, automotive, and agriculture, fostering steady economic growth.\n\n-'Obituaries':\n The country honors the legacy of influential leaders and cultural icons whose contributions have shaped modern Morocco and continue to inspire progress and unity.\n\n-'Politics':\n The Moroccan government is pursuing progressive reforms, strengthening democratic institutions, and expanding diplomatic ties—efforts that are crucial for maintaining stability and addressing ongoing challenges.\n\n-'Wars':\n Committed to peace and security, Morocco actively engages in diplomatic initiatives to resolve regional disputes, and continues to garner international support for its sovereign claim over the Moroccan Sahara, reinforcing its stance through peaceful dialogue. \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "africa" in news_preference:
                print("These are the big headlines on various topics in Africa: \n\n-Climate Crisis:\n Africa is grappling with rising temperatures and unpredictable rainfall that threaten traditional agriculture, while innovative adaptation strategies and renewable energy projects are emerging to build resilience.\n\n-'Environment':\n Efforts to protect biodiversity and manage natural resources are growing, with initiatives aimed at sustainable agriculture and combating deforestation across the continent.\n\n-'Science':\n African research institutions are making strides in renewable energy and healthcare solutions, laying the groundwork for regional innovation and progress.\n\n-'Global Development':\n Collaborative projects with international partners are enhancing infrastructure, education, and healthcare, driving inclusive development in both urban and rural communities.\n\n-'Sports':\n Passion for football and other sports unites nations, with major tournaments like the Africa Cup of Nations inspiring youth and community pride.\n\n-'Tech':\n A burgeoning tech ecosystem—with innovations in fintech and digital services—is opening up new economic opportunities across the continent.\n\n-'Business':\n Economic reforms and targeted investments are strengthening diverse markets, particularly in agriculture, mining, and telecommunications.\n\n-'Obituaries':\n Africa honors the legacies of visionary leaders and cultural icons whose contributions continue to inspire growth and unity.\n\n-'Politics':\n Many African nations are deepening democratic reforms and regional cooperation, even as some grapple with political instability and shifting power dynamics.\n\n-'Wars':\n Despite localized conflicts in regions like the Sahel, ongoing peacebuilding efforts and international mediation are fostering hopes for long-term stability. \n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "europe" in news_preference:
                print("These are the latest news in Europe: \n\n-Climate Crisis:\n Europe is facing intensifying heatwaves and wildfires—especially in the Mediterranean—prompting urgent measures for climate resilience and sustainable energy transitions.\n\n-'Environment':\n Ambitious policies across the EU are reducing carbon emissions and protecting natural landscapes, setting a global benchmark in environmental stewardship.\n\n-'Science':\n European scientists are driving breakthroughs in carbon capture, AI, and space exploration, reinforcing the continent’s role as a leader in global innovation.\n\n-'Global Development':\n Europe actively supports humanitarian aid and sustainable development projects worldwide, while also tackling domestic challenges to ensure social equity.\n\n-'Sports':\n With a rich sporting heritage, European leagues and events like the UEFA Champions League continue to captivate fans and strengthen community ties.\n\n-'Tech':\n A dynamic tech sector—fueled by investments in AI, cybersecurity, and green technologies—is transforming Europe’s digital landscape.\n\n-'Business':\n Strategic economic reforms and fiscal policies are driving growth, even as the region navigates post-pandemic recovery and global market shifts.\n\n-'Obituaries':\n Europe pays homage to influential figures in politics, art, and science whose enduring legacies continue to shape the region.\n\n-'Politics':\n Political debates around EU integration, social reforms, and national sovereignty are actively shaping the continent’s future.\n\n-'Wars':\n While largely peaceful, Europe remains vigilant—with conflicts such as the ongoing situation in Ukraine underscoring the need for strong diplomatic engagement. \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower() 
            elif "asia" in news_preference:
                print("These are the headlines in Asia: \n\n-Climate Crisis:\n Asia faces extreme weather events—from monsoon floods to heatwaves—that disrupt communities, prompting nations to invest in sustainable practices and disaster preparedness.\n\n-'Environment':\n Major economies are tackling pollution and habitat degradation with robust conservation programs and stricter environmental regulations.\n\n-'Science':\n From advanced robotics in Japan to biotechnology breakthroughs in India and South Korea, Asian research institutions are at the forefront of scientific innovation.\n\n-'Global Development':\n Rapid urbanization and economic growth are being balanced with initiatives to improve public services, healthcare, and education, driving inclusive progress.\n\n-'Sports':\n Prestigious events like the Asian Games showcase the region’s athletic talent and foster cultural unity among diverse nations.\n\n-'Tech':\n Asia’s tech industry is booming, with significant investments in AI, 5G, and digital finance positioning the region as a global technology leader.\n\n-'Business':\n Despite economic challenges, vibrant markets across Asia are evolving through reforms, innovation, and expanding international trade.\n\n-'Obituaries':\n The region honors the memory of influential figures in politics, science, and the arts, whose contributions continue to inspire future generations.\n\n-'Politics':\n Dynamic political landscapes—from democratic reforms to regional rivalries—characterize Asia’s governance, with ongoing efforts to balance tradition and modernity.\n\n-'Wars':\n While historical conflicts and border disputes persist in some areas, ongoing diplomatic efforts aim to resolve tensions and secure lasting peace. \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "australia" in news_preference:
                print("Here's a look at the headlines across different areas in Australia: \n\n-Climate Crisis:\n Australia confronts severe bushfires, floods, and heatwaves—effects of climate change that are spurring a strong shift towards renewable energy and climate adaptation measures.\n\n-'Environment':\n Dedicated conservation efforts, such as those protecting the Great Barrier Reef, underscore Australia’s commitment to preserving its unique natural heritage.\n\n-'Science':\n Australian researchers are contributing critical insights in marine biology, climate science, and medicine, enhancing the global scientific community.\n\n-'Global Development':\n Through strategic partnerships, Australia is supporting infrastructure and resilience projects in the Pacific region, reinforcing regional solidarity.\n\n-'Sports':\n With international events like the Australian Open, sports continue to be a vital part of national identity, driving unity and global recognition.\n\n-'Tech':\n A growing startup culture in sectors like cybersecurity and digital health is propelling Australia into a new era of technological innovation.\n\n-'Business':\n Robust sectors such as mining, tourism, and finance are underpinning economic stability, even as the country adapts to evolving global markets.\n\n-'Obituaries':\n Australia honors its cultural and political icons, whose impactful legacies have helped shape the nation’s identity and progress.\n\n-'Politics':\n Ongoing debates over environmental policy, social justice, and economic reform are steering Australia’s political discourse towards a more inclusive future.\n\n-'Wars':\n While not engaged in active conflict, Australia continues to contribute to international peacekeeping and defense partnerships, reinforcing its commitment to global security. \n\n____________________________________________________________\n____________________________________________________________\n ")
                conversation = input("What else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "north america" in news_preference:
                print("Let's see what happennig in Northern America: \n\n-Climate Crisis:\n North America faces a spectrum of challenges—from wildfires in the West to hurricanes in the Southeast—prompting significant investments in resilient infrastructure and clean energy.\n\n-'Environment':\n Both the U.S. and Canada are advancing robust conservation efforts to safeguard natural resources and reduce pollution, protecting expansive ecosystems for future generations.\n\n-'Science':\n With trailblazing research at institutions like NASA and leading universities, North America is driving innovations in space exploration, healthcare, and technology.\n\n-'Global Development':\n Through extensive foreign aid and development programs, the region supports global initiatives to combat poverty and promote educational opportunities worldwide.\n\n-'Sports':\n Iconic events—from the NFL playoffs to international competitions—unite communities and celebrate the vibrant sporting culture across the continent.\n\n-'Tech':\n As home to major tech giants and dynamic startups, North America leads in breakthroughs across AI, cloud computing, and renewable energy innovations.\n\n-'Business':\n A robust economic landscape, fueled by entrepreneurial spirit and dynamic financial markets, underpins North America’s influential role in global commerce.\n\n-'Obituaries':\n The region remembers influential visionaries in politics, arts, and sciences, whose legacies continue to shape cultural and societal progress.\n\n-'Politics':\n Active political debates over healthcare, immigration, and social equity illustrate a vibrant democratic process, even as polarization presents ongoing challenges.\n\n-'Wars':\n Balancing military commitments with diplomatic initiatives, North America plays a strategic role in international defense while working to resolve global conflicts. \n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "south america" in news_preference:
                print("This is what happennig in Southern America: \n\n-Climate Crisis:\n South America is confronting severe climate impacts—from droughts in Brazil to flooding in the Andes—driving urgent calls for sustainable practices and climate resilience.\n\n-'Environment':\n Regional initiatives to safeguard the Amazon and other critical ecosystems are intensifying, with governments implementing policies to curb deforestation and preserve biodiversity.\n\n-'Science':\n Innovative research in biotechnology and renewable energy is emerging from South America, contributing new solutions to both local and global challenges.\n\n-'Global Development':\n Collaborative efforts with international organizations are focused on enhancing infrastructure, education, and healthcare, aiming to reduce inequality across the region.\n\n-'Sports':\n Football remains a unifying force, with events like the Copa América inspiring national pride and uniting diverse communities throughout the continent.\n\n-'Tech':\n An emerging tech scene in countries like Brazil and Argentina is driving growth in fintech and digital innovation, fostering economic diversification.\n\n-'Business':\n Despite challenges such as inflation and fiscal constraints, economic reforms and foreign investments are gradually transforming South American markets.\n\n-'Obituaries':\n The region pays tribute to prominent leaders and cultural figures whose enduring contributions have shaped national identities and inspired future progress.\n\n-'Politics':\n Political transitions and reforms are central to the region’s evolution, as nations strive to balance social justice, economic stability, and democratic governance.\n\n-'Wars':\n While traditional warfare is rare, internal conflicts and regional tensions—such as those seen in Venezuela—continue to influence the security landscape.\n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower() 
            else:
                conversation = input("Sorry our current update don't fulfill your request\n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
       
        elif word_life in menu_input:

            tips_preference = input("Sure, please pick one life skill to talk about: \n\n1- Time Management \n2- Deal with Stress \n3- Build Healthy Habits \n4- Improve Communication Skills \n5- Set Clear Goals \n ").lower()
            if "time management" in tips_preference:
                print("\n1- Time Management \n\n- Steps to Master It: \n >>> Create a to-do list or use a planner to organize your day. \n >>> Prioritize tasks using methods like the Eisenhower Matrix (urgent vs. important). \n >>> Allocate specific time slots for tasks and avoid multitasking. \n\n- Why It’s Worth It: \n >>> You accomplish more in less time, reducing stress and feeling more in control. \n\n- The Price of Neglect: \n >>> You may feel overwhelmed, miss deadlines, and struggle to achieve your goals.\n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "deal with stress" in tips_preference:
                print("\n2- Deal with Stress\n\n - Ways to Conquer It: \n >>> Practice relaxation techniques like deep breathing or meditation.\n >>> Exercise regularly to release endorphins.\n >>> Talk to a trusted friend or seek professional help if needed.\n\n- The Reward of Calmness:\n >>> Reduces the risk of stress-related health issues, such as heart problems or anxiety disorders.\n\n- The Cost of Ignoring It: \n >>> Chronic stress can lead to burnout, mental health issues, and physical illnesses.\n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "build healthy habits" in tips_preference:
                print("\n3- Build Healthy Habits \n\n- Simple Steps to Start: \n >>> Start small by incorporating one new habit at a time (e.g., drinking water every morning).\n >>> Use reminders or habit-tracking apps to stay consistent.\n >>> Reward yourself for milestones achieved. \n\n- The Power of Consistency:\n >>> Over time, small habits compound into significant improvements in your health and well-being. \n\n- The Risks of Neglecting It:\n >>> Poor habits can accumulate and negatively impact your physical and mental health over time.\n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("What else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "improve communication skills" in tips_preference:
                print("\n4- Improve Communication Skills \n\n- How to Make It Work:\n >>> Practice active listening by focusing on the speaker without interrupting.\n >>> Be clear and concise in expressing your thoughts.\n >>> Pay attention to non-verbal cues like body language and tone.\n\n- The Strength in Connection:\n >>> Builds stronger relationships and enhances teamwork and collaboration.\n\n- The Fallout of Avoidance:\n >>> Misunderstandings and conflicts may arise, leading to strained relationships and missed opportunities.\n\n____________________________________________________________\n____________________________________________________________\n")        
                conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
            elif "set clear goals" in tips_preference:   
                print("\n5- Set Clear Goals \n\n- The Path to Clarity:\n >>> Use the SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) to define goals.\n >>> Break larger goals into smaller, actionable steps.\n >>> Regularly review and adjust your goals as needed.\n\n- The Drive to Succeed:\n >>> Provides direction and motivation, making it easier to track and achieve success.\n\n- The Pitfalls of Uncertainty:\n >>> Lack of clarity can lead to aimlessness, decreased motivation, and unfulfilled potential.\n\n____________________________________________________________\n____________________________________________________________\n")
                conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()  
            else:  
                conversation = input("Sorry our current update don't fulfill your request \n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
   
        elif word_python in menu_input:    
            print('\nSometimes, after finishing your tasks on the Algorithmics platform, you may have a lot of time and a lot of energy to practice Python, which is why I would like to suggest what you can do in this case. \n\n-Just take this as a note❗️:\n - Your proficiency in Python does not grow just with your attendance at in-person lessons, but also with your home "hard intelligent work." \nWhat you can do:\n\n-Online sources: \n>>>Try to find a complete course that will be a helpful reminder of Python lessons, and of course, be sure that it will be in English. For example:\n-NetworkChuck (full series for Python) |-Youtube platform \n-Bro code (12h full course on Python) |-Youtube platform \n-freeCodeCamp.org (4h course on Python) |-Youtube platform \n-https://www.w3schools.com/ (a free tutorial for many languages including Python to revise your lessons) \n-Codecademy (Offers structured Python courses with interactive exercises) \n\n-Work Through Tutorials: \n >>> Follow online tutorials or book exercises step by step. Don’t just copy and paste; try to understand the code and modify it.\n\n-Practice Regularly:\n >>> Consistency is key. Even short, regular practice sessions are more effective than infrequent long ones.\n\n-Work on Small Projects: \n >>> Apply your knowledge by building small projects. Here are some ideas:\n-A chatbot (like this one or a higher-quality version). \n-A simple calculator \n-Basic games \n-And much more \n\n-Join Online Communities: \n >>> Participate in online forums, communities (example: Stack Overflow), or meetups to ask questions, share your progress, and learn from others. \n\n\n Of course, everything we’ve broken down here is just a drop in the ocean of what you can do. Just practice consistently, and over time, you will become a professional.\n\n____________________________________________________________\n____________________________________________________________\n')
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
       
        elif word_games in menu_input:
            wished_game = input("\nThese are the games available for now: \n(Please enter the full  name of the game or just the number of the game) \n\n1-Mad Libs. \n2-rock, paper, scissors ").lower()
            if "mad libs" in wished_game or "1" in wished_game:
                ready_yes_no = input("\nHere is a brief explanation about the game:\n >>> You will be asked to enter some words with specific parts of speech (e.g., singular noun, plural noun, adjective, verb, etc.). These words will then be placed randomly into phrases, and we'll see what funny or unexpected results you get! \n\nAre you ready, yes? no?")
                if "yes" in ready_yes_no :

                    from random import *

                    example_number =  randint(1, 7)


                
                    if example_number == 1 : 
                        example_one_adjective = input("\nEnter an 'adjective' ")
                        example_one_noun = input("\nEnter a 'noun' ")
                        example_one_location = input("\nEnter a 'location' ")
                        example_one_adverb = input("\nEnter an 'adverb' ")
                        example_one_verb = input("\nEnter a 'verb' ")
                        print("\nHere is the result after entering the missing words \n\n >>> Yesterday, I saw a “",example_one_adjective,"“elephant eating a “",example_one_noun,"“ in the “",example_one_location,"“. I was feeling very “",example_one_adverb,"“ and decided to “",example_one_verb,"“ my camera to capture the moment. ")
                    
                    elif example_number == 2 :
                        example_two_adjective = input("\nEnter an 'adjective' ")
                        example_two_noun = input("\nEnter a 'noun' ")
                        example_two_verb = input("\nEnter a 'liquid' ")
                        example_two_location = input("\nEnter a 'location' ")
                        print("\nHere is the result after entering the missing words \n\n >>> As I walked into the “",example_two_adjective,"“ restaurant, I tripped on my “", example_two_noun,"“ and spilled my “",example_two_verb,"“ all over the “",example_two_location,"“.")

                    elif  example_number == 3:
                        example_three_celebrity =  input("\nEnter a 'Famous person' ")
                        example_three_verb = input("\nEnter a 'verb' ")
                        example_three_location = input("\nEnter a 'location' ")
                        example_three_adjective = input("\nEnter an 'adjective' ")
                        print("\nHere is the result after entering the missing words \n\n >>> The “",example_three_celebrity,"“ was seen “",example_three_verb,"“ down the “",example_three_location,"“ runway, wearing a “",example_three_adjective,"“ outfit.")
                    
                    elif example_number == 4 :
                        example_four_adverb = input("\nEnter an 'adverb' ")
                        example_four_location = input("\nEnter a 'location' ")
                        print("\nHere is the result after entering the missing words \n\n >>> I felt like I was on a “",example_four_adverb,"“ rollercoaster ride as I navigated the “",example_four_location,"“ obstacle course.")


                    elif example_number == 5 :
                        example_five_adjective = input("\nEnter an 'adjective' ")
                        example_five_noun = input("\nEnter a 'noun' ")
                        example_five_verb = input("\nEnter a 'verb' ")
                        print("\nHere is the result after entering the missing words \n\n >>> As I relaxed on the beach, I couldn’t help but notice the “",example_five_adjective,"“ seagulls flying overhead. Suddenly, a “",example_five_noun,"“ appeared out of nowhere and started “",example_five_verb,"“ in the sand.")

                    elif example_number == 6 :
                        example_six_adjective = input("\nEnter an 'adjective' ")
                        example_six_name = input("\nEnter a 'name' ")
                        example_six_verb = input("\nEnter a 'verb' ")
                        example_six_plural_noun = input("\nEnter a 'plural noun' ")
                        example_six_food_drink = input("\nEnter a 'food/drink' ")
                        print("\nHere is the result after entering the missing words \n\n >>> You’re invited to a “",example_six_adjective,"“ party at “",example_six_name,"“'s house! Come prepared to “",example_six_verb,"“ the night away with “",example_six_plural_noun,"“ and “",example_six_food_drink,"“.")

                    elif  example_number == 7 :
                        example_seven_adjective = input("\nEnter an 'adjective' ")                    
                        example_seven_noun = input("\nEnter a 'noun' ")
                        example_seven_adjective = input("\nEnter an 'adjective' ")
                        print("\nHere is the result after entering the missing words \n\n >>> According to the ancient art of “",example_seven_adjective,"“, your future holds “",example_seven_noun,"“ riches and “",example_seven_adjective,"“ success!")
                    
                    else:
                        conversation = input("\nSorry, our current update can't handle your request. \n\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
               
                elif "no" in ready_yes_no: 
                    conversation = input("Sure, feel free to change to another topic.\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
                else:
                    conversation = input("\nSorry, something went wrong. \n\nPlease resent your request\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
           
           
           
            elif "rock, paper, scissors" in wished_game or "2" in wished_game :
                ready_no_yes = input("\nHere is a brief explanation about the game(even if it very known):\n >>> You will be asked to enter one of the three words (rock, paper, scissors) and I am going to pick a word and we will see who is the winners\n\n  > rock - scissors (rock win) \n  > rock - paper (paper win) \n  > paper - scissors (scissors win) \n\nAre you ready, yes? no?")
                while ready_no_yes == "yes":
                
                    print("\n\n____________________________________________________________\n____________________________________________________________\nThe game begin °_^:\n ")
                    import random

                    options = ("rock", "paper", "scissors")
                    user = None
                    chatbot = random.choice(options)
                    
                    while user not in options:
                        user = input("pick one choice (rock, paper, scissors):")
                
                    print("User choice is :",user)
                    print("My choice is :",chatbot) 

                    if user == "rock" and chatbot == "scissors":
                        print("Oh! you won, I will try my best next time.")
                        ready_no_yes = input("\nRematch time! I’m ready to claim my victory! (yes,no)")

                    elif user == "scissors" and chatbot == "rock":
                        print("And that’s how it’s done! Who’s the best? : Me! -_°")
                        ready_no_yes = input("\nHere we go—get ready to lose, champ! (yes,no)")
                
                    elif user == "paper" and chatbot == "scissors":
                        print("hhhh! I beat you, I knew that I am the best")
                        ready_no_yes = input("\nReady to taste defeat again? (yes,no)")
                
                    elif user == "scissors" and chatbot == "paper":
                        print("Nice one! But watch out, I’m coming back stronger!") 
                        ready_no_yes = input("\nAnother round? Get ready for a comeback!(yes,no)")
                
                
                    elif user == "paper" and chatbot == "rock":
                        print("You won fair and square. Let’s see if I can turn the tables next time!")
                        ready_no_yes = input("\nLet’s do it again—I’m feeling lucky this time!(yes,no)")
                
                    elif user == "rock" and chatbot == "paper":
                        print("Oops! Guess I’m just too good!")
                        ready_no_yes = input("\nAnother round, another win for me! (yes,no)")
                
                
                    elif user == chatbot :
                        print("I think it's a tie")
                        ready_no_yes = input("\nGet ready—this round’s mine! (yes,no)").lower()                    
                if ready_no_yes == "no": 
                    conversation = input("Sure, feel free to change to another topic.\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
                else:
                    conversation = input("\nSorry, something went wrong. \n\nPlease resent your request\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()  
            else:
                conversation = input("\nSorry, our current update can't handle your request. \n\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()


        else:
            conversation = input("\nSorry, something went wrong. \n\nPlease resent your request\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()  
   
    elif word_music in conversation:
        music_preference = input("\nHmm, let see what we have here: \n-Actually it depends on your music preference, which type of music do you  prefer '"+ name+"' ? \n\n-Rap \n-Pop  \n-Jazz \n-Classic music \n-Heavy metal \n ").lower()
        if "rap" in music_preference:
            print("Rap music was always a way for the musiscians to express love, loyalty or even treir life strugles. \nIf I were you, I will enjoy listening to: \n\n-Mockingbird -by 'Eminem' \n-Keep Ya Head Up -by '2Pac' \n-Dear Mama -by '2Pac' \n-Al Rissala -by 'Muslim' \n-Mama -by 'Muslim' \nYou can start your journey from here and then explore this art within yourself \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()          
        elif "pop" in music_preference:
            print("Modern pop, there are my suggestions: \n\n-Bad Guy -by 'Billie Eilish' \n-Shake It Off -by 'Taylor Swift' \n-Smooth Criminal -by 'Michael Jackson' \n-On the Floor -by 'Jennifer Lopez' \n\n____________________________________________________________\n____________________________________________________________\n ")              
            conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "jazz" in music_preference:
            print("Sure! here are of  some the iconic songs: \n\n-Take Five -by 'The Dave Brubeck Quartet' \n-So What -by 'Miles Davis' \n-Fly Me to the Moon -by 'Frank Sinatra' \nMy Favorite Things -by 'John Coltrane' \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("What else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()        
        elif "classic" in music_preference:
            print("OH! I admire your taste in music; classical music is a wonderful piece of art. these are my suggestions \n\n-Eine Kleine Nachtmusik -by 'Mozart' \n-Rondo Alla Turca -by 'Mozart' \n-Symphony No.5 -by 'Beethoven \n-Ode to Joy -by 'Beethoven' \n-Bagatelle in a minor Woo 59 or Für Elise -by 'Beethoven' \n-Four seasons -by 'Vilvadi' \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "heavy metal" in music_preference:
            print("Let's see what we have: \n\n-Black Sabbath \n-Iron Maiden \n-Metallica \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        else:
             conversation = input("Sorry our current update don't fulfill your request \n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
    
    elif word_movie in conversation:

        Movies_preference = input("Ah! I see that we have a cinema lover here, which type of movies do you  prefer '"+ name+"' ? \n\n-Action \n-Comedy \n-Drama \n-Fantasy \n-Horror \n-Science Fiction \n-Documentary \n ")  
        if "action" in Movies_preference:
            print("Great! let's see our list of oscar award winners: \n\n-Inception -by 'Christopher Nolan' \n-Braveheart -by 'Mel Gibson' \n-Gladiator -by 'Ridley Scott' \n-The Lord of the Rings: The Return of the King -by 'Peter Jackson' \n-The Dark Knight -by 'Christopher Nolan' \n-The Matrix -by 'Lana Wachowski & Lilly Wachowski' \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "comedy" in Movies_preference:
            print("Ah! it look like a cheerful soul is here,  enjoy : \n-Asal Eswed -by 'Khaled Marei' \n-Excuse My French (La Mo'akhza) -by 'Amr Salama' \n-Green Book -by 'Peter Farrelly' \n-El-Limbi -by 'Wael Ihsan' \n-Shaun of the Dead -by 'Edgar Wright' \n(but the last movie may contain some scary scenes that may be distributing to some people ) \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "drama" in Movies_preference:
            print("OK, here some of the best drama films: \n-The Godfather -by 'Francis Ford Coppola' \n-Forrest Gump -by 'Robert Zemeckis' \n-12 Years a Slave -by 'Steve McQueen' \n-The Departed -by 'Martin Scorsese \n-The King's Speech -by 'Tom Hooper \n\n____________________________________________________________\n____________________________________________________________\n" )
            conversation = input("change to another topic??\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()     
        elif "fantasy" in Movies_preference:
            print("Sure, Take a look: \n-The Lord of the Rings: The Return of the King -by 'Peter Jackson' \n-Kubo and the Two Strings -by 'Travis Knight' \n-The Witcher: Nightmare of the Wolf -by 'Kwang Il Han' \n-Howl’s Moving Castle -by 'Hayao Miyazaki' \n-The Green Knight -by 'David Lowery' \n-Spirited Away -by 'Hayao Miyazaki' \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "horror" in Movies_preference:
            print("Here are my horror films suggestions: \n-The Witch -by 'Robert Eggers' \n-The Babadook -by 'Jennifer Kent' \n-The Conjuring -by 'James Wan' \n-The Others -by 'Alejandro Amenábar' \n Shutter Island -by 'Martin Scorsese' \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "science fiction" in Movies_preference:
            print("That all what I can give for the moment: \n-Interstellar -by 'Christopher Nolan' \n-Ex Machina -by 'Alex Garland' \n-Avatar -by 'James Cameron' \n-The Martian -by 'Ridley Scott' \n-Snowpiercer -by 'Bong Joon-ho' \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("What else??\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()                            
        elif "documentary" in Movies_preference:
            print("Oh, these are my best masterpieces: \n\n-American Factory -by 'Steven Bognar & Julia Reichert' \n-13th -by 'Ava DuVernay' \n-20 Feet Stardom -by 'Morgan Neville' \n-Chasing Ice -by 'Jeff Orlowski' \n-The Great Hack -by 'Karim Amer & Jehane Noujaim' \n-Hackers: Outlaws and Angels -by 'Stephen McGann' \n-DARK WEB: GUNS, Kidnapping & More - The Disturbing Side of the Internet |-by ENDEVR Documentary\n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()    
        else:
            conversation = input("Sorry our current update don't fulfill your request \n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()

    elif word_news in conversation:

        news_preference = input("There is a lot of News to discover, \nPlease give a specific topic to talk about: \n\n-Morocco \n-Africa  \n-Europe \n-Asia \n-Australia \n-North America \n-South America ").lower()
        if "morocco" in news_preference:
            print("Here there are the latest news about Kindom of Morocco: \n\n-Climate Crisis:\n Morocco continues to combat the effects of desertification and drought, implementing ambitious plans like the Green Morocco Plan to enhance agricultural resilience and water management. \n\n-'Environment':\n Morocco has announced new initiatives to expand its renewable energy projects, particularly in solar and wind power, to reduce its carbon footprint. \n\n-'Science':\n Moroccan universities are advancing research in sustainable agriculture and renewable energy technologies, with partnerships involving international institutions. \n\n-'Global Development':\n Morocco is working with global organizations to improve education and healthcare infrastructure, particularly in rural areas, while enhancing women's access to economic opportunities. \n\n-'Sports':\n Moroccan football teams are excelling in local and international tournaments, with preparations underway for hosting or participating in major global competitions. \n\n-'Tech':\n Morocco is becoming a regional tech hub, focusing on e-commerce and digital transformation, with new government incentives to attract startups. \n\n-'Business':\n Moroccan industries, especially in automotive and agriculture, are seeing growth, with increased exports and foreign investment in key sectors. \n\n-'Obituaries':\n Morocco mourns the loss of prominent cultural and political figures who have significantly contributed to national development. \n\n-'Politics':\n The Moroccan government is focusing on constitutional reforms, economic development, and fostering stronger diplomatic relations, particularly within Africa and the Arab world. Iraq's recent recognition of the Moroccan Sahara adds to the growing international support for Morocco's sovereignty over the region. \n\n-'Wars':\n Morocco remains committed to peaceful diplomacy and is actively engaging in international efforts to resolve conflicts, while continuing to strengthen its position on the Moroccan Sahara issue through global partnerships. \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "africa" in news_preference:
            print("These are the big headlines on various topics in Africa: \n\n-'Climate Crisis':\n   Africa is experiencing severe droughts and rising temperatures, with significant impacts on agriculture, water resources, and food security. (e.g., Southern Africa faces worsening drought conditions) \n\n-'Environment':\n   In Kenya, new efforts are being made to conserve wildlife, with the establishment of new protected areas to combat poaching and habitat loss. \n\n-'Science': \n   African researchers are working on solar-powered solutions to provide electricity to rural areas, helping to improve energy access across the continent. \n\n-'Global Development': \n   African countries are working with international organizations to enhance healthcare and education systems, with a focus on improving living standards. \n\n-'Sports': \n   The African Cup of Nations football tournament is set to begin, with countries from across the continent preparing for the prestigious competition. \n\n-'Tech': \n   African tech startups are innovating in mobile banking and blockchain technologies, especially in Kenya and Nigeria. \n\n-'Business': \n   A number of African countries are implementing economic reforms to boost trade, infrastructure, and attract foreign investment.\n\n-'Obituaries': \n   The continent mourns the passing of prominent political and cultural figures who have contributed to Africa’s growth and development.\n\n-'Politics': \n   Several African countries, including Mali and Burkina Faso, are grappling with political instability and the rise of military coups.\n\n-'Wars': \n   Conflicts in regions like the Sahel, Ethiopia, and the Democratic Republic of Congo continue to affect millions of people, with international efforts to mediate peace. \n\n____________________________________________________________\n____________________________________________________________\n")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "europe" in news_preference:
            print("These are the latest news in Europe: \n\n-'Climate Crisis':\n Europe is experiencing increasing heatwaves and wildfires, particularly in Southern countries like Greece and Spain, due to higher-than-average summer temperatures. \n\n-'Environment':\n The European Union has introduced stricter emissions regulations and carbon taxes to reduce its carbon footprint and promote green energy. \n\n-'Science':\n European scientists have developed cutting-edge carbon capture technologies aimed at reducing atmospheric CO2 levels. \n\n-'Global Development':\n The European Union continues to provide humanitarian aid and support for sustainable development projects in developing countries, especially in Africa. \n\n-'Sports':\n The UEFA Champions League continues to showcase the best football clubs in Europe, with top teams vying for the prestigious title. \n\n-'Tech':\n European tech companies are advancing in the AI field, with countries like Germany and France leading in AI research and development. \n\n-'Business':\n The European Central Bank has raised interest rates in response to inflationary pressures, impacting businesses and consumers across the eurozone. \n\n-'Obituaries':\n Europe mourns the loss of influential political figures, including notable heads of state and social activists who have shaped the region’s policies. \n\n-'Politics':\n Political debates are heating up in Europe, especially in the UK over the ongoing effects of Brexit and in Poland regarding judicial reforms. \n\n-'Wars':\n The war in Ukraine continues to dominate European politics, with ongoing international sanctions on Russia and efforts to support Ukraine’s defense. \n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower() 
        elif "asia" in news_preference:
            print("These are the headlines in Asia: \n\n-'Climate Crisis':\n Asia faces extreme weather events, including flooding in Southeast Asia and severe heatwaves in parts of India and Pakistan. \n\n-'Environment':\n China is making strides in combatting air pollution through green energy projects and tightening regulations on industrial emissions. \n\n-'Science':\n Japanese scientists are leading research in robotics, with innovations set to transform industries like healthcare and manufacturing. \n\n-'Global Development':\n India is expanding its renewable energy capacity, aiming to become a global leader in solar energy production. \n\n-'Sports':\n The Asian Games saw groundbreaking achievements, with countries like China, Japan, and South Korea excelling in athletics and gymnastics. \n\n-'Tech':\n South Korea’s tech industry is investing heavily in AI and 5G technologies, positioning the country as a global tech leader. \n\n-'Business':\n China is navigating a challenging economic landscape with reforms aimed at stabilizing its real estate market and boosting domestic consumption. \n\n-'Obituaries':\n The passing of influential figures in politics, science, and culture from across the continent, such as renowned Asian diplomats and innovators. \n\n-'Politics':\n Tensions continue to rise in Asia, with political conflicts between China and Taiwan, as well as ongoing issues in Myanmar and Hong Kong. \n\n-'Wars':\n >>> The conflict in Afghanistan persists in the aftermath of the U.S. withdrawal, while tensions between India and Pakistan remain high over disputed regions like Kashmir.\n >>> The genocide in Gaza in being continued by the occupied forces 'israel', resulting in over 45,000 death and thousands of injuries, most of them children and women.\nFurthermore, there is a silence that lingers, further breaking the spirit of the Palestinian people. Despite the order of the International Court of Justice for Israel to stop the genocide, occupied forces has continued the destruction and murder in Palestine. \nThis raises the question: Is Israel above the law?\n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "australia" in news_preference:
            print("Here's a look at the headlines across different areas in Australia: \n\n-'Climate Crisis':\n Australia is battling severe bushfires and floods, both intensified by climate change, threatening communities and biodiversity. \n\n-'Environment':\n The Australian government is investing in renewable energy and conservation efforts to protect the Great Barrier Reef from further damage. \n\n-'Science':\n Australian scientists have made breakthroughs in marine biology, discovering new species and exploring ocean ecosystems. \n\n-'Global Development':\n Australia is focusing on Pacific Island nations, providing financial support for climate change resilience and infrastructure development. \n\n-'Sports':\n The Australian Open tennis tournament is drawing attention with top global players competing for the title. \n\n-'Tech':\n Australia is fostering innovation in tech startups, especially in fields like cybersecurity and AI, to bolster its digital economy. \n\n-'Business':\n The Australian stock market is experiencing growth, with mining and technology sectors showing strong performance. \n\n-'Obituaries':\n Australia has lost notable figures in politics, sports, and entertainment, with tributes pouring in for those who shaped the nation's history. \n\n-'Politics':\n The Australian government faces growing pressure over climate change action and environmental policies, with elections on the horizon. \n\n-'Wars':\n Australia's role in international peacekeeping missions continues, particularly in conflict zones such as Afghanistan and the Pacific region.\n\n____________________________________________________________\n____________________________________________________________\n ")
            conversation = input("What else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "north america" in news_preference:
            print("Let's see what happennig in Northern America: \n\n-'Climate Crisis':\n The United States and Canada are facing wildfires, heatwaves, and hurricanes, with growing concerns about the future of natural resources. \n\n-'Environment':\n Canada is taking significant steps to protect its boreal forests and limit resource extraction to preserve biodiversity. \n\n-'Science':\n NASA has successfully landed a rover on Mars, advancing our understanding of the planet's geology and potential for life. \n\n-'Global Development':\n The U.S. is ramping up its foreign aid programs, with a focus on helping developing countries in Africa and Latin America combat poverty and disease. \n\n-'Sports':\n The NFL playoffs are underway, with intense competition as teams aim for the Super Bowl. \n\n-'Tech':\n The U.S. continues to lead in tech innovation, with major breakthroughs in artificial intelligence and space exploration. \n\n-'Business':\n The U.S. economy is showing strong growth, with record highs in the stock market and increasing consumer spending. \n\n-'Obituaries':\n The U.S. has mourned the loss of iconic cultural figures, including artists, politicians, and activists. \n\n-'Politics':\n The U.S. continues to face political polarization, with debates over issues like healthcare, immigration, and election security. \n\n-'Wars':\n The U.S. is involved in military operations in the Middle East, particularly in support of Ukraine, while addressing ongoing tensions with China over Taiwan. \n ")
            conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "south america" in news_preference:
            print("This is what happennig in Southern America: \n\n-'Climate Crisis':\n Brazil is facing severe droughts in the Amazon, with impacts on water supplies and agricultural production. \n\n-'Environment':\n Argentina has announced stricter environmental protection policies to combat deforestation in the Amazon and other vital ecosystems. \n\n-'Science':\n In Colombia, researchers have made significant advances in medicine, focusing on diseases that disproportionately affect the region. \n\n-'Global Development':\n South American countries are collaborating with international organizations to improve education and healthcare systems across the continent. \n\n-'Sports':\n Football is the dominant sport in South America, with the Copa América continuing to excite fans across the continent. \n\n-'Tech':\n Brazil is emerging as a tech hub in Latin America, with a growing number of startups focused on fintech and digital services. \n\n-'Business':\n The economic outlook for South America remains cautious, with inflation and debt levels affecting countries like Argentina and Venezuela. \n\n-'Obituaries':\n South America has lost prominent leaders, cultural figures, and activists who have played key roles in shaping the continent’s history. \n\n-'Politics':\n Political instability continues in countries like Venezuela, where there are ongoing protests and power struggles, while Chile and Brazil are focusing on economic reforms. \n\n-'Wars':\n Venezuela’s ongoing political and economic crisis has led to social unrest and border conflicts with neighboring Colombia.\n\n____________________________________________________________\n____________________________________________________________\n")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower() 
        else:
            conversation = input("Sorry our current update don't fulfill your request\n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()

    elif word_life in conversation:
        tips_preference = input("Sure, please pick one life skill to talk about: \n\n1- Time Management \n2- Deal with Stress \n3- Build Healthy Habits \n4- Improve Communication Skills \n5- Set Clear Goals \n ").lower()
        if "time management" in tips_preference:
            print("\n1- Time Management \n\n- Steps to Master It: \n >>> Create a to-do list or use a planner to organize your day. \n >>> Prioritize tasks using methods like the Eisenhower Matrix (urgent vs. important). \n >>> Allocate specific time slots for tasks and avoid multitasking. \n\n- Why It’s Worth It: \n >>> You accomplish more in less time, reducing stress and feeling more in control. \n\n- The Price of Neglect: \n >>> You may feel overwhelmed, miss deadlines, and struggle to achieve your goals.\n\n____________________________________________________________\n____________________________________________________________\n")
            conversation = input("change to another topic?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "deal with stress" in tips_preference:
            print("\n2- Deal with Stress\n\n - Ways to Conquer It: \n >>> Practice relaxation techniques like deep breathing or meditation.\n >>> Exercise regularly to release endorphins.\n >>> Talk to a trusted friend or seek professional help if needed.\n\n- The Reward of Calmness:\n >>> Reduces the risk of stress-related health issues, such as heart problems or anxiety disorders.\n\n- The Cost of Ignoring It: \n >>> Chronic stress can lead to burnout, mental health issues, and physical illnesses.\n\n____________________________________________________________\n____________________________________________________________\n")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "build healthy habits" in tips_preference:
            print("\n3- Build Healthy Habits \n\n- Simple Steps to Start: \n >>> Start small by incorporating one new habit at a time (e.g., drinking water every morning).\n >>> Use reminders or habit-tracking apps to stay consistent.\n >>> Reward yourself for milestones achieved. \n\n- The Power of Consistency:\n >>> Over time, small habits compound into significant improvements in your health and well-being. \n\n- The Risks of Neglecting It:\n >>> Poor habits can accumulate and negatively impact your physical and mental health over time.\n\n____________________________________________________________\n____________________________________________________________\n")
            conversation = input("What else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "improve communication skills" in tips_preference:
            print("\n4- Improve Communication Skills \n\n- How to Make It Work:\n >>> Practice active listening by focusing on the speaker without interrupting.\n >>> Be clear and concise in expressing your thoughts.\n >>> Pay attention to non-verbal cues like body language and tone.\n\n- The Strength in Connection:\n >>> Builds stronger relationships and enhances teamwork and collaboration.\n\n- The Fallout of Avoidance:\n >>> Misunderstandings and conflicts may arise, leading to strained relationships and missed opportunities.\n\n____________________________________________________________\n____________________________________________________________\n")        
            conversation = input("Anything speacial you would recommend?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
        elif "set clear goals" in tips_preference:   
            print("\n5- Set Clear Goals \n\n- The Path to Clarity:\n >>> Use the SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound) to define goals.\n >>> Break larger goals into smaller, actionable steps.\n >>> Regularly review and adjust your goals as needed.\n\n- The Drive to Succeed:\n >>> Provides direction and motivation, making it easier to track and achieve success.\n\n- The Pitfalls of Uncertainty:\n >>> Lack of clarity can lead to aimlessness, decreased motivation, and unfulfilled potential.\n\n____________________________________________________________\n____________________________________________________________\n")
            conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()  
        else:  
            conversation = input("Sorry our current update don't fulfill your request \n\n >>>Please How can I help?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()

    elif word_python in conversation:  

        print('\nSometimes, after finishing your tasks on the Algorithmics platform, you may have a lot of time and a lot of energy to practice Python, which is why I would like to suggest what you can do in this case. \n\n-Just take this as a note❗️:\n - Your proficiency in Python does not grow just with your attendance at in-person lessons, but also with your home "hard intelligent work." \nWhat you can do:\n\n-Online sources: \n>>>Try to find a complete course that will be a helpful reminder of Python lessons, and of course, be sure that it will be in English. For example:\n-NetworkChuck (full series for Python) |-Youtube platform \n-Bro code (12h full course on Python) |-Youtube platform \n-freeCodeCamp.org (4h course on Python) |-Youtube platform \n-https://www.w3schools.com/ (a free tutorial for many languages including Python to revise your lessons) \n-Codecademy (Offers structured Python courses with interactive exercises) \n\n-Work Through Tutorials: \n >>> Follow online tutorials or book exercises step by step. Don’t just copy and paste; try to understand the code and modify it.\n\n-Practice Regularly:\n >>> Consistency is key. Even short, regular practice sessions are more effective than infrequent long ones.\n\n-Work on Small Projects: \n >>> Apply your knowledge by building small projects. Here are some ideas:\n-A chatbot (like this one or a higher-quality version). \n-A simple calculator \n-Basic games \n-And much more \n\n-Join Online Communities: \n >>> Participate in online forums, communities (example: Stack Overflow), or meetups to ask questions, share your progress, and learn from others. \n\n\n Of course, everything we’ve broken down here is just a drop in the ocean of what you can do. Just practice consistently, and over time, you will become a professional.\n\n____________________________________________________________\n____________________________________________________________\n')
        conversation = input("Anything else?\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower() 
      
    elif word_games in conversation:
            wished_game = input("\nThese are the games available for now: \n(Please enter the full  name of the game or just the number of the game) \n\n1-Mad Libs. \n2-rock, paper, scissors ").lower()
            if "mad libs" in wished_game or "1" in wished_game :
                ready_yes_no = input("\nHere is a brief explanation about the game:\n >>> You will be asked to enter some words with specific parts of speech (e.g., singular noun, plural noun, adjective, verb, etc.). These words will then be placed randomly into phrases, and we'll see what funny or unexpected results you get! \n\n-Are you ready, yes? no?")
                if "yes" in ready_yes_no :
                    from random import *

                    example_number =  randint(1, 7)
                    if example_number == 1 : 
                        example_one_adjective = input("\nEnter an 'adjective' ")
                        example_one_noun = input("\nEnter a 'noun' ")
                        example_one_location = input("\nEnter a 'location' ")
                        example_one_adverb = input("\nEnter an 'adverb' ")
                        example_one_verb = input("\nEnter a 'verb' ")
                        print("\nHere is the result after entering the missing words \n\n >>> Yesterday, I saw a “",example_one_adjective,"“elephant eating a “",example_one_noun,"“ in the “",example_one_location,"“. I was feeling very “",example_one_adverb,"“ and decided to “",example_one_verb,"“ my camera to capture the moment. ")
                    elif example_number == 2 :
                        example_two_adjective = input("\nEnter an 'adjective' ")
                        example_two_noun = input("\nEnter a 'noun' ")
                        example_two_verb = input("\nEnter a 'liquid' ")
                        example_two_location = input("\nEnter a 'location' ")
                        print("\nHere is the result after entering the missing words \n\n >>> As I walked into the “",example_two_adjective,"“ restaurant, I tripped on my “", example_two_noun,"“ and spilled my “",example_two_verb,"“ all over the “",example_two_location,"“.")

                    elif example_number == 3 :
                        example_three_celebrity =  input("\nEnter a 'Famous person' ")
                        example_three_verb = input("\nEnter a 'verb' ")
                        example_three_location = input("\nEnter a 'location' ")
                        example_three_adjective = input("\nEnter an 'adjective' ")
                        print("\nHere is the result after entering the missing words \n\n >>> The “",example_three_celebrity,"“ was seen “",example_three_verb,"“ down the “",example_three_location,"“ runway, wearing a “",example_three_adjective,"“ outfit.")
                    
                    elif example_number == 4 :
                        example_four_adverb = input("\nEnter an 'adverb' ")
                        example_four_location = input("\nEnter a 'location' ")
                        print("\nHere is the result after entering the missing words \n\n >>> I felt like I was on a “",example_four_adverb,"“ rollercoaster ride as I navigated the “",example_four_location,"“ obstacle course.")


                    elif example_number == 5 :
                        example_five_adjective = input("\nEnter an 'adjective' ")
                        example_five_noun = input("\nEnter a 'noun' ")
                        example_five_verb = input("\nEnter a 'verb' ")
                        print("\nHere is the result after entering the missing words \n\n >>> As I relaxed on the beach, I couldn’t help but notice the “",example_five_adjective,"“ seagulls flying overhead. Suddenly, a “",example_five_noun,"“ appeared out of nowhere and started “",example_five_verb,"“ in the sand.")

                    elif example_number == 6 :
                        example_six_adjective = input("\nEnter an 'adjective' ")
                        example_six_name = input("\nEnter a 'name' ")
                        example_six_verb = input("\nEnter a 'verb' ")
                        example_six_plural_noun = input("\nEnter a 'plural noun' ")
                        example_six_food_drink = input("\nEnter a 'food/drink' ")
                        print("\nHere is the result after entering the missing words \n\n >>> You’re invited to a “",example_six_adjective,"“ party at “",example_six_name,"“'s house! Come prepared to “",example_six_verb,"“ the night away with “",example_six_plural_noun,"“ and “",example_six_food_drink,"“.")

                    elif example_number == 7 :
                        example_seven_adjective = input("\nEnter an 'adjective' ")                    
                        example_seven_noun = input("\nEnter a 'noun' ")
                        example_seven_adjective = input("\nEnter an 'adjective' ")
                        print("\nHere is the result after entering the missing words \n\n >>> According to the ancient art of “",example_seven_adjective,"“, your future holds “",example_seven_noun,"“ riches and “",example_seven_adjective,"“ success!")
               
                    else:
                        conversation = input("\nSorry, our current update can't handle your request. \n\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
               
                elif "no" in ready_yes_no: 
                    conversation = input("Sure, feel free to change to another topic.\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
                else:
                    conversation = input("\nSorry, something went wrong. \n\nPlease resent your request\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()
           
            elif "rock, paper, scissors" in wished_game or "2" in wished_game :
                ready_no_yes = input("\nHere is a brief explanation about the game(even if it very known):\n >>> You will be asked to enter one of the three words (rock, paper, scissors) and I am going to pick a word and we will see who is the winners\n\n  > rock - scissors (rock win) \n  > rock - paper (paper win) \n  > paper - scissors (scissors win) \n\nAre you ready, yes? no?")
                while ready_no_yes == "yes":
                
                    print("\n\n____________________________________________________________\n____________________________________________________________\nThe game begin °_^:\n ")
                    import random

                    options = ("rock", "paper", "scissors")
                    user = None
                    chatbot = random.choice(options)
                    
                    while user not in options:
                        user = input("pick one choice (rock, paper, scissors):")
                
                    print("User choice is :",user)
                    print("My choice is :",chatbot) 

                    if user == "rock" and chatbot == "scissors":
                        print("Oh! you won, I will try my best next time.")
                        ready_no_yes = input("\nRematch time! I’m ready to claim my victory! (yes,no)")

                    elif user == "scissors" and chatbot == "rock":
                        print("And that’s how it’s done! Who’s the best? : Me! -_°")
                        ready_no_yes = input("\nHere we go—get ready to lose, champ! (yes,no)")
                
                    elif user == "paper" and chatbot == "scissors":
                        print("hhhh! I beat you, I knew that I am the best")
                        ready_no_yes = input("\nReady to taste defeat again? (yes,no)")
                
                    elif user == "scissors" and chatbot == "paper":
                        print("Nice one! But watch out, I’m coming back stronger!") 
                        ready_no_yes = input("\nAnother round? Get ready for a comeback!(yes,no)")
                             
                
                    elif user == "paper" and chatbot == "rock":
                        print("You won fair and square. Let’s see if I can turn the tables next time!")
                        ready_no_yes = input("\nLet’s do it again—I’m feeling lucky this time!(yes,no)")
                
                    elif user == "rock" and chatbot == "paper":
                        print("Oops! Guess I’m just too good!")
                        ready_no_yes = input("\nAnother round, another win for me! (yes,no)")
                
                
                    elif user == chatbot :
                        print("I think it's a tie")
                        ready_no_yes = input("\nGet ready—this round’s mine! (yes,no)").lower()                    
                if ready_no_yes == "no": 
                    conversation = input("Sure, feel free to change to another topic.\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)\n ").lower()
                else:
                    conversation = input("\nSorry, something went wrong. \n\nPlease resent your request\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()  
           
           
            else:
                conversation = input("\nSorry, our current update can't handle your request. \n\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()


    else:
        conversation = input("\nSorry, something went wrong. \n\nPlease resent your request\n(write 'end' to finish the conversation) \n(write 'menu' if you want my suggetions)").lower()


end = time()
time_calculation_seconds = end - start

if time_calculation_seconds <60:
    
    print("【 We've been talking for",int(time_calculation_seconds),"s 】 \nThank you for trying our chatbot,\nPlease feel free to give us feedback if you have faced issues, or any suggestions about news updates\n\n   Your thoughts matter to us ❤️❤️❤️ ")
elif time_calculation_seconds >= 60:
    time_calculation_minutes = time_calculation_seconds // 60 
    seconds_remainder = int(time_calculation_seconds % 60)
    print("【 We've been talking for",time_calculation_minutes,"min and",int(time_calculation_seconds) ,"s 】 \nThank you for trying our chatbot,\nPlease feel free to give us feedback if you have faced issues, or any suggestions about news updates\n\n   Your thoughts matter to us ❤️❤️❤️ ")
elif time_calculation_minutes >=60:
    time_calculation_hours = time_calculation_minutes // 60
    minutes_remainder = time_calculation_minutes % 60
    print("【 We've been talking for",time_calculation_hours ,"h and",time_calculation_minutes,"min and",int(time_calculation_seconds) ,"s 】\nThank you for trying our chatbot,\nPlease feel free to give us feedback if you have faced issues, or any suggestions about news updates\n\n   Your thoughts matter to us ❤️❤️❤️ ")

