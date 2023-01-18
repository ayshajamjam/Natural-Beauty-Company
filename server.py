from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 15
data = {
    "1":
    {
        "id": "1",
        "name": "Intensive Repair Balm",
        "company": "Tammy Fender",
        "image": "/static/images/1.jpeg",
        "summary": "An intensively hydrating moisturizer blending the most powerful regeneratives in the botanical world, from Helichrysum to White Lily and Lotus. Created to treat damaged skin, and beneficial to all skin types, this is Tammy’s best-selling and most requested formula, sealing in moisture with dewy, protective veil. Because it is made with a base of floral hydrosols, it smells like a delicate cup of tea.",
        "cost": "150",
        "size": "2.3",
        "container": "jar",
        "ingredients": ["Helichrysum Flower Water", "Chamomile Essential Oil", "Rose Hip Fruit Oil"],
        "directions": "Apply to face and neck, allowing cream to absorb; if in healing mode, reapply for added hydration and protection. May be used morning and evening, or as often as needed.",
        "type": "moisturizer",
        "problem": ["Dark patches and scars", "Dehydration"],
        "skin": ["All"],
    },
    "2":
    {
        "id": "2",
        "name": "Vital Balm Cream",
        "company": "Josh Rosebrook",
        "image": "/static/images/2.jpeg",
        "summary": "Most of the time, you have to choose between a cream the deeply hydrates or a balm that creates a protective layer. Not with this multi-benefit cream, which establishes that defensive barrier while nourishing the skin on the cellular level. It’s a vital addition to your daily routine, especially if you're constantly fighting dry skin. Vital balm cream is a uniquely effective, powerful moisturizer that combines the barrier benefits of a natural balm with the absorption and luxury finish of a cream. This multi-benefit moisturizer supports true skin health and beauty by facilitating maximum cellular hydration, repair, and restoring vital skin function",
        "cost": "90",
        "size": "1.5",
        "container": "jar",
        "ingredients": ["Aloe Vera Leaf Juice", "Mango Seed Butter", "Avocado Oil"],
        "directions": "Apply a pea-sized amount to cleansed and toned skin using upward, outward motions. It'll last longer if you apply it to damp, toned skin. The cream will penetrate deeper and you'll get away with using less.",
        "type": "moisturizer",
        "problem": ["Dehydration", "Inflammation"],
        "skin": ["Dry", "Normal", "Sensitive"],
    },
    "3":
    {
        "id": "3",
        "name": "Atmosphere Protection Cream",
        "company": "Osea",
        "image": "/static/images/3.jpeg",
        "summary": "Help your skin face the day. This lightweight moisturizer hydrates and helps support skin experiencing environmental stressors such as dry climates, wind and air pollution. An OSEA fan favorite for its light, luxurious feel and soothing natural fragrance of pure lavender and geranium. It features USDA certified organic algae, shea butter, and avocado oil moisturize and firm skin leaving a matte, silky finish",
        "cost": "48",
        "size": "2",
        "container": "pump",
        "ingredients": ["Aqua", "Algae Extract", "Macadamia Ternifolia"],
        "directions": "After cleansing skin, apply preferred serum. Apply cream, massaging upwards. For extra hydration, layer with Essential Hydrating Oil or Undaria Argan Oil. Use morning + night.",
        "type": "moisturizer",
        "problem": ["Dehydration", "Redness"],
        "skin": ["Normal", "Combination"],
    },
    "4":
    {
        "id": "4",
        "name": "Golden Hour Recovery Cream",
        "company": "Ursa Major",
        "image": "/static/images/4.jpeg",
        "summary": "Golden Hour is a green beauty cult favorite. Packed with rich butters, oils and hydrators, it is a tall glass of water for parched or weather worn skin. Featuring key ingredients like sea buckthorn to protection skin's barrier, calendula to repair and black currant to brighten - it's a powerhouse in a little pot. Use it as a daily moisturizer, as a night cream or anytime your skin needs extra TLC.",
        "cost": "48",
        "size": "1.57",
        "container": "jar",
        "ingredients": ["Sea Buckthorn", "Calendula", "Sandalwood"],
        "directions": "Apply a dime-sized dab to clean, dry skin. Massage gently 'til fully absorbed. Finally, take a moment to bask in the glow.",
        "type": "moisturizer",
        "problem": ["Redness", "Dehydration"],
        "skin": ["Dry", "Sensitive"],
    },
    "5":
    {
        "id": "5",
        "name": "Miracle Cream",
        "company": "Skincando",
        "image": "/static/images/5.jpeg",
        "summary": "This delightfully thick treatment cream scented with pure rose essential oil is handcrafted in micro batches to ensure quality and freshness.  Helps hydrate all skin types especially dry, sensitive, irritated/rosacea and post surgery stressed skin. It has had a loyal following for over fifteen years. Super dense night time treatment ideal for skin in need of extra nourishment",        
        "cost": "75",
        "size": "2",
        "container": "jar",
        "ingredients": ["apricot kernel oil", "distilled water", "coconut oil"],
        "directions": "Apply anytime of the day",
        "type": "moisturizer",
        "problem": ["Dull skin", "Dehydration"],
        "skin": ["All"],
    },
    "6":
    {
        "id": "6",
        "name": "Seabiotic Water Cream",
        "company": "Osea",
        "image": "/static/images/6.jpeg",
        "summary": "Nutrient-rich, weightless water cream delivers up to 72 hours of deep hydration to thirsty skin exposed to pollution and blue light. Seaweed and a microbiome-friendly pre and probiotic* visibly promote skin radiance. This breakthrough formula leaves skin soft with a silky, smooth finish. Clinically and Dermatologist tested. Fragrance and Essential Oil Free.",
        "cost": "54",
        "size": "1.6",
        "container": "jar",
        "ingredients": ["Aqua", "Glycerin", "Caprylic"],
        "directions": "Massage into face and neck until absorbed. Use morning and night.",
        "type": "moisturizer",
        "problem": ["Dull skin", "Dehydration"],
        "skin": ["All"],
    },
    "7":
    {
        "id": "7",
        "name": "Pink Cloud Soft Moisture Cream",
        "company": "Herbivore Botanicals",
        "image": "/static/images/7.jpeg",
        "summary": "Herbivore Botanicals Pink Cloud Soft Moisture Cream works to support a healthy skin barrier while hydrating deep down, leaving you with a natural-dewy finish. This super hydrating facial moisturizer is made with tremella mushroom, which holds up to 500x its weight in water, and vegan squalane to moisturize and soften skin while helping to naturally plump. This rich, fluffy facial cream has a light floral scent from moroccan rose, which also helps to soothe skin.",
        "cost": "44",
        "size": "1.7",
        "container": "jar",
        "ingredients": ["Tremella Mushroom", "Vegan Squalane", "Morrocan Rose"],
        "directions": "Massage into skin after cleansing and applying serum. Follow with your favorite Herbivore oil to help seal in hydration and create a custom routine. Suitable for use both AM + PM.",
        "type": "moisturizer",
        "problem": ["Dryness", "Dehydration"],
        "skin": ["All"],
    },
    "8":
    {
        "id": "8",
        "name": "Fortifying Moisturizer",
        "company": "Tata Harper",
        "image": "/static/images/8.jpeg",
        "summary": "A new offering from Tata Harper, the Fortifying Moisturizer is an ultra-silky and soothing formula that delivers a cocoon-like barrier that hydrates, fortifies, comforts, and defends reactive, stressed skin. It is nice and creamy without feeling too heavy - we think it's great for year-round use! This formula is hypoallergenic, derm tested, and vegan. Free from: gluten, wheat, soy, and nut derivatives, fragrances, essential oils, and 85+ common allergens and irritants.",
        "cost": "120",
        "size": "2",
        "container": "pump",
        "ingredients": ["Calendula Officinalis Flower", "Shea Butter Ethyl Esters", "Safflower"],
        "directions": "",
        "type": "moisturizer",
        "problem": ["Fine Lines and Wrinkles", "Dryness", "Redness"],
        "skin": ["Reactive", "Sensitive", "Stressed", "Dry"],
    },
    "9":
    {
        "id": "9",
        "name": "Samadara Ultimate Age Defying Face Creme",
        "company": "Sodashi",
        "image": "/static/images/9.jpeg",
        "summary": "A powerful age-control formula to stimulate the skin’s cell renewal for an extraordinary transformative effect. This luxuriously rich and intensely hydrating crème provides all-day moisture and deeply nourishes to visibly firm, lift and plump the skin. An alchemy of bioactives Rosehip, Everlasting, Rose and Centella, it provides advanced antioxidant protection to future proof the skin, whilst Rose Quartz Crystal water gives a calming and healing vibration to the treatment. Skin regains youthful clarity and luminosity, whilst fine lines and pigmentation are diminished. Appropriate for sensitive skin.",
        "cost": "358",
        "size": "1.7",
        "container": "jar",
        "ingredients": ["Immortelle", "Damask Rose", "Rosehip Oil"],
        "directions": "After cleansing and exfoliation, apply a small amount over face, neck & décolletage. Can be used in the evenings or day and night for a more mature/dry/dehydrated skin type. Rose quartz crystals can be used to massage the product into the skin following our ancient Ayurvedic healing techniques.",
        "type": "moisturizer",
        "problem": ["Anti-aging", "Dull skin"],
        "skin": ["Sensitive"],
    },
    "10":
    {
        "id": "10",
        "name": "Deep Nourishing Cream",
        "company": "Flamingo",
        "image": "/static/images/10.jpeg",
        "summary": "Flamingo Deep Nourishing Cream is made with Squalane, White Willow Bark, Papaya Extract, Shea Butter, and Vitamin E. Squalane is derived from sugar cane and provides immediate, long-lasting moisture to the skin. White Willow Bark and Papaya Extract exfoliate the skin's surface for smoother skin, revealing more radiant skin over time. Shea Butter is from the fruit of the shea tree and naturally reinforces skin’s barrier against the elements. Flamingo Nourishing Cream provides up to 24 hours of hydration (without being too sticky!).",
        "cost": "10",
        "size": "1.7",
        "container": "jar",
        "ingredients": ["Shea Butter", "Squalane", "White Willow Bark"],
        "directions": "Apply after waxing or showering on clean body",
        "type": "moisturizer",
        "problem": ["Dehydration"],
        "skin": ["Dry", "Normal"],
    },
    "11":
    {
        "id": "11",
        "name": "Hyper Even Brightening Dark Spot Vitamin C Serum",
        "company": "Hyper Skin",
        "image": "/static/images/11.jpeg",
        "summary": "Stubborn scarring and rough texture have met their match with this lightweight gel-based serum. Packed with proven brightening (not lightening!) ingredients like vitamin C, bearberry, licorice, and kojic acid, Hyper Clear dramatically clears hyperpigmentation like dark marks, age spots, and acne scars. Plus, anti-inflammatories like aloe and turmeric not only brighten spots from the past, but also work to heal and prevent future breakouts.",
        "cost": "36",
        "size": "0.5",
        "container": "pump",
        "ingredients": ["Ethyl Ascorbic Acid", "Kojic Acid", "Bearberry Extract"],
        "directions": "Daily at night: gently massage serum onto clean, damp face and neck daily before applying moisturizer.",
        "type": "Serum",
        "problem": ["Hyperpigmentation", "Acne"],
        "skin": ["Acneic", "Combination", "Dry", "Normal", "Sensitive"],
    },
    "12":
    {
        "id": "12",
        "name": "Natural Hydrating Sunscreen SPF 30",
        "company": "Grown Alchemist",
        "image": "/static/images/12.jpeg",
        "summary": "An invisible, light weight, vegan formulation that blends effortlessly to the skin, that features innovative ultra-sheer natural Zinc Oxide to provide broad spectrum protection from damaging UVA/B rays and environmental aggressors. 100% Natural. 100% Reef Safe.",
        "cost": "39",
        "size": "1.7",
        "container": "tube",
        "ingredients": ["Zinc Oxide", "Rosehip Seed Oil", "Sodium Hyaluronate"],
        "directions": "Daily in morning: apply 1/2 teaspoon to face and neck each morning.",
        "type": "Sunscreen",
        "problem": ["Dilated Capillaries", "Hyperpigmentation"],
        "skin": ["All"],
    },
    "13":
    {
        "id": "13",
        "name": "Botanical B Enzyme Cleansing Oil",
        "company": "One Love Organics",
        "image": "/static/images/13.jpeg",
        "summary": "This multi-tasking oil cleanser effortlessly sweeps away impurities and restores skin’s pH balance. Any skin type will love this as the first step in a double cleanse. This non-stripping formula features papaya extract, a gentle fruit enzyme that eats away dead skin cells to exfoliate and soften. Meanwhile, sunflower and pumpkin seed oils tone and restore moisture.",
        "cost": "12",
        "size": "1.0",
        "container": "pump",
        "ingredients": ["Papaya Extract", "Sunflower Seed Oil", "Pumpkin Seed Oil"],
        "directions": "Dispense a small amount (1-2 pumps) into dry hands and work gently onto dry skin, focusing on areas of buildup. Add a small amount of water and spread across skin, creating a silky emulsion before rinsing clean.",
        "type": "Cleanser",
        "problem": ["Dehydration", "Blackheads", "Rough Texture"],
        "skin": ["All"],
    },
    "14":
    {
        "id": "14",
        "name": "Carbon Star",
        "company": "Pai Skincare",
        "image": "/static/images/14.jpeg",
        "summary": "This overnight complexion clarifier brings new meaning to the term beauty sleep. When managing acne-prone skin feels like a round-the-clock job, let this detoxifying facial oil work its magic overnight so you can wake up to happier skin. Formulated with healing black cumin seed oil and pore-clearing vegetable charcoal, this oil works to keep sebum production balanced and fight acne-causing bacteria. Just pat a few drops on before bed to clear active blemishes and prevent future ones.",
        "cost": "59",
        "size": "1.0",
        "container": "pump",
        "ingredients": ["Black Cumin Seed", "Vegetable Charcoal", "Copaiba Balsalm"],
        "directions": "3-5x per week: Apply one to two drops with a toner to clean skin. Use nightly or alternate with other facial oils and moisturizers",
        "type": "Face Oil",
        "problem": ["Acne", "Inflammation"],
        "skin": ["Acneic"],
    },
    "15":
    {
        "id": "15",
        "name": "Brightwave Energizing + Brightening Eye Cream",
        "company": "Kinship",
        "image": "/static/images/15.jpeg",
        "summary": "Kinship Brightwave Energizing + Brightening Eye Cream helps to awaken tired eyes by hydrating and blurring fine lines for a wide-awake look. This eye cream is made with clinically-proven actives and soft-focus blurring pigments that work to brighten the delicate under-eye area, while also helping reduce the appearance of dark circles and hydrate skin. Made with red algae, an energizing amino acid, chaga mushroom, an antioxidant that helps de-puff skin and vitamin C ester which helps to protect the delicate skin in the eye area. With a rich, cooling feeling, this eye cream will give your under-eyes a hydrated and refreshed feeling that lasts.",
        "cost": "32",
        "size": "0.5",
        "container": "jar",
        "ingredients": ["Oat kernel oil", "Jojoba Seed Oil", "Tucuma Seed Butter"],
        "directions": "Before moisturizer, use your ring finger to gently tap Brightwave around the eye area, AM + PM. A pea-sized amount is enough for both eyes. TIP: Use as an eye primer before concealer for smoother application. You can also use a small amount over concealer to refresh the look of eyes + add a touch of brightness.",
        "type": "Eye Cream",
        "problem": ["Dull skin"],
        "skin": ["All"],
    },
}

# ROUTES

@app.route('/')
def home_page():
   return render_template('home_page.html', data=data)   

@app.route('/view/<id>')
def search_result(id=None):
    global data
    product_id = data[id]

    return render_template('view.html', product=product_id, data=data)  

@app.route('/search', methods=['GET', 'POST'])
def search():
    global data

    print(request.args)
    print(request.args.get("product_to_search"))

    query = request.args.get("product_to_search")
    query = query.strip()
    valid_results = []

    if len(query) == 0:
        return render_template('search_list.html', query = query, valid_results = valid_results)

    # Iterate through dictionary
    i = 1
    for product in data:
        name = data[product]["name"]
        type_product = data[product]["type"]
        company = data[product]["company"]

        # Compare the name of the current elemnent to search term using substring matching
        if (query.lower() in name.lower() or 
            query.lower() in type_product.lower() or 
            query.lower() in company.lower()):
                valid_results.append(data[product])     # Store any matched results in a temporary array
        i = i + 1
    
    # Render a template and pass the search term as well as the temp array
    if(len(valid_results) >= 0):
        return render_template('search_list.html', query = query, valid_results = valid_results)


@app.route('/add')
def add_product():
    global data
    return render_template('add.html', data=data)

@app.route('/edit/<id>')
def edit_product(id=None):
    global data
    product_id = data[id]
    
    return render_template('edit.html', product=product_id, data=data)   

#AJAX FUNCTIONS

# ajax for adding product
@app.route('/edit_product', methods=['GET', 'POST'])
def edit_submit():
    global current_id
    global data

    json_data = request.get_json()
    id_cur = json_data["id"]
    name = json_data["name"]
    company = json_data["company"]
    image = json_data["image"]
    summary = json_data["summary"]
    cost = json_data["cost"]
    size = json_data["size"]
    container = json_data["container"]
    ingredients = json_data["ingredients"]
    directions = json_data["directions"]
    type_product = json_data["type"]
    problem = json_data["problem"]
    skin = json_data["skin"]

    edit_entry = {
        "id": id_cur,
        "name": name,
        "company": company,
        "image": image,
        "summary": summary,
        "cost": cost,
        "size": size,
        "container": container,
        "ingredients": ingredients,
        "directions": directions,
        "type": type_product,
        "problem": problem,
        "skin": skin
    }
    # adds to the dictionary
    data[str(id_cur)] = edit_entry

    #send back the WHOLE array of data
    return jsonify(data = data, current_id = id_cur)

@app.route('/add_product', methods=['GET', 'POST'])
def add_sale(): 
    global current_id
    global data

    json_data = request.get_json()
    name = json_data["name"]
    company = json_data["company"]
    image = json_data["image"]
    summary = json_data["summary"]
    cost = json_data["cost"]
    size = json_data["size"]
    container = json_data["container"]
    ingredients = json_data["ingredients"]
    directions = json_data["directions"]
    type_product = json_data["type"]
    problem = json_data["problem"]
    skin = json_data["skin"]

    # add new entry to array with 
    # a new id and the name the user sent in JSON
    current_id += 1
    new_id = current_id 
    new_entry = {
        "id": new_id,
        "name": name,
        "company": company,
        "image": image,
        "summary": summary,
        "cost": cost,
        "size": size,
        "container": container,
        "ingredients": ingredients,
        "directions": directions,
        "type": type_product,
        "problem": problem,
        "skin": skin
    }
    # adds to the dictionary
    if new_id not in data:
       data[str(new_id)] = new_entry

    #send back the WHOLE array of data
    return jsonify(data = data, current_id = current_id)

if __name__ == '__main__':
   app.run(debug = True)




