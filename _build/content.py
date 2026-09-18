# Content for lennartreic.github.io/Portfolio
# Texts are Lennart's own (from the previous Google Sites portfolio), lightly edited.
# Edit here, then run: python3 _build/build.py

SITE = {
    "name": "Lennart Reichow",
    "email": "lennart.reichow@gmail.com",
    "linkedin": "https://www.linkedin.com/in/lennart-reichow/",
    "tagline": "Shaping public space through interdisciplinary connection.",
    "meta_line": "Urban planner · MSc Nordic Urban Planning Studies · Copenhagen",
    "description": "Portfolio of Lennart Reichow, urban planner in Copenhagen. Projects and research on public space, civil protection, collaborative governance and everyday urban life.",
    "quote": "A good city is like a good party. People stay longer than really necessary, because they are enjoying themselves.",
    "quote_by": "Jan Gehl",
    "youtube_las": "nn3u1KvwxLU",
    "youtube_lygten": "IEmJo--uLfQ",
}

ABOUT = {
    "paragraphs": [
        "I am an urban planner with an MSc in Nordic Urban Planning Studies, combining urban strategy, public-sector consulting and business development. I bring together public and private stakeholders to shape public space.",
        "My master's thesis looked at Helsinki's civil defence bunkers and urban resilience. Before that, I developed Smart City strategies for municipalities, facilitated stakeholder workshops and learned to translate complex topics to anyone. I am also the site planner of a small festival near Berlin, which is urban planning in miniature.",
    ],
    "facts": [
        ("Based in", "Copenhagen, Denmark"),
        ("Languages", "German (native), English (fluent), French and Spanish (basics)"),
        ("Education", "MSc Nordic Urban Planning Studies, Roskilde University (2026)<br>BA Sociology, Politics &amp; Economics, Zeppelin University (2023)"),
        ("Experience", "Smart City consulting (City &amp; Bits), public affairs (Cosmonauts &amp; Kings), business development and sales in Copenhagen"),
    ],
}

# ---------- Selected work (home page tiles, in this order) ----------
WORK = [
    {
        "slug": "swimming-in-the-bunker",
        "title": "Swimming in the Bunker",
        "eyebrow": "Master thesis · Helsinki · 2026",
        "tile": "How institutional trust takes physical form in Helsinki's dual-use civil defence bunkers.",
        "image": "bunker/blast-door",
        "sizes": [1200, 1800],
    },
    {
        "slug": "lost-and-sound",
        "title": "Lost &amp; Sound Festival",
        "eyebrow": "Site planning · Brodowin · 2025 and 2026",
        "tile": "A festival near Berlin with the goal to create space for young artists and guests to get lost in music and space.",
        "image": "las/dancefloor-2026",
        "sizes": [1200, 1920],
    },
    {
        "slug": "lygten-bazar",
        "title": "Lygten Bazar",
        "eyebrow": "Video ethnography · Nørrebro, Copenhagen · 2025",
        "tile": "A video ethnography of Lygten Bazar in Nørrebro, Copenhagen.",
        "image": "lygten/storefront",
        "sizes": [1200, 1920],
    },
    {
        "slug": "student-study",
        "title": "Student Study: Sustainable Urban Development",
        "eyebrow": "Student-led course · Friedrichshafen · 2021",
        "tile": "A self-organised course at Zeppelin University in cooperation with the City of Friedrichshafen.",
        "image": "student-study/poster-langes-feld",
        "sizes": [1200, 2000],
    },
]

# ---------- Research (home page list, in this order) ----------
RESEARCH = [
    {
        "slug": "city-apps",
        "title": "City Apps",
        "question": "How do municipalities develop city apps? A comparative case study.",
        "meta": "Humboldt Project · Zeppelin University · 2022",
    },
    {
        "slug": "strategic-partnerships",
        "title": "Strategic Partnerships",
        "question": "How is trust impacting collaboration?",
        "meta": "Bachelor thesis · Zeppelin University · 2023",
    },
    {
        "slug": "adult-play",
        "title": "Adult Play in Public Spaces",
        "question": "How can we design public spaces to make adults play?",
        "meta": "Group project · Roskilde University · 2024",
    },
    {
        "slug": "helsinki-tallinn",
        "title": "Helsinki-Tallinn Twin City Strategy",
        "question": "How is the relationship perceived from above and below?",
        "meta": "Group project · Roskilde University · 2025",
    },
]

EMAIL_CTA = "lennart.reichow@gmail.com"

# ---------- Project pages ----------
# Block types:
#   ("h2", "Heading")
#   ("p", "Paragraph html")
#   ("ul", ["item", ...])            items may contain html
#   ("figure", {"src": "group/name", "sizes": [..], "alt": "", "caption": "", "framed": bool})
#   ("figgrid", {"items": [figure dicts], "cover": bool})
#   ("video", {"src": "assets/video/x.mp4", "poster": "group/name-1200", "caption": ""})
#   ("youtube", {"id": "...", "poster": "group/name", "sizes": [...], "title": "", "caption": ""})
#   ("cta", "Sentence before the email link")

PAGES = {}

PAGES["swimming-in-the-bunker"] = {
    "section": "work",
    "kind": "Master thesis",
    "title": "Swimming in the Bunker",
    "subtitle": "The spatial materialisation of institutional trust in Helsinki's civil defence system through dual-use bunkers",
    "eyebrow": "Master thesis · Nordic Urban Planning Studies · 2026",
    "description": "Master thesis on Helsinki's dual-use civil defence bunkers: how institutional trust is inscribed, routinised and domesticated in swimming halls, skateparks and sports arenas.",
    "hero": {"src": "bunker/blast-door", "sizes": [1200, 1800], "alt": "Green blast door of a civil defence shelter in Helsinki with a car driving through"},
    "meta": [
        ("Format", "Master thesis"),
        ("University", "Roskilde University, Nordic Urban Planning Studies"),
        ("Supervisor", "Majken Toftager Larsen"),
        ("Cases", "Itäkeskus Swimming Hall, Formula Helsinki, Arena Center Hakaniemi, Luuppi Indoor Skatepark and the Civil Defence Museum Merihaka as contrast case"),
        ("Methods", "Document analysis, semi-structured expert interviews, field observations and walking interviews"),
        ("Year", "2026"),
    ],
    "blocks": [
        ("h2", "Abstract"),
        ("p", "Helsinki has around 5,500 civil defence shelters, enough to protect more than its entire population. Most of them are dual-use: in normal times they operate as swimming halls, sports arenas, skateparks, car parks and go-kart tracks. In a crisis, the Rescue Act requires them to be cleared and converted within 72 hours. My thesis asks how institutional trust in the Finnish civil defence system is spatially materialised through these bunkers: how it is written into laws, contracts and materials, how it is kept alive through routines, and how it becomes so normal that nobody thinks about the blast doors on the way to the pool."),
        ("p", "While other European countries are rebuilding civil protection from scratch, Finland has spent decades weaving it into ordinary city life. The thesis argues that this arrangement is not just a technical solution. It is trust that has taken physical form."),
        ("figure", {"src": "bunker/pool-itakeskus", "sizes": [1200, 2000], "alt": "Swimming hall built into bedrock in Itäkeskus, Helsinki", "caption": "Itäkeskus Swimming Hall, built into the bedrock and used by around 500,000 visitors a year."}),
        ("h2", "Methods"),
        ("p", "The thesis is a qualitative single-case study. I combined an analysis of legal and policy documents (the Rescue Act, lease contracts and guidelines) with semi-structured expert interviews with the Helsinki Rescue Department, the city and civic organisations, and with field observations and informal walking interviews at five sites: Itäkeskus Swimming Hall, the Formula Helsinki go-kart track, Arena Center Hakaniemi, Luuppi Indoor Skatepark and, as a contrast case, the Civil Defence Museum in Merihaka, the only site without an everyday civilian use."),
        ("p", "The material was coded along three mechanisms that together form the analytical framework: inscription, routinisation and domestication."),
        ("figgrid", {"cover": True, "items": [
            {"src": "bunker/arena-center", "sizes": [1200, 2000], "alt": "Blue blast doors and a red running figure in the entrance of Arena Center Hakaniemi", "caption": "Arena Center Hakaniemi. A playful path leads through the blast doors into the sports arena."},
            {"src": "bunker/luuppi-doors", "sizes": [1200, 2000], "alt": "Graffiti-covered blast door and gas-tight door at Luuppi Indoor Skatepark", "caption": "Luuppi Indoor Skatepark. The blast door and the gas-tight door are completely covered in graffiti."},
            {"src": "bunker/luuppi-hall", "sizes": [1200, 2000], "alt": "Wooden ramps inside the Luuppi skate hall carved into rock", "caption": "The skatepark is built from timber. Fixed concrete obstacles are ruled out by the 72-hour clearance obligation."},
            {"src": "bunker/formula-helsinki", "sizes": [1200, 2000], "alt": "Green LED light on the underground go-kart track of Formula Helsinki", "caption": "Formula Helsinki. An underground go-kart track in a former military shooting range."},
        ]}),
        ("h2", "Findings"),
        ("p", "Institutional trust in Helsinki's dual-use bunkers is not a cultural baseline the system happens to enjoy. It is something the system actively produces. Trust is <strong>inscribed</strong> into regulation and material: the skatepark is built from plywood because concrete would break the 72-hour rule. It is <strong>routinised</strong> through inspections, training and operators who simply run their business, which confirms again and again that the system will work when it is needed. And it is <strong>domesticated</strong> through everyday use: the strongest sign of a resilient system is that people stop paying attention to it."),
        ("p", "The Civil Defence Museum was the case-internal proof. It is the only site where the shelter function is deliberately in the foreground, and it was the only place during fieldwork where the shelter felt close and present. In a mature institutional arrangement, preparedness looks like ordinary life."),
        ("h2", "Implications &amp; Personal Learning"),
        ("p", "For cities that are rebuilding civil protection today, the Helsinki case shows that dual-use is more than a way to save money. It is a design principle that bridges the slow time of hardened infrastructure and the fast, changing needs of urban life. Trust works as a governance technology: it lowers the cost of coordination without the state stepping back, because the state still legislates, funds and inspects."),
        ("p", "Personally, the thesis connected my interest in public space with civil protection and urban resilience, a field that most European cities are only now rediscovering. It also taught me to read infrastructure through the people who use it every day: the swimmer, the skater, the operator with a lap record he is proud of."),
        ("cta", "The full thesis is available on request. If you work on civil protection, dual-use infrastructure or urban resilience, I would love to exchange ideas."),
    ],
}

PAGES["lost-and-sound"] = {
    "section": "work",
    "kind": "Festival",
    "title": "Lost &amp; Sound Festival",
    "subtitle": "Site planning for a fully biological music and arts festival on an organic farm near Berlin",
    "eyebrow": "Site planning · Brodowin, Brandenburg · 2025 and 2026",
    "description": "Site planner for Lost & Sound, a non-profit music and arts festival on an organic farm in Brodowin near Berlin: masterplan, site plans, materials and on-site coordination.",
    "hero": {"src": "las/night-aerial-2026", "sizes": [1200, 2000], "alt": "Aerial view of the illuminated festival site at night, 2026"},
    "meta": [
        ("Format", "Festival, non-profit association"),
        ("My role", "Site planner"),
        ("Place", "Organic farm, former GDR potato chip factory in Brodowin (90 min from Berlin)"),
        ("Edition", "4th edition in 2026"),
        ("Duration", "3 days"),
        ("Visitors", "850"),
        ("Stages", "4"),
        ("Team and volunteers", "60"),
    ],
    "blocks": [
        ("h2", "Overview"),
        ("p", "Lost &amp; Sound is a fully biological music and arts festival that takes place on the grounds of an organic farm in Brodowin. It is conceived as an immersive space rather than a conventional event: there is no clear separation between audience and performers, no fixed paths, and no single way to experience the festival. Visitors are participants, moving freely between music, quiet moments, nature and spontaneous encounters."),
        ("p", "Founded by five students and realised through the commitment of many volunteers, the festival aims to give small and emerging artists a stage and to create an environment where self-expression, connection and sustainability are lived practices rather than abstract ideas. By 2026, Lost &amp; Sound has grown to 850 visitors, with four stages and a wide range of informal spaces in between: places to dance, to pause, to meet others, or to get lost for a while. The festival balances collective energy with intimacy, creating a temporary landscape where music, people and environment merge."),
        ("youtube", {"id": "nn3u1KvwxLU", "poster": "las/night-aerial-2026-alt", "sizes": [1200, 2000], "title": "Lost & Sound Festival 2026, night flight over the site", "caption": "Night flight over the festival site, 2026. Video opens on YouTube."}),
        ("split", {
            "figure": {"src": "las/explaining-plan", "sizes": [1200], "alt": "Lennart explaining the site plan drawn on a large concrete wall", "caption": "Explaining the site plan to the team on site."},
            "blocks": [
                ("h2", "What is my role?"),
                ("p", "My role at Lost &amp; Sound is Site Planner. I am responsible for translating many individual ideas into a coherent spatial plan that can be built and used during the festival. This involves creating maps and layouts that align artistic visions, practical requirements and the natural conditions of the site."),
                ("p", "Rather than directing creatives or craftsmen, my task is to facilitate collaboration. I bring together volunteers, builders, artists and organisers, coordinate materials and workflows, and make sure that ideas can be realised on site without losing their character. The planning process is highly iterative and hands-on, closely connected to construction and on-site improvisation."),
                ("p", "The work starts around six months before the festival with concept meetings, where ideas for stages, social spaces and chill-out areas are developed and discussed. Based on these inputs, a masterplan is created in close coordination with other teams, including technical production and infrastructure (toilets, food, logistics), to ensure spatial and operational alignment across the site."),
                ("p", "One of the most challenging aspects is organising materials within a very limited budget. Relying largely on reused materials, second-hand items and donated resources requires creative problem-solving and flexible design solutions, turning material constraints into a driver for spatial creativity."),
            ],
        }),
        ("video", {"src": "assets/video/las-setup-2025.mp4", "poster": "las/setup-2025-poster", "caption": "Drone flight over the site during setup, 2025."}),
        ("h2", "The Snake Bench"),
        ("p", "A project I am particularly proud of is a large bench structure I designed in 2025. It was conceived as a flexible social element: a place where many small groups could sit together, interact or remain slightly separate, depending on how it was used. At the same time, the structure functioned as a small stage, allowing it to shift between everyday use and performance."),
        ("figure", {"src": "las/snake-bench", "sizes": [1200], "alt": "Curved wooden bench built from reclaimed timber on the asphalt site", "caption": "The Snake Bench, built from reclaimed timber by volunteers.", "max": 720}),
        ("h2", "Edition 2026"),
        ("p", "For the first time, a large part of the visitors found the festival through Instagram: a community that had formed online and then helped a lot with building the site."),
        ("p", "Spatially, the goal for 2026 was to give the site a clearer edge. We used construction fences for the first time, even though the owner of the farm is generally against fences. To keep them from looking bare, we covered them with white tarpaulin and hung up coloured markers, so guests could paint them themselves. A small participatory element that turned a boundary into a canvas."),
        ("p", "The large open asphalt area remained a challenge. A planned swing built from an old boat did not make it into the build. Instead, we concentrated on permanent timber structures for the coming years: the bar and the fire pit. The goal of making the site feel rounder and avoiding dead corners worked out really well."),
        ("figure", {"src": "las/site-plan-2026", "sizes": [1200], "alt": "Site plan 2026 on an aerial photo with stages, bar, camping and routes", "caption": "Site plan 2026.", "framed": True, "max": 960}),
        ("cta", "Curious how a festival site comes together, from concept meeting to the last pallet? I am happy to share plans and lessons learned."),
    ],
}

PAGES["lygten-bazar"] = {
    "section": "work",
    "kind": "Video ethnography",
    "title": "Lygten Bazar",
    "subtitle": "Lived multicultural urbanism in Nørrebro",
    "eyebrow": "Video ethnography · Cities, Culture &amp; Politics · 2025",
    "description": "A video ethnography of Lygten Bazar in Nørrebro, Copenhagen, produced for the course Cities, Culture & Politics at Roskilde University.",
    "hero": {"src": "lygten/storefront", "sizes": [1200, 1920], "alt": "Storefront of Lygten Bazar in Nørrebro with vegetable crates and bicycles"},
    "meta": [
        ("Format", "Exam project for the course Cities, Culture &amp; Politics"),
        ("University", "Roskilde University, Nordic Urban Planning Studies"),
        ("Supervisor", "David Pinder"),
        ("Collaboration", "Lygten Bazar, Nørrebro"),
        ("Produced with", "Gerald Reed Dolan"),
        ("Year", "2025"),
    ],
    "blocks": [
        ("h2", "About the project"),
        ("p", "This video project was produced as part of the course Cities, Culture &amp; Politics in the Nordic Urban Planning Studies programme at Roskilde University. The course examines how urban spaces are shaped by the interaction of culture, economy and power, and how everyday places reveal broader political and social dynamics in cities."),
        ("p", "Our project focused on Lygten Bazar in Nørrebro, Copenhagen, a local market that functions as more than a place to buy groceries. The bazar brings together diverse cultural backgrounds, products and practices, creating a space where economic exchange, social interaction and cultural identity are closely intertwined. It attracts both people seeking familiar goods from their countries of origin and others looking for an intercultural urban experience."),
        ("youtube", {"id": "IEmJo--uLfQ", "poster": "lygten/aerial-building", "sizes": [1200, 1920], "title": "Lygten Bazar, video ethnography", "caption": "The film (6 min). Produced together with Gerald Reed Dolan. Enjoy!"}),
        ("h2", "Approach"),
        ("p", "The video explores the bazar as a lived urban space rather than a branded or curated one. Due to filming restrictions, we avoided showing faces and instead focused on textures, sounds, movements and everyday interactions. This shifted our attention to how people navigate the space, how informal routines emerge, and how a sense of atmosphere and belonging is produced through ordinary practices."),
        ("p", "Through filming and interviews, the project also revealed tensions surrounding visibility, gentrification and urban branding. While Lygten Bazar represents a grassroots cultural economy, it exists within a city increasingly shaped by redevelopment and marketing strategies. The video therefore reflects both the vibrancy of everyday multicultural urban life and its fragile position within wider urban transformation processes."),
        ("figgrid", {"cover": True, "items": [
            {"src": "lygten/spices", "sizes": [1200, 1920], "alt": "A crate full of walnuts", "caption": "Stills from the film: textures, hands and goods instead of faces."},
            {"src": "lygten/peppers", "sizes": [1200, 1920], "alt": "A hand picking a red pepper from a crate", "caption": ""},
            {"src": "lygten/hands", "sizes": [1200, 1920], "alt": "Fish on ice at the counter with a handwritten price sign", "caption": ""},
            {"src": "lygten/metro", "sizes": [1200, 1920], "alt": "The square in front of Nørrebro station with parked bicycles", "caption": ""},
        ]}),
        ("cta", "Interested in ethnographic methods in planning, or simply in Nørrebro? I am happy to hear from you."),
    ],
}

PAGES["student-study"] = {
    "section": "work",
    "kind": "Student-led course",
    "title": "Student Study: Sustainable Urban Development",
    "subtitle": "A self-organised semester course at Zeppelin University in cooperation with the City of Friedrichshafen",
    "eyebrow": "Student Study · Zeppelin University · 2021",
    "description": "A student-organised semester course on sustainable urban development at Zeppelin University, working with the City of Friedrichshafen on the climate-neutral district Langes Feld.",
    "hero": {"src": "student-study/map-friedrichshafen", "sizes": [1200], "alt": "Plan of Friedrichshafen with the Langes Feld development area marked in red", "contain": True, "caption": "Plan of Friedrichshafen with the \u201cLanges Feld\u201d marked in red."},
    "meta": [
        ("Format", "Student Study (group-based, student-led course, 6 ECTS)"),
        ("University", "Zeppelin University"),
        ("Supervisor", "Chair of Socio-Economics"),
        ("Collaboration", "City of Friedrichshafen (municipal planning practice)"),
        ("Participants", "25 students"),
        ("Year", "2021"),
    ],
    "blocks": [
        ("h2", "Overview"),
        ("p", "Together with three fellow students, I organised the Student Study “Sustainable Urban Development”, a semester-long academic format at Zeppelin University. A Student Study allows students to design and run their own course (6 ECTS) alongside the formal curriculum. As organisers, we were responsible for the course content, the organisation of guest lecturers, and the seamless operation of the course. While the standard examination format is a presentation and report, our assessment consisted of an extensive reflective paper on the course itself."),
        ("p", "The central case was the planned development of “Langes Feld”, Friedrichshafen's first climate-neutral urban district. The area is a long-term urban development project designed for approximately 2,500 residents and involves complex challenges related to climate neutrality, mobility, green infrastructure, housing, governance and citizen participation. The project combined academic input with real-world practice through close cooperation with the City of Friedrichshafen."),
        ("h2", "Interdisciplinary Process &amp; Methods"),
        ("p", "The Student Study combined expert input, methodological training and collaborative group work in an interdisciplinary setting. Weekly thematic sessions brought together perspectives from academia, public administration and professional practice, complemented by direct input from the City of Friedrichshafen on planning frameworks, constraints and long-term ambitions for the “Langes Feld” district."),
        ("p", "Alongside these inputs, participants worked in small groups on specific dimensions of sustainable urban development for the Langes Feld case. The thematic focus areas included:"),
        ("ul", [
            "Climate-neutral urban districts and blue-green infrastructure",
            "Sustainable mobility and transport economics",
            "Smart City concepts, digitalisation and open government",
            "Integration of urban development strategies (SDGs, SMART goals)",
            "Corporate Urban Responsibility and the role of private actors",
            "Cultural planning, participation and place-based identity",
        ]),
        ("p", "Methodologically, the course relied on stakeholder analysis, long-term perspective building and user-centred approaches such as personas and Design Thinking to better understand citizen needs. Impact-oriented goal setting and strategic reflection on governance, implementation and scalability were central throughout the process."),
        ("p", "A strong emphasis was placed on recognising real planning trade-offs, for example between climate targets and housing demand, infrastructure expansion and environmental protection, or digital efficiency and ethical and democratic concerns. Rather than aiming for a single master plan, the process encouraged iterative thinking, critical reflection and realistic positioning within municipal planning realities."),
        ("h2", "Outcome"),
        ("p", "The Student Study resulted in five coherent conceptual approaches developed by each group, addressing the core dimensions mentioned above. Key outcomes included:"),
        ("ul", [
            "Strategically grounded concept ideas for a climate-neutral urban district",
            "A deep understanding of sustainable urban development as a long-term, negotiated and multi-actor process",
            "Practical experience in working at the interface of academia, public administration and urban practice",
        ]),
        ("p", "Beyond the concrete outputs, the Student Study functioned as a real-world learning laboratory. It demonstrated how universities can actively contribute to local urban transformation and laid the groundwork for continued cooperation between students, the university and the City of Friedrichshafen."),
        ("figure", {"src": "student-study/poster-langes-feld", "sizes": [1200, 2000], "alt": "Consolidated sketch of the Langes Feld district combining the concepts of all groups", "caption": "Consolidated sketch combining the outcomes of all groups (in German).", "framed": True}),
        ("h2", "Personal Learning"),
        ("p", "Organising the course was my first direct exposure to planning actors from municipalities, academia and private companies. This experience significantly broadened my perspective and deepened my interest in urban planning. It became the first real spark in my planning career."),
        ("p", "I was particularly drawn to the idea that many global challenges can be addressed at the local scale, by working with the people who are actively shaping cities and implementing change. Engaging with practitioners and understanding the groundwork behind urban transformation fascinated me, and continues to do so."),
        ("p", "Through the Student Study, I also established contact with the consultancy City &amp; Bits, who contributed a lecture on personas, Design Thinking and their work with municipalities. This connection led to an internship and later a position as a student worker. Ultimately, these experiences played a key role in my decision to pursue urban planning as a field of study. In this sense, the Student Study marked the beginning of something much larger."),
        ("cta", "Interested in the concepts or in the course format? I am happy to share the reflective paper."),
    ],
}

PAGES["city-apps"] = {
    "section": "research",
    "kind": "Humboldt Project",
    "title": "Effects of Collaborative Innovation on the Design of City Apps",
    "subtitle": "How do municipalities develop city apps? A comparative case study of four German cities",
    "eyebrow": "Research · Humboldt Project · 2022",
    "description": "Research project on collaborative innovation in the development of municipal city apps, comparing Karlsruhe, Solingen, Wolfsburg and HEAG Darmstadt.",
    "hero": None,
    "meta": [
        ("Format", "Humboldt Project"),
        ("University", "Zeppelin University"),
        ("Supervisor", "Chair of Public Management &amp; Public Policy (Prof. Dr. Ulf Papenfuß)"),
        ("Cases", "City of Karlsruhe, City of Solingen, City of Wolfsburg, HEAG Darmstadt"),
        ("Year", "2022"),
    ],
    "blocks": [
        ("h2", "Abstract"),
        ("p", "There is competition between platform companies and urban actors to provide digital public services. This research project investigates the effects of collaborative innovation on the design of city apps in order to further explore and improve the practical implementation of collaborative innovation. For this purpose, a comparative case study of four German city apps was conducted. The results show that city apps are limited in their design by problems known from the literature (technical know-how, conflicts of interest, goal congruence). Further research should conduct area-wide, empirical surveys on the interests of additional urban representatives."),
        ("h2", "Methods"),
        ("p", "The project applied a qualitative research design focused on understanding governance and collaboration processes behind city apps. A comparative case study approach was used to analyse multiple city apps across four different German municipalities. Data was collected through semi-structured expert interviews with project leads and operational stakeholders involved in the development and management of the apps. The interviews were systematically coded to identify patterns in cooperation, decision-making and responsibility allocation. Particular attention was paid to governance structures, actor constellations and implementation challenges rather than technical features. This approach allowed for an in-depth understanding of institutional dynamics and power relations shaping digital public services. The qualitative design was chosen to capture complexities that are often overlooked by purely quantitative evaluations of digital tools."),
        ("figure", {"src": "research/digital-services-framework", "sizes": [1200], "alt": "Diagram of the fields of digital public services between civil society, state and economy", "caption": "Fields of digital public services between civil society, state and economy (in German).", "framed": True, "max": 760}),
        ("h2", "Implications &amp; Personal Learning"),
        ("p", "The findings imply that the success of city apps depends more on governance capacity and coordination than on technological sophistication. Collaborative innovation can increase legitimacy and idea quality, but only if roles, responsibilities and expectations are clearly defined. Municipalities risk long-term dependency when strategic control over data and development is outsourced to private actors. City apps should therefore be understood as ongoing governance projects rather than short-term digital products."),
        ("p", "From this work, I learned to critically assess digitalisation narratives and to distinguish between technical solutions and institutional realities. I also developed a deeper understanding of how public sector constraints shape innovation processes. Personally, the project strengthened my ability to translate abstract governance concepts into concrete, practice-oriented insights."),
        ("cta", "Interested in the full report (in German) or in how cities build digital services? I am happy to share it."),
    ],
}

PAGES["strategic-partnerships"] = {
    "section": "research",
    "kind": "Bachelor thesis",
    "title": "Empirical Findings on Strategic Partnerships between City Administrations, Municipal Companies and Private Startups",
    "subtitle": "How is trust impacting collaboration in digital public services?",
    "eyebrow": "Research · Bachelor thesis · 2023",
    "description": "Bachelor thesis on trust and cooperation in partnerships between city administrations, municipal companies and startups in Germany, based on a nationwide survey (n = 39).",
    "hero": None,
    "meta": [
        ("Format", "Bachelor thesis"),
        ("University", "Zeppelin University"),
        ("Supervisor", "Chair of Public Management &amp; Public Policy (Prof. Dr. Ulf Papenfuß)"),
        ("Subject", "Municipalities, municipal companies and startups"),
        ("Data", "Nationwide online survey, n = 39"),
        ("Year", "2023"),
    ],
    "blocks": [
        ("h2", "Abstract"),
        ("p", "To ensure a sovereign digital provision of services of general interest within the framework of SDG 17.17, the cooperation of the actors administration, municipal companies and start-ups is necessary in Germany. This work has collected empirical findings (n = 39) in this network. Based on the results, a good basis for cooperation can be derived. Known weaknesses of the administration were confirmed as obstacles to cooperation. The results also show that start-ups have complementary strengths. Using linear regressions, a positive correlation was found between trust and network performance, as well as between trust and network cooperation. Accordingly, actors' trust in cooperation should be actively promoted through network strategies."),
        ("h2", "Methods"),
        ("p", "The bachelor thesis employed a quantitative research design to analyse partnerships in the context of digital public services in Germany. Data was collected through a nationwide online survey targeting actors from public administrations, municipal enterprises and startups. The survey operationalised key concepts from network governance theory, including trust, cooperation quality and network performance. Descriptive statistics were used to identify structural patterns across actor groups. Linear regression models were applied to examine the relationship between trust and both cooperation and performance outcomes. This approach enabled a systematic comparison of perceptions across different organisational contexts. The quantitative design was chosen to complement existing qualitative research on public-private collaboration with empirical evidence."),
        ("h2", "Implications &amp; Personal Learning"),
        ("p", "The results indicate that trust is a central enabling factor for effective partnerships in digital public services. Formal structures and contracts alone are insufficient to ensure productive collaboration across organisational boundaries. Municipal enterprises can play a crucial intermediary role between public administrations and startups by translating logics and expectations. Digital public services should therefore be governed as long-term collaborative networks rather than isolated innovation projects."),
        ("p", "Through this thesis, I learned how abstract governance concepts can be empirically tested and operationalised. I also gained practical experience in survey design, data analysis and regression modeling. On a personal level, the project strengthened my interest in governance, collaboration and public value creation in digital transformation processes."),
        ("cta", "Interested in the thesis (in German) or in the survey data? I am happy to share it."),
    ],
}

PAGES["adult-play"] = {
    "section": "research",
    "kind": "Group project",
    "title": "In Defense of Public Adult Play",
    "subtitle": "How can public spaces in Copenhagen be planned to make adults play?",
    "eyebrow": "Research · Group project · 2024",
    "description": "Group project at Roskilde University on adult play in public spaces in Copenhagen, using Practice Theory, case studies of Guldbergs Plads and Fælledparken, and a planning checklist.",
    "hero": None,
    "meta": [
        ("Format", "Group project"),
        ("University", "Roskilde University, Nordic Urban Planning Studies"),
        ("Supervisor", "Jonas Larsen, Department of People and Technology"),
        ("Cases", "Guldbergs Plads and Fælledparken, Copenhagen"),
        ("Year", "2024"),
    ],
    "blocks": [
        ("h2", "Abstract"),
        ("p", "This research examines how public urban spaces in Copenhagen can be planned to encourage adult play practices. Drawing on Practice Theory, the study analyses how materials, competences and meanings shape adult play, challenging the assumption that play is primarily for children. Using case studies, observations, document analysis, expert interviews and a survey, the research shows that adult play is supported by natural environments and social infrastructure but constrained by social stigma and physical ability. The findings highlight how adult play is often reframed as exercise or competition to gain legitimacy. The study argues for urban spaces that support diverse forms of adult play and introduces the concept of “The Right to the Playground” as a planning principle for equitable access to playful public spaces."),
        ("h2", "Methods"),
        ("p", "The project applied a qualitative, theory-driven research design grounded in Practice Theory to analyse adult play in public space. Two case studies in Copenhagen, Guldbergs Plads and a grass field in Fælledparken, were selected to compare different spatial and social conditions. Empirical data was collected through on-site observations, document analysis of planning strategies, expert interviews and a survey. Observations focused on how adults used space, interacted with others and navigated social norms around play. Interviews with planners, designers and private play operators provided insights into institutional perspectives and design intentions. The survey complemented qualitative findings by capturing broader perceptions of adult play, barriers and motivations. This mixed-method approach allowed the project to connect everyday practices with planning frameworks and welfare-state contexts."),
        ("figure", {"src": "research/guldbergs-plads-map", "sizes": [1200], "alt": "Hand-drawn map of Guldbergs Plads with photos of swings, gymnastics rings, benches and bars", "caption": "Map of Guldbergs Plads and its options for play.", "framed": True, "max": 820}),
        ("h2", "Implications &amp; Personal Learning"),
        ("p", "The findings suggest that adult play is less constrained by spatial absence than by social norms, stigma and perceived legitimacy. Natural environments and flexible spaces support adult play, while rigid or overly programmed designs tend to limit it. Adult play is often reframed as exercise, competition or fitness to align with socially accepted meanings. For planning practice, this implies that enabling adult play requires addressing both spatial design and cultural meanings. Public spaces should support a range of playful competences, abilities and seasonal uses to ensure inclusivity."),
        ("p", "Through this project, I learned to analyse public space as a product of practices rather than fixed functions. Personally, the research strengthened my ability to link theory, empirical observation and concrete planning recommendations, and deepened my interest in human-centred and welfare-oriented urban planning."),
        ("h2", "A checklist for planners"),
        ("p", "Based on our findings we formulated a checklist that planners can use when they plan for play:"),
        ("ul", [
            "<span class=\"li-title\">Who do you want?</span> Planning for everyone doesn't work when planning for play. Choose a clear target group and design play elements for them.",
            "<span class=\"li-title\">Look &amp; fit.</span> Adjust colours and materials to adult tastes.",
            "<span class=\"li-title\">People magnet.</span> Attract and keep other people (beyond the target group) as social infrastructure. They don't have to play.",
            "<span class=\"li-title\">Beginner friendly.</span> Make it easy to join in. Include elements that work for low physical and mental confidence or ability.",
            "<span class=\"li-title\">Challenge time.</span> Match the target group's competences and enable competition on different levels.",
            "<span class=\"li-title\">Nature.</span> Nature appeals to most people. Use seasonality playfully and integrate climate adaptation features.",
            "<span class=\"li-title\">Open space.</span> Leave room for unplanned, spontaneous play.",
            "<span class=\"li-title\">No sweat without fun.</span> Offer fitness potential, but keep fun as the main focus.",
            "<span class=\"li-title\">No fun without risk.</span> Add exciting elements. Play involves risk, but it should not be dangerous.",
            "<span class=\"li-title\">Outside the ordinary.</span> Create an environment that feels different from everyday life, making it easier to play (and be a bit weird).",
            "<span class=\"li-title\">Be aware of kids.</span> Kids can spark play for parents and playful adults, but they can also dominate an area and discourage adult play.",
            "<span class=\"li-title\">The right to the playground.</span> Some groups may be marginalised. Observe who uses the space, how it develops, and who feels welcome.",
        ]),
        ("cta", "Interested in the full report or in planning for play? I am happy to share it."),
    ],
}

PAGES["helsinki-tallinn"] = {
    "section": "research",
    "kind": "Group project",
    "title": "Two Branches of the Same Tree: Rethinking the Helsinki-Tallinn Twin City Strategy",
    "subtitle": "How is the relationship between the two capitals perceived from above and below?",
    "eyebrow": "Research · Group project · 2025",
    "description": "Group project at Roskilde University on the Helsinki-Tallinn twin city strategy, comparing planning documents and expert interviews with 34 interviews conducted on the ferries.",
    "hero": None,
    "meta": [
        ("Format", "Group project"),
        ("University", "Roskilde University, Nordic Urban Planning Studies"),
        ("Supervisor", "Anette Stenslund, Department of People and Technology"),
        ("Cases", "City of Helsinki, City of Tallinn"),
        ("Data", "8 policy documents, 5 expert interviews, 34 interviews on board the ferries"),
        ("Year", "2025"),
    ],
    "blocks": [
        ("h2", "Abstract"),
        ("p", "This project examines the Helsinki-Tallinn twin city strategy through the lens of planning practices and everyday mobilities. Despite strong political narratives promoting cross-border integration, the research reveals a disconnect between strategic ambitions and lived experiences. Using document analysis, expert interviews and ferry-based interviews, the study identifies asymmetries in planning priorities, economic power and cultural engagement, and argues for a more plural and practice-oriented understanding of the twin city relationship."),
        ("figure", {"src": "research/gulf-of-finland-map", "sizes": [1200], "alt": "Map of the Gulf of Finland between Helsinki and Tallinn", "caption": "80 kilometres of sea between the two capitals.", "framed": True}),
        ("h2", "Methods"),
        ("p", "The project employed a qualitative, multi-method research design to analyse the Helsinki-Tallinn twin city strategy. Eight policy and planning documents were analysed to understand official narratives and strategic goals. Five expert interviews with planners and policy actors in both cities provided insight into institutional perspectives and governance priorities. 34 semi-structured interviews conducted aboard ferries captured everyday mobility practices and user perceptions. This ferry-based fieldwork allowed the project to observe cross-border mobility as a lived social practice. The analysis was guided by the concepts of soft spaces, urban identity and Lefebvre's theory of spatial production. Together, these methods enabled a comparison between conceived planning spaces and everyday experiences."),
        ("h2", "Implications &amp; Personal Learning"),
        ("p", "The findings suggest that twin city strategies risk remaining symbolic when they are not grounded in everyday practices and institutionalised forms of interaction. The Helsinki-Tallinn relationship is characterised by asymmetries, with Tallinn relying more heavily on the twin city narrative than Helsinki. This highlights the need for more flexible and plural policy framings that acknowledge differing interests and identities. Practical implications include strengthening cultural exchange mechanisms beyond transport infrastructure and recognising distinct urban identities within integration strategies."),
        ("p", "Through this project, I learned how mobility-based fieldwork can reveal gaps between planning discourse and lived experience. I also developed a stronger understanding of cross-border governance and identity formation. Personally, the project sharpened my ability to integrate theory, qualitative methods and critical spatial analysis in complex urban contexts."),
        ("cta", "Interested in the full report or in cross-border planning? I am happy to share it."),
    ],
}

# Order used for "Next project" links
ORDER = ["swimming-in-the-bunker", "lost-and-sound", "lygten-bazar", "student-study",
         "city-apps", "strategic-partnerships", "adult-play", "helsinki-tallinn"]
