from app import app
from models import db, Activity, User
from werkzeug.security import generate_password_hash, check_password_hash

with app.app_context():
    db.drop_all()
    db.create_all()

    activities = [
        Activity(
            name="Canada's Penitentiary Museum",
            keywords="history, learning, quiet, seated, indoor, conversational",
            description="Explore Canada’s federal corrections history in a historic building, with exhibits on prison life, rehabilitation programs, inmate arts and crafts, and historical artifacts",
            image="penitentiary.jpg"

        ),
        Activity(
            name="1000 Islands Cruise",
            keywords="scenic, nature, relaxed, seated, outdoor, conversational",
            description="Enjoy scenic cruises along the St. Lawrence River, passing historic estates and islands, with options for sightseeing, dining, and live commentary.",
            image="1000_islands_cruise.jpg"
    
        ),
        Activity(
            name="Fort Henry National Historic Site",
            keywords="history, outdoor, walking, learning, scenic",
            description="Tour a 19th-century military fort with historic buildings, reenactments, and panoramic views of Kingston Harbour.",
            image="fort_henry.jpg"
           
        ),
        Activity(
            name="Great Lakes Museum",
            keywords="history, learning, quiet, indoor",
            description="Discover exhibits about the ecology, history, and shipping of the Great Lakes, with interactive displays and artifacts.",
            image="great_lakes_museum.png"

        ),
        Activity(
            name="Miller Museum of Geology",
            keywords="learning, science, quiet, indoor",
            description="Explore collections of rocks, minerals, and fossils while learning about geological history in an indoor museum setting.",
            image="miller_museum_of_geology.jpg"
            
        ),
        Activity(
            name="Frontenac County Schools Museum",
            keywords="history, learning, quiet, indoor",
            description="Explore exhibits on the history of local education and schools in an indoor museum setting.",
            image="frontenac_county_schools_museum.webp"
            
        ),
        Activity(
            name="Military Communications & Electronics Museum",
            keywords="history, learning, quiet, indoor",
            description="Discover military technology and electronics history through indoor exhibits and artifacts.",
            image="military_communications.jpeg"
            
        ),
        Activity(
            name="Original Hockey Hall of Fame",
            keywords="history, sports, learning, indoor, conversational",
            description="View hockey memorabilia and exhibits in an indoor, seated space suitable for fans and casual visitors.",
            image="original_hockey_hall_of_fame.webp"
        ),
        Activity(
            name="Pumphouse Museum",
            keywords="history, learning, quiet, indoor",
            description="Explore the museum’s model trains, local history exhibits, and interactive displays indoors.",
            image="pumphouse_museum.jpg"
       
        ),
        Activity(
            name="Historic City Hall",
            keywords="history, learning, quiet, indoor",
            description="Tour the historic building and learn about Kingston’s civic history in an indoor setting.",
            image="historic_city_hall.jpg"
       
        ),
        Activity(
            name="Canadian Museum of Healthcare",
            keywords="history, learning, quiet, indoor",
            description="Explore exhibits on the history of healthcare and medicine indoors.",
            image="canadian_museum_of_healthcare.webp"
            
        ),
        Activity(
            name="Marine Museum",
            keywords="history, learning, quiet, indoor",
            description="Explore exhibits on maritime history, ships, and artifacts indoors.",
            image="marine_museum.jpg"
            
        ),
        Activity(
            name="The Screening Room",
            keywords="film, quiet, seated, indoor",
            description="Watch independent and classic films in a small, comfortable indoor cinema.",
            image="the_screening_room.avif"
           
        ),
        Activity(
            name="Landmark Cinemas",
            keywords="film, seated, indoor, casual",
            description="Enjoy popular movies in a modern indoor theater with comfortable seating and concessions.",
            image="landmark_cinemas.jpg"
           
        ),
        Activity(
            name="Bellevue House",
            keywords="history, learning, walking, scenic",
            description="Tour the historic home of Canada’s first Prime Minister, including indoor exhibits and gardens.",
            image="bellevue_house.webp"
            
        ),

        Activity(
            name="Isabel Bader Centre for Performing Arts",
            keywords="theatre, music, seated, indoor",
            description="Attend concerts, performances, and art events in a modern indoor venue.",
            image="isabel_bader_centre.webp"
            
        ),
        Activity(
            name="Martello Alley",
            keywords="art, casual, outdoor, conversational",
            description="Walk through an art-focused alley featuring local artists’ works in a casual, open space.",
            image="martello_alley.jpg"
          
        ),
        Activity(
            name="Improbable Escapes",
            keywords="games, puzzles, indoor, lively",
            description="Solve puzzles and complete challenges in immersive escape rooms that encourage teamwork and problem-solving.",
            image="improbable_escapes.jpg"
            
        ),
        Activity(
            name="Sherlock's Escapes",
            keywords="games, puzzles, indoor, lively",
            description="Solve immersive puzzles and challenges in themed escape rooms indoors.",
            image="sherlocks_escapes.jpg"
            
        ),
        Activity(
            name="Amaranth Stoneware",
            keywords="art, crafts, quiet, seated, indoor",
            description="Participate in pottery and ceramic workshops in a hands-on indoor studio environment.",
            image="amaranth_stoneware.webp"
            
        ),
        Activity(
            name="Crock A Doodle",
            keywords="art, crafts, casual, seated, indoor",
            description="Paint pottery and create art projects in a guided indoor studio setting.",
            image="crock_a_doodle.webp"
          
        ),
        Activity(
            name="Tett Centre for Creativity & Learning",
            keywords="learning, creativity, quiet, seated, indoor",
            description="Participate in creative workshops and hands-on learning experiences in a quiet indoor space.",
            image="tett_centre.jpg"
           
        ),
        Activity(
            name="Gangue Art and History Farm",
            keywords="learning, creativity, outdoor",
            description="Explore local farm life, art exhibits, and historic demonstrations in a rustic outdoor setting.",
            image="gangue_art_and_history_farm.webp"
           
        ),
        Activity(
            name="Novel Idea",
            keywords="books, learning, quiet, seated, indoor",
            description="Browse books, attend readings, or participate in literary events in a quiet indoor space.",
            image="novel_idea.webp"
            
        ),Activity(
            name="Strategies Board Game Café",
            keywords="games, casual, conversational, indoor, seated",
            description="Play board games and socialize in a casual indoor café environment.",
            image="strategies_board_game_cafe.jpg"

        ),Activity(
            name="The Grand Theatre",
            keywords="theatre, music, seated, indoor",
            description="Attend live theatre performances, concerts, and cultural events in a seated indoor venue.",
            image="grand_theatre.jpg"
            
        ),Activity(
            name="Knifey Spooney Cooking Classes",
            keywords="food, learning, standing, indoor",
            description="Learn to cook in guided indoor workshops with hands-on participation.",
            image="knifey_spooney_cooking_classes.webp"
           
        ),Activity(
            name="Victoria Park",
            keywords="nature, outdoor, walking, scenic, casual",
            description="Relax or take a walk in a scenic, well-maintained park with benches, open spaces, and occasional events.",
            image="victoria_park.JPG"
           
        ),
        Activity(
            name="Kingston Mills",
            keywords="history, scenic, outdoor, walking",
            description="Visit the historic locks along the Rideau Canal, with walking trails and scenic views.",
            image="kingston_mills.jpg"
           
        ),
         Activity(
            name="Kingston Trolley Tours",
            keywords="lively, seated, relaxed",
            description="Take a guided trolley tour around Kingston to see historic sites while seated and relaxed.",
            image="kingston_trolley_tours.jpg"
           
        ),
        Activity(
            name="Kingston Waterfront Pathway",
            keywords="nature, scenic, walking, outdoor",
            description="Walk or relax along the scenic waterfront path, with benches and lake views.",
            image="kingston_waterfront_pathway.jpg"
            
        ),
        Activity(
            name="Grass Creek Park",
            keywords="nature, scenic, outdoor, walking",
            description="Enjoy outdoor walking, nature, and casual relaxation in a scenic park setting.",
            image="grass_creek_park.webp"
            
        ),
        Activity(
            name="Maclean Trail Park",
            keywords="nature, outdoor, walking, quiet",
            description="Walk or bike along trails in a quiet outdoor park surrounded by nature.",
            image="maclean_trail_park.jpg"
           
        ),Activity(
            name="Rotary Park",
            keywords="nature, outdoor, casual, walking",
            description="Relax or stroll in a community park with open spaces and scenic views.",
            image="rotary_park.jpeg"
            
        ),Activity(
            name="Meadowbrook Park",
            keywords="nature, outdoor, casual, walking",
            description="Enjoy a casual walk or leisure activities in a local outdoor park setting.",
            image="meadowbrook_park.webp"
            
        ),Activity(
            name="K&P Trail",
            keywords="nature, outdoor, walking, scenic",
            description="Hike or walk along a scenic trail that runs through natural areas and parks.",
            image="k_and_p_trail.jpg"
            
        ),Activity(
            name="Rideau Trail",
            keywords="nature, outdoor, walking, scenic",
            description="Take a scenic walk or hike along a long trail that features natural landscapes and historic points.",
            image="rideau_trail.jpg"
            
        ),Activity(
            name="Lemoine Point",
            keywords="nature, scenic, outdoor, walking",
            description="Walk or relax along natural trails with scenic lake views in a peaceful",
            image="lemoine_point.webp"
            
        ),Activity(
            name="Douglas R. Fluhrer Park",
            keywords="nature, outdoor, casual, walking",
            description="Enjoy outdoor recreation, walking trails, and picnic areas in a local park.",
            image="douglas_r_fluhrer_park.jpg"
            
        ),Activity(
            name="Breakwater Park",
            keywords="nature, scenic, outdoor, walking",
            description="Relax or stroll along waterfront paths and open spaces with lake views.",
            image="breakwater_park.webp"
            
        ),Activity(
            name="Kingston Public Market",
            keywords="food, local, casual, outdoor, conversational",
            description="Browse fresh produce, crafts, and artisanal goods in a lively outdoor market atmosphere.",
            image="kingston_public_market.jpg"
           
        ),Activity(
            name="Kingston Brew Pub",
            keywords="food, casual, lively, indoor",
            description="Enjoy casual dining, drinks, and conversation in a lively indoor environment.",
            image="kingston_brew_pub.jpg"
            
        ),Activity(
            name="Mio Gelato",
            keywords="food, casual, seated, indoor",
            description="Enjoy handcrafted gelato in a small indoor café, perfect for a casual sweet treat.",
            image="mioGelato.jpg"

        ),Activity(
            name="Pan Chancho",
            keywords="food, casual, indoor, conversational",
            description="Dine at a bakery and café offering fresh bread, pastries, and light meals in a cozy indoor space.",
            image="panChancho.webp"
       
        ),Activity(
            name="Tango Nuevo",
            keywords="food, lively, seated, indoor",
            description="Experience live music, dancing, and dining in a lively indoor venue.",
            image="tango.jpg"
         
        ),Activity(
            name="Juniper Cafe",
            keywords="food, quiet, seated, indoor",
            description="Relax with coffee, light meals, or pastries in a quiet, comfortable indoor café.",
            image="juniper.jpg"
         
        ),Activity(
            name="The Everly",
            keywords="food, casual, seated, indoor",
            description="Enjoy casual dining in a welcoming indoor space, with options for brunch or dinner.",
            image="theEverly.webp"
           
        ),Activity(
            name="Chez Piggy",
            keywords="food, lively, seated, indoor",
            description="Dine in a popular, lively restaurant with a cozy indoor atmosphere.",
            image="piggy.jpg"
        
        ),Activity(
            name="AquaTerra",
            keywords="food, scenic, seated, indoor",
            description="Enjoy meals with waterfront views in a comfortable indoor restaurant setting.",
            image="aquaterra.jpg"
        
        ),Activity(
            name="Olivea",
            keywords="food, lively, seated, indoor",
            description="Dine in a modern indoor restaurant offering casual meals and a lively atmosphere.",
            image="olivea.jpeg"
            
          
        ),Activity(
            name="Phnom Penh",
            keywords="food, casual, seated, indoor",
            description="Enjoy Cambodian cuisine and casual dining in a cozy indoor restaurant.",
            image="phnomPenh.jpg"
       
        ),Activity(
            name="Delightfully Different Tea Room",
            keywords="food, quiet, seated, indoor, high tea",
            description="Enjoy a traditional high tea experience with pastries and tea in a quiet, indoor setting.",
            image="teaRoom.jpg"
        
        ),Activity(
            name="Wooden Heads",
            keywords="food, casual, lively, indoor",
            description="Enjoy gourmet pizza, and casual indoor seating.",
            image="woodenHeads.jpeg"
            
        ),Activity(
            name="Cocoa Bistro",
            keywords="food, learning, workshop, indoor",
            description="Participate in chocolate-making workshops or tastings in an indoor studio setting.",
            image="cocoaBistro.jpg"
            
        ),Activity(
            name="The Toucan",
            keywords="food, lively, indoor",
            description="Enjoy casual dining and beverages in a lively indoor environment with group-friendly seating.",
            image="theToucan.jpg"
           
        ),
        Activity(
            name="Daft Brewing",
            keywords="food, casual, lively, indoor",
            description="Taste local beers and socialize in a casual indoor brewery setting.",
            image="daftBrewing.jpg"
        
        ),
        Activity(
            name="Amadeus Cafe",
            keywords="food, quiet, seated, indoor",
            description="Relax with coffee, light meals, and quiet indoor seating in a cozy café.",
            image="amadeus.jpeg"
          
        ),Activity(
            name="LaVida Bistro & Social",
            keywords="food, casual, conversational, indoor",
            description="Enjoy casual dining and socializing in a comfortable indoor bistro.",
            image="lavida.jpg"
           
        ),Activity(
            name="Cataraqui Golf & Country Club",
            keywords="sports, outdoor, walking, low-impact",
            description="Play golf in a scenic outdoor course suitable for light exercise and socializing.",
            image="golf.jpeg"
        ),Activity(
            name="Artillery Park Aquatic Centre",
            keywords="exercise, indoor, low-impact",
            description="Participate in indoor swimming and fitness activities designed for gentle exercise.",
            image="artillerypool.webp"

        ),Activity(
            name="Kingston Frontenac Public Library",
            keywords="learning, quiet, seated, indoor",
            description="Browse books, attend readings, or enjoy quiet study in an indoor library space.",
            image="publicLibrary.jpeg"
        
        ),Activity(
            name="Community Ice Rink Volunteering",
            keywords="community, volunteering, outdoor, active",
            description="Volunteer for community ice rink activities, assisting with events and skating programs.",
            image="communityIceVolunteering.jpeg"
           
        ),Activity(
            name="Grand Theatre Usher Volunteering",
            keywords="community, volunteering, indoor",
            description="Volunteer as an usher for live performances, helping audience members in a seated indoor venue.",
            image="grandTheatre.jpeg"
          
        ),Activity(
            name="Pumphouse Museum Model Railway Volunteer",
            keywords="community, volunteering, learning, indoor",
            description="Volunteer with museum exhibits and model railway displays in a quiet indoor setting.",
            image="pumphouse_museum.jpg"
           
        ),Activity(
            name="The Glass House",
            keywords="arts and crafts,learning, indoor",
            description="Enjoy classes in stained glass, mosaic and glass fusing",
            image="glassHouse.png"
         
        ),Activity(
            name="Kingston Nerd Night at the Royal Canadian Legion Branch 560",
            keywords="learning, discussion, lively, indoor",
            description="Join discussions, games, and social events for enthusiasts of comics, games, and pop culture indoors.",
            image="nerdNight.webp"
            
        ),Activity(
            name="Splitsville Bowl",
            keywords="games, casual, lively, indoor",
            description="Enjoy a fun bowling experience in a lively indoor venue suitable for groups.",
            image="splitsville.jpg"

        ),Activity(
            name="Something in the Water",
            keywords="games, casual, lively, indoor",
            description="Participate in a social trivia night with games, questions, and friendly competition indoors.",
            image="somethingInTheWater.jpg"
        )
        
    ]


    fake_users = [
    {
        'username': 'Alice',
        'email': 'alice@example.com', 
        'password': generate_password_hash('password123'),  
        'interests': 'reading, gardening, knitting',
        'bio': 'I love reading historical novels, knitting scarves, and relaxing in tea gardens.',
        'mobility_level': 'medium',
        'profile_pic': 'alice.jpg'
    },
    {
        'username': 'Bob',
        'email': 'bob@example.com',  
        'password': generate_password_hash('password123'),  
        'interests': 'hiking, photography, cooking',
        'bio': 'Outdoor enthusiast who loves capturing nature and trying new recipes.',
        'mobility_level': 'very limited',
        'profile_pic': 'bob.webp'
    },
    {
        'username': 'Carol',
        'email': 'carol@example.com',  
        'password': generate_password_hash('password123'),  
        'interests': 'painting, yoga, coffee shops',
        'bio': 'Creative soul seeking peaceful activities and meaningful conversations.',
        'mobility_level': 'limited',
        'profile_pic': 'carol.webp'
    },
    {
    "username": "Dave",
    "email": "dave@example.com",
    "password": generate_password_hash('password123'),
    "interests": "hiking, kayaking, photography", 
    "bio": "I love active adventures like hiking, kayaking, and photography outdoors.",
    "mobility_level": "high",
    "profile_pic": "dave.jpg"
},
{
    "username": "Eve",
    "email": "eve@example.com",
    "password": generate_password_hash('password123'),
    "interests": "music, theatre, dancing", 
    "bio": "I enjoy music, theatre, and dancing at social events.",
    "mobility_level": "moderate",
    "profile_pic": "eve.jpg"
}

]


    db.session.add_all(activities)
    for u in fake_users:
        if not User.query.filter_by(username=u['username']).first():
            user = User(
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
