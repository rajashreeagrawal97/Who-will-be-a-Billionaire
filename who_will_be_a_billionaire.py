print("🎯 Who Will Be a Billionaire? 🎯\n")
print("Welcome, future tycoon! In this game, you'll face a series of strategic choices.")
print("Make your decisions wisely, balancing judgment and risk appetite to climb your way to billionaire status.")
print("Let the challenge begin — good luck!\n")

print("💼 You’re starting with a portfolio of $10,000.")
print("Choose one asset to invest in:")
print("1. TechNova")
print("2. HealthZen")
print("3. GreenCore")
print("4. FinTrust")
print("5. CryptoX\n")

valid_stocks_input = [1, 2, 3, 4, 5]

Technova = [
    {
        "prompt": "Tech stocks are surging thanks to AI excitement.\n1. Stay fully invested\n2. Sell half your position after 10% gain\n3. Exit and stay in cash\nEnter your choice (1-3): ",
        "multipliers": [1.1, 1.05, 0.95]
    },
    {
        "prompt": "Regulators traget big tech monopolies\n1. Ignore it (PR stunt)\n2. Hedge with ETFs\n3. Sell and reenter later\nEnter your choice (1-3): ",
        "multipliers": [0.9, 1.0, 1.1]
    },
    {
        "prompt": "Supply chain issues hit GPU and AI chip production.\n1. Hold through shortage\n2. Rotate to software tech\n3. Panic sell\nEnter your choice (1-3): ",
        "multipliers": [0.85, 1.05, 0.95]
    },
    {
        "prompt": "TechNova beats earnings and raises guidance.\n1. Double down on position\n2. Stay fully invested\n3. Lock in partial gains\nEnter your choice (1-3): ",
        "multipliers": [1.25, 1.15, 1.10]
    },
    {
        "prompt": "Cloud outage disrupts services; ransom paid.\n1. Sell immediately\n2. Assume reputation will rebound and hold\n3. Bet competitors will get hit next and short peers\nEnter your choice (1-3): ",
        "multipliers": [0.75, 0.90, 1.10]
    },
    {
        "prompt": "10% workforce cut as 'efficiency move.'\n1. View it as red flag and exit position\n2. Stay calm and assume it's a strategic move\n3. Buy more shares, treating it as an operational bullish signal\nEnter your choice (1-3): ",
        "multipliers": [0.85, 1.00, 1.30]
    },
    {
        "prompt": "Fed pauses rate hikes — tech stocks rejoice!\n1. Buy aggressively\n2. Rebalance portfolio to take advantage of lower rates\n3. Wait for confirmation before making any moves\nEnter your choice (1-3): ",
        "multipliers": [1.20, 1.40, 1.05]
    },
    {
        "prompt": "TechNova spin-off (NovaCloud) IPOs next week.\n1. Invest: Get in early via pre-IPO round\n2. Buy post-IPO dip\n3. Stay out of speculation\nEnter your choice (1-3): ",
        "multipliers": [1.3, 1.15, 0.95]
    },
    {
        "prompt": "Earthquake halts Taiwan chip exports.\n1. Reduce exposure to TechNova.\n2. Rotate to asset-light software plays.\n3. See it as a short-term dip and reinvest.\nEnter your choice (1-3): ",
        "multipliers": [0.90, 1.20, 1.40]
    },
    {
        "prompt": "TechNova reveals quantum AI chip.\n1. Take early bet and Pre-Invest.\n2. Hold through the event.\n3. Sell when profit spike.\nEnter your choice (1-3): ",
        "multipliers": [2.0, 1.50, 1.10]
    },
    {
        "prompt": "New 5% tax on tech company net profits.\n1. Sell before policy effect\n2. Assume law won’t pass\n3. Shift to Environment, Social, Governance-compliant fund structure\nEnter your choice (1-3): ",
        "multipliers": [0.85, 1.00, 1.30]
    },
    {
        "prompt": "Redditors start pumping TechNova stock.\n1. YOLO thus, Go max long\n2. Partial Profit, Sell half on spike\n3. Exit, Avoid the mania\nEnter your choice (1-3): ",
        "multipliers": [3.0, 1.30, 0.80]
    },
    {
        "prompt": "Major rollout into Indian market announced.\n1. Invest More: High conviction\n2. Wait: Monitor regulatory risk\n3. Exit Early: Sell after announcement\nEnter your choice (1-3): ",
        "multipliers": [2.50, 1.30, 0.90]
    },
    {
        "prompt": "Whistleblower reveals privacy violations.\n1. Sell on panic\n2. Hold, assume recovery\n3. Buy the dip, reinvest at bottom\nEnter your choice (1-3): ",
        "multipliers": [0.30, 0.80, 3.0]
    },
    {
        "prompt": "TechNova launches 'NovaBrain' quantum-AI product line.\n1. Go all in: Bet everything\n2. Conservative hedge: 50/50 strategy\n3. Exit: Take profits before launch\nEnter your choice (1-3): ",
        "multipliers": [10.0, 2.0, 0.50]
    }
]

Health = [
    {
        "prompt": "HealthZen announces promising results for a new diabetes treatment entering Phase 2.\n1. Be cautious, no immediate move\n2. Buy early and get in before hype\n3. Assume it is not a big deal\nEnter your choice (1-3): ",
        "multipliers": [1.0, 1.20, 0.95]
    },
    {
        "prompt": "An aggressive flu season leads to a spike in demand for HealthZen over-the-counter meds.\n1. Keep current position\n2. Add more capital\n3. Sell early: Book quick gains\nEnter your choice (1-3): ",
        "multipliers": [1.05, 1.25, 1.10]
    },
    {
        "prompt": "A partner company fails their trial, possibly delaying a joint therapy pipeline.\n1. Dump shares quickly\n2. Reduce position, invest in rivals\n3. Hold long-term\nEnter your choice (1-3): ",
        "multipliers": [0.85, 1.00, 1.10]
    },
    {
        "prompt": "HealthZen ranks #1 in a national workplace culture index, attracting talent and media attention.\n1. Short term tactical trade\n2. Stay quiet: Internal news only \n3. Cash out while sentiment is high\nEnter your choice (1-3): ",
        "multipliers": [1.30, 1.10, 1.15]
    },
    {
        "prompt": "The FDA announces a surprise audit of HealthZen manufacturing plant.\n1. Risk-averse exit\n2. Hold tight and trust compliance\n3. Buy on dip\nEnter your choice (1-3): ",
        "multipliers": [0.75, 1.00, 1.15]
    },
    {
        "prompt": "Rising global infections prompt fear of another pandemic.\n1. Double down and go big on pharma\n2. Add a small stake\n3. Sit back and avoid the volatility\nEnter your choice (1-3): ",
        "multipliers": [1.40, 1.20, 1.00]
    },
    {
        "prompt": "HealthZen acquires a small biotech with promising Alzheimer research.\n1. Join the deal and invest in biotech\n2. Avoid integration risk: Stay in HealthZen only\n3. Invest in rival firm: Bet against integration\nEnter your choice (1-3): ",
        "multipliers": [1.50, 1.10, 0.90]
    },
    {
        "prompt": "HealthZen top drug is added to major insurance providers approved lists.\n1. Reinvest profits\n2. Buy call options as a high-leverage bet\n3. Ignore policy change & assume it is priced in\nEnter your choice (1-3): ",
        "multipliers": [1.60, 1.30, 1.10]
    },
    {
        "prompt": "A competitor claims HealthZen violated their patent on a delivery mechanism.\n1. Dump stock: Avoid uncertainty\n2. Wait for judgment: Legal outcome pending\n3. Bet on win: Buy the dip\nEnter your choice (1-3): ",
        "multipliers": [0.50, 1.00, 2.00]
    },
    {
        "prompt": "HealthZen announces CRISPR-based cancer cell editing in mice.\n1. Ride the biotech hype\n2. Wait for peer review & play it safe\n3. Avoid hype thinking it is a distraction\nEnter your choice (1-3): ",
        "multipliers": [2.50, 1.30, 1.00]
    },
    {
        "prompt": "The diabetes drug from Round 1 shows statistically significant results in Phase 3.\n1. Stay steady and hold\n2. Leverage boost: Use margin or options\n3. Sell before results\nEnter your choice (1-3): ",
        "multipliers": [1.30, 3.00, 1.10]
    },
    {
        "prompt": "CFO is caught selling stock before trial results.\n1. Avoid reputational risk and exit fast\n2. Wait for board action and trust governance\n3. Buy low after dip\nEnter your choice (1-3): ",
        "multipliers": [0.4, 1.00, 3.00]
    },
    {
        "prompt": "A co-developed vaccine wins WHO approval for worldwide distribution.\n1. Go all in & bet everything\n2. Conservative hold: Ride gains safely\n3. Profit partially: Book half\nEnter your choice (1-3): ",
        "multipliers": [5.00, 2.50, 1.80]
    },
    {
        "prompt": "Former patients file a lawsuit for side effects of a lesser-known drug.\n1. Dump stock & avoid litigation drag\n2. Trust legal team, assume they’ll handle it\n3. Double down on dip by betting on market overreaction\nEnter your choice (1-3): ",
        "multipliers": [0.20, 1.10, 4.00]
    },
    {
        "prompt": "HealthZen offers IPO for its biotech arm, then receives an M&A offer from a global pharma giant.\n1. Take cash buyout: Secure exit\n2. Merge with AI Health: Join two giants\n3. Go independent: Risky solo bet\nEnter your choice (1-3): ",
        "multipliers": [1.00, 5.00, 10.00]
    }
]

Green = [
    {
        "prompt": "A $300B climate bill is signed in the U.S. offering subsidies for renewables.\n1. Stay invested\n2. Reallocate fully to GreenCore\n3. Ignore\nEnter your choice (1-3): ",
        "multipliers": [1.10, 1.30, 1.00]
    },
    {
        "prompt": "Crude oil hits $130/barrel. Demand for green alternatives rises.\n1. Ride the green premium\n2. Short fossil fuels\n3. Sit out\nEnter your choice (1-3): ",
        "multipliers": [1.25, 1.15, 1.00]
    },
    {
        "prompt": "Silicon and rare earth shortages drive solar supply chain panic.\n1. Panic sell\n2. Hold steady\n3. Hedge with rare-earth miner\nEnter your choice (1-3): ",
        "multipliers": [0.85, 1.00, 1.20]
    },
    {
        "prompt": "BlackRock and others pour money into ESG ETFs.\n1. Ride momentum\n2. Take early gains\n3. Shift to tech\nEnter your choice (1-3): ",
        "multipliers": [1.40, 1.20, 1.10]
    },
    {
        "prompt": "GreenCore wins a $2B energy storage deal with a national grid.\n1. Reinvest profits\n2. Wait for revenue impact\n3. Ignore\nEnter your choice (1-3): ",
        "multipliers": [1.50, 1.10, 1.00]
    },
    {
        "prompt": "A batch of turbines fails quality control, hitting press.\n1. Dump stock\n2. Stay calm\n3. Buy dip\nEnter your choice (1-3): ",
        "multipliers": [0.75, 1.00, 1.30]
    },
    {
        "prompt": "COP29 concludes with a pledge for 70% clean energy by 2035.\n1. Reallocate to global ESG\n2. Buy carbon credits\n3. Hold position\nEnter your choice (1-3): ",
        "multipliers": [1.50, 1.25, 1.10]
    },
    {
        "prompt": "New graphene battery doubles EV range. GreenCore holds key patent.\n1. Buy early\n2. Wait for tests\n3. Sell rival tech\nEnter your choice (1-3): ",
        "multipliers": [2.00, 1.30, 1.10]
    },
    {
        "prompt": "Lithium miners face protests; green tech material costs spike.\n1. Exit and avoid temporary chaos\n2. Invest in recyclers\n3. Ignore disruption\nEnter your choice (1-3): ",
        "multipliers": [0.60, 2.20, 0.90]
    },
    {
        "prompt": "Global consensus on carbon pricing. Dirty energy stocks drop.\n1. Buy emissions-free companies\n2. Stay passive\n3. Sell exposed peers\nEnter your choice (1-3): ",
        "multipliers": [2.50, 1.20, 1.50]
    },
    {
        "prompt": "Green ETFs double AUM in 3 months.\n1. Add to GreenCore\n2. Diversify and gain partial benefits\n3. Cash out early and avoid risk\nEnter your choice (1-3): ",
        "multipliers": [3.00, 1.50, 1.20]
    },
    {
        "prompt": "Investors demand more transparency and ESG commitments.\n1. Support reform board\n2. Wait for vote\n3. Exit nervously\nEnter your choice (1-3): ",
        "multipliers": [3.00, 1.10, 0.50]
    },
    {
        "prompt": "Massive flooding disables key oil infrastructure.\n1. All-in green shift\n2. Invest in recovery infra\n3. Stay neutral\nEnter your choice (1-3): ",
        "multipliers": [5.00, 2.00, 1.20]
    },
    {
        "prompt": "U.S. lawmakers criticize ESG investing and threaten restrictions.\n1. Shift to Europe/Asia\n2. Hold firm\n3. Dump ESG funds\nEnter your choice (1-3): ",
        "multipliers": [4.00, 1.10, 0.30]
    },
    {
        "prompt": "GreenCore spins off its EV battery arm and merges with AI-grid startup.\n1. Take IPO gains\n2. Merge with AI-grid firm\n3. Launch global green ETF\nEnter your choice (1-3): ",
        "multipliers": [1.00, 5.00, 10.00]
    }
]

Finance = [
    {
        "prompt": "The Federal Reserve raises rates by 0.5% to curb inflation.\n1. Increase stake in FinTrust\n2. Wait and watch\n3. Rotate out to tech\nEnter your choice (1-3): ",
        "multipliers": [1.25, 1.10, 0.95]
    },
    {
        "prompt": "FinTrust reports strong net interest income and loan growth.\n1. Reinvest dividends\n2. Hold position\n3. Sell on earnings day\nEnter your choice (1-3): ",
        "multipliers": [1.30, 1.15, 1.00]
    },
    {
        "prompt": "Several mid-tier firms miss debt payments.\n1. Shift to high-quality banks\n2. Hedge with CDS ETFs\n3. Panic sell all finance\nEnter your choice (1-3): ",
        "multipliers": [1.20, 1.05, 0.85]
    },
    {
        "prompt": "Rising rates slow mortgage issuance.\n1. Switch to commercial banking\n2. Hold steady\n3. Exit FinTrust\nEnter your choice (1-3): ",
        "multipliers": [1.25, 1.00, 0.90]
    },
    {
        "prompt": "A fintech competitor IPOs and grabs investor attention.\n1. Double down on FinTrust\n2. Diversify into fintech\n3. Dump FinTrust\nEnter your choice (1-3): ",
        "multipliers": [1.10, 1.20, 0.95]
    },
    {
        "prompt": "Long-term yields jump — banks love the spread.\n1. Go heavy on FinTrust\n2. Stay the course\n3. Rotate to bonds\nEnter your choice (1-3): ",
        "multipliers": [1.40, 1.15, 0.90]
    },
    {
        "prompt": "Consumer credit demand hits record levels.\n1. Expand position in FinTrust\n2. Buy fintech lenders\n3. Ignore the data\nEnter your choice (1-3): ",
        "multipliers": [1.50, 1.20, 1.00]
    },
    {
        "prompt": "New capital reserve rules are proposed.\n1. Buy FinTrust on dip\n2. Exit temporarily\n3. Panic sell\nEnter your choice (1-3): ",
        "multipliers": [1.40, 1.10, 0.75]
    },
    {
        "prompt": "A smaller regional bank fails, sparking fear.\n1. Stick with FinTrust as a big bank\n2. Invest in ETFs for sector recovery\n3. Sell everything\nEnter your choice (1-3): ",
        "multipliers": [2.00, 1.30, 0.60]
    },
    {
        "prompt": "FinTrust announces major fintech acquisition.\n1. Back the deal\n2. Wait for integration\n3. Sell on uncertainty\nEnter your choice (1-3): ",
        "multipliers": [2.50, 1.20, 0.90]
    },
    {
        "prompt": "News leaks insider dealings at multiple banks.\n1. Trust FinTrust’s governance\n2. Cut exposure sector-wide\n3. Short financials\nEnter your choice (1-3): ",
        "multipliers": [1.30, 1.00, 0.70]
    },
    {
        "prompt": "Housing rebounds, banks increase origination volumes.\n1. Add mortgage division exposure\n2. Hold FinTrust as-is\n3. Rotate to REITs\nEnter your choice (1-3): ",
        "multipliers": [2.00, 1.20, 0.90]
    },
    {
        "prompt": "Central bank launches a digital currency pilot program.\n1. Invest in FinTrust’s digital transition\n2. Buy stablecoins and blockchain funds\n3. Ignore the shift\nEnter your choice (1-3): ",
        "multipliers": [3.00, 1.50, 0.80]
    },
    {
        "prompt": "Repo market stress causes interbank rates to spike.\n1. Bet on FinTrust’s strong balance sheet\n2. Diversify into gold & bonds\n3. Flee to cash\nEnter your choice (1-3): ",
        "multipliers": [4.00, 2.00, 0.90]
    },
    {
        "prompt": "Fed injects liquidity; FinTrust is offered a major M&A deal.\n1. Take cash exit via merger\n2. Launch FinTrust Digital division\n3. Go private via LBO with PE firm\nEnter your choice (1-3): ",
        "multipliers": [1.00, 5.00, 10.00]
    }
]

Crypto = [
    {
        "prompt": "Elon Musk tweets a meme with your coin's logo. Market goes wild.\n1. YOLO all-in on hype\n2. Take partial profit\n3. Stay rational and ignore\nEnter your choice (1-3): ",
        "multipliers": [1.50, 1.20, 1.00]
    },
    {
        "prompt": "China bans crypto mining (again). Market panics.\n1. Sell fast\n2. Hold strong\n3. Buy dip aggressively\nEnter your choice (1-3): ",
        "multipliers": [0.60, 1.10, 1.30]
    },
    {
        "prompt": "The SEC approves the first U.S. spot Bitcoin ETF.\n1. Shift to Bitcoin\n2. Stay in altcoins like CryptoX\n3. Diversify between both\nEnter your choice (1-3): ",
        "multipliers": [1.20, 1.40, 1.30]
    },
    {
        "prompt": "CryptoX hard fork announced: potential chain split.\n1. Vote for upgrade and hold\n2. Dump before fork\n3. Buy into the chaos\nEnter your choice (1-3): ",
        "multipliers": [1.00, 0.90, 1.50]
    },
    {
        "prompt": "A whale wallet moves $2B in CryptoX. Rumors swirl.\n1. Panic and sell\n2. Ignore it\n3. Front-run buying activity\nEnter your choice (1-3): ",
        "multipliers": [0.80, 1.00, 1.25]
    },
    {
        "prompt": "CryptoX blockchain halts for 12 hours due to a bug.\n1. Exit immediately\n2. Hold and monitor dev response\n3. Join community fix DAO\nEnter your choice (1-3): ",
        "multipliers": [0.70, 1.00, 1.40]
    },
    {
        "prompt": "A major rug pull rocks another altcoin.\n1. Sell CryptoX in fear\n2. Move funds to stablecoin\n3. Hold firm and trust fundamentals\nEnter your choice (1-3): ",
        "multipliers": [0.75, 1.10, 1.25]
    },
    {
        "prompt": "Gas fees spike to all-time highs.\n1. Switch to L2 scaling chains\n2. Ride it out\n3. Use alternatives (like SolX)\nEnter your choice (1-3): ",
        "multipliers": [1.30, 1.00, 1.20]
    },
    {
        "prompt": "Altcoin season begins. Meme tokens are surging.\n1. Rotate into meme coins\n2. Stake CryptoX\n3. Hold main position\nEnter your choice (1-3): ",
        "multipliers": [1.50, 1.30, 1.10]
    },
    {
        "prompt": "A top exchange gets hacked.\n1. Withdraw funds immediately\n2. Hold your position\n3. Buy the dip\nEnter your choice (1-3): ",
        "multipliers": [1.10, 0.95, 1.50]
    },
    {
        "prompt": "CryptoX goes viral in South America. Adoption rises.\n1. Increase position\n2. Wait for confirmation\n3. Exit fearing hype\nEnter your choice (1-3): ",
        "multipliers": [2.00, 1.20, 0.90]
    },
    {
        "prompt": "Regulators announce global crypto crackdown.\n1. Switch to DeFi plays\n2. Sell immediately\n3. Hedge with CBDCs\nEnter your choice (1-3): ",
        "multipliers": [2.00, 0.70, 1.30]
    },
    {
        "prompt": "A popular stablecoin de-pegs overnight.\n1. Panic sell everything\n2. Stay calm and hold\n3. Short the stablecoin\nEnter your choice (1-3): ",
        "multipliers": [0.50, 1.00, 2.50]
    },
    {
        "prompt": "All major exchanges pause trading due to volatility.\n1. Move to DEXs\n2. Sit tight and wait it out\n3. Sell before next freeze\nEnter your choice (1-3): ",
        "multipliers": [3.00, 1.20, 1.10]
    },
    {
        "prompt": "CryptoX unveils AI-powered on-chain governance. Hype explodes.\n1. Go all-in\n2. Conservative 50% bet\n3. Exit to cash\nEnter your choice (1-3): ",
        "multipliers": [10.0, 5.0, 1.0]
    }
]


stock_input = input("Enter the stock code you want to invest in \n1-TechNova,\n2-HealthZen,\n3-GreenCore,\n4-FinTrust,\n5-CrytoX : ")
stock_input = int(stock_input)
count = 10000.00


if stock_input == 1:
    print("You have chosen TechNova. Let's begin your investment journey!\n")
    for event in Technova:
        user_input = input(event["prompt"])
        if user_input not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        idx = int(user_input) - 1
        count = count * event["multipliers"][idx]
        print(f"Your current portfolio value: {count}\n")
        
elif stock_input == 2:
    print("You have chosen HealthZen. Let's begin your investment journey!\n")
    for event in Health:
        user_input = input(event["prompt"])
        if user_input not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        idx = int(user_input) - 1
        count = count * event["multipliers"][idx]
        print(f"Your current portfolio value: {count}\n")

elif stock_input == 3:
    print("You have chosen GreenCore. Let's begin your investment journey!\n")
    for event in Green:
        user_input = input(event["prompt"])
        if user_input not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        idx = int(user_input) - 1
        count = count * event["multipliers"][idx]
        print(f"Your current portfolio value: {count}\n")

elif stock_input == 4:
    print("You have chosen FinTrust. Let's begin your investment journey!\n")
    for event in Finance:
        user_input = input(event["prompt"])
        if user_input not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        idx = int(user_input) - 1
        count = count * event["multipliers"][idx]
        print(f"Your current portfolio value: {count}\n")

elif stock_input == 5:
    print("You have chosen CryptoX. Let's begin your investment journey!\n")
    for event in Crypto:
        user_input = input(event["prompt"])
        if user_input not in ["1", "2", "3"]:
            print("Invalid choice. Please enter a number between 1 and 3.")
            continue
        idx = int(user_input) - 1
        count = count * event["multipliers"][idx]
        print(f"Your current portfolio value: {count}\n")
    
else:
    print("Invalid stock code. Please choose from the available options.")

if count >= 1e9:
    print("Congratulations! You have become a billionaire with a portfolio value of $", count)
else:
    print("Your final portfolio value is $", count)
    print("Keep investing wisely and you might reach billionaire status in the future!")
