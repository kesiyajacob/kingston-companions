from app import app
from models import db, Activity, User
from werkzeug.security import generate_password_hash, check_password_hash

with app.app_context():
    db.drop_all()
    db.create_all()

    activities = [
        Activity(
            name="Canada's Penitentiary Museum",
            keywords="history, learning, displays",
            description="Explore Canada’s federal corrections history in a historic building, with exhibits on prison life, rehabilitation programs, inmate arts and crafts, and historical artifacts",
            image="penitentiary.jpg",
            url="https://www.penitentiarymuseum.ca/"

        ),
        Activity(
            name="1000 Islands Cruise",
            keywords="scenic, nature, relaxed, seated, outdoor, conversational",
            description="Enjoy scenic cruises along the St. Lawrence River, passing historic estates and islands, with options for sightseeing, dining, and live commentary.",
            image="1000_islands_cruise.jpg",
            url="https://www.1000islandscruises.ca/"
    
        ),
        Activity(
            name="Fort Henry National Historic Site",
            keywords="history, outdoor, walking, learning, scenic",
            description="Tour a 19th-century military fort with historic buildings, reenactments, and panoramic views of Kingston Harbour.",
            image="fort_henry.jpg",
            url="https://www.forthenry.com/"
           
        ),
        Activity(
            name="Great Lakes Museum",
            keywords="history, learning, quiet, indoor",
            description="Discover exhibits about the ecology, history, and shipping of the Great Lakes, with interactive displays and artifacts.",
            image="great_lakes_museum.png",
            url="https://greatlakesmuseum.ca/"

        ),
        Activity(
            name="Miller Museum of Geology",
            keywords="learning, science, quiet, indoor",
            description="Explore collections of rocks, minerals, and fossils while learning about geological history in an indoor museum setting.",
            image="miller_museum_of_geology.jpg",
            url="https://www.queensu.ca/millermuseumofgeology/"
            
        ),
        Activity(
            name="Frontenac County Schools Museum",
            keywords="history, learning, quiet, indoor",
            description="Explore exhibits on the history of local education and schools in an indoor museum setting.",
            image="frontenac_county_schools_museum.webp",
            url="https://www.fcsmuseum.com/"
            
        ),
        Activity(
            name="Military Communications & Electronics Museum",
            keywords="history, learning, quiet, indoor",
            description="Discover military technology and electronics history through indoor exhibits and artifacts.",
            image="military_communications.jpeg",
            url="https://www.candemuseum.org/"
            
        ),
        Activity(
            name="Original Hockey Hall of Fame",
            keywords="history, sports, learning, indoor, conversational",
            description="View hockey memorabilia and exhibits in an indoor, seated space suitable for fans and casual visitors.",
            image="original_hockey_hall_of_fame.webp",
            url="https://www.originalhockeyhalloffame.com/"
        ),
        Activity(
            name="Pumphouse Museum",
            keywords="history, learning, quiet, indoor",
            description="Explore the museum’s model trains, local history exhibits, and interactive displays indoors.",
            image="pumphouse_museum.jpg",
            url="https://www.kingstonpumphouse.ca/"
       
        ),
        Activity(
            name="Historic City Hall",
            keywords="history, learning, quiet, indoor",
            description="Tour the historic building and learn about Kingston’s civic history in an indoor setting.",
            image="historic_city_hall.jpg",
            url="https://www.cityofkingston.ca/arts-culture-and-events/history-and-heritage/city-hall/"
       
        ),
        Activity(
            name="Canadian Museum of Healthcare",
            keywords="history, learning, quiet, indoor",
            description="Explore exhibits on the history of healthcare and medicine indoors.",
            image="canadian_museum_of_healthcare.webp",
            url="https://www.museumofhealthcare.ca/"
            
        ),

        Activity(
            name="The Screening Room",
            keywords="film, quiet, seated, indoor",
            description="Watch independent and classic films in a small, comfortable indoor cinema.",
            image="the_screening_room.avif",
            url="https://www.screeningroomkingston.com/the-screening-room-movie-theatre"
           
        ),
        Activity(
            name="Landmark Cinemas",
            keywords="film, seated, indoor, casual",
            description="Enjoy popular movies in a modern indoor theater with comfortable seating and concessions.",
            image="landmark_cinemas.jpg",
            url="https://www.landmarkcinemas.com/showtimes/kingston"
           
        ),
        Activity(
            name="Bellevue House",
            keywords="history, learning, walking, scenic",
            description="Tour the historic home of Canada’s first Prime Minister, including indoor exhibits and gardens.",
            image="bellevue_house.webp",
            url="https://parks.canada.ca/lhn-nhs/on/bellevue"
            
        ),

        Activity(
            name="Isabel Bader Centre for Performing Arts",
            keywords="theatre, music, seated, indoor",
            description="Attend concerts, performances, and art events in a modern indoor venue.",
            image="isabel_bader_centre.webp",
            url="https://www.queensu.ca/theisabel/"
            
        ),
        Activity(
            name="Martello Alley",
            keywords="art, casual, outdoor, conversational",
            description="Walk through an art-focused alley featuring local artists’ works in a casual, open space.",
            image="martello_alley.jpg",
            url="https://www.martelloalley.com/en-us?srsltid=AfmBOor1-HjB7FQALzBMhqmLMhruuOcldd_9wPrf-nSLf00p1TTzzZ3-"
          
        ),
        Activity(
            name="Improbable Escapes",
            keywords="games, puzzles, indoor, lively",
            description="Solve puzzles and complete challenges in immersive escape rooms that encourage teamwork and problem-solving.",
            image="improbable_escapes.jpg",
            url="https://improbableescapes.com/"
            
        ),
        Activity(
            name="Sherlock's Escapes",
            keywords="games, puzzles, indoor, lively",
            description="Solve immersive puzzles and challenges in themed escape rooms indoors.",
            image="sherlocks_escapes.jpg",
            url="https://www.sherlocksescapes.com/"
            
        ),
        Activity(
            name="Amaranth Stoneware",
            keywords="art, crafts, quiet, seated, indoor",
            description="Participate in pottery and ceramic workshops in a hands-on indoor studio environment.",
            image="amaranth_stoneware.webp",
            url="https://amaranthstoneware.ca/?srsltid=AfmBOoqIkLdlDMmXuHaXs_3EpwrL3KgMHMBXPrj7PgBJis2xo1qHZtFb"
            
        ),
        Activity(
            name="Crock A Doodle",
            keywords="art, crafts, casual, seated, indoor",
            description="Paint pottery and create art projects in a guided indoor studio setting.",
            image="crock_a_doodle.webp",
            url="https://crockadoodle.com/kingston/"
          
        ),
        Activity(
            name="Tett Centre for Creativity & Learning",
            keywords="learning, creativity, quiet, seated, indoor",
            description="Participate in creative workshops and hands-on learning experiences in a quiet indoor space.",
            image="tett_centre.jpg",
            url="https://www.tettcentre.org/"
           
        ),
        Activity(
            name="Gangue Art and History Farm",
            keywords="learning, creativity, outdoor",
            description="Explore local farm life, art exhibits, and historic demonstrations in a rustic outdoor setting.",
            image="gangue_art_and_history_farm.webp",
            url="https://gunguo.art/"
           
        ),
        Activity(
            name="Novel Idea",
            keywords="books, learning, quiet, seated, indoor",
            description="Browse books, attend readings, or participate in literary events in a quiet indoor space.",
            image="novel_idea.webp",
            url="http://novelideabooks.ca/wp/"
            
        ),Activity(
            name="The Grand Theatre",
            keywords="theatre, music, seated, indoor",
            description="Attend live theatre performances, concerts, and cultural events in a seated indoor venue.",
            image="grand_theatre.jpg",
            url="https://www.kingstongrand.ca/"
            
        ),Activity(
            name="Knifey Spooney Cooking Classes",
            keywords="food, learning, standing, indoor",
            description="Learn to cook in guided indoor workshops with hands-on participation.",
            image="knifey_spooney_cooking_classes.webp",
            url="https://knifeyspooney.com/"
           
        ),Activity(
            name="Victoria Park",
            keywords="nature, outdoor, walking, scenic, casual",
            description="Relax or take a walk in a scenic, well-maintained park with benches, open spaces, and occasional events.",
            image="victoria_park.JPG",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/parks/"
           
        ),
        Activity(
            name="Kingston Mills",
            keywords="history, scenic, outdoor, walking",
            description="Visit the historic locks along the Rideau Canal, with walking trails and scenic views.",
            image="kingston_mills.jpg",
            url="https://parks.canada.ca/lhn-nhs/on/rideau/visit/posteeclusage-lockstation/ecluse-lock-kingston-mills"
           
        ),
         Activity(
            name="Kingston Trolley Tours",
            keywords="lively, seated, relaxed",
            description="Take a guided trolley tour around Kingston to see historic sites while seated and relaxed.",
            image="kingston_trolley_tours.jpg",
            url="https://www.kingstontrolley.ca/"
           
        ),
        Activity(
            name="Kingston Waterfront Pathway",
            keywords="nature, scenic, walking, outdoor",
            description="Walk or relax along the scenic waterfront path, with benches and lake views.",
            image="kingston_waterfront_pathway.jpg",
            url="https://waterfronttrail.org/places/communities/kingston/?/?utm_source=google&utm_medium=cpc&utm_campaign=search&gad_source=1&gad_campaignid=729754543&gbraid=0AAAAADtlaUzLjxzx6YS1iRJn8st0-C1AV&gclid=CjwKCAiAvaLLBhBFEiwAYCNTfytGyhRzNaEBKvZ9GCpysUL4tthuJO1f2fipCzQ9vhpDJj51ScTAbxoCZioQAvD_BwE"
            
        ),
        Activity(
            name="Grass Creek Park",
            keywords="nature, scenic, outdoor, walking",
            description="Enjoy outdoor walking, nature, and casual relaxation in a scenic park setting.",
            image="grass_creek_park.webp",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/parks/"
            
        ),
        Activity(
            name="Maclean Trail Park",
            keywords="nature, outdoor, walking, quiet, pets",
            description="Walk or bike along trails in a quiet outdoor park surrounded by nature.",
            image="maclean_trail_park.jpg",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/dog-parks/"
           
        ),Activity(
            name="Rotary Park",
            keywords="nature, outdoor, casual, walking",
            description="Relax or stroll in a community park with open spaces and scenic views.",
            image="rotary_park.jpeg",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/parks/"
            
        ),Activity(
            name="Meadowbrook Park",
            keywords="nature, outdoor, casual, walking, pets",
            description="Enjoy a casual walk or leisure activities in a local outdoor park setting.",
            image="meadowbrook_park.webp",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/dog-parks/"
            
        ),Activity(
            name="K&P Trail",
            keywords="nature, outdoor, walking, scenic",
            description="Hike or walk along a scenic trail that runs through natural areas and parks.",
            image="k_and_p_trail.jpg",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/trails/kp-trail-map/"

        ),Activity(
            name="Rideau Trail",
            keywords="nature, outdoor, walking, scenic",
            description="Take a scenic walk or hike along a long trail that features natural landscapes and historic points.",
            image="rideau_trail.jpg",
            url="https://www.rideautrail.org/"
            
        ),Activity(
            name="Lemoine Point",
            keywords="nature, scenic, outdoor, walking",
            description="Walk or relax along natural trails with scenic lake views in a peaceful",
            image="lemoine_point.webp",
            url="https://cataraquiconservation.ca/pages/lemoine-point-conservation-area"
            
        ),Activity(
            name="Douglas R. Fluhrer Park",
            keywords="nature, outdoor, casual, walking",
            description="Enjoy outdoor recreation, walking trails, and picnic areas in a local park.",
            image="douglas_r_fluhrer_park.jpg",
            url="https://www.cityofkingston.ca/activities-and-recreation/parks-trails-and-sports-fields-and-courts/trails/"
            
        ),Activity(
            name="Breakwater Park",
            keywords="nature, scenic, outdoor, walking",
            description="Relax or stroll along waterfront paths and open spaces with lake views.",
            image="breakwater_park.webp",
            url="https://www.visitkingston.ca/stories/kingstons-beautiful-breakwater-park/"
            
        ),Activity(
            name="Kingston Public Market",
            keywords="food, local, casual, outdoor, conversational",
            description="Browse fresh produce, crafts, and artisanal goods in a lively outdoor market atmosphere.",
            image="kingston_public_market.jpg",
            url="https://www.cityofkingston.ca/activities-and-recreation/farmers-market/kingston-public-market/"
           
        ),Activity(
            name="The Kingston Brewing Company",
            keywords="food, casual, lively, indoor",
            description="Enjoy casual dining, drinks, and conversation in a lively indoor environment.",
            image="kingston_brew_pub.jpg",
            url="https://www.kingstonbrewing.ca/"
            
        ),Activity(
            name="Mio Gelato",
            keywords="food, casual, seated, indoor",
            description="Enjoy handcrafted gelato in a small indoor café, perfect for a casual sweet treat.",
            image="mioGelato.jpg",
            url="https://www.miogelato.ca/"

        ),Activity(
            name="Pan Chancho",
            keywords="food, casual, indoor, conversational",
            description="Dine at a bakery and café offering fresh bread, pastries, and light meals in a cozy indoor space.",
            image="panChancho.webp",
            url="https://pan-chancho-bakery.myshopify.com/"
       
        ),Activity(
            name="Tango Nuevo",
            keywords="food, lively, seated, indoor",
            description="Experience live music, dancing, and dining in a lively indoor venue.",
            image="tango.jpg",
            url="http://www.tangonuevo.ca/"
         
        ),Activity(
            name="Juniper Cafe",
            keywords="food, quiet, seated, indoor",
            description="Relax with coffee, light meals, or pastries in a quiet, comfortable indoor café.",
            image="juniper.jpg",
            url="https://junipercafe.ca/?srsltid=AfmBOorLV2wXlxoHQ12KOvL5df8nnN0Kz2vMgiO1sj1TBcclf-jbNAM8"
         
        ),Activity(
            name="The Everly",
            keywords="food, casual, seated, indoor",
            description="Enjoy casual dining in a welcoming indoor space, with options for brunch or dinner.",
            image="theEverly.webp",
            url="https://theeverly.ca/"
           
        ),Activity(
            name="Chez Piggy",
            keywords="food, lively, seated, indoor",
            description="Dine in a popular, lively restaurant with a cozy indoor atmosphere.",
            image="piggy.jpg",
            url="https://chezpiggy.ca/"
        
        ),Activity(
            name="AquaTerra",
            keywords="food, scenic, seated, indoor",
            description="Enjoy meals with waterfront views in a comfortable indoor restaurant setting.",
            image="aquaterra.jpg",
            url="https://aquaterrakingston.com/"
        
        ),Activity(
            name="Olivea",
            keywords="food, lively, seated, indoor",
            description="Dine in a modern indoor restaurant offering casual meals and a lively atmosphere.",
            image="olivea.jpeg",
            url="https://www.olivea.ca/"
          
        ),Activity(
            name="Phnom Penh",
            keywords="food, casual, seated, indoor",
            description="Enjoy Cambodian cuisine and casual dining in a cozy indoor restaurant.",
            image="phnomPenh.jpg",
            url="https://www.tripadvisor.ca/Restaurant_Review-g154992-d688264-Reviews-Phnom_Penh_Restaurant-Kingston_Ontario.html"
       
        ),Activity(
            name="Delightfully Different Tea Room",
            keywords="food, quiet, seated, indoor, high tea",
            description="Enjoy a traditional high tea experience with pastries and tea in a quiet, indoor setting.",
            image="teaRoom.jpg",
            url="https://www.tripadvisor.ca/Restaurant_Review-g154992-d11642162-Reviews-Delightfully_Different_Tea_Room-Kingston_Ontario.html"
        
        ),Activity(
            name="Wooden Heads",
            keywords="food, casual, lively, indoor",
            description="Enjoy gourmet pizza, and casual indoor seating.",
            image="woodenHeads.jpeg",
            url="https://www.woodenheads.com/"
            
        ),Activity(
            name="Cocoa Bistro",
            keywords="food, learning, workshop, indoor",
            description="Participate in chocolate-making workshops or tastings in an indoor studio setting.",
            image="cocoaBistro.jpg",
            url="https://cocoabistro.ca/"
            
        ),Activity(
            name="The Toucan",
            keywords="food, lively, indoor",
            description="Enjoy casual dining and beverages in a lively indoor environment with group-friendly seating.",
            image="theToucan.jpg",
            url="https://www.tripadvisor.ca/Restaurant_Review-g154992-d779430-Reviews-The_Toucan-Kingston_Ontario.html"
           
        ),
        Activity(
            name="Daft Brewing",
            keywords="food, casual, lively, indoor",
            description="Taste local beers and socialize in a casual indoor brewery setting.",
            image="daftBrewing.jpg",
            url="https://daftbrewing.com/"
        
        ),
        Activity(
            name="Amadeus Cafe",
            keywords="food, quiet, seated, indoor",
            description="Relax with coffee, light meals, and quiet indoor seating in a cozy café.",
            image="amadeus.jpeg",
            url="https://www.amadeuscafe.ca/"
          
        ),Activity(
            name="LaVida Bistro & Social",
            keywords="food, casual, conversational, indoor",
            description="Enjoy casual dining and socializing in a comfortable indoor bistro.",
            image="lavida.jpg",
            url="https://www.lavida.social/"
           
        ),Activity(
            name="Cataraqui Golf & Country Club",
            keywords="sports, outdoor, walking, low-impact",
            description="Play golf in a scenic outdoor course suitable for light exercise and socializing.",
            image="golf.jpeg",
            url="https://cataraqui.com/"

        ),Activity(
            name="Artillery Park Aquatic Centre",
            keywords="exercise, indoor, low-impact",
            description="Participate in indoor swimming and fitness activities designed for gentle exercise.",
            image="artillerypool.webp",
            url="https://www.cityofkingston.ca/activities-and-recreation/aquatics-and-swimming/artillery-park-aquatic-centre/"

        ),Activity(
            name="Kingston Frontenac Public Library",
            keywords="learning, quiet, seated, indoor",
            description="Browse books, attend readings, or enjoy quiet study in an indoor library space.",
            image="publicLibrary.jpeg",
            url="https://www.kfpl.ca/"
        
        ),Activity(
            name="Community Ice Rink Volunteering",
            keywords="community, volunteering, outdoor, active",
            description="Volunteer for community ice rink activities, assisting with events and skating programs.",
            image="communityIceVolunteering.jpeg",
            url="https://www.cityofkingston.ca/careers-and-volunteering/volunteering/"
           
        ),Activity(
            name="Grand Theatre Usher Volunteering",
            keywords="community, volunteering, indoor",
            description="Volunteer as an usher for live performances, helping audience members in a seated indoor venue.",
            image="grandTheatre.jpeg",
            url="https://www.cityofkingston.ca/careers-and-volunteering/volunteering/grand-theatre-usher-volunteer/"
          
        ),Activity(
            name="Pumphouse Museum Model Railway Volunteer",
            keywords="community, volunteering, learning, indoor",
            description="Volunteer with museum exhibits and model railway displays in a quiet indoor setting.",
            image="pumphouse_museum.jpg",
            url="https://www.cityofkingston.ca/careers-and-volunteering/volunteering/pumphouse-museum-model-railway-volunteer/"
           
        ),Activity(
            name="The Glass House",
            keywords="arts and crafts,learning, indoor",
            description="Enjoy classes in stained glass, mosaic and glass fusing",
            image="glassHouse.png",
            url="https://theglasshouse.ca/"
         
        ),Activity(
            name="Kingston Nerd Night at the Royal Canadian Legion Branch 560",
            keywords="learning, discussion, lively, indoor",
            description="Join discussions, games, and social events for enthusiasts of comics, games, and pop culture indoors.",
            image="nerdNight.webp",
            url="https://www.visitkingston.ca/events/kingston-nerd-night/"

        ),Activity(
            name="Splitsville Bowl",
            keywords="games, casual, lively, indoor",
            description="Enjoy a fun bowling experience in a lively indoor venue suitable for groups.",
            image="splitsville.jpg",
            url="https://www.splitsvillebowl.ca/kingston-bowling"

        ),Activity(
            name="Something in the Water",
            keywords="games, casual, lively, indoor",
            description="Participate in a social trivia night with games, questions, and friendly competition indoors.",
            image="somethingInTheWater.jpg",
            url="https://somethingbrewing.ca/?srsltid=AfmBOorftfL1ywZ9QOzKolNvpyFWmvBaZsB_xNcANxLr86zfWgha-m7F"
        )
        
    ]


    fake_users = [
    {   'name': 'Alice Smith',
        'username': 'Alice',
        'email': 'alice@example.com', 
        'password': generate_password_hash('password123'),  
        'interests': 'reading, gardening, knitting',
        'bio': 'I love reading historical novels, knitting scarves, and relaxing in tea gardens.',
        'mobility_level': 'medium',
        'profile_pic': 'alice.jpg'
    },
    {
        'name': 'Bob Johnson',
        'username': 'Bob',
        'email': 'bob@example.com',  
        'password': generate_password_hash('password123'),  
        'interests': 'hiking, photography, cooking',
        'bio': 'Outdoor enthusiast who loves capturing nature and trying new recipes.',
        'mobility_level': 'very limited',
        'profile_pic': 'bob.webp'
    },
    {
        'name': 'Carol Davis',
        'username': 'Carol',
        'email': 'carol@example.com',  
        'password': generate_password_hash('password123'),  
        'interests': 'painting, yoga, coffee shops',
        'bio': 'Creative soul seeking peaceful activities and meaningful conversations.',
        'mobility_level': 'limited',
        'profile_pic': 'carol.webp'
    },
    {
        'name': 'Dave Wilson',
        'username': 'Dave',
        'email': 'dave@example.com',
        'password': generate_password_hash('password123'),
        'interests': 'hiking, kayaking, photography',
        'bio': 'I love active adventures like hiking, kayaking, and photography outdoors.',
        'mobility_level': 'high',
        'profile_pic': 'dave.jpg'
    },
    {
        'name': 'Eve Adams',
        'username': 'Eve',
        'email': 'eve@example.com',
        'password': generate_password_hash('password123'),
        'interests': 'music, theatre, dancing',
        'bio': 'I enjoy music, theatre, and dancing at social events.',
        'mobility_level': 'moderate',
        'profile_pic': 'eve.jpg'
    }
]


    db.session.add_all(activities)
    for u in fake_users:
        if not User.query.filter_by(username=u['username']).first():
            user = User(
                name=u['name'],
                username=u['username'],
                email=u['email'],
                password=u['password'],
                interests=u['interests'],
                bio=u['bio'],
                mobility_level=u['mobility_level'],
                profile_pic=u.get('profile_pic')
            )
            db.session.add(user)
    db.session.commit()

    print("Database seeded!")
