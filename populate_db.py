from app import app, db, Brand, Model, Engine

def populate_database():
    with app.app_context():
        # First, clear existing data
        db.drop_all()
        db.create_all()

        # Create brands
        brands_data = {
            'Volkswagen': [
                {
                    'name': 'Golf VI',
                    'year_start': 2008,
                    'year_end': 2012,
                    'engines': [
                        {'type': 'benzin', 'displacement': 1.6, 'power': 102},
                        {'type': 'dizel', 'displacement': 2.0, 'power': 140},
                        {'type': 'benzin', 'displacement': 1.4, 'power': 122}
                    ],
                    'pros': [
                        'Odlična završna obrada',
                        'Udobna vožnja',
                        'Prostran enterijer',
                        'Pouzdani motori',
                        'Dobra zvučna izolacija',
                        'Visoka vrednost pri preprodaji'
                    ],
                    'cons': [
                        'Skuplje održavanje od konkurencije',
                        'DSG menjač može biti problematičan',
                        'Tvrđe vešanje na lošim putevima',
                        'Skupi rezervni delovi'
                    ],
                    'description': 'Volkswagen Golf VI predstavlja šestu generaciju legendarnog Golf modela. Poznat je po visokom kvalitetu izrade, odličnoj završnoj obradi i pouzdanim motorima. Nudi odličan balans između komfora i upravljivosti, uz prostranu unutrašnjost i kvalitetne materijale.',
                    'rating': 85,
                    'reliability': 88,
                    'comfort': 85,
                    'performance': 82,
                    'running_costs': 75
                },
                {
                    'name': 'Passat B7',
                    'year_start': 2010,
                    'year_end': 2014,
                    'engines': [
                        {'type': 'dizel', 'displacement': 2.0, 'power': 140},
                        {'type': 'dizel', 'displacement': 1.6, 'power': 105},
                        {'type': 'benzin', 'displacement': 2.0, 'power': 220}
                    ],
                    'pros': [
                        'Prostrana unutrašnjost',
                        'Veliki prtljažnik',
                        'Kvalitetna izrada',
                        'Udobnost na dugim putovanjima',
                        'Dobra zvučna izolacija'
                    ],
                    'cons': [
                        'Visoki troškovi održavanja',
                        'Problemi sa DPF filterom',
                        'Skupi rezervni delovi',
                        'Potrošnja u gradskoj vožnji'
                    ],
                    'description': 'Passat B7 je poslovni automobil koji nudi odličan komfor i prostranost. Posebno je pogodan za duga putovanja, sa odličnom zvučnom izolacijom i udobnim sedištima.',
                    'rating': 82,
                    'reliability': 80,
                    'comfort': 90,
                    'performance': 78,
                    'running_costs': 70
                },
                {
                    'name': 'Polo',
                    'year_start': 2009,
                    'year_end': 2014,
                    'engines': [],
                    'pros': [
                        'Kompaktna veličina',
                        'Ekonomičnost',
                        'Lak za parkiranje',
                        'Pristupačna cena'
                    ],
                    'cons': [
                        'Manji prostor unutra',
                        'Manje snage od konkurencije'
                    ],
                    'description': 'Volkswagen Polo je gradski automobil koji se ističe svojom kompaktnošću i ekonomičnošću. Idealno rešenje za gradske vozače koji traže praktičnost i pristupačnost.',
                    'rating': 80,
                    'reliability': 85,
                    'comfort': 80,
                    'performance': 75,
                    'running_costs': 90
                }
            ],
            'BMW': [
                {
                    'name': '3 Series E90',
                    'year_start': 2005,
                    'year_end': 2012,
                    'engines': [
                        {'type': 'benzin', 'displacement': 2.0, 'power': 143},
                        {'type': 'benzin', 'displacement': 3.0, 'power': 231},
                        {'type': 'dizel', 'displacement': 2.0, 'power': 163},
                        {'type': 'dizel', 'displacement': 3.0, 'power': 204}
                    ],
                    'pros': [
                        'Odlične vozne karakteristike',
                        'Kvalitetna izrada',
                        'Snažni i pouzdani motori',
                        'Sportski karakter',
                        'Dobra dinamika vožnje'
                    ],
                    'cons': [
                        'Tvrđe vešanje',
                        'Skupo održavanje',
                        'Manji prtljažnik od konkurencije',
                        'Bučniji dizel motori'
                    ],
                    'description': 'BMW E90 serije 3 je sportska limuzina koja postavlja standarde u klasi po pitanju voznih karakteristika. Poznata po odličnoj upravljivosti i snažnim motorima.',
                    'rating': 88,
                    'reliability': 82,
                    'comfort': 78,
                    'performance': 95,
                    'running_costs': 65
                }
            ],
            'Mercedes-Benz': [
                {
                    'name': 'C-Class W204',
                    'year_start': 2007,
                    'year_end': 2014,
                    'engines': [
                        {'type': 'benzin', 'displacement': 1.8, 'power': 156},
                        {'type': 'dizel', 'displacement': 2.2, 'power': 170},
                        {'type': 'dizel', 'displacement': 3.0, 'power': 224}
                    ],
                    'pros': [
                        'Vrhunska udobnost',
                        'Prestižan izgled',
                        'Kvalitetna izrada',
                        'Odlična zvučna izolacija',
                        'Dobra bezbednosna oprema'
                    ],
                    'cons': [
                        'Visoki troškovi održavanja',
                        'Skupi servisi',
                        'Manje dinamična vožnja od BMW-a',
                        'Ograničen prostor pozadi'
                    ],
                    'description': 'Mercedes C-klase W204 je luksuzna limuzina koja nudi odličan komfor i prestižan osećaj. Poznata po kvalitetnoj izradi i visokom nivou bezbednosti.',
                    'rating': 86,
                    'reliability': 83,
                    'comfort': 92,
                    'performance': 85,
                    'running_costs': 68
                }
            ],
            'Audi': [
                {
                    'name': 'A4 B8',
                    'year_start': 2008,
                    'year_end': 2015,
                    'engines': [
                        {'type': 'dizel', 'displacement': 2.0, 'power': 143},
                        {'type': 'benzin', 'displacement': 1.8, 'power': 160},
                        {'type': 'dizel', 'displacement': 2.0, 'power': 150}
                    ],
                    'pros': [
                        'Vrhunska izrada enterijera',
                        'Quattro pogon na sve točkove',
                        'Moderna tehnologija',
                        'Odlična završna obrada',
                        'Dobra vrednost pri preprodaji'
                    ],
                    'cons': [
                        'Skupo održavanje',
                        'Tvrđe vešanje',
                        'Manje dinamičan od BMW-a',
                        'Skuplji od konkurencije'
                    ],
                    'description': 'Audi A4 B8 je premium limuzina koja se ističe kvalitetom izrade i tehnološkim inovacijama. Quattro pogon pruža odličnu stabilnost u svim uslovima.',
                    'rating': 87,
                    'reliability': 85,
                    'comfort': 88,
                    'performance': 86,
                    'running_costs': 70
                }
            ],
            'Ford': [
                {
                    'name': 'Focus II',
                    'year_start': 2004,
                    'year_end': 2011,
                    'engines': [
                        {'type': 'benzin', 'displacement': 1.6, 'power': 100},
                        {'type': 'benzin', 'displacement': 2.0, 'power': 240},
                        {'type': 'dizel', 'displacement': 1.6, 'power': 115}
                    ],
                    'pros': [
                        'Odlične vozne karakteristike',
                        'Pristupačno održavanje',
                        'Prostrana kabina',
                        'Pouzdani motori',
                        'Dobar odnos cene i kvaliteta'
                    ],
                    'cons': [
                        'Prosečan kvalitet materijala',
                        'Bučniji na većim brzinama',
                        'Jednostavan dizajn enterijera',
                        'Manja vrednost pri preprodaji'
                    ],
                    'description': 'Ford Focus II generacije je poznat po odličnim voznim karakteristikama i pristupačnom održavanju. Nudi dobar balans između praktičnosti i voznog užitka.',
                    'rating': 80,
                    'reliability': 82,
                    'comfort': 75,
                    'performance': 85,
                    'running_costs': 85
                }
            ]
        }

        # Insert data
        for brand_name, models in brands_data.items():
            brand = Brand(name=brand_name)
            db.session.add(brand)
            db.session.flush()  # This will assign the ID to the brand

            for model_data in models:
                model = Model(
                    name=model_data['name'],
                    year_start=model_data['year_start'],
                    year_end=model_data['year_end'],
                    brand_id=brand.id,
                    pros=model_data['pros'],
                    cons=model_data['cons'],
                    description=model_data['description'],
                    rating=model_data['rating'],
                    reliability=model_data['reliability'],
                    comfort=model_data['comfort'],
                    performance=model_data['performance'],
                    running_costs=model_data['running_costs']
                )
                db.session.add(model)
                db.session.flush()  # This will assign the ID to the model

                for engine_data in model_data['engines']:
                    engine = Engine(
                        type=engine_data['type'],
                        displacement=engine_data['displacement'],
                        power=engine_data['power'],
                        model_id=model.id
                    )
                    db.session.add(engine)

        db.session.commit()

        # Adding VW Polo engines
        polo = Model.query.filter_by(name='Polo').first()
        if polo:
            # 1.0 MPI (60 KS)
            engine_1_0 = Engine(
                type='benzin',
                displacement=1.0,
                power=60,
                model_id=polo.id,
                advantages=[
                    "Ekonomičnost: Niska potrošnja goriva, idealan za gradsku vožnju",
                    "Održavanje: Jednostavan motor sa niskim troškovima održavanja",
                    "Pouzdanost: Manje složenosti znači manje potencijalnih kvarova"
                ],
                disadvantages=[
                    "Performanse: Slabije ubrzanje i manjak snage na otvorenom putu",
                    "Autoput: Nije idealan za duža putovanja pri većim brzinama"
                ],
                common_issues=[
                    "Bobine paljenja: Mogući problemi sa paljenjem",
                    "Termostat: Povremeni problemi sa regulacijom temperature"
                ],
                fuel_consumption_city_declared=6.5,
                fuel_consumption_highway_declared=4.3,
                fuel_consumption_combined_declared=5.2,
                fuel_consumption_city_real="7.0–7.5 l/100 km",
                fuel_consumption_highway_real="4.8–5.3 l/100 km",
                fuel_consumption_combined_real="5.8–6.3 l/100 km"
            )

            # 1.2 MPI (70 KS)
            engine_1_2 = Engine(
                type='benzin',
                displacement=1.2,
                power=70,
                model_id=polo.id,
                advantages=[
                    "Balans: Bolje performanse od 1.0 MPI uz zadržanu ekonomičnost",
                    "Održavanje: Jednostavan i pouzdan motor"
                ],
                disadvantages=[
                    "Snaga: I dalje ograničene performanse za bržu vožnju",
                    "Buka: Glasniji pri višim obrtajima"
                ],
                common_issues=[
                    "Svećice i bobine: Mogući problemi sa paljenjem",
                    "Termostat: Povremeni problemi sa regulacijom temperature"
                ],
                fuel_consumption_city_declared=6.8,
                fuel_consumption_highway_declared=4.5,
                fuel_consumption_combined_declared=5.5,
                fuel_consumption_city_real="7.2–7.8 l/100 km",
                fuel_consumption_highway_real="4.9–5.5 l/100 km",
                fuel_consumption_combined_real="6.0–6.5 l/100 km"
            )

            # 1.2 TSI (90 KS / 105 KS)
            engine_1_2_tsi = Engine(
                type='benzin',
                displacement=1.2,
                power=105,
                model_id=polo.id,
                advantages=[
                    "Performanse: Turbo punjač pruža bolje ubrzanje i vozačko iskustvo",
                    "Ekonomičnost: Dobra potrošnja s obzirom na snagu",
                    "Univerzalnost: Pogodan za gradsku i otvorenu vožnju"
                ],
                disadvantages=[
                    "Kompleksnost: Više komponenti znači potencijalno više kvarova",
                    "Održavanje: Viši troškovi održavanja u odnosu na atmosferske motore"
                ],
                common_issues=[
                    "Lanac razvoda: Moguće istezanje lanca, što zahteva zamenu",
                    "Turbo punjač: Potencijalni problemi sa performansama i curenjem ulja"
                ],
                fuel_consumption_city_declared=6.0,
                fuel_consumption_highway_declared=4.1,
                fuel_consumption_combined_declared=4.8,
                fuel_consumption_city_real="6.5–7.0 l/100 km",
                fuel_consumption_highway_real="4.5–5.0 l/100 km",
                fuel_consumption_combined_real="5.5–6.0 l/100 km"
            )

            # 1.4 MPI (86 KS)
            engine_1_4 = Engine(
                type='benzin',
                displacement=1.4,
                power=86,
                model_id=polo.id,
                advantages=[
                    "Pouzdanost: Dokazan motor sa solidnim performansama",
                    "Održavanje: Relativno jednostavan i pristupačan za servisiranje"
                ],
                disadvantages=[
                    "Potrošnja: Nešto viša potrošnja u odnosu na moderne turbo motore",
                    "Performanse: Prosečne performanse, nedostatak snage pri većim brzinama"
                ],
                common_issues=[
                    "Termostat: Problemi sa regulacijom temperature",
                    "Lambda sonda: Mogući problemi sa očitavanjem izduvnih gasova"
                ],
                fuel_consumption_city_declared=7.5,
                fuel_consumption_highway_declared=4.8,
                fuel_consumption_combined_declared=5.8,
                fuel_consumption_city_real="8.0–8.5 l/100 km",
                fuel_consumption_highway_real="5.2–5.8 l/100 km",
                fuel_consumption_combined_real="6.5–7.0 l/100 km"
            )

            # 1.4 TSI (180 KS) – GTI verzija
            engine_1_4_tsi = Engine(
                type='benzin',
                displacement=1.4,
                power=180,
                model_id=polo.id,
                advantages=[
                    "Performanse: Izuzetno ubrzanje i sportske karakteristike",
                    "Oprema: Bogata standardna oprema i sportski detalji"
                ],
                disadvantages=[
                    "Potrošnja: Viša potrošnja goriva zbog visokih performansi",
                    "Održavanje: Skuplje održavanje i potencijalno viši troškovi popravki"
                ],
                common_issues=[
                    "Lanac razvoda: Problemi sa istezanjem lanca",
                    "Turbo i kompresor: Mogući problemi sa pouzdanošću ovih komponenti"
                ],
                fuel_consumption_city_declared=7.5,
                fuel_consumption_highway_declared=5.5,
                fuel_consumption_combined_declared=6.5,
                fuel_consumption_city_real="8.5–9.5 l/100 km",
                fuel_consumption_highway_real="6.0–7.0 l/100 km",
                fuel_consumption_combined_real="7.5–8.5 l/100 km"
            )

            # 1.2 TDI (75 KS)
            engine_1_2_tdi = Engine(
                type='dizel',
                displacement=1.2,
                power=75,
                model_id=polo.id,
                advantages=[
                    "Ekonomičnost: Vrlo niska potrošnja goriva, idealan za duže relacije",
                    "Pouzdanost: Dobar izbor za štedljive vozače s niskim troškovima održavanja",
                    "Emisije: Zadovoljava Euro 5 standarde"
                ],
                disadvantages=[
                    "Performanse: Slabiji motor sa skromnim ubrzanjem",
                    "Buka: Glasniji rad u poređenju sa benzinskim motorima"
                ],
                common_issues=[
                    "EGR ventil: Problemi sa začepljenjem zbog naslaga čađi",
                    "DPF filter: Začepljenje ako se često vozi u gradu"
                ],
                fuel_consumption_city_declared=4.5,
                fuel_consumption_highway_declared=3.2,
                fuel_consumption_combined_declared=3.8,
                fuel_consumption_city_real="5.0–5.5 l/100 km",
                fuel_consumption_highway_real="3.5–4.0 l/100 km",
                fuel_consumption_combined_real="4.2–4.8 l/100 km"
            )

            # 1.6 TDI (90 KS / 105 KS)
            engine_1_6_tdi = Engine(
                type='dizel',
                displacement=1.6,
                power=105,
                model_id=polo.id,
                advantages=[
                    "Performanse: Dobro ubrzanje i snaga, pogodan za sve vrste vožnje",
                    "Ekonomičnost: Niska potrošnja goriva uz solidne performanse",
                    "Pouzdanost: Popularan motor s dobrim balansom između troškova i performansi"
                ],
                disadvantages=[
                    "DPF problemi: Začepljenje filtera čestica kod česte gradske vožnje",
                    "Turbo: Mogućnost curenja ulja ili smanjenja performansi pri većim kilometrima"
                ],
                common_issues=[
                    "EGR ventil: Uobičajeni problemi sa začepljenjem",
                    "Injektori: Problemi sa curenjem goriva kod starijih modela"
                ],
                fuel_consumption_city_declared=4.8,
                fuel_consumption_highway_declared=3.5,
                fuel_consumption_combined_declared=4.1,
                fuel_consumption_city_real="5.2–5.8 l/100 km",
                fuel_consumption_highway_real="4.0–4.5 l/100 km",
                fuel_consumption_combined_real="4.5–5.0 l/100 km"
            )

            # 2.0 TDI (180 KS) – GTI verzija
            engine_2_0_tdi = Engine(
                type='dizel',
                displacement=2.0,
                power=180,
                model_id=polo.id,
                advantages=[
                    "Performanse: Snažan motor s odličnim ubrzanjem i maksimalnom brzinom",
                    "Ekonomičnost za performanse: Dobra potrošnja u poređenju sa benzinskim ekvivalentima",
                    "Pouzdanost: Robustan dizel motor"
                ],
                disadvantages=[
                    "Troškovi održavanja: Viši troškovi popravki zbog kompleksnosti motora",
                    "DPF problemi: Začepljenje filtera čestica kod neredovne vožnje na duže staze"
                ],
                common_issues=[
                    "Turbo punjač: Potencijalni problemi sa curenjem ulja ili performansama",
                    "DPF filter: Začepljenje kod vozača koji retko voze na autoputu"
                ],
                fuel_consumption_city_declared=5.5,
                fuel_consumption_highway_declared=4.2,
                fuel_consumption_combined_declared=4.8,
                fuel_consumption_city_real="6.0–6.5 l/100 km",
                fuel_consumption_highway_real="4.5–5.0 l/100 km",
                fuel_consumption_combined_real="5.0–5.5 l/100 km"
            )

            db.session.add_all([
                engine_1_0, engine_1_2, engine_1_2_tsi, engine_1_4, engine_1_4_tsi,
                engine_1_2_tdi, engine_1_6_tdi, engine_2_0_tdi
            ])
            db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate_database()
