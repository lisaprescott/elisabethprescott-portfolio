#!/usr/bin/env python3
"""Generates casestudy/<slug>.html from the PROJECTS data below.

Edit copy here, then run:  python3 _build/case_studies.py
(_build/ is ignored by GitHub Pages' Jekyll build, so this file is not published.)

Every figure is either from Lisa's LinkedIn or from a public source listed in
that project's `sources`. Do not add numbers without a source.
"""
import html
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "casestudy"

PROJECTS = [
    {
        "slug": "eventbrite-app",
        "title": "Eventbrite App",
        "eyebrow": "Eventbrite · Product · 2025",
        "dek": "Rebuilt Eventbrite's consumer app as part of the company's full rebrand, taking it from ticketing to a place to find things to do with friends.",
        "facts": [("Role", "SVP Design"), ("Org", "120-person design org, reporting to the CPO"), ("Shipped", "March 2025, all markets"), ("Partners", "Instrument")],
        "hero": "../images/eventbrite-app.png",
        "problem": [
            "Eventbrite powered millions of events, but consumers opened the app to show a ticket, not to find something to do. Discovery was fragmented, and mobile engagement was declining against mobile-first competitors.",
            "The business needed the app to drive demand for creators, not just fulfil it.",
        ],
        "approach": [
            "Set the strategy with the CPO to reposition the app from transaction to discovery, and directed the product design team through it: a Discover tab built on curated It-Lists from local tastemakers in London, New York, Los Angeles and Melbourne; contact sync to see which events friends are attending; video and social signals in recommendations.",
            "Had the design systems team rebuild the interface on a modular, card-based system so product teams could extend it after launch, and aligned the release with the brand refresh as a single moment.",
            "Sponsored a three-month beta with product and data leadership to prove revenue impact before global rollout.",
        ],
        "results": [("+12%", "paid tickets on iOS; $3M net revenue in a 3-month beta"), ("+8%", "paid tickets on Android; $2M net revenue"), ("+23%", "monthly active users"), ("+14%", "traffic to Eventbrite surfaces year over year (Instrument)")],
        "leadership": [
            "Built and led a 120-person organization spanning product design, brand, design systems, UX research, innovation and design operations, reporting to the CPO.",
            "Partnered with the CPO and CMO on the product vision, brought in Instrument as an extension of the in-house team, and held the bar on a single system across product and brand so both launched as one story.",
        ],
        "gallery": [("../images/cs/eventbrite-app-blueprint.jpg", "Eventbrite app experience blueprint")],
        "sources": [
            ("Eventbrite: Eventbrite welcomes Lisa Prescott as SVP of Design and Brand (Aug 29, 2023)", "https://www.eventbrite.com/blog/?p=408473"),
            ("The Webby Awards 2026: Reimagining Eventbrite, Best User Experience nominee (credits Lisa Prescott, SVP Design)", "https://winners.webbyawards.com/2026/apps-software-immersive/app-excellence/best-user-experience/382209/reimagining-eventbrite-a-new-vision-for-discovery-and-connection"),
            ("Business Wire: Eventbrite's reimagined app (Mar 4, 2025)", "https://www.businesswire.com/news/home/20250304175630/en/Get-Into-It-Eventbrites-Reimagined-App-Makes-Discovering-Your-Next-Favorite-Live-Experience-as-Enjoyable-as-Being-There"),
            ("Instrument: Eventbrite app case study", "https://www.instrument.com/work/eventbrite-app"),
            ("Fast Company: Eventbrite app redesign", "https://www.fastcompany.com/91289655/eventbrite-app-redesign-event-discovery"),
            ("TicketNews: Eventbrite launches Discover tab", "https://www.ticketnews.com/2025/03/eventbrite-launches-app-update-with-discover-tab/"),
        ],
    },
    {
        "slug": "eventbrite-rebrand",
        "title": "Eventbrite Rebrand",
        "eyebrow": "Eventbrite · Brand · 2024–2025",
        "dek": "The most significant brand refresh in Eventbrite's history, taking the company from ticketing to a place to find things to do with friends.",
        "facts": [("Role", "SVP Design, rebrand lead"), ("Partners", "CMO and CPO"), ("Timeline", "May 2024 to launch in March 2025"), ("Recognition", "Fast Company, 2025")],
        "hero": "../images/eventbrite-rebrand.png",
        "problem": [
            "Eventbrite was known as a logo on a ticket stub: infrastructure that sat behind other people's events, built around one-time ticket sales. As the company moved to a consumer marketplace, the brand had to make people want to go out, not just check in.",
            "The company had a renewed mission, to bring people together through live experiences, and a new role for product: to maximize the enjoyment of gathering. The brand had to carry both.",
        ],
        "approach": [
            "Ran the program from the pitch in May 2024 through strategy, logo, visual identity and tone-of-voice workshops in June, eight rounds of creative review through the summer, and an internal brand roadshow before launch.",
            "Built one system for brand, marketing and product, then launched it with the Get Into It campaign and the redesigned app as a single moment.",
        ],
        "extra": "EVENTBRITE_BRAND",
        "results": [("+22%", "brand awareness"), ("8", "rounds of creative review, June to July 2024"), ("1", "system across brand, marketing and product")],
        "leadership": [
            "Led the rebrand end to end, from the first pitch to launch, partnering with the CMO and CPO and directing the VP Brand, the in-house brand and design team, and design program management.",
            "Held one bar across brand and product, so the identity, the app and the launch campaign shipped as one story.",
        ],
        "gallery": [],
        "sources": [
            ("Brand partner case study: Eventbrite rebrand (team credits include Lisa Prescott, SVP Design)", "https://buck.co/work/eventbrite"),
            ("It's Nice That: Eventbrite's new identity", "https://www.itsnicethat.com/articles/buck-eventbrite-graphic-design-project-100325"),
            ("Eventbrite: Eventbrite welcomes Lisa Prescott as SVP of Design and Brand (Aug 29, 2023)", "https://www.eventbrite.com/blog/?p=408473"),
            ("Creative Bloq: Eventbrite's vibrant rebrand", "https://creativebloq.com/design/branding/eventbrites-vibrant-rebrand-revives-the-magic-of-live-experiences"),
            ("Eventbrite: brand refresh announcement", "https://www.eventbrite.com/blog/?p=436270"),
        ],
    },
    {
        "slug": "eventbrite-openai",
        "title": "Eventbrite & OpenAI",
        "eyebrow": "Eventbrite · Product · AI · 2024",
        "dek": "An Innovation-team exploration of conversational event discovery: what Eventbrite looks like when the front door is a chat, not a search box.",
        "facts": [("Role", "SVP Design"), ("Team", "Innovation team, stood up within Design"), ("Stage", "Concept and prototype"), ("Platform", "ChatGPT")],
        "hero": "../images/eventbrite-openai.png",
        "problem": [
            "Discovery was moving into AI assistants. If people asked ChatGPT what to do this weekend, Eventbrite's supply needed to be the answer, and the experience needed to feel like Eventbrite, not a list of links.",
        ],
        "approach": [
            "Stood up a dedicated Innovation team inside Design to address fragmented discovery and declining mobile engagement.",
            "Directed the team's prototype of an Eventbrite experience inside ChatGPT: conversational queries resolved into rich event cards, social proof from friends, and a path to purchase without leaving the conversation.",
            "Took the work to the executive team as a point of view on AI-era distribution.",
        ],
        "results": [],
        "leadership": [
            "Created the Innovation function and its charter, staffed it from within the design org, and set the questions it had to answer for the business.",
        ],
        "gallery": [],
        "sources": [
            ("Eventbrite: Eventbrite welcomes Lisa Prescott as SVP of Design and Brand (Aug 29, 2023)", "https://www.eventbrite.com/blog/?p=408473"),
            ("TechCrunch: Eventbrite integrates GPT capabilities (May 2023)", "https://techcrunch.com/2023/05/09/eventbrite-integrates-gpt-capabilites-into-platform-to-aid-the-event-planning-process/"),
        ],
    },
    {
        "slug": "airbnb-categories",
        "title": "Airbnb Categories",
        "eyebrow": "Airbnb · Product · 2022",
        "dek": "Contributed to the 2022 Summer Release, described by Brian Chesky as the biggest change to Airbnb in a decade.",
        "facts": [("Role", "Senior Director, Product Design"), ("Team", "Workshop, Airbnb's 0→1 innovation team"), ("Shipped", "May 2022"), ("Scale", "220+ countries and regions")],
        "hero": "../images/press/airbnb-OMG-list_en-1.png",
        "hero_phones": ["../images/press/airbnb-Press_Pre_Brief_Design_List.png", "../images/press/airbnb-OMG-list_en-1.png", "../images/press/airbnb-Press-Categories-Camping.png"],
        "problem": [
            "Travel search had worked the same way for 25 years: type a destination, pick dates. Most people can name only a few dozen destinations, yet Airbnb had listings in roughly 100,000 towns and cities. Unique homes were invisible unless you already knew where to look.",
        ],
        "approach": [
            "Led design for a new way to browse, organizing homes by what makes them special rather than where they are: 55+ categories such as OMG!, Design, Camping and National Parks, covering more than 4 million homes.",
            "Worked with product, engineering and data science leads to pair machine learning across titles, descriptions, photo captions and reviews with human curation of the lead photo for every listing in every category.",
            "Pushed for the map to respond to the category, zooming to show where those homes are, so browsing became a way to discover destinations, not just homes.",
        ],
        "results": [("180M", "views in the first weeks"), ("4M+", "homes organized into 55+ categories"), ("Record", "daily visitors after launch")],
        "leadership": [
            "Senior Director in Workshop, Airbnb's internal 0→1 team, leading designers across the categories and maps work on a marketplace serving 220+ countries and $17B in gross booking value in Q2 2022.",
        ],
        "gallery": [("../images/cs/airbnb-categoryList.png", "Airbnb Categories list")],
        "sources": [
            ("US Design Patent D1054441, Airbnb (inventors include Lisa Prescott)", "https://patents.justia.com/patent/D1054441"),
            ("US Design Patent D1056932, Airbnb (inventors include Lisa Prescott)", "https://patents.justia.com/patent/D1056932"),
            ("Airbnb Newsroom: 2022 Summer Release", "https://news.airbnb.com/2022-summer-release/"),
            ("Uproxx: biggest change to the platform in a decade", "https://uproxx.com/life/airbnb-summer-release-2022"),
            ("The Points Guy: Airbnb Categories and AirCover", "https://thepointsguy.com/news/airbnb-new-categories-aircover"),
        ],
    },
    {
        "slug": "airbnb-wishlist",
        "title": "Airbnb Wishlists & Maps",
        "eyebrow": "Airbnb · Product · 2021–2023",
        "dek": "Turned Wishlists from a save button into the foundation of group trip planning, and redesigned Maps as a destination-first discovery surface.",
        "facts": [("Role", "Senior Director, Product Design"), ("Team", "Workshop, Airbnb's 0→1 innovation team"), ("Shipped", "2024 Summer Release"), ("Patents", "3 US design patents")],
        "hero": "../images/press/airbnb-Joined-Wishlist-en-US.png",
        "hero_phones": ["../images/press/airbnb-LPM1-_-Trip-invite.png", "../images/press/airbnb-Joined-Wishlist-en-US.png", "../images/press/airbnb-Guest-thread-en-US.png"],
        "problem": [
            "More than 80% of Airbnb bookings are group trips, but the app was built for one person. Planning happened in group chats and screenshots, outside Airbnb, and Wishlists were a private save list.",
            "Maps, the platform's largest discovery surface, showed price pins rather than helping guests understand a place.",
        ],
        "approach": [
            "Set the vision for Wishlists as a shared planning space and led the team that designed it: invite the group, add homes, write notes and vote; sharing a listing automatically creates a wishlist.",
            "Extended the work into the trip itself: invitations as digital postcards and a single group thread with the host.",
            "Directed the redesign of Maps as a destination-first experience, so the map answers where to go, not just where the pins are.",
        ],
        "results": [("80%+", "of bookings are group trips, now planned inside Airbnb"), ("3", "US design patents issued Aug 22, 2024: Calendar, Wishlists, Simple Save")],
        "leadership": [
            "Led the design team for Maps and Wishlists within Workshop, taking the work from concept through three design patents to a global release, in partnership with product and engineering leadership.",
        ],
        "gallery": [],
        "sources": [
            ("US Design Patent D1054441, Airbnb (inventors include Lisa Prescott)", "https://patents.justia.com/patent/D1054441"),
            ("US Design Patent D1056932, Airbnb (inventors include Lisa Prescott)", "https://patents.justia.com/patent/D1056932"),
            ("Airbnb Newsroom: 2024 Summer Release", "https://news.airbnb.com/airbnb-2024-summer-release/"),
            ("Sunset: Airbnb just made planning group trips easier", "https://www.sunset.com/travel/airbnb-group-trip-features"),
            ("LinkedIn: patents", "https://www.linkedin.com/in/elisabethprescott/details/patents/"),
        ],
    },
    {
        "slug": "nio",
        "title": "NIO ES8",
        "eyebrow": "NIO · Automotive · 2018",
        "dek": "0→1 design of the in-car HMI for NIO's first production vehicle, the ES8, later recognized with an iF Design Award and showcased at SXSW.",
        "facts": [("Role", "Senior UX Director"), ("Scope", "In-vehicle HMI, 0→1"), ("Shipped", "NIO ES8, 2018"), ("Recognition", "iF Design Award 2020 (NIO OS)")],
        "hero": "../images/nio.png",
        "problem": [
            "NIO was launching its first production car into a market that compared every screen to a smartphone. The HMI had to be fast to operate while driving, coherent across the centre display and instrument cluster, and distinctive enough to define a new brand.",
        ],
        "approach": [
            "Set the direction for the HMI system from first principles: navigation as the anchor, media and vehicle controls one gesture away, and fast-control patterns that keep eyes on the road.",
            "Led the team that delivered the 11.3-inch centre display experience, which shipped in the ES8 and carried into the ES6 as NIO OS.",
            "Wrote the ES8 UX/UI design principles that guided the team, and oversaw an immersive digital experience showcased at SXSW.",
        ],
        "results": [("97%", "customer satisfaction"), ("+35%", "ES8 sales contribution"), ("iF", "Design Award for the ES8/ES6 infotainment HMI")],
        "leadership": [
            "Led the UX team for the ES8 HMI program from zero to production, working across NIO's studios and with vehicle engineering.",
        ],
        "gallery": [("../images/cs/nio-hmi-home.png", "Centre-display concept, June 2018: navigation as the anchor, media and climate one gesture away")],
        "sources": [
            ("iF Design: Infotainment System HMI for NIO ES8/ES6", "https://ifdesign.com/en/winner-ranking/project/infotainment-system-hmi-design-for-nio-es8es6/282405"),
            ("Electric Cars Report: NIO OS wins iF Design Award 2020", "https://electriccarsreport.com/2020/05/nio-os-and-nio-life-concept-scooter-win-if-design-award-2020/"),
            ("NIO: Automotive News PACE recognition", "https://www.nio.com/blog/nio-recognized-automotive-news-pace-awards"),
        ],
    },
    {
        "slug": "spatialand",
        "title": "Spatialand",
        "eyebrow": "Spatialand · Brand · Immersive · 2018–2019",
        "dek": "Brand and platform design for Spatialand (Spatia), the VR studio from the founders of Prologue, acquired by Walmart's Store No 8.",
        "facts": [("Company", "Spatialand / Spatia"), ("Scope", "Brand, platform worlds, spatial language"), ("Role", "Design lead, via agency:collective"), ("Timeline", "2018–2019")],
        "hero": "../images/spatialand.jpg",
        "problem": [
            "VR content was built one-off and thrown away. Spatialand set out to give brands persistent worlds they could return to, and it needed a brand and an interface language that made that idea legible to clients who had never worn a headset.",
        ],
        "approach": [
            "Led design of the Spatia platform worlds, branded environments built on one system. Concepts included worlds for Chanel, Apple and Walmart.",
            "Directed a spatial language for type and UI in 3D (lower thirds, prompts and confirmations) so information could live in the environment rather than float over it.",
            "Brought the brand and the in-headset experience together under one direction, so the identity was something you could stand inside.",
        ],
        "results": [("3", "brand platform worlds designed: Chanel, Apple, Walmart"), ("2018", "Spatialand acquired by Walmart's Store No 8")],
        "leadership": [
            "Worked with founders Kyle and Kim Cooper in a 10-person studio, leading design for the platform and client worlds.",
        ],
        "gallery": [
            ("../images/cs/spatia-world-movement.jpg", "A Spatia world in progress: gears, spheres and dial markings at architectural scale"),
            [("../images/cs/spatia-style-product.jpg", "In-world UI: choosing between a style and a product, each held in its own sphere"), ("../images/cs/spatia-room-set.jpg", "A platform world room set, rendered for the headset")],
            ("../images/cs/spatia-world-movement-2.jpg", "Alternate pass on the movement world"),
            ("../images/cs/spatia-storyboard.jpg", "Storyboard: from the headset into the world, as the walls of the pod open"),
        ],
        "sources": [
            ("UploadVR: Prologue Immersive introduces Spatialand", "https://www.uploadvr.com/prologue-immersive-introduces-spatialand-vr-interface/"),
            ("UploadVR: Walmart acquires Spatialand", "https://www.uploadvr.com/walmart-acquires-content-studio-spatialand-drive-vr-retail/"),
            ("Fortune: Walmart virtual reality", "https://fortune.com/2018/02/06/walmart-virtual-reality/"),
        ],
    },
    {
        "slug": "chanel",
        "title": "Chanel Immersive",
        "eyebrow": "Chanel × Spatialand · Immersive · 2018",
        "dek": "A Chanel world on the Spatia platform, built around the J12 watch: step inside the movement and the Paris addresses that define the house.",
        "facts": [("Studio", "Spatialand"), ("Product", "Chanel J12"), ("Scope", "Immersive world and art direction"), ("Year", "2018")],
        "hero": "../images/chanel.png",
        "problem": [
            "Luxury depends on craft that is invisible at the counter. The brief was to let a visitor step inside a Chanel J12 and understand its craft and the house's Paris heritage without a word of copy.",
        ],
        "approach": [
            "Directed the world from the movement outward: gears, gemstones and dial elements at architectural scale, threaded with rue Cambon, rue de Rivoli and Madeleine, the addresses that define the house.",
            "Developed it as one of the Spatia platform's brand worlds, using the same system as the Walmart and Apple worlds.",
        ],
        "results": [],
        "leadership": [
            "Led the experience design and art direction within the Spatialand studio.",
        ],
        "gallery": [],
        "sources": [],
    },
    {
        "slug": "walmart",
        "title": "Walmart Immersive",
        "eyebrow": "Walmart × Spatialand · Immersive · 2018–2019",
        "dek": "Virtual reality retail for Walmart's Store No 8: shoppable rooms, product stories and avatars that turn browsing into a place you step into.",
        "facts": [("Client", "Walmart · Store No 8"), ("Studio", "Spatialand"), ("Role", "Design lead, via agency:collective"), ("Timeline", "May 2018 – Dec 2019")],
        "hero": "../images/walmart.png",
        "problem": [
            "Walmart acquired Spatialand in February 2018 to explore how virtual reality could change shopping. The open question was what VR commerce should feel like for a mass-market customer, not a tech demo: how you enter, how you find products, and why you'd stay.",
        ],
        "approach": [
            "Led the design of The World of Walmart, an immersive environment you enter through a portal and move through as a series of shoppable rooms.",
            "Directed room sets around lifestyle collections (Glam and Farmhouse) where each product has its own story moment: the rug, the sofa, the lamp and the pillow each animate into focus with materials, context and price.",
            "Shaped the avatar and personalization layer (\"Is this you?\"), along with in-world alerts, product selection and the type system that carries pricing and calls to action in 3D space.",
        ],
        "results": [("2", "lifestyle collections designed as shoppable VR room sets"), ("19 mo", "from first demo to the World of Walmart program")],
        "leadership": [
            "Led design from the first demo explorations in May 2018 through the 2019 World of Walmart program, working with the Spatialand team and Store No 8.",
        ],
        "gallery": [("../images/cs/walmart-roomsets.jpg", "World of Walmart room set progression"), [("../images/cs/walmart-glam-rug.jpg", "Glam collection: rug product story"), ("../images/cs/walmart-glam-sofa.jpg", "Glam collection: sofa product story")]],
        "sources": [
            ("UploadVR: Walmart acquires Spatialand", "https://www.uploadvr.com/walmart-acquires-content-studio-spatialand-drive-vr-retail/"),
            ("Fortune: Walmart virtual reality", "https://fortune.com/2018/02/06/walmart-virtual-reality/"),
            ("Retail Dive: Spatialand launches first VR experience", "https://www.retaildive.com/news/walmart-startup-spatialand-launches-first-vr-experience/548501/"),
        ],
    },
    {
        "slug": "ford-sync",
        "title": "Ford SYNC 3",
        "eyebrow": "Ford · Automotive · 2013–2016",
        "dek": "Built Ford's product design organization and led SYNC 3, the system that replaced MyFord Touch.",
        "facts": [("Role", "Senior UX Director"), ("Org", "Product design organization, built from the ground up"), ("Shipped", "2016 model year"), ("Platform", "BlackBerry QNX")],
        "hero": "../images/ford-sync.png",
        "hero_ui": "../images/cs/ford-sync-ui.png",
        "problem": [
            "MyFord Touch was slow, cluttered and widely criticised, and complaints about it were dragging down Ford's quality and satisfaction scores in J.D. Power and other surveys. Ford needed to win back trust in its in-car experience.",
        ],
        "approach": [
            "Led the design team that rebuilt the system from scratch on QNX, with an 8-inch capacitive touchscreen that responds like a phone.",
            "Set the principles the team designed to: a home screen of three zones (navigation, audio, phone) that expand on touch; kept physical knobs for volume and climate; shortened voice commands to natural phrases; added over-the-air updates.",
            "Established Ford's first automotive design system and shaped a 10-year EV and infotainment roadmap with product leadership.",
            "The SYNC 3 home-screen layout is still in Ford vehicles today.",
        ],
        "results": [("Best", "on the market, per Forbes"), ("DT", "Recommended Product, Digital Trends"), ("1st", "automotive design system at Ford")],
        "leadership": [
            "Built the product design organization from the ground up, hiring and structuring the team that shipped SYNC 3 across Ford and Lincoln.",
        ],
        "gallery": [
            [("../images/cs/ford-myford-touch-layout.svg", "Before: MyFord Touch, four colour-coded corners with small targets and deep menus (diagram)"), ("../images/cs/ford-sg-p49.jpg", "After: SYNC 3 home screen, navigation, audio and phone in three zones above a persistent bar, a layout still in Ford vehicles today")],
            ("../images/cs/ford-day-night.jpg", "Daytime and nighttime themes: the same screen tuned for sun washout and night glare"),
            [("../images/cs/ford-sg-p52.jpg", "HD Radio source screen"), ("../images/cs/ford-sg-p57.jpg", "Destination entry")],
            ("../images/cs/ford-8in-to-10in.jpg", "Scaling the 8-inch design (left) to the 10.1-inch display: the wireframe stage before final assets, January 2016"),
        ],
        "sources": [
            ("Digital Trends: Ford SYNC 3 review", "https://digitaltrends.com/cars/ford-sync-3-review"),
            ("Fox Business: Ford reboots touch-screen system", "https://www.foxbusiness.com/features/ford-reboots-touch-screen-system-with-new-sync-3"),
            ("BlackBerry: Forbes and Fast Company on SYNC 3", "https://blogs.blackberry.com/en/2015/07/forbes-fast-company-on-fords-qnx-powered-sync-3-infotainment-system-cutting-edge"),
        ],
    },
    {
        "slug": "nokia-ngage",
        "title": "Nokia N-Gage",
        "eyebrow": "Nokia × IDEO · Product · 2007",
        "dek": "Reinvented N-Gage as a social mobile gaming service, Nokia's third and most considered attempt at mobile games.",
        "facts": [("Role", "UX Lead, IDEO Storytelling Group"), ("Client", "Nokia"), ("Research", "6+ cities including Barcelona, Tokyo, Shanghai"), ("Launched", "2008")],
        "hero": "../images/nokia-ngage.png",
        "problem": [
            "The original N-Gage hardware, nicknamed the taco, sold about two million units but failed as both a phone and a console. Nokia decided to relaunch N-Gage as software across its smartphones and needed to know what would make people actually play.",
        ],
        "approach": [
            "Field research with Nokia's design team in San Francisco and six cities worldwide to watch how people play games on phones.",
            "The key finding was that people mainly want to play against friends and know the skill of their opponents. The service was designed around it: see what your friends own and whether they are online, skill-based matchmaking, and try before you buy.",
        ],
        "results": [("6+", "cities of field research"), ("EA", "and other major publishers at launch")],
        "leadership": [
            "Led UX within IDEO's Storytelling Group, turning research into the service concept and interface.",
        ],
        "gallery": [],
        "sources": [
            ("TechCrunch: N-Gage returns as a software-only gaming service", "https://techcrunch.com/2007/08/27/will-it-still-suck-nokia-n-gage-returns-this-week-reborn-as-a-software-only-gaming-service"),
            ("MediaPost: Nokia relaunches N-Gage", "https://www.mediapost.com/publications/article/66399/nokia-relaunches-n-gage-as-smartphone-service.html"),
            ("Wikipedia: N-Gage (service)", "https://en.wikipedia.org/wiki/N-Gage_(service)"),
        ],
    },
    {
        "slug": "spiderman",
        "title": "Spider-Man Main Titles",
        "eyebrow": "Imaginary Forces · Film · 2002",
        "dek": "Art direction on the main title sequence for Sam Raimi's Spider-Man with Kyle Cooper at Imaginary Forces.",
        "facts": [("Role", "Art Director"), ("Studio", "Imaginary Forces"), ("Director", "Kyle Cooper"), ("Film", "Spider-Man (Columbia Pictures, 2002)")],
        "hero": "../images/spiderman.png",
        "problem": [
            "Columbia's producers asked Kyle Cooper and Imaginary Forces to open the first major Spider-Man film with a prologue that set its tone before a single line of dialogue.",
        ],
        "approach": [
            "Built the sequence from the web itself: fractured panels, sketch-line portraiture and graphic diagonals that cut between Peter Parker, Mary Jane and the city.",
        ],
        "results": [],
        "leadership": [
            "Art directed within the Imaginary Forces team. That foundation in motion, narrative and systems thinking runs through every product role since, alongside title work on Minority Report, Panic Room and Band of Brothers.",
        ],
        "gallery": [("../images/cs/spiderman-storyboard.jpg", "Original storyboard for the main title sequence, from the web and the eye to the Marvel card and the cast names")],
        "sources": [
            ("Prologue: Spider-Man", "https://prologue.com/?p=3941"),
            ("Art of the Title: Kyle Cooper", "https://www.artofthetitle.com/designer/kyle-cooper"),
        ],
    },
]

E = html.escape


def native_width(src):
    """Pixel width of a local image, via macOS sips (no third-party deps)."""
    path = (OUT / src).resolve()
    try:
        out = subprocess.run(["sips", "-g", "pixelWidth", str(path)], capture_output=True, text=True).stdout
        return int(out.split("pixelWidth:")[1].strip())
    except Exception:
        return None


def paras(items):
    return "\n".join(f"      <p>{E(p)}</p>" for p in items)


def page(p, prev_p, next_p):
    facts = "\n".join(
        f'      <div class="cs-fact"><div class="cs-fact__label">{E(k)}</div><div class="cs-fact__value">{E(v)}</div></div>'
        for k, v in p["facts"])
    if p.get("hero_phones"):
        imgs = "\n".join(f'    <img src="{src}" alt="">' for src in p["hero_phones"])
        hero = f'  <div class="cs-hero cs-hero--phones">\n{imgs}\n  </div>'
    elif p.get("hero_ui"):  # UI screens: show large (1x), legibility beats retina sharpness
        hero = f'  <div class="cs-hero cs-hero--native cs-hero--ui"><img src="{p["hero_ui"]}" alt="{E(p["title"])}"></div>'
    else:
        w = native_width(p["hero"])
        if w and w < 2880:  # can't fill a 1440px-wide screen at 2x: show at native sharpness
            hero = f'  <div class="cs-hero cs-hero--native"><img src="{p["hero"]}" alt="{E(p["title"])}" style="max-width:{w // 2}px"></div>'
        else:
            hero = f'  <div class="cs-hero"><img src="{p["hero"]}" alt="{E(p["title"])}"></div>'
    results = ""
    if p["results"]:
        tiles = "\n".join(
            f'      <div class="cs-stat"><div class="cs-stat__value">{E(v)}</div><div class="cs-stat__label">{E(l)}</div></div>'
            for v, l in p["results"])
        results = f'''  <section class="cs-section">
    <h2 class="cs-label">Results</h2>
    <div class="cs-stats">
{tiles}
    </div>
  </section>'''
    def fig(item):
        if isinstance(item, list):  # side-by-side pair
            imgs = "".join(f'<div><img src="{src}" alt="{E(alt)}" loading="lazy"><figcaption>{E(alt)}</figcaption></div>' for src, alt in item)
            return f'  <figure class="cs-figure cs-figure--pair">{imgs}</figure>'
        src, alt = item
        return f'  <figure class="cs-figure"><img src="{src}" alt="{E(alt)}" loading="lazy"><figcaption>{E(alt)}</figcaption></figure>'
    gallery = "\n".join(fig(g) for g in p["gallery"])
    extra = (pathlib.Path(__file__).parent / "eventbrite_brand.html").read_text() if p.get("extra") == "EVENTBRITE_BRAND" else ""
    sources = ""
    if p["sources"]:
        items = "\n".join(f'      <li><a href="{E(u)}" target="_blank" rel="noopener">{E(t)}</a></li>' for t, u in p["sources"])
        sources = f'''  <section class="cs-section cs-sources">
    <h2 class="cs-label">Sources</h2>
    <ul>
{items}
    </ul>
  </section>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p["title"])} — Elisabeth Prescott</title>
<meta name="description" content="{E(p["dek"])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/styles.css?v=16">
</head>
<body class="cs-page">

<nav class="nav">
  <a href="../index.html" class="nav__logo">EP</a>
  <div class="nav__links">
    <a href="../index.html#work">Work</a><a href="../index.html#about">About</a><a href="../resume.html">Resume</a><a href="../index.html#contact">Contact</a>
  </div>
</nav>

<main class="cs">
  <header class="cs-header">
    <a class="cs-back" href="../index.html#work">← All work</a>
    <div class="masthead__eyebrow">{E(p["eyebrow"])}</div>
    <h1 class="cs-title">{E(p["title"])}</h1>
    <p class="cs-dek">{E(p["dek"])}</p>
    <div class="cs-facts">
{facts}
    </div>
  </header>

{hero}

  <section class="cs-section">
    <h2 class="cs-label">The problem</h2>
    <div class="cs-body">
{paras(p["problem"])}
    </div>
  </section>

  <section class="cs-section">
    <h2 class="cs-label">The approach</h2>
    <div class="cs-body">
{paras(p["approach"])}
    </div>
  </section>

{extra}

{results}

{gallery}

  <section class="cs-section">
    <h2 class="cs-label">Leadership</h2>
    <div class="cs-body">
{paras(p["leadership"])}
    </div>
  </section>

{sources}

  <nav class="cs-next">
    <a href="{prev_p["slug"]}.html"><span>Previous</span>{E(prev_p["title"])}</a>
    <a href="{next_p["slug"]}.html"><span>Next</span>{E(next_p["title"])}</a>
  </nav>
</main>

<footer class="contact resume__footer">
  <div class="contact__footer">
    <span class="contact__copyright">© 2026 Elisabeth Prescott. All rights reserved.</span>
    <div class="contact__social"><a href="../index.html">Back to work</a></div>
  </div>
</footer>
</body>
</html>
'''


def load_more():
    """Archive projects: one JSON spec per project in _build/projects/."""
    import json
    more = []
    for f in sorted((pathlib.Path(__file__).parent / "projects").glob("*.json")):
        d = json.loads(f.read_text())
        d["facts"] = [tuple(x) for x in d.get("facts", [])]
        d["results"] = [tuple(x) for x in d.get("results", [])]
        d["sources"] = [tuple(x) for x in d.get("sources", [])]
        d["gallery"] = [tuple(g) if isinstance(g[0], str) else [tuple(x) for x in g] for g in d.get("gallery", [])]
        for k in ("problem", "approach", "leadership"):
            d.setdefault(k, [])
        more.append(d)
    more.sort(key=lambda d: (-int(d.get("year", 0)), d["title"]))
    return more


def write_index_grid(more):
    """Fill the More work grid on the home page between its markers."""
    index = OUT.parent / "index.html"
    html_ = index.read_text()
    a, b = "<!-- MORE-WORK:START -->", "<!-- MORE-WORK:END -->"
    if a not in html_:
        return
    cards = "\n".join(
        f'    <a href="casestudy/{E(d["slug"])}.html" class="work-card" data-cat="{E(d.get("category", ""))}">'
        f'<div class="work-card__img" style="background-image:url({E(d["card"].replace("../", ""))})"></div>'
        f'<div class="work-card__meta">{E(d["eyebrow"])}</div><div class="work-card__title">{E(d["title"])}</div></a>'
        for d in more)
    start, end = html_.index(a) + len(a), html_.index(b)
    index.write_text(html_[:start] + "\n" + cards + "\n    " + html_[end:])


def main():
    OUT.mkdir(exist_ok=True)
    more = load_more()
    PROJECTS.extend(more)
    write_index_grid(more)
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        (OUT / f'{p["slug"]}.html').write_text(page(p, PROJECTS[i - 1], PROJECTS[(i + 1) % n]))
    print(f"wrote {n} case studies to {OUT}")


if __name__ == "__main__":
    main()
