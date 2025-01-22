from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, MessageHandler, filters
import random

# Expanded Data for the bot
billionaires = [
    {"name": "Jeff Bezos", "title": "Founder of Amazon", "net_worth": "$120B", "quote": "If you double the number of experiments you do per year, you’re going to double your inventiveness."},
    {"name": "Elon Musk", "title": "CEO of Tesla and SpaceX", "net_worth": "$200B", "quote": "When something is important enough, you do it even if the odds are not in your favor."},
    {"name": "Warren Buffett", "title": "Investor", "net_worth": "$118B", "quote": "Price is what you pay. Value is what you get."},
    {"name": "Bill Gates", "title": "Co-founder of Microsoft", "net_worth": "$115B", "quote": "Success is a lousy teacher. It seduces smart people into thinking they can't lose."},
    {"name": "Bernard Arnault", "title": "Chairman of LVMH", "net_worth": "$180B", "quote": "Luxury goods are the only area in which it is possible to make luxury margins."},
    {"name": "Mark Zuckerberg", "title": "Founder of Facebook", "net_worth": "$100B", "quote": "The biggest risk is not taking any risk."},
    {"name": "Larry Ellison", "title": "Co-founder of Oracle", "net_worth": "$108B", "quote": "When you innovate, you've got to be prepared for people telling you that you are nuts."},
    {"name": "Larry Page", "title": "Co-founder of Google", "net_worth": "$100B", "quote": "Always deliver more than expected."},
    {"name": "Sergey Brin", "title": "Co-founder of Google", "net_worth": "$96B", "quote": "Solving big problems is easier than solving little problems."},
    {"name": "Steve Jobs", "title": "Co-founder of Apple", "net_worth": "Legacy", "quote": "Innovation distinguishes between a leader and a follower."},
    {"name": "Oprah Winfrey", "title": "Media Mogul", "net_worth": "$2.5B", "quote": "The biggest adventure you can take is to live the life of your dreams."},
    {"name": "Richard Branson", "title": "Founder of Virgin Group", "net_worth": "$4B", "quote": "Business opportunities are like buses, there’s always another one coming."},
    {"name": "Amancio Ortega", "title": "Founder of Zara", "net_worth": "$70B", "quote": "The customer is the one who decides what fashion is."},
    {"name": "Carlos Slim Helu", "title": "Business Magnate", "net_worth": "$80B", "quote": "Maintain austerity in times of prosperity."},
    {"name": "Michael Bloomberg", "title": "Founder of Bloomberg LP", "net_worth": "$70B", "quote": "Don’t be afraid to assert yourself, have confidence in your abilities."},
    {"name": "Jack Ma", "title": "Founder of Alibaba", "net_worth": "$40B", "quote": "Never give up. Today is hard, tomorrow will be worse, but the day after tomorrow will be sunshine."},
    {"name": "Larry Fink", "title": "CEO of BlackRock", "net_worth": "$1B", "quote": "The biggest threat to our economy is inequality."},
    {"name": "Elon Musk", "title": "CEO of Tesla and SpaceX", "net_worth": "$200B", "quote": "Some people don't like change, but you need to embrace change if the alternative is disaster."},
    {"name": "Tim Cook", "title": "CEO of Apple", "net_worth": "$1.5B", "quote": "Let your joy be in your journey—not in some distant goal."},
    {"name": "Jeff Weiner", "title": "Executive Chairman of LinkedIn", "net_worth": "$2B", "quote": "Leadership is about making others better as a result of your presence and making sure that impact lasts in your absence."},
    {"name": "Indra Nooyi", "title": "Former CEO of PepsiCo", "net_worth": "$290M", "quote": "The glass ceiling will go away when women help other women break through it."},
    {"name": "Sundar Pichai", "title": "CEO of Alphabet (Google)", "net_worth": "$1.5B", "quote": "A lot of companies don't succeed over time. What do they fundamentally do wrong? They usually miss the future."},
    {"name": "Sheryl Sandberg", "title": "Former COO of Facebook", "net_worth": "$1.8B", "quote": "In the future, there will be no female leaders. There will just be leaders."},
    {"name": "Reed Hastings", "title": "Co-founder of Netflix", "net_worth": "$5B", "quote": "Do not tolerate brilliant jerks. The cost to teamwork is too high."},
    {"name": "Evan Spiegel", "title": "Co-founder of Snapchat", "net_worth": "$2B", "quote": "If you’re not doing something that you’re passionate about, you’re not going to put in the work."},
    {"name": "Richard Li", "title": "Chairman of PCCW", "net_worth": "$33B", "quote": "A good businessman makes others believe in him."},
    {"name": "Jeff Yass", "title": "Co-founder of 3G Capital", "net_worth": "$18B", "quote": "You don’t need to have everything figured out to take the first step."},
    {"name": "Stephen Schwarzman", "title": "CEO of Blackstone", "net_worth": "$21B", "quote": "You have to be able to deal with adversity and learn from it."},
    {"name": "Larry Ellison", "title": "Co-founder of Oracle", "net_worth": "$108B", "quote": "When you innovate, you've got to be prepared for people telling you that you are nuts."},
    {"name": "Mark Cuban", "title": "Owner of Dallas Mavericks", "net_worth": "$4.5B", "quote": "Work like there is someone working 24 hours a day to take it all away from you."},
    {"name": "Paul Allen", "title": "Co-founder of Microsoft", "net_worth": "Deceased", "quote": "The value of a company is a function of how good the company is at innovation."},
    {"name": "Michael Dell", "title": "Founder of Dell Technologies", "net_worth": "$38B", "quote": "You can never make the same mistake twice unless you fail to learn from it."},
    {"name": "John Malone", "title": "Chairman of Liberty Media", "net_worth": "$9.4B", "quote": "The key to success is being prepared to make mistakes."},
    {"name": "George Soros", "title": "Investor", "net_worth": "$8B", "quote": "I am only rich because I know when I’m wrong."},
    {"name": "Tom Steyer", "title": "Investor", "net_worth": "$1.6B", "quote": "If you have enough people who care, you can change the world."},
    {"name": "Eli Broad", "title": "Co-founder of KB Home", "net_worth": "$6.9B", "quote": "I don’t believe in retiring. I just believe in staying busy."},
    {"name": "Dustin Moskovitz", "title": "Co-founder of Facebook", "net_worth": "$20B", "quote": "The future will be about making big, long-term decisions."},
    {"name": "Brian Chesky", "title": "Co-founder of Airbnb", "net_worth": "$11.5B", "quote": "Don't be afraid to start small."},
    {"name": "Travis Kalanick", "title": "Co-founder of Uber", "net_worth": "$5.8B", "quote": "It’s always too early to quit."},
    {"name": "Jack Dorsey", "title": "Co-founder of Twitter", "net_worth": "$5B", "quote": "Make decisions quickly, adjust them slowly."},
    {"name": "Bobby Murphy", "title": "Co-founder of Snapchat", "net_worth": "$2B", "quote": "Focus on making the product something that people want."},
    {"name": "Evan Williams", "title": "Co-founder of Twitter", "net_worth": "$2B", "quote": "It’s better to have a small percentage of something big, than a big percentage of something small."},
    {"name": "Arianna Huffington", "title": "Founder of Huffington Post", "net_worth": "$100M", "quote": "Success is not about climbing the ladder; it’s about how you get there."},
    {"name": "Andrew Carnegie", "title": "Steel Magnate", "net_worth": "Deceased", "quote": "The man who dies rich dies disgraced."},
    {"name": "Thomas Edison", "title": "Inventor", "net_worth": "Deceased", "quote": "Genius is one percent inspiration, ninety-nine percent perspiration."},
    {"name": "Ralph Lauren", "title": "Fashion Designer", "net_worth": "$7B", "quote": "I don’t design clothes. I design dreams."},
    {"name": "Diane Hendricks", "title": "Chairman of ABC Supply", "net_worth": "$9B", "quote": "To succeed, you have to be passionate and persistent."},
    {"name": "Steve Ballmer", "title": "Former CEO of Microsoft", "net_worth": "$85B", "quote": "Greatness is a lot of small things done well."},
    {"name": "Phil Knight", "title": "Co-founder of Nike", "net_worth": "$44B", "quote": "The only time to be positive you’re in the right position is when you’re on the edge."},
    {"name": "Sara Blakely", "title": "Founder of Spanx", "net_worth": "$1.2B", "quote": "You can never be too busy to dream."},
    {"name": "Jack Ma", "title": "Founder of Alibaba", "net_worth": "$40B", "quote": "If you don't give up, you still have a chance."},
    {"name": "Catherine McKenna", "title": "Canadian Minister", "net_worth": "$1.5B", "quote": "Building strong economies requires investing in people."}
]



quotes = [
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Don’t be afraid to give up the good to go for the great. - John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "Your income is directly related to your philosophy, not the economy. - Jim Rohn",
    "You must gain control over your money or the lack of it will forever control you. - Dave Ramsey",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "It’s not whether you get knocked down; it’s whether you get up. - Vince Lombardi",
    "If you really look closely, most overnight successes took a long time. - Steve Jobs",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "Do not be embarrassed by your failures, learn from them and start again. - Richard Branson",
    "Opportunities don't happen, you create them. - Chris Grosser",
    "Don’t let the fear of losing be greater than the excitement of winning. - Robert Kiyosaki",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "You only live once, but if you do it right, once is enough. - Mae West",
    "Success is how high you bounce when you hit bottom. - George S. Patton",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Don't wait for opportunity. Create it. - Unknown",
    "Nothing will work unless you do. - Maya Angelou",
    "Dream big and dare to fail. - Norman Vaughan",
    "I am not a product of my circumstances. I am a product of my decisions. - Stephen Covey",
    "The secret of getting ahead is getting started. - Mark Twain",
    "The best way to predict the future is to create it. - Peter Drucker",
    "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
    "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
    "Do one thing every day that scares you. - Eleanor Roosevelt",
    "Don't be afraid to give up the good to go for the great. - John D. Rockefeller",
    "The journey of a thousand miles begins with one step. - Lao Tzu",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
    "Act as if what you do makes a difference. It does. - William James",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "You can't cross the sea merely by standing and staring at the water. - Rabindranath Tagore",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is the sum of small efforts, repeated day in and day out. - Robert Collier",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "A person who never made a mistake never tried anything new. - Albert Einstein",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Don’t count the days, make the days count. - Muhammad Ali",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Failure is not the opposite of success, it is part of success. - Arianna Huffington",
    "Success is how you bounce back from failure. - Unknown",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman"
]


facts = [
    "The top 1% of earners globally own more than 40% of the world’s wealth.",
    "There are over 2,600 billionaires in the world today.",
    "The richest 10% of the global population owns 76% of the world’s wealth.",
    "Elon Musk became the richest person in the world in 2021 due to Tesla's soaring stock prices.",
    "Warren Buffett bought his first stock at age 11 and filed his first tax return at age 13.",
    "Jeff Bezos started Amazon as an online bookstore in 1994 from his garage.",
    "Bernard Arnault’s LVMH is the largest luxury goods company in the world.",
    "Bill Gates has donated over $50 billion to charitable causes through the Gates Foundation.",
    "Mark Zuckerberg became a billionaire at the age of 23, making him one of the youngest self-made billionaires in history.",
    "Oprah Winfrey was born into poverty but became the first African American female billionaire.",
    "The world's first billionaire was John D. Rockefeller, in 1916.",
    "In 2023, the top five wealthiest individuals collectively held over $800 billion in wealth.",
    "China has the most self-made female billionaires in the world.",
    "The most common industry for billionaires is finance and investments.",
    "The wealthiest 20% of Americans own 88% of the country's wealth.",
    "Bill Gates founded Microsoft in 1975 with Paul Allen, revolutionizing the software industry.",
    "Amazon started as a bookstore but later expanded into a global e-commerce and technology empire.",
    "Tesla's Model 3 is one of the best-selling electric vehicles globally.",
    "The United States has the highest number of billionaires, followed by China.",
    "LVMH owns more than 70 luxury brands, including Louis Vuitton, Moët & Chandon, and Christian Dior.",
    "Warren Buffett's Berkshire Hathaway has holdings in diverse sectors, including insurance, energy, and food.",
    "The top 10 richest people in the world have more combined wealth than the entire GDP of some countries.",
    "Mark Zuckerberg co-founded Facebook in 2004, which eventually grew into Meta Platforms, a tech giant.",
    "Jack Ma built Alibaba from a small start-up into one of the world's largest e-commerce companies.",
    "The world's biggest private employer is Walmart, employing over 2.3 million people globally.",
    "Elon Musk founded SpaceX with the goal of reducing space transportation costs and making Mars colonization possible.",
    "Facebook has more than 2.8 billion active monthly users globally, making it the most popular social media platform.",
    "Tesla’s market cap exceeded $1 trillion for the first time in 2021, making it one of the most valuable car companies globally.",
    "The total value of global luxury goods sales in 2021 was estimated to be over $300 billion.",
    "Apple became the first company to reach a $2 trillion market capitalization in 2020.",
    "In 2020, Amazon’s annual revenue was over $380 billion, making it one of the largest companies in the world.",
    "Mark Zuckerberg spent $100 million to purchase the land surrounding his home to ensure privacy.",
    "Elon Musk’s company, SpaceX, was the first private company to send astronauts to the International Space Station in 2020.",
    "The wealthiest woman in the world, as of 2021, was L'Oréal heir Françoise Bettencourt Meyers.",
    "In 2021, the United States had more than 750 billionaires, the highest number of billionaires in any country.",
    "Tesla’s Gigafactories aim to produce more electric vehicles than all other manufacturers combined by 2030.",
    "Apple’s iPhone is one of the most profitable consumer products ever created, with over 2 billion units sold worldwide.",
    "The total value of all the world's real estate is estimated to exceed $280 trillion.",
    "Bill Gates owns one of the largest private landholdings in the United States, with over 242,000 acres of farmland.",
    "Google processes more than 3.5 billion searches per day, making it the most-used search engine in the world.",
    "The Amazon Rainforest is sometimes referred to as the ‘lungs of the planet’ due to its role in absorbing carbon dioxide.",
    "The world’s largest oil company is Saudi Aramco, with a market value of over $1.9 trillion.",
    "The richest person in history is thought to be Mansa Musa I of Mali, whose wealth would amount to over $400 billion today.",
    "Bitcoin reached an all-time high value of over $64,000 in April 2021.",
    "The total value of the world's stock markets exceeds $100 trillion.",
    "In 2020, the global wealth of billionaires grew by over $3.9 trillion.",
    "The average age of the world's richest billionaires is 67 years old.",
    "Apple's revenue from its App Store exceeded $64 billion in 2020.",
    "Nike is one of the most valuable sportswear brands globally, valued at over $200 billion.",
    "The top 10 most valuable brands in the world are all worth over $200 billion each.",
    "Dubai's Burj Khalifa is the tallest building in the world, standing at 828 meters (2,717 feet).",
    "The first trillion-dollar company was Apple, which reached the milestone in 2018.",
    "Billionaires saw their combined wealth increase by 27% in 2020 during the global pandemic.",
    "Tesla's electric cars have been credited with significantly accelerating the adoption of electric vehicles worldwide.",
    "The financial technology (fintech) industry has grown rapidly, with global fintech investment reaching over $100 billion in 2020."
]


async def elite(update: Update, context: CallbackContext):
    response_type = random.choice(["billionaire", "quote", "fact"])
    if response_type == "billionaire":
        billionaire = random.choice(billionaires)
        response = (
            f"\U0001F31F **{billionaire['name']}**\n"
            f"*{billionaire['title']}*\n"
            f"Net Worth: {billionaire['net_worth']}\n"
            f"_\"{billionaire['quote']}\"_"
        )
    elif response_type == "quote":
        response = f"\U0001F4A1 *Motivational Quote:*\n_{random.choice(quotes)}_"
    else:
        response = f"\U0001F4CA *Wealth Fact:*\n{random.choice(facts)}"

    await update.message.reply_text(response, parse_mode="Markdown")

async def welcome(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        await update.message.reply_text(
            f"Welcome to the future top 1% in the world, {member.first_name}! \U0001F389\n"
            "Type /elite to get inspired by the wealthiest and most successful people in the world!"
        )

async def start_message(update: Update, context: CallbackContext):
    # Send a welcome message when the bot is started
    await update.message.reply_text(
        "Welcome to the future top 1%! Type /elite to get inspired by the wealthiest and most successful people in the world!"
    )

# Main function
def main():
    # Initialize the Application with your bot token
    application = Application.builder().token("7846804361:AAHSTz20bVshGiMhO9uXyoI0tlBpdGaSdxw").build()

    # Adding handlers
    application.add_handler(CommandHandler("elite", elite))
    application.add_handler(CommandHandler("start", start_message))  # Add handler for /start command
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    # Start polling for updates
    application.run_polling()

if __name__ == "__main__":
    main()